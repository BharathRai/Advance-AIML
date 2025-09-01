def main():
    print("Choose an event type:")
    print("1. Numbers greater than 3")
    print("2. Multiples of 3")
    print("3. Specific numbers (comma-separated, e.g., 2,5,6)")

    choice = input("Enter choice (1-3): ").strip()

    if choice == "1":
        e = [4, 5, 6]
        e_desc = "Numbers > 3"
    elif choice == "2":
        e = [3, 6]
        e_desc = "Multiples of 3"
    elif choice == "3":
        e_input = input("Enter event numbers (comma-separated): ")
        # clean and convert only valid integers
        e = []
        for x in e_input.split(","):
            x = x.strip()
            if x.isdigit():
                e.append(int(x))
        e_desc = f"Custom event: {e}"
    else:
        print("Invalid choice.")
        return

    # Get sample outcomes
    s_input = input("Enter dice rolls (comma-separated): ")
    s = []
    for x in s_input.split(","):
        x = x.strip()
        if x.isdigit():
            s.append(int(x))

    # Calculate probability
    f = sum(1 for x in s if x in e)
    p = f / len(s) if s else 0

    print("\n--- Probability ---")
    print(f"Event: {e} ({e_desc})")
    print(f"Sample: {s}")
    print(f"Favorable: {f}")
    print(f"Total: {len(s)}")
    print(f"P(E) = {f}/{len(s)} = {p:.4f}")

    return p

# Run the function
main()
