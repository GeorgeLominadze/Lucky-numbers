#Calculator of lucky numbers.For example if your birth date is 15 september of 1940.
#1+5+9+1+9+4+0 = 29,2+9 = 11
s = input('Enter your birth date here dd.mm.yyyy:')
s1 = s.split('.')
day= int(s1[0])
month = int(s1[1])
year = int(s1[2])

total = 0

while day>0:
  total += day %10
  day = day // 10

while month>0:
  total += month %10
  month = month // 10

while year>0:
  total += year %10
  year = year // 10

total1= 0

while total>0:
  total1 += total %10
  total = total // 10

print(total1)