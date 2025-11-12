def open_or_senior(data):
    res = []
    for i in data:
        age,bel = i[0] , i[1]
        if age >= 55 and bel >= 7:
            res.append("Senior")
        else:
            res.append("Open")
    return res
        
            
            
