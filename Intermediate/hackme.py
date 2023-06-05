def drawX(xw: int = 5, bw: int = 10, p: str = '*', s: str = ' ') -> None: 
  for i in range(1, 2 * bw):
    n = (-abs(i - bw) + bw)
    print(''.join([k * j for k, j in \
      zip([n, xw, (bw - n) * 2, xw, n],\
      s.join(3 * p))]))
  print()

for i in [(),\
          (3, 8, '#'),\
          (6, 12, '#', '.'),\
          (6, 12, ' ', '#'),\
          (1, 8, '*.', '.'), #Hack me\
          (1, 8, '.*', '*') #Hack me\
          ]:
  drawX(*i)