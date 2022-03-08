from typing import Optional
from fastapi import FastAPI

import csv

from modules.make_new_data import make_new_data

from modules.view_data import make_category

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/data/create")
def read_item(q: Optional[str] = None):
    if q == None:
        q = '100'
    q = int(q)
    make_new_data('data.csv', q)
    return {"message": "success"}

@app.get("/data/view")
def get_data ():
    def get_csv_file ():
        with open('modules/csv/data.csv', 'r') as f:
            reader = csv.reader(f)
            data = [row for row in reader]
        return data
    return {"data": get_csv_file()}

@app.get("/data/category/create")
def create_category ():
    make_category()
    return {"message": "success"}

@app.get("/data/category/near/{id}")
def get_near_category (id: str):
    def get_caterogy_id (id): # カテゴリIDを取得
        csv_file = 'modules/csv/res.csv'
        res_array = []
        for row in csv.reader(open(csv_file, 'r')):
            if row[0] == id and row[1] != 'id':
                res_array.append(row[1])
        return res_array

    def get_same_category (data_id_array):
        csv_file = 'modules/csv/data.csv'
        res_data = []
        for row in csv.reader(open(csv_file, 'r')):
            if row[0] in data_id_array:
                res_data.append(row)
        return res_data
    
    return {"res": get_same_category(get_caterogy_id(id))}