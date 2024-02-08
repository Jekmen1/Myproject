import csv
import requests
import json
import os

Api_key = '3733862c77f2424db17213ca9b494dc9'
class Person:
    def __init__(self, name_last_name, age, weight, height, result):
        self.name_last_name = name_last_name
        self.age = age
        self.weight = weight
        self.height = height
        self.result = result
    @classmethod
    def from_input(cls):
        name_last_name = input("Enter your name and last name: ")
        age = int(input("Enter your age: "))
        weight = float(input("Enter your weight: "))
        height = float(input("Enter your height in cm: "))
        return cls(name_last_name, age, weight, height, result='')
    def ratio(self):
        balance = self.height - self.weight
        if balance in range(70, 111):
            self.result = 'Good ratio'
            save_information(name_last_name=self.name_last_name, age=self.age, weight=self.weight, height=self.height, result=self.result)
            return good_ratio()
        else:
            self.result = "Bed ratio"
            save_information(name_last_name=self.name_last_name, age=self.age, weight=self.weight, height=self.height, result=self.result)
            return bed_ratio(balance)
def main():
    print("Welcome to FA.AI😎")
    while True:
        try:
            person = Person.from_input()
            print(f"Hi {person.name_last_name}.We give you all necessary information about you\n------------------------------------------------------------------------")
            return person.ratio()
            break
        except AttributeError:
            print("Invalid input, Try again")
            pass
        except ValueError:
            print("Invalid input, Try again")
            pass
def receipt(food):
    url = f'https://api.spoonacular.com/recipes/complexSearch?apiKey={Api_key}&query={food}'
    response = requests.get(url)
    data = json.loads(response.text)
    titles = [item['title'] for item in data['results']]
    for i in titles:
        print(i, "\n------------------------------------------------------------------------")
def wine(j):
    try:
        url = f"https://api.spoonacular.com/food/wine/description?apiKey={Api_key}&wine={j}"
        response = requests.get(url)
        data = response.json()
        print(f"There is description of {j},{data['wineDescription']}\nYour choice is brilliant ")
    except KeyError:
        print("Oh sorry, Inputed wine is not in our menu\n------------------------------------------------------------------------")
def good_ratio():
    # Write code for health people, free choice
    food = input("You can eat what do you want, Which ingredient do you like?")
    print(f"Okey,There is some foods with '{food}'")
    receipt(food=food)
    choose = input("Which one do you want? ")
    w = input(f"Do you want some wine with '{choose}' ")
    if w == "yes":
        print("There is menu of wine\n[Cabernet Sauvignon, merlot, Pinot Noir, Malbec, Sauvignon Blanc, ...]")
        j = input("Which one? ")
        wine(j=j)
        print("Have a nice meal")
    else:
        pass
def bed_ratio(balance):
    # write code for unhealthy people, not free choice
    if balance < 70:
        diet()
    elif balance > 110:
        bulk()
def diet():
    # write code for fat people
    print("You need diet")
    ingredient = input("Which ingredient is your favorite? ")
    url = f"https://api.spoonacular.com/food/ingredients/search?apiKey={Api_key}&query={ingredient}&minFatPercent=10&sort=calories"
    response = requests.get(url)
    data = json.loads(response.text)
    titles = [item['name'] for item in data['results']]
    print("There are foods with minFatPercent")
    for i in titles:
        print(i, "\n------------------------------------------------------------------------")
    choose = input("Which one do you want?:")
    if choose in titles:
        print("Have a nice meal")
    else:
        print("Oh sorry, Inputed ingredient is not in our menu")
def bulk():
    # write code for skinny guys
    print("You need Bulking")
    food = input("Which ingredient is your favorite? ")
    url = f"https://api.spoonacular.com/food/ingredients/search?apiKey={Api_key}&query={food}&maxFatPercent=90&sort=calories"
    response = requests.get(url)
    data = json.loads(response.text)
    titles = [item['name'] for item in data['results']]
    print("There are foods with maxFatPercent")
    for i in titles:
        print(i, "\n------------------------------------------------------------------------")
    choose = input("Which one do you want?:")
    if choose in titles:
        print("Have a nice meal")
    else:
        print("Oh sorry, Inputed ingredient is not in our menu")
def save_information(name_last_name, age, weight, height, result):
    fieldnames = ['Person', 'Age', 'Weight', 'Height', 'Result']
    file_exists = os.path.isfile("../../../Desktop/Project/personal.information.csv")
    with open("../../../Desktop/Project/personal.information.csv", 'a+', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow({'Person': name_last_name, 'Age': age, 'Weight': weight, 'Height': height, 'Result': result})
if __name__ == '__main__':
    main()
    print("Your personal data will be safe in information.csv")
