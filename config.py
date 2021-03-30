import os 
from dotenv import load_dotenv
load_dotenv()
DATABASE=os.environ['DATABASE']
USER=os.getenv('USER')
PASSWORD=os.getenv('PASSWORD')
HOST=os.getenv('HOST')
PORT=os.getenv('PORT')


