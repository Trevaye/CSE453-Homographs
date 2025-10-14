# Import the canonicalization function from the module
from canonicalization import canonicalize
from homograph import are_homographs

# List of test cases where path should be considered homographs
# Each tuple contains two paths that should be equivalent
homograph_paths = [
    ("secret/password.txt", "./secret/password.txt"),
    ("secret/password.txt", "subdir/../secret/password.txt"),
    ("secret/password.txt", "secret/./password.txt"),

]

#Loop through each pair of paths and check if they are homographs
for original, test in homograph_paths:
    # Call the homograph checking function
    result = are_homographs(original, test)

    # Print the result for verification
    print(f"{original} vs {test} -> Homograph? {result}")