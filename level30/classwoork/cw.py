def list_difference(a, b):
    result = []
    for item in a:
        if item not in b:
            result.append(item)
    return result



