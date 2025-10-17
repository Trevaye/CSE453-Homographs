# ==================================
# Homograph Detection Module - Combined Source
# ==================================

#----- Canonicalization Functions -----#
def canonicalize(path: str) -> str:
    parts = []
    #This should split paths by using '/'.
    for segment in path.split('/'):
        if segment == '' or segment == '.':
            #skips empty or the current directory segment.
            continue
        elif segment == '..':
            #moves up one directory if possible
            if parts:
                parts.pop()
        else:
            parts.append(segment)
    #Combines.
    canonical_path = '/'.join(parts)
    return canonical_path

#----- Homograph Functions -----#
def are_homographs(path1: str, path2: str) -> bool:
    canon1 = canonicalize(path1)
    canon2= canonicalize(path2)
    return canon1 == canon2

# ----- Test Cases -----
homograph_paths = [
    ("secret/password.txt", "./secret/password.txt"),
    ("secret/password.txt", "subdir/../secret/password.txt"),
    ("secret/password.txt", "secret/./password.txt"),

]

non_homograph_paths = [
    ("secret/password.txt", "secret/passw0rd.txt"),
    ("secret/password.txt", "subdir/password.txt"),
    ("secret/password.txt", "otherdir/../secret/pass.txt"),
]

# ------- Main Program to Run Tests -------
def run_manual_mode():
    print("\nManual Homograph Checker.")
    path1 = input("Enter the first path: ").strip()
    path2 = input("Enter the second path: ").strip()
    result = are_homographs(path1, path2)
    print(f"\nResult: {'These are Homographs.' if result else 'These are not homographs.'}\n")

def run_test_cases():
    
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