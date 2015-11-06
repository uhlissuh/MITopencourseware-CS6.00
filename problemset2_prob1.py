def diphantine(x):
  for a in range(0, 100):
    for b in range(0, 100):
      for c in range(0, 100):
        if 6 * a + 9 * b + 20 * c == x:
          print "for", x, ", values are", a, b, c




diphantine(50)
diphantine(51)
diphantine(52)
diphantine(53)
diphantine(54)
diphantine(55)
