import os
from dotenv import load_dotenv
load_dotenv()


GPT_CONFIG = {
    'key': os.getenv("OPEN_AI_API_KEY"),
    'model': "gpt-3.5-turbo",
    
}