def get_summ(p_one, p_two, delimiter= '&'):
    str_one = str(p_one)
    str_two = str(p_two)
    return (str_one + delimiter + str_two).lower()
    
    
print (get_summ (1,'python','-')) 


