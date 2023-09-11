from fastapi import FastAPI, APIRouter
import uvicorn

from stat_router import r as stat_router

r = APIRouter()
app = FastAPI(title="Stat for front")
app.include_router(stat_router, tags=['stat'])


if __name__ == "__main__":
    uvicorn.run("main:app", host='localhost', port=8001, reload=True)
