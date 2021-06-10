import json


def write_order_to_json(item: str, quantity: int, price: int, buyer: str, date: str):
    with open('orders.json') as f:
        data = json.load(f)

    data['orders'].append({
        'item': item,
        'quantity': quantity,
        'price': price,
        'buyer': buyer,
        'date': date
    })

    with open('orders.json', 'w', encoding='UTF-8') as f:
        json.dump(data, f, indent=4)


def main():
    write_order_to_json('ASUS GX531GM', 5, 135000, 'Chuzhikov D. R.', '27.09.2020')


if __name__ == '__main__':
    main()
