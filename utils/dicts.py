def val(collection, key, default='ooops!'):
    if key not in collection:
        return default
    return collection[key]
