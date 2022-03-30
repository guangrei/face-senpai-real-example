from senpai import *


def menu(x):
    p = {1: train, 2: recognize, 3: list_database, 4: quit}.get(
        x, lambda: "please select 1,2,3 or 4!")
    p()


while True:
    print("please pick a number!")
    print("1. train new face.")
    print("2. recognize a face.")
    print("3. list trained faces.")
    print("4. quit!")
    pilih = int(input("your choice: "))
    menu(pilih)
