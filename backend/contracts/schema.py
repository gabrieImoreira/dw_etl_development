from typing import Union, Dict

GenericSchema = Dict[str, Union[str, int]]


RoomsSchema:GenericSchema = {
    "name": str,
    "city": str,
    "neighborhood_group": str,
    "neighborhood": str,
    "address": str,
    "room_type": str,
    "price": int,
    "number_of_reviews": int,
    "last_review": str,
    "license": str,
    "rating": str,
    "beds": str,
    "baths": str
}