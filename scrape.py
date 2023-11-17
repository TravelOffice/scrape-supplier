import pprint

import googlemaps
from tqdm import tqdm
import time
import utils
import json

# Define the API Key.
API_KEY = 'AIzaSyBgluW0F_1IRO5MCOsc-xED2GUWESxB3Tk'
FIELDS_DETAIL_PLACE = ['place_id', 'name', 'formatted_phone_number', 'formatted_address',
                       'international_phone_number',
                       'website', 'type', 'opening_hours',
                       'editorial_summary',
                       'serves_breakfast', 'serves_lunch', 'serves_dinner',
                       'serves_vegetarian_food', 'serves_beer', 'serves_wine', 'serves_wine'
                       ]
MAX_RESULTS_PER_QUERY = 300

# Define the Client
gmaps = googlemaps.Client(key=API_KEY)

def scrape(query_file, output_file):
    with open(query_file, 'r') as f:
        query_hotel = json.load(f)

    stored_results = []
    for query in tqdm(query_hotel):
        places_result = gmaps.places(
            query=query,
            language='vi',
        )
        next_page_token = None
        if 'next_page_token' in places_result:
            next_page_token = places_result['next_page_token']
        time.sleep(3)

        total_result = 0

        while total_result < MAX_RESULTS_PER_QUERY and next_page_token is not None:
            # loop through each of the places in the results, and get the place details.
            for place in places_result['results']:
                try:
                    # make a request for the details.
                    places_details = gmaps.place(place_id=place['place_id'], fields=FIELDS_DETAIL_PLACE)
                    place_detail = utils.format_place_detail(places_details['result'])

                    # store the results in a list object.
                    stored_results.append(place_detail)

                    places_result = gmaps.places(page_token=next_page_token)
                    total_result += len(places_result['results'])
                except Exception as e:
                    print(e)
                    continue
    with open(output_file, 'w') as f:
        json.dump(stored_results, f, indent=4, ensure_ascii=False)


scrape('query_hotel.json', 'data_hotel.json')

