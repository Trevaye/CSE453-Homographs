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