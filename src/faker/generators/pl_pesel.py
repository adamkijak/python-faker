from random import randrange

def pesel():
	year = randrange(70,100)
	month = randrange(1,13)
	day = randrange(1,32) 	
	rest = randrange(1,10000)
	pesel = str(year)+'%0*d' % (2, month)+'%0*d' % (2, day)+'%0*d' % (4, rest)
	p = [int(i) for i in pesel]
	check_sum = 1*p[0] + 3*p[1] + 7*p[2] + 9*p[3] + 1*p[4] + 3*p[5] + 7*p[6] + \
				9*p[7] + 1*p[8] + 3*p[9]
	check_sum = check_sum % 10
	if check_sum != 0: check_sum = 10 - check_sum
	pesel+=str(check_sum)
	return pesel
	
