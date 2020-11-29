numele=str(input('introduceti numele persoanei :'))
prenumele=str(input('introduceti prenumele persoanei :'))
numele.split()
for a in numele:
    if ord(a) in range (65 , 122):
        if (numele.title()==numele):
            for b in prenumele:
                if ord(b) in range (65 , 122):
                    if (prenumele.title()==prenumele) :        
                        print('numele este scris corect')
    else:
        print('numele nu este corect')