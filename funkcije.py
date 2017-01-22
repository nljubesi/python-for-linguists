# -*- coding: UTF-8 -*-

def frekvencijska_distribucija(sekvenca):
	rjecnik={}
	for element in sekvenca:
		rjecnik[element]=rjecnik.get(element,0)+1
	return rjecnik


def sortiraj_distribuciju(rjecnik):
	return sorted(rjecnik.items(),key=lambda x:-x[1])


def opojavnici(niz):
	import re
	return re.findall(r'\w+',niz,re.UNICODE)



# testiranje
if __name__=='__main__':
	print frekvencijska_distribucija('neki niz znakova')
	print frekvencijska_distribucija([1,2,2,3,3,3,4,4,4,4,])
	print sortiraj_distribuciju({'a':3,'b':8,'c':5})
	print opojavnici('neki niz znakova')
	print opojavnici('Neki neki niz znakova')