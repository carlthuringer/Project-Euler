#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#a^(2) + b^(2) = c^(2)

#For example, 3^(2) + 4^(2) = 9 + 16 = 25 = 5^(2).

#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

triplet = 1000
result = 0

for c in range(1000, 1, -1):
  for b in range(1000 - c, 1, -1):
    for a in range(1000 - c - b, 1, -1):
      print "A:", a, "B:", b, "C:", c
      if not a < b < c or a + b + c != 1000: break
      if a ** 2 + b ** 2 == c ** 2 and a + b + c == 1000: 
        result = a * b * c
        break
    if result > 0: break
  if result > 0: break

print result
