from homograph import are_homographs
def run_manual_mode():
    print("\nManual Homograph Checker.")
    path1 = input("Enter the first path: ").strip()
    path2 = input("Enter the second path: ").strip()
    result = are_homographs(path1, path2)
    print(f"\nResult: {'These are Homographs.' if result else 'These are not homographs.'}\n")

def run_test_cases():
    from test_homographs import homograph_paths
    from test_non_homographs import non_homograph_paths
    from homograph import are_homographs

    print("\n--- Homograph Test Cases ---")
    for a, b in homograph_paths:
        print(f"{a} vs {b} -> {are_homographs(a, b)}")

    print("\n--- Non-Homograph Test Cases ---")
    for a, b in non_homograph_paths:
        print(f"{a} vs {b} -> {are_homographs(a, b)}")

def main():
    while True:
        print("\nHomograph Checker Menu")
        print("1. Run Test Cases.")
        print("2. Check Manually.")
        print("3. Exit.")

        choice = input("Please select an Option: ").strip()
        if choice == '1':
            run_test_cases()
        elif choice == '2':
            run_manual_mode()
        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Please select an appropriate choice.")

if __name__ == "__main__":
    main()
