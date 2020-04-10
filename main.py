# main.py
import uvicorn
from xuan import app


@app.get("/")
async def read_root():
    return {"Hello": "World"}


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
