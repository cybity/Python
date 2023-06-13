class Cat:
  def __init__(self, color, legs):
    self.color = color
    self.legs = legs

felix = Cat("ginger", 4)
rover = Cat("dog-colored", 4)
stumpy = Cat("brown", 3)

nums = {1, 2, 3, 4, 5, 6}
nums = {0, 1, 2, 3} & nums
nums = filter(lambda x: x > 1, nums)
print(len(list(nums)))

def power(x, y):
  if y == 0:
    return 1
  else:
    return x * power(x, y-1)
		
print(power(2, 3))

def func(**kwargs):
  print(kwargs["zero"])

func(a = 0, zero = 8)