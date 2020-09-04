"""
Name: Sheldon Rush
Date started: 28/08/2020
GitHub URL:
"""

PLACES_FILE = "places.csv"
MENU = """
Menu:
L - List places
A - Add new place
M - Mark a place as visited
Q - Quit
>>>"""


def main():
    print("Travel Tracker 1.0 - by Sheldon Rush")
    print("3 places loaded from places.csv")
    print(MENU)
    choice = input(">").upper()
    while choice != "Q":
        if choice == "L":
            print("List")
        elif choice == "A":
            print("Add")
        elif choice == "M":
            print("Visit")
        else:
            print("Invalid ")
        print(MENU)
        choice = input(">").upper()
    print("Finished")
main()

