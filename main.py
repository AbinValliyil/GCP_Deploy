from fastapi import FastAPI


app = FastAPI()

@app.get('/')
def sap():
    return 'hello success'