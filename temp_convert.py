def conver_temp(temp,unit):
    if unit=='c':
        return temp * 9/5 + 32
    elif unit=='f':
        return (temp - 32) * 5/9
    else:
        return none
print(conver_temp(100,'c'))
print(conver_temp(212,'f'))


    

