from get_values import*

def manual():
  number = 1
  for major_Color in MAJOR_COLORS:
    for minor_Color in MINOR_COLORS:
      print(number, major_Color, minor_Color)
      number += 1


if __name__ == '__main__':
    manual()
