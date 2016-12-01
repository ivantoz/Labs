def data_type(data):
    if data is None:
        return 'no value'
    elif type(data) == str :
        return len(data)
    elif type(data) == bool:
        return data
    elif type(data) == int:
      if data < 100:
        return "less than 100"
      elif data == 100:
        return 'equal to 100'
      else:
        return "more than 100"
    elif isinstance(data, list):
      if len(data) > 2:
        return data[2]
      else:
        return None