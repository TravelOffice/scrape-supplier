import json

query_statement_hotel = 'Địa điểm lưu trú tại '
query_statement_restaurant = 'Địa điểm ăn uống tại '

def generate_query(query_statement):
    query = []
    with open('provinces.json', 'r') as f:
        provinces = json.load(f)
        for item in provinces:
            query.append(query_statement + item['Province'])
    return query

query_hotel = generate_query(query_statement_hotel)
with open('query_hotel.json', 'w') as f:
    json.dump(query_hotel, f, indent=4, ensure_ascii=False)

query_restaurant = generate_query(query_statement_restaurant)
with open('query_restaurant.json', 'w') as f:
    json.dump(query_restaurant, f, indent=4, ensure_ascii=False)