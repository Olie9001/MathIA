import mpmath

##
mpmath.mp.prec = 1024

## Print out the current findings
def info():
    print(
        f"Found {num_birthday_match/num_birthdays_sets}% {num_birthday_match} in {num_birthdays_sets} sets of {birthday_set_size} birthdays.")

# Check if the list has any duplicates
def anydup(thelist):
    seen = set()
    for x in thelist:
        if x in seen:
            return True
        seen.add(x)
    return False

# Calculate the probability of a collision given a set of size b with r samples
# Using the Birthday problem formula https://en.wikipedia.org/wiki/Birthday_problem
def calcCollisionProbability(n, r):
    fac_n = mpmath.fac(n) 
    pow_nr = mpmath.power(n,r)
    fac_nr = mpmath.fac(n-r)
    p = mpmath.mpf(1) - (fac_n / (fac_nr*pow_nr))
    return p

# Calculate the probability of a collision given a set of size b bits with r samples
def calcCollisionProbabilityBits(b, r):
    n = mpmath.power(2,b)
    return calcCollisionProbability(n, r)

def calcCollisionSamples(n,p):
    e = mpmath.mpf(0.01)
    upper = n
    lower = 0
    x = n/2
    q = 1000.0
    while(abs(p-q)>e and lower<=upper):
        x = round((upper+lower)/2)
        q = calcCollisionProbability(n,x)
        if(q<p):
            lower = x+1
        else:
            upper = x-1
    return x

def calcCollisionSamplesBits(b,p):
    n = mpmath.power(2,b)
    return calcCollisionSamples(n,p)

def printCollisionSamplesBits(b,p):
    x = calcCollisionSamplesBits(b,p)
    print(f"Bits {b}, p {mpmath.nstr(p,5)}, samples {mpmath.nstr(x,5)}")


def printPercentiles(n):
    print(f"Percentile for hash space {mpmath.nstr(n,5)}")
    i=0
    while(i<=10):
        p = i/10.0
        x = calcCollisionSamples(n,p)
        print(f"percentile {mpmath.nstr(p,5)}, samples {mpmath.nstr(x,5)}")
        i=i+1

def printPercentilesBits(b):
    print(f"Percentile for hash bits {mpmath.nstr(b,5)}")
    n = mpmath.power(2,b)
    printPercentiles(n)

def printSamplesForHashSizes(p):
    hashSizeBits = [32,40,48,64,96,128,192,256,384,512]
    print(f"Samples for {p} probability")
    for b in hashSizeBits:
        printCollisionSamplesBits(b,p)

def printHackDetails(label,data_leak_size):
    print(f"{label} data breach {data_leak_size}")
    hashSizeBits = [32,40,48,64,96,128,192,256,384,512]
    tests_per_second = 1000000000
    for b in hashSizeBits:
        p = calcCollisionProbabilityBits(b,data_leak_size)
        num_tests = mpmath.mpf(1.0)/p
        num_seconds = num_tests/tests_per_second
        num_hours = num_seconds/(60.0*60.0)
        num_days = num_hours/(24.0)
        num_years = num_days/(365.0)
        print(f"bits {b}, probability {mpmath.nstr(p,5)}, num tests {mpmath.nstr(num_tests,5)}, num days {mpmath.nstr(num_days,5)}, num years {mpmath.nstr(num_years,5)}")


calcCollisionProbability(365,23)

printPercentiles(365)
printPercentilesBits(32)
printPercentilesBits(128)

printSamplesForHashSizes(0.5)
printSamplesForHashSizes(0.9)

# https://dataprot.net/articles/biggest-data-breaches/
# Facebook 
# Year of breach: 2019
# Data breached: 540 million records
facebookLeakSize = 540000000

# Yahoo
# Year of breach: 2013 - 2016
# Data breached: 3 billion user accounts
# https://asamborski.github.io/cs558_s17_blog/2017/04/02/yahoo.html
yahooLeakSize =    3000000000

printHackDetails('Facebook',facebookLeakSize)
printHackDetails('Yahoo',yahooLeakSize)
