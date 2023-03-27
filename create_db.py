from database import Base,engine
from models import User , Post ,Category

print("Creating database ....")
Base.metadata.create_all(engine)