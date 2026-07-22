def calculate_bill(customer_type, units):
    if customer_type == "1":
        name = "Residential"
        service_charge = 50
        if units <= 100:
            rate = 5
        elif units <= 300:
            rate = 7
        else:
            rate = 10
    elif customer_type == "2":
        name = "Commercial"
        service_charge = 100
        if units <= 100:
            rate = 8
        elif units <= 300:
            rate = 10
        else:
            rate = 12
    elif customer_type == "3":
        name = "Industrial"
        service_charge = 150
        if units <= 200:
            rate = 10
        elif units <= 500:
            rate = 12
        else:
            rate = 15
    else:
        raise ValueError("Invalid customer type")

    energy_charge = units * rate
    vat = energy_charge * 0.12
    total_bill = energy_charge + service_charge + vat

    return name, rate, energy_charge, service_charge, vat, total_bill


print("Welcome to the Electric Bill Calculator")
print("=" * 40)

while True:
    print("Please select the type of customer:")
    print("1. Residential")
    print("2. Commercial")
    print("3. Industrial")
    print("4. Exit")

    customer_type = input("Enter your choice (1-4): ").strip()

    if customer_type == "4":
        print("Thank you for using the Electric Bill Calculator!")
        break

    if customer_type not in {"1", "2", "3"}:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
        continue

    customer_name = input("Enter customer name: ").strip()
    customer_address = input("Enter customer address: ").strip()
    customer_contact = input("Enter customer contact number: ").strip()

    while True:
        units_input = input("Enter the number of units consumed: ").strip()
        if units_input.isdigit() and int(units_input) > 0:
            units = int(units_input)
            break
        print("Please enter a valid positive number of units.")

    customer_type_name, rate, energy_charge, service_charge, vat, total_bill = calculate_bill(customer_type, units)

    print("\nElectric Bill Summary")
    print("Customer Name:", customer_name)
    print("Customer Address:", customer_address)
    print("Contact Number:", customer_contact)
    print("Customer Type:", customer_type_name)
    print("Units Consumed:", units)
    print("Rate per Unit:", rate)
    print("Energy Charge:", format(energy_charge, ".2f"))
    print("Service Charge:", format(service_charge, ".2f"))
    print("VAT (12%):", format(vat, ".2f"))
    print("Total Bill:", format(total_bill, ".2f"))
    print("=" * 40)

    another = input("Do you want to calculate another bill? (y/n): ").strip().lower()
    if another != "y":
        print("Thank you for using the Electric Bill Calculator!")
        break