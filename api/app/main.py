from typing import Optional
from fastapi import FastAPI

import csv

from modules.make_new_data import make_new_data

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/data/create")
def read_item(q: Optional[str] = None):
    q = int(q)
    make_new_data('data.csv', q)

@app.get("/data/view")
def get_data ():
    def get_csv_file ():
        with open('modules/csv/data.csv', 'r') as f:
            reader = csv.reader(f)
            data = [row for row in reader]
        return data
    return {"data": get_csv_file()}
