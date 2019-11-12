while True:
  try:
    x=int(input("Enter the value of x"))
    y=int(input("ENter the value of y"))
    avg=(x+y)/2
    print(avg)
  except Exception as e:
      print(e)
      print("Please provide an integer value")
  finally:
      print("I am going to be always executed")
