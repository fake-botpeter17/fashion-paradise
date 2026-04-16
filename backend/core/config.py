from dotenv import load_dotenv
from os import getenv
from urllib.parse import quote_plus

load_dotenv()


class Config:
    MongoClientURI = (
        "mongodb+srv://%s:%s@bms-test.xydlsxv.mongodb.net/?appName=bms-test"
        % (quote_plus(getenv("DB_User", "")), quote_plus(getenv("DB_Password", "")))
    )
    DBName = getenv("DB_Name")
