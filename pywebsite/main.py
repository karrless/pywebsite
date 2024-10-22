import uvicorn
from .config import SERVER_HOST, SERVER_PORT

def start():
  uvicorn.run("pywebsite.app:app", host=SERVER_HOST, port=SERVER_PORT, reload=True)