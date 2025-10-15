from canonicalization import canonicalize
def are_homographs(path1: str, path2: str) -> bool:
    canon1 = canonicalize(path1)
    canon2= canonicalize(path2)
    return canon1 == canon2