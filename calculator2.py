while True:
    while True:
        A=input("숫자 연산자 숫자를 입력하세요.: ").split()
        if ('c' in A)or('C' in A) :
            print("다시 입력하세요.")
        elif(('+'not in A)and ('-'not in A)and ('*'not in A)and('/' not in A)and('e' not in A)):
            print("다시 입력하세요.")
        else :
            D=" ".join(A)
            break
        
    if ('e' in D)or('E'in D):
            break
    
    a,b,F=D.split()
    a=int(a)
    F=int(F)
    
    def add(a,F):
        return a+F     
    def minus(a,F):
        return a-F
    def mult(a,F):
        return a*F
    def div(a,F):
        return a/F
        
    if b=='+' :
        intvalue=add(a,F)
    elif b=='-' :
        intvalue=minus(a,F)
    elif b=='*' :
        intvalue=mult(a,F)
    elif b=='/' :
        intvalue=div(a,F)
    
    file=open("result.txt",'a')
    result="결과값:%d \n"%intvalue
    file.write((result))
    file.close()
    print(intvalue)