def create_dict_from_lists(keys, values):
    """
    This function returns a dict made from two lists.
    """
    return dict(zip(keys, values))  # implement me

def merge_two_dicts(d1, d2):
    """
    Merge two Python dictionaries into one
    """
    return d1 | d2  # implement me

def init_dict_with_values(lst, d1):
    """
    Create a dict with default values for each key listed.

    """
    new_dict = dict.fromkeys(lst, d1)  # implement me
    return new_dict

def extract_keys_to_dict(datadict, keylist):
    """
    Create a dictionary by extracting the keylist from a given dictionary
    """
    #
    return {key: datadict[key] for key in keylist}  # implement me

def delete_keys_from_dict(datadict, keylist):
    """
    Delete a list of keys from a dictionary
    """
    for key in keylist:
        datadict.pop(key, None)
    return datadict

def check_dict_for_key(datadict, key):
    """
    Check if a value exists in a dictionary
    (NO FOR loops!)
    """
    return key in datadict.values()

def get_key_of_min_value(ddd):
    """ 
    Get the key of the minimum value from a dictionary
    """
    return min(ddd, key = ddd.get)

def get_key_of_max_value(ddd):
    """
    Get the key of the maximum value from a dictionary
    """
    return max(ddd, key = ddd.get)