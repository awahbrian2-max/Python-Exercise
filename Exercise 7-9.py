sandwich_orders=["Tuna Sandwich","Meat Sandwich","Veggie Sandwich","Cheese Sandwich","pastrami","pastrami","pastrami"]
finished_sandwiches=[]
for sandwich_order in sandwich_orders:
    print("I made your ",sandwich_order)
    while "pastrami" in sandwich_orders:
        sandwich_orders.remove("pastrami")
    finished_sandwiches.append(sandwich_order)
print("\n")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich,"Has been made")