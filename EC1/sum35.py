# Find the sum of multiples of a and b from 0 to n.
def factorsum(a, b, n):
    result = 0
    print "Factors:",
    for x in range(1, n):
        if x % a == 0 or x % b == 0:
            result += x
            print x,
        elif x % a == 0 and x % b == 0:
            result += x
            print x,
    print "\nSum:", result
    
if __name__ == "__main__":
    import sys
    factorsum(3, 5, 1000)
