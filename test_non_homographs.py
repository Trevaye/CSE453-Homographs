# Import the conicalization function from the module
from canonicalization import canonicalize
from homograph import are_homographs

# List of test cases where path should NOT be considered homographs
# Each tuple contains two paths that should NOT be equivalent
non_homograph_paths = [
    ("secret/password.txt", "secret/passw0rd.txt"),
    ("secret/password.txt", "subdir/password.txt"),
    ("secret/password.txt", "otherdir/../secret/pass.txt"),
]
# Loop through each pair of paths and check if they are NOT homographs
for original, test in non_homograph_paths:

    # Call the homograph checking function
    result = are_homographs(original, test)

    # Print the result for verification
    print(f"{original} vs {test} -> Homograph? {result}")