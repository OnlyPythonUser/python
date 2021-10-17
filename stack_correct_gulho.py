def solution(a:str)->bool:
    result=[]
    for i in a:
        if i=="(":
            result.append("(")
        else:
            try:
                result.pop()
            except:
                return False
    if len(result)==0:
        return True
    else:
        return False
