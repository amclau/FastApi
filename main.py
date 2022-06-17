from fastapi import File, UploadFile
import aiofiles
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    try:
        async with aiofiles.open(file.filename, 'wb') as f:
            while contents := await file.read(1024): # async read chunk
                await f.write(contents)
    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        await file.close()

    return {"message": f"Successfuly uploaded {file.filename}"}