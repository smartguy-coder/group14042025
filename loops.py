from pprint import pprint

some_list = [55, 666] * 6
some_string = ",dfngkf8dgfgjkhdfkjghfdjkgf"
products = ["banana", "vodka", "milk", "bread", "vodka"]
# products = []
#
# for product in products:
#
#     if product == "milk":
#         break
#
#     if product == "vodka":
#         continue
#
#     print(product)
#     if product == "vodka":
#         print("No booze today")
#
# # print(product)
# print(8888888888)

people = [
    ["Alex", "Bush", "Odesa", 35, True, 12131],
    ["Petr", "Kovalsky", "Odesa", 35, True, 68785456],
    ["Alex", "Bush", "Kyiv", 65, False, 65476857],
    ["Alex", "Bush", "Kyiv, Lobanovskoho str", 65, False, 65476857],
    ["Alex", "Bush", "Odesa", 35, True, 454656],
    ["Petr", "Kovalsky", "Odesa", 35, True, 65656],
    ["Alex", "Bush", "KYIV", 65, False, 655654666],
    ["Alex", "Bush", "Odesa", 35, True, 465444],
    ["Petr", "Kovalsky", "Odesa", 35, True, 22],
    [
        "Olga",
        "Butterfly",
        "",
        22,
        False,
        2222,
    ],
]
# -------------------------------------------------------------------------------------------------
# all married people
# not married from Kyiv
# average age of married people
all_married_people = []
not_married_from_city = []
city = "Kyiv"

total_age = 0

##############################################
# for person in people:
for index, person in enumerate(people):
    # person: ['Alex', 'Bush', 'Odesa', 35, True, 12131]
    name, surname, address, age, is_married, inn = person

    # is_married = person[4]
    # address = person[2].lower()
    # address = address.lower()
    if is_married:
        # print(person)
        all_married_people.append(person)
    if not is_married and city.lower() in address.lower():
        not_married_from_city.append(person)

if all_married_people:
    ages = []
    for married_person in all_married_people:
        age = married_person[3]
        total_age += age  # use this

        #     option 2
        ages.append(age)

    print(f"Average age of married = {total_age/len(all_married_people)}")
    print(f"Average age of married = {sum(ages)/len(all_married_people)}")
else:
    print("No married - no age")


print("all married ")
pprint(all_married_people)
print(f"not married from {city}")
pprint(not_married_from_city)
#############################################
#
#
# for person in people:
#     # person: ['Alex', 'Bush', 'Odesa', 35, True, 12131]
#     is_married = person[4]
#     if is_married:
#         # print(person)
#         all_married_people.append(person)
#
#
#
# not_married_from_city = []
# city = "Kyiv"
# for person in people:
#     # person: ['Alex', 'Bush', 'Odesa', 35, True, 12131]
#     is_married = person[4]
#     address = person[2].lower()
#     if not is_married and city.lower() in address:
#         not_married_from_city.append(person)


# WARNING
list_string = "123"
print(id(list_string))
for number in list_string:
    print(number)
    print(id(list_string))
    new_number = int(number) * 2
    list_string += str(new_number)


list_data = [55, 66]
for number in list_data:
    print(number)
    new_number = number * 2
    list_data.append(new_number)
