def getMatrix(n):
  #print("len: " + str(matrix_len))
  matrix = []
  for i in range(n):
    # array = 'glim_code()'
    # matrix.append(array)
    matrix.append(0) # Placeholder for now, to be removed when actual function is implemented
  print(matrix)

class main:
  user_inp  = input("Enter matrix size: ")
  try:
    user_inp = int(user_inp)
    getMatrix(user_inp)
  except:
    # Kill program if user_inp is wrong datatype
    print("Error, non-integer as input")