import os
from dotenv import load_dotenv
load_dotenv()

loginId = os.getenv('CLIENT_ID')
loginPassword = os.getenv('CLIENT_SECRET')
workStartTime = os.getenv('CLIENT_START_TIME')
workStartBreak = os.getenv('CLIENT_START_BREAK')
workEndBreak = os.getenv('CLIENT_END_BREAK')
workEndTime = os.getenv('CLIENT_END_TIME')
workMessage = os.getenv('CLIENT_MESSAGE')