def factorial(num):
  if num == 1 or num == 0:
    return 1
  else:
    return num * factorial(num-1)



def fibonacci(num):
    if num == 0:
        return 0
    if num==1:
        return 1
    else:
        return fibonacci(num-1)+fibonacci(num-2)
