from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.lyrics_searcher import LyricsSearcher

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create an instance of the neural searcher
lyrics_searcher = LyricsSearcher(collection_name='lyrics')

@app.get("/")
async def read_root():
    return {"status": "ok"}

@app.get("/search_lyrics/{prompt}")
async def search_lyrics(prompt: str):
    return {
        "result": lyrics_searcher.search(text = prompt)
    }


# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)