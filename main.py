from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def root(): return {"msg": "招聘API"}
@app.get("/list")
def jobs(city: str = "北京"):
    return {"success": True, "jobs": [{"title": "职位1", "salary": "20k"}]}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
