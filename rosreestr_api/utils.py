def prepare_cad_value_string(cad_value):
    elements = cad_value.split(':')
    elements = [str(int(element)) for element in elements]
    result = ':'.join(elements)
    return result