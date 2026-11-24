# Class List Manager - Group 1
# MIS 211 Bonus Assignment (GitHub Teamwork)

names = ["Shaden", "Maryam", "Shahad", "Ghaliah", "Rahaf", "Shaden"]



# Written by: Shaden (task 1)
def count_names(names):
    count = 0
    for name in names:
        count = count + 1
    return count

# Written by: Shahad (task 2)
def search_name(names, name):
    return name in names



def main():
    print("Welcome to the Class List Manager!")
    print("Class list:", names)
    print("Number of names:", count_names(names))
        print("Search for Ghaliah:", search_name(names, "Ghaliah"))

main()

