import urllib2
import sys
import gmpy2

from gmpy2 import mpz

#http://stackoverflow.com/questions/18479510/why-ruby-and-python-long-division-differs-from-gmp-and-java-biginteger


p= 13407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903427690031858186486050853753882811946569946433649006084171
g= 11717829880366207009516117596335367088558084999998952205599979459063929499736583746670572176471460312928594829675428279466566527115212748467589894601965568
h= 3239475104050450443565264378728065788649097520952449527834792452971981976143292558073856937958553180532878928001494706097394108577585732452307673444020333

p1 = mpz(p)
g1 = mpz(g)
h1 = mpz(h) 

global hashtable
global gb_table

def gen_hash_table(numiter):
	hash_table = {}
	hash_table[0] = gmpy2.f_mod(h1,p1)

	r = gmpy2.divm(h1,g1,p1)
	aux2 = gmpy2.divm(mpz(1),g1,p1)
	for i in range(1,numiter+1):
		
		if i == 1:
			aux = gmpy2.f_mod(gmpy2.mul(r,1),p1)
		else:
			aux = gmpy2.f_mod(gmpy2.mul(r,aux2),p1)
		
		hash_table[aux] = i
		r = aux
	return hash_table
	
	
def findx(table,numiter):
	

	gb = gmpy2.f_mod(pow(g1,numiter),p1)
	res = gb
	for i in range(0,numiter+1):
		if i == 0:
			aux = 1
		else:
			aux = gmpy2.f_mod(gmpy2.mul(res,gb),p1)

		res = aux		
		if aux in hashtable:
			x1 = hashtable[aux]
			x = i * numiter + x1
			print "x=", x


if __name__ == '__main__':
	
	
	B = pow(2,20);
	hashtable = gen_hash_table(B)
	findx(hashtable,B)
