import csv
import requests
BASE_URL = "https://vpic.nhtsa.dot.gov/api/vehicles"

print("Welcome to the Car Info CLI!")

while True:
    make = input("\nEnter a Car Maker name or 'exit' to quit: ").strip().lower()

    if make.lower() == 'exit':
        print("Thank you for using Car Info CLI 👋")
        break

    print(f"Searching for {make}...")
    
    url = f"{BASE_URL}/getmodelsformake/{make}?format=json"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        results = data.get("Results", [])
        
        if results:
            results.sort(key=lambda x: x["Model_Name"].lower())
            
            try:
                n = int(input("Enter number of results to display: "))
            except ValueError:
                print("Invalid number. Showing all available results.")
                n = len(results)
            
            for car in results[:n]:
                print(f"\n Result found!")
                print(f"Make: {car['Make_Name']}") #so here the Make_Name is the key name returned by the API and the same goes for Model_Name
                print(f"Model: {car['Model_Name']}")

            print(f"Showing {min(n, len(results))} of {len(results)} models found.")
            
            filename = "search_history.csv"
            try:
                with open(filename, "a", newline="") as file:
                    writer = csv.writer(file)
                    for car in results:
                        writer.writerow([make, car["Model_Name"]])
                print("💾 Saved to CSV!")
            except Exception as e:
                print("Error saving CSV:", e)
        else:
            print(f"No info found for '{make}'. Please check your spelling.")
    
    except Exception as e:
        print("Error fetching data:", e)