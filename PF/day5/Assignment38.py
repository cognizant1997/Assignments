#PF-Assgn-38

def check_double(number):
    num1=''.join(sorted(str(number)))
    num2=''.join(sorted(str(number*2)))
    if(num1==num2):
        return True
    else:
        return False
print(check_double(125874))

