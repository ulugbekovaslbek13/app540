def clean_string_data(raw_input_string):
    """Sanitizes incoming text inputs before database commitment."""
    if not raw_input_string:
        return ''
    return str(raw_input_string).strip().lower()