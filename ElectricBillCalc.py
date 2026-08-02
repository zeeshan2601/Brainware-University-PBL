rates = {
    "1": ("Residential", 50, [(100, 5), (300, 7), (float("inf"), 10)]),
    "2": ("Commercial", 100, [(100, 8), (300, 10), (float("inf"), 12)]),
    "3": ("Industrial", 150, [(200, 10), (500, 12), (float("inf"), 15)]),
}


def bill(kind, units):
    n, svc, tiers = rates[kind]
    r = next(rate for lim, rate in tiers if units <= lim)
    e = units * r
    vat = e * 0.12
    return n, r, e, svc, vat, e + svc + vat


def pos_int(prompt):
    while True:
        try:
            v = int(input(prompt))
            if v > 0:
                return v
        except Exception:
            pass
        print("Enter a valid positive integer.")


def main():
    print("Welcome to the Electric Bill Calculator\n" + "=" * 40)
    while True:
        c = input("\n1.Residential 2.Commercial 3.Industrial 4.Exit\nChoose: ").strip()
        if c == "4":
            break
        if c not in rates:
            print("Invalid choice.")
            continue
        name = input("Name: ").strip()
        addr = input("Address: ").strip()
        contact = input("Contact: ").strip()
        kind, rate, energy, service, vat, total = bill(c, pos_int("Units consumed: "))
        print(f"\nElectric Bill Summary\nName: {name}\nAddress: {addr}\nContact: {contact}\nType: {kind}\n"
              f"Units: {int(energy/rate)}\nRate: {rate}\nEnergy: {energy:.2f}\nService: {service:.2f}\nVAT: {vat:.2f}\nTotal: {total:.2f}\n" + "=" * 40)
        if input("Another bill? (y/n): ").strip().lower() != "y":
            break
    print("Thank you for using the Electric Bill Calculator!")


if __name__ == "__main__":
    main()