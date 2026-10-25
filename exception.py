'''
try:
    result = 10 /2
    a=b
except ZeroDivisionError as e:
    print(e)
    print("please enter the number greater than zero")
except Exception as e1:
    print(e1)


try:
    num = int(input("Enter a number"))
    result = 10 / num
except ZeroDivisionError as e:
    print(e)
    print("please enter the number greater than zero")
except Exception as e1:
    print(e1)
    print("please enter the valid number")

## try,except,else
try:
    number=int(input("Enter a number"))
    result= 10 / number
except ZeroDivisionError as e:
    print(e)
    print("please enter the number greater than zero")  
except ValueError as e1:
    print(e1)
    print("please enter the valid number")  
except Exception as e2:
    print(e2)
    print("please enter the valid number")
else:
    print(f"Result is {result}")



## try,except,else,finally

try:
    number=int(input("Enter a number"))
    result= 10 / number
except ZeroDivisionError as e:
    print(e)
    print("please enter the number greater than zero")  
except ValueError as e1:
    print(e1)
    print("please enter the valid number")  
except Exception as e2:
    print(e2)
    print("please enter the valid number")
else:
    print(f"Result is {result}")
finally:
    print("Execution completed")
    '''

## file handling and exception handling

try:
    file = open("sample.txt",'r')
    content=file.read()
    print(content)
    a=b
except FileNotFoundError:
    print("File not found")
except Exception as e:
    print(e)
finally:
    if 'file' in locals() or not file.closed():
        file.close()
        print("File closed successfully")

