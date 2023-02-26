def shop_from_grocery_list(budget, shopping_list, *args) -> str:
    shopping_list_copy = shopping_list
    lenght = len(args)
    for i in range(lenght):
        if args[i][0] in shopping_list_copy:
            if budget >= args[i][1]:
                budget -= args[i][1]
                shopping_list_copy.remove(args[i][0])
                if len(shopping_list_copy) == 0:
                    return f"Shopping is successful. Remaining budget: {budget:.2f}."
            else:
                return "You did not buy all the products. Missing products: " + ', '.join(shopping_list_copy) + "."
    else:
        return "You did not buy all the products. Missing products: " + ', '.join(shopping_list_copy) + "."


print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))


