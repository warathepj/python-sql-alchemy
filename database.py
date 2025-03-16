from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, inspect
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

# Create an engine connected to an SQLite database file
engine = create_engine("sqlite:///example.db", echo=True)

# Base class for our classes definitions
Base = declarative_base()


# Define a User model
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)

    addresses = relationship("Address", back_populates="user")

    def __repr__(self):
        return f"<User(name={self.name}, fullname={self.fullname}, nickname={self.nickname})>"


# Define an Address model
class Address(Base):
    __tablename__ = "addresses"

    id = Column(Integer, primary_key=True)
    email_address = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="addresses")

    def __repr__(self):
        return f"<Address(email_address={self.email_address})>"


# Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Check if tables exist using inspect
inspector = inspect(engine)
if not inspector.has_table("users"):  # Check if tables exist
    Base.metadata.create_all(engine)

    # Create initial data only if tables were just created
    session = Session()

    # Create some User instances
    user1 = User(name="john", fullname="John Doe", nickname="johnny")
    user2 = User(name="jane", fullname="Jane Doe", nickname="jane")

    # Add users to the session and commit them to the database
    session.add_all([user1, user2])
    session.commit()

    # Create Address instances and associate them with users
    address1 = Address(email_address="john@example.com", user=user1)
    address2 = Address(email_address="john.doe@example.com", user=user1)
    address3 = Address(email_address="jane@example.com", user=user2)

    # Add addresses and commit the changes
    session.add_all([address1, address2, address3])
    session.commit()
    session.close()

# Create a new session for querying
session = Session()

# Query the database and print all users with their addresses
print("All users and their addresses:")
for user in session.query(User).all():
    print(user)
    for addr in user.addresses:
        print("  ", addr)

# Query a specific user by filtering
print("\nUser with the name 'john':")
john_user = session.query(User).filter_by(name="john").first()
print(john_user)
for addr in john_user.addresses:
    print("  ", addr)
