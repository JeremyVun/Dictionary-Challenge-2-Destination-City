def fast(paths, start):
  dictionary = {}

  for path in paths:
    start_city = path[0]
    end_city = path[1]
    dictionary[start_city] = end_city
  
  location = start
  while location in dictionary:
    location = dictionary[location]

  return location