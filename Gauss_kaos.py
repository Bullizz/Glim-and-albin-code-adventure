def getMatrix(matrix_len):
  #print("len: " + str(matrix_len))
  matrix = []
  for i in range(matrix_len):
    # array = 'glim_code()'
    # matrix.append(array)
    matrix.append(0)
  print(matrix)

class main:
  user_inp  = input("Enter matrix size: ")
  try:
    user_inp = int(user_inp)
    getMatrix(user_inp)
  except:
    print("Error, non-integer as input")