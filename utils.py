def format_opening_hours(opening_hours):
    periods = opening_hours['periods']

def format_place_detail(place_detail):
    projected_attrs = ['name', 'formatted_phone_number', 'formatted_address',
                       'address_components', 'international_phone_number', 'website',
                       'serves_breakfast', 'serves_lunch', 'serves_dinner',
                       'serves_vegetarian_food', 'serves_beer', 'serves_wine', 'serves_wine',
                       'opening_hours', 'editorial_summary',
                       ]
    projected_obj = {k: place_detail[k] for k in projected_attrs if k in place_detail}
    projected_obj['id'] = place_detail['place_id']

    return projected_obj
