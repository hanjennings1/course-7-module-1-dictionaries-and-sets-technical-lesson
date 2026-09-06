class CustomerManager:
    def __init__(self, customers):
        self.customers = customers

    def display_customers(self):
        """Displays all customer records."""
        for cust_id, details in self.customers.items():
            print(f"ID: {cust_id} | Name: {details['name']} | Location: {details['location']} | Purchases: {details['purchases']}")

    def filter_customers_by_city(self, city):
        """Filters customers by their location using dictionary comprehension."""
        filtered_customers = {
            cust_id: details
            for cust_id, details in self.customers.items()
            if details["location"].lower() == city.lower()
        }

        if filtered_customers:
            print(f"\nCustomers in {city}:")
            for cust_id, details in filtered_customers.items():
                print(f"ID: {cust_id} | Name: {details['name']} | "
                    f"Location: {details['location']} | Purchases: {details['purchases']}")
        else:
            print(f"\nNo customers found in {city}.")

        return filtered_customers

    def get_unique_locations(self):
        """Returns a set of unique customer locations."""
        customer_locations = {customer["location"] for customer in self.customers.values()}
        print("\nUnique Customer Locations:", customer_locations)
        return customer_locations

    def update_customer_location(self, customer_id, new_location):
        """Updates a customer's location and refreshes the set of unique locations."""
        if customer_id in self.customers:
            old_location = self.customers[customer_id]["location"]
            self.customers[customer_id]["location"] = new_location
            print(f"\nUpdated {self.customers[customer_id]['name']}'s location "
                  f"from {old_location} to {new_location}.")
            self.get_unique_locations()
        else:
            print("\nCustomer not found.")