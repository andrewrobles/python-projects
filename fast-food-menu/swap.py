def swap():
    (x, y) = input("Please enter two float values").split()
    (y, x) = (x, y)

    print('x: {}'.format(x))
    print('y: {}'.format(y))
  

swap()