sandwich_orders=["Tuna Sandwich","Meat Sandwich","Veggie Sandwich","Cheese Sandwich"]
finished_sandwiches=[]
for sandwich_order in sandwich_orders:
    print("I made your ",sandwich_order)
    finished_sandwiches.append(sandwich_order)
print("\n")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich,"Has been made")