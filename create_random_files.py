import random
import string
from pathlib import Path

# Creating directory for 10 random_files
p = Path("./random_files")
try:
    p.mkdir()
except FileExistsError as exception:
    print(exception)

characters = string.printable


# The function which creates 10 random files and writes 1000 random printable characters in them
def create_files():
    for i in range(10):
        with open(f"./random_files/random_file_{i}.txt", "w") as file:
            data = "".join(random.choice(characters) for n in range(1000))
            file.write(data)


try:
    create_files()
except FileExistsError as exception:
    print(exception)
