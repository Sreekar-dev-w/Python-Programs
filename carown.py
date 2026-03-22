   
# This version of program is CLI tool and it uses funtions but the previous version uses just main block
import csv
import requests

BASE_URL = "https://vpic.nhtsa.dot.gov/api/vehicles"
def fetch_models(make_name):
    url = f"{BASE_URL}/getmodelsformake/{make_name}?format=json"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        results = data.get("Results", [])
        
        if not results:
            return None
        
        results.sort(key=lambda x: x["Model_Name"].lower())
        
        return results
    
    
    except Exception as e:
        print("Error fetching data:", e)
        return None

def display_car(make, model):
    print(f"\n Result found!")
    print(f"Make: {make}")
    print(f"Model: {model}")

def start_cli():
    print("Welcome to the Car Info CLI!")

    while True:
        make = input("\nEnter a Car Maker name or 'exit' to quit: ").strip().lower()

        if make.lower() == 'exit':
            print("Thank you for using Car Info CLI 👋")
            break

        print(f"Searching for {make}...")
        cars = fetch_models(make)

        if cars:
            try:
                n = int(input("Enter number of results to display: "))
            except ValueError:
                print("Invalid number. Showing all available results.")
                n = len(cars)
            for car in cars[:n]:
                display_car(car["Make_Name"], car["Model_Name"])

            print(f"Showing {min(n, len(cars))} of {len(cars)} models found.")
            save_to_csv(make, cars)



        else:
            print(f"No info found for '{make}'. Please check your spelling.")
        
def save_to_csv(make, cars):
    filename = "search_history.csv"

    try:
        with open(filename, "a", newline="") as file:
            writer = csv.writer(file)

            for car in cars:
                writer.writerow([make, car["Model_Name"]])

        print("💾 Saved to CSV!")

    except Exception as e:
        print("Error saving CSV:", e)

if __name__ == "__main__":
    start_cli()
#i wrote it 😁😁