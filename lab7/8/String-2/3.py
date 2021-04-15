def cat_dog(str):
  count_cat = 0
  count_dog = 0
  for i in range(len(str)):
    cur = str[i:i+3]
    if cur == "cat": count_cat += 1
    if cur == "dog": count_dog += 1
  return(count_cat == count_dog)