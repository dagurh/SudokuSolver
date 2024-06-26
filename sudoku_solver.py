import numpy as np

possibilities = [[list(range(1, 10)) for _ in range(9)] for _ in range(9)]

def solving_algorithm(array):

  changed = False

  def mod3(number):
    return (number - 1) - ((number - 1) % 3)

  for i in range(9):
    for j in range(9):
      if array[i][j] != 0:
        possibilities[i][j] = []
      else:
        for n in range(9):
          if array[n][j] in possibilities[i][j]:
            possibilities[i][j].remove(array[n][j])
          if array[i][n] in possibilities[i][j]:
            possibilities[i][j].remove(array[i][n])
        ii = mod3(i+1)
        jj = mod3(j+1)
        for x in range(3):
          for y in range(3):
            if (array[ii+x][jj+y] != 0) and (array[ii+x][jj+y] in possibilities[i][j]):
             possibilities[i][j].remove(array[ii+x][jj+y])    

  for i in range(9):
    for j in range(9):
      if len(possibilities[i][j]) == 1:
        array[i][j] = possibilities[i][j][0]
        changed = True

  def assert_possibilities_empty(possibilities):
    for sublist in possibilities:
      for item in sublist:
        if item:
          return False
    return True

  if not changed:
    return assert_possibilities_empty(possibilities)

  return solving_algorithm(array)

def main():
  testArray = np.array([[6,3,0,0,2,0,0,0,9],
                        [0,4,0,5,3,1,0,0,2],
                        [0,7,5,0,4,9,0,3,1],
                        [8,0,0,4,0,6,1,0,0],
                        [0,0,0,2,1,0,3,9,6],
                        [0,0,0,7,0,3,2,0,4],
                        [3,8,7,0,0,0,4,0,0],
                        [4,0,2,1,0,0,0,6,3],
                        [0,0,0,0,7,0,0,0,0]])
  
  targetArray = np.array([[6,3,1,8,2,7,5,4,9],
                          [9,4,8,5,3,1,6,7,2],
                          [2,7,5,6,4,9,8,3,1],
                          [8,2,3,4,9,6,1,5,7],
                          [7,5,4,2,1,8,3,9,6],
                          [1,6,9,7,5,3,2,8,4],
                          [3,8,7,9,6,2,4,1,5],
                          [4,9,2,1,8,5,7,6,3],
                          [5,1,6,3,7,4,9,2,8]])
  
  testArray = solving_algorithm(testArray)

  print(testArray)

  a = 0

  for i in range(9):
    for j in range(9):
      if testArray[i][j] == targetArray[i][j]:
        a += 1

  print(str(a) + " out of 81 correct")

  if np.array_equal(testArray, targetArray):
    print("Solved successfully")
  else:
    print("Failed")

if __name__ == "__main__":
  main()