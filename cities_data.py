import json

def list_cities():
    with open("cities.json") as cities_file:
        try:
            cities_data = json.load(cities_file)

            print(f"The largest cities in the U.S are:")
            for index , city in enumerate(cities_data):
                print(f"{index + 1}. {city['name']} : {city['pop']}")
        # or run this when you fall into an error
        except json.decoder.JSONDecodeError as error:
            print(f"Sorry there was an error decoding that file:")
            print(f"\t {error}")

    print(f"File is now closed at this spot")



if __name__ == "__main__":
    list_cities()
