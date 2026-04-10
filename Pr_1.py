import cmath

x = 4 

numerator = cmath.sqrt(x - 1) - cmath.tan(x + 1)
denominator = cmath.acos(x) + cmath.log(x)

y = (numerator / denominator) + 2.75

print(y)
