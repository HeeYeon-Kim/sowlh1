while True :
    
    A=input("숫자 연산자 숫자를 입력하세요: ").split()
   
    
    if ('c' in A) :
      print("다시입력하세요")
    elif ('/' in A) and ('0' in A) :
      print("다시입력하세요")
      D=" ".join(A)
    elif (('+'not in A)and ('-'not in A)and ('*'not in A)and('/' not in A)) :
      print("다시입력하세요")
    else :
      D=" ".join(A)
      print("결과값: ", eval(D))  #"숫자연산자숫자"는 안되고 "숫자 연산자 숫자" 만 가능