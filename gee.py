def cel_to_fahr(cel_value_to_fahr):
    """
    :param cel_value_to_fahr:
    :return:
    >>> cel_to_fahr(16)
    60.8
    """
    return cel_value_to_fahr * 1.8 + 32.0


cel_value_to_fahr = 16

print(cel_to_fahr(cel_value_to_fahr), "fahrenheit")
