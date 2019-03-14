def html2text(html):
    pass


def triangle_calculate_membership(left, core, right, value):
    if value == core:
        return 1
    elif value > core:
        return (right - value) / (right - core)
    return (value - left) / (core - left)


def average_without_max(array, beta):
    return (sum(array) - beta)/(len(array) - 1)


def calculate_certainty_factor(array, beta):
    return (beta - average_without_max(array, beta))/sum(array)


def safe_invert(index):
    inverted_index = {}
    for key, value in index.items():
        locations = inverted_index.setdefault(value, [])
        locations.append(key)
    return inverted_index

