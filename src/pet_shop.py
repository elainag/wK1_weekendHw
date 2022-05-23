# WRITE YOUR FUNCTIONS HERE
from http.client import CannotSendHeader
from itertools import count
from operator import index


def get_pet_shop_name(shop_name):
    return shop_name["name"]


def get_total_cash(total_cash):
    return total_cash["admin"]["total_cash"]

    # def test_add_or_remove_cash__add(self):
    #     add_or_remove_cash(self.cc_pet_shop, 10)
    #     cash = get_total_cash(self.cc_pet_shop)
    #     self.assertEqual(1010, cash)

    # def add_or_remove_cash(shop, money):
    new_total = shop["admin"]["total_cash"] = +(money)
    return new_total

    # def add_or_remove_cash(shop, money):
    new_total = shop["admin"]["total_cash"] = +(money)
    return new_total


def get_pets_sold(sold):
    return sold["admin"]["pets_sold"]


def increase_pets_sold(shop, pets_sold):
    current_sales = shop["admin"]["pets_sold"] = +int(pets_sold)
    return current_sales


def get_stock_count(shop):
    total_stock = len(shop["pets"])
    return total_stock


def get_pets_by_breed(shop, breed):
    numb_breed = []
    for dog in shop["pets"]:
        if dog["breed"] == breed:
            numb_breed.append(dog)
        else:
            pass
    return numb_breed


def find_pet_by_name(shop, name):
    for dog in shop["pets"]:
        if dog["name"] == name:
            return dog


def remove_pet_by_name(shop, name):
    to_delete = []
    for dog in shop["pets"]:
        if dog["name"] == name:
            to_delete.append(dog)
            to_delete.clear()
            return to_delete
