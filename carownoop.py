import requests

class VehicleAPI:
    #Handles all communication with the NHTSA API 
    BASE_URL = "https://vpic.nhtsa.dot.gov/api/vehicles"

    def fetch_models(self, make_name):
        url = f"{self.BASE_URL}/getmodelsformake/{make_name}?format=json"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            return data.get("Results", [])
        except requests.RequestException as e:
            print(f" Error fetching data: {e}")
            return []

class CarCLI:
    #Handles the Command Line Interface and user input 
    def __init__(self):
        self.api = VehicleAPI()

    def display_car(self, make, model):
        print(f"Make: {make} | Model: {model}")

    def start(self):
        print("Welcome to the Car Info CLI! ")

        while True:
            make = input("\nEnter a Car Maker (or 'exit' to quit): ").strip()

            if make.lower() == 'exit':
                print("Thank you for using Car Info CLI 👋")
                break

            print(f"Searching for {make}...")
            cars = self.api.fetch_models(make)

            if cars:
                try:
                    limit_input = input(f"Found available models. How many to show?:  ")
                    limit = int(limit_input)
                except ValueError:
                    print("Invalid number. Showing all results.")
                    limit = len(cars)

                for car in cars[:limit]:
                    self.display_car(car["Make_Name"], car["Model_Name"])
                
                print(f"\n Showing {min(limit, len(cars))} of {len(cars)} models.")
            else:
                print(f"No info found for '{make}'. Check your spelling!")

if __name__ == "__main__":
    app = CarCLI()
    app.start()