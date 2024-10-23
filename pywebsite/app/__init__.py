from .app import app
from .routers import routers

for router in routers:
    app.include_router(router)