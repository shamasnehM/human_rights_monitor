
import motor.motor_asyncio
from pymongo import ASCENDING

MONGO_DETAILS = "mongodb+srv://admin:admin@cluster0.w2oudme.mongodb.net/human_rights_monitor?retryWrites=true&w=majority&appName=Cluster0"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
database = client.human_rights_monitor

# Collections
db = database
