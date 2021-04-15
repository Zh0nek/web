def count_hi(str):
    count = 0
    for i in range(len(str)):
        cursor = str[i:i+2]
        if cursor == "hi": count +=1
    return count