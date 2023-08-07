import os
from dotenv import load_dotenv
load_dotenv()


API_CONFIG = {
    'KEY': os.getenv("OPEN_AI_API_KEY"),
    'MODEL': "gpt-3.5-turbo",
    
}