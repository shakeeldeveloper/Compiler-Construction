def start(s):
    r=a(s)
    if(r==1):
        token=get_next()
        if(token==-1):
            return 0
        r=b(token)
        return r
    else:
        return 0
     
def a(s):
    if(s=='_'):
        return 1
    elif(s.isalpha()):
        return 1
    else:
        return 0
         
def b(s):
    if(s=='_'):
        token=get_next()
        if(token==-1):
            return 1
        r=b(token)
        return r
        
    elif(s.isalpha()):
        token=get_next()
        if(token==-1):
            return 1
        r=b(token)
        return r
    elif(s.isdigit()):
        token=get_next()
        if(token==-1):
            return 1
        r=b(token)
        return r
   # elif(" "):

    else:
        return 0
     
    
def get_next():
    global i
    if(i<length):
        token=infix_expression[i]
        i=i+1
        return token
    else:
        print("Complete")
        return -1
def display_error():
    print("Error")
def read_expression_from_file(file_path):
    with open(file_path, 'r') as file:
        expression = file.read().strip()
        length = len(expression)  # Get the length of the expression
#        print(f"length{length}")
    return expression
i=0
file_path = 'C:/Users/Muhammad Shakeel/Downloads/code.txt'
infix_expression = read_expression_from_file(file_path)
length = len(infix_expression)
print(length)
token=get_next()
re=start(token)
print(re)

if(re==1):
    print("Correct")
else:
    print("InCorrect")

