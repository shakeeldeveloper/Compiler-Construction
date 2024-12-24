def getStat(current,character):
    if(current==0):
        if(character=='_'):
            return 1
        elif(character.isalpha()):
            return 1
        elif(character==','):
            return 2
        elif(character==';'):
            return 3
        elif(character=='='):
            return 4
        elif(character.isdigit()):
            return 6
        elif(character==' '):
            return 0
        else:
            return -1
    elif(current==1):
        if(character=='_'or character.isdigit() or character.isalpha()):
            return 1
        elif(character==" "):
            return 0
        else:
            return -1
    elif(current==2):
        if(character==" "):
            return 0
        else:
            return -1
    elif(current==3):
        if(character==" " or character =='/'):
            return 0
        else:
            return -1
    elif(current==4):
        if(character=='='):
            return 5
        elif(character==" "):
            return 0
        else:
            return -1
    elif(current==5):
        if(character==" "):
            return 0
        else:
            return -1
    elif(current==6):
        if(character=='.'):
            return 7
        elif(character.isdigit()):
            return 6
        elif(character==" "):
            return 0
        else:
            return -1
    elif(current==7):
        if(character.isdigit):
            return 8
        elif(character==" "):
            return 0
        else:
            return -1
    elif(current==8):
        if(character.isdigit()):
            return 8
        elif(character==" "):
            return 0
        else:
            return -1
 
        
    

def read_expression_from_file(file_path):
    with open(file_path, 'r') as file:
        expression = file.read().strip()
        length = len(expression)  # Get the length of the expression
#        print(f"length{length}")
    return expression

CS=0
LS=0
FS=0
LineNo=1
IWLFSV=-1
LFSV=-1

key_values = {1: 'ID', 2:'comma' , 3:'Semicolon', 4:'Assignment',5: 'Equal',6:'Int',7:'Invalid',8:'Float'}
Keywords={'int','float','string','char','if','else','elif','for','while'}
   
file_path = 'shakeeldeveloper/Compiler-Construction/cc lab/string.txt'
infix_expression = read_expression_from_file(file_path)
for char in infix_expression:
   # print(char)
    if(CS==0):
        CS=getStat(CS,char)
        LFSV=CS
    else:
        LFSV=CS
        CS=getStat(CS,char)

    IWLFSV=FS
    FS=FS+1
   # print(CS)
    if(CS==0):
        temp=""
        for c in infix_expression[LS:IWLFSV]:
            temp=temp+c
      #  print(temp)
      #  print(f"lsfv : {LFSV}")
        if(LFSV==1):
            if temp in Keywords:  
                print(f"< {temp} : Keyword >")  
            else:
                print(f"< {temp} : Identifier >")
        else:
            if LFSV in key_values:
                print(f"< {temp} : {key_values[LFSV]} >")  
              
            
        IWLFSV=-1
        LFSV=-1
        LS=FS
    elif(CS==-1):
        print("Invalid")
        CS=0



    #print(f"cs: {CS} | fs: {FS} | IWLFSV : {IWLFSV} | LFSV : {LFSV} | LS : {LS}")