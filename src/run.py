"""For development usage"""
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app="main:app", port=8000, reload=True, workers=2)
