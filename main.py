from fastapi import FastAPI

app = FastAPI(title='Smartphones')

@app.get('/')
def hello():
    return "hello"



database = {
    '1':(('brand', 'samsung'), ('screen','AMOLED')),
    '2':(('brand', 'samsung2'), ('screen','AMOLED222'))
}

@app.get('/{id}')
def get_smartphone(id):
    return database[id]
