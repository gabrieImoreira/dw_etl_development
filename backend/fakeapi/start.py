from fastapi import FastAPI
from faker import Faker
import variables.variables as variables
import pandas as pd
import random

app = FastAPI()
fake = Faker()

df = pd.read_csv(variables.CSV_AIRBNB_API)
df["indice"] = range(1, len(df) + 1)
df.set_index("indice", inplace=True)

@app.get("/room")
async def get_room():
    index = random.randint(1, len(df) - 1)
    tuple = df.iloc[index]  
    fake_data = {
        "name": tuple["name"],
        "city": "New York",
        "neighborhood_group": tuple["neighbourhood_group"],
        "neighborhood": tuple["neighbourhood"],
        "address": fake.address().split("\n")[0],
        "room_type": tuple["room_type"],
        "price": tuple["price"],
        "number_of_reviews": int(tuple["number_of_reviews"]),
        "last_review": tuple["last_review"],
        "license": tuple["license"],
        "rating": tuple["rating"],
        "beds": int(tuple["beds"]),
        "baths": int(tuple["baths"])
        }
    return fake_data

@app.get("/rooms/{num_rooms}")
async def get_rooms(num_rooms: int):
    if num_rooms < 1:
        return "Number of rooms must be greater than 0"
    
    fake_data = []
    for index in range(num_rooms):
        index = random.randint(1, len(df) - 1)
        tuple = df.iloc[index]
        fake_data.append({
            "name": tuple["name"],
            "city": "New York",
            "neighborhood_group": tuple["neighbourhood_group"],
            "neighborhood": tuple["neighbourhood"],
            "address": fake.address().split("\n")[0],
            "room_type": tuple["room_type"],
            "price": tuple["price"],
            "number_of_reviews": int(tuple["number_of_reviews"]),
            "last_review": tuple["last_review"],
            "license": tuple["license"],
            "rating": tuple["rating"],
            "beds": str(tuple["beds"]),
            "baths": str(tuple["baths"])
            })
        
    return fake_data
