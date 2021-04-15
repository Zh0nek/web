def xyz_there(str):
    for i in range(len(str)):
        cur1 = str[i:i+4]
        cur2 = str[i+1:i+4]
        cur3 = str[i:i+3]
        #print(cur1, cur2, cur3)
        if (i == 0 and cur3 == "xyz") or (cur1 != ".xyz" and cur2 == "xyz"): return True    
    return False