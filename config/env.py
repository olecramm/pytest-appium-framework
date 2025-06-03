from dotenv import load_dotenv
import os   

load_dotenv(dotenv_path=".env.qa")

appium_url = os.getenv("APPIUM_SERVER_URL")