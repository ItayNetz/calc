while True:
   print("Options:")
   print("Enter 'add' to add two numbers")
   print("Enter 'subtract' to subtract two numbers")
   print("Enter 'multiply' to multiply two numbers")
   print("Enter 'divide' to divide two numbers")
   print("Enter 'quit' to end the program")
   input_ = input("/")

   if input_ == "quit":
      break
   elif input_ == "add":
      num1 = float(input("Enter a number: "))
      num2 = float(input("Enter another number: "))
      result = str(num1 + num2)
      print("The answer is " + result)
   elif input_ == "subtract":
      num1 = float(input("Enter a number: "))
      num2 = float(input("Enter another number: "))
      result = str(num1 - num2)
      print("The answer is " + result)
   elif input_ == "multiply":
      num1 = float(input("Enter a number: "))
      num2 = float(input("Enter another number: "))
      result = str(num1 * num2)
      print("The answer is " + result)
   elif input_ == "divide":
      num1 = float(input("Enter a number: "))
      num2 = float(input("Enter another number: "))
      result = str(num1 / num2)
      print("The answer is " + result)
   else:
      print("Unknown input")
