def count_units(data):
    purchases = {}
    
    for record in data:
        customer_id, product, quantity = record.split()
        customer_id = int(customer_id)
        quantity = int(quantity)
        
        if customer_id in purchases:
            purchases[customer_id].append((product, quantity))
        else:
            purchases[customer_id] = [(product, quantity)]
    
    return purchases


n = int(input("Введите количество записей о покупках: "))
purchase_data = []

for _ in range(n):
    record = input("Введите запись о покупке: ")
    purchase_data.append(record)

purchases = count_units(purchase_data)

for customer_id, customer_purchases in purchases.items():
    print("Покупатель ID", customer_id, "купил:")
    for product, quantity in customer_purchases:
        print(f"{quantity} единиц товара {product}")
