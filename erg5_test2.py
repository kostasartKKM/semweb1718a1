import csv

with open('out.csv','r',newline='') as ifp:
		ir = csv.reader(ifp)	


		for s,p,o in ir:
			s = '_'+s[1:]
			p = '<'+p+'>'
			if p == '<http://dilab77.ionio.gr/sw/p14sken/myvocab#ΗΜΕΡΑ>' :
				o = '"'+o+'"'
			elif p =='<http://dilab77.ionio.gr/sw/p14sken/myvocab#ΕΝΑΡΞΗ>' or p =='<http://dilab77.ionio.gr/sw/p14sken/myvocab#ΛΗΞΗ>' :
				if len(o) == 4: o ='0'+o
				o = '"'+o+':00"'+'^^'+'<http://www.w3.org/2001/XMLSchema#time>'				
			else:
				o ='<'+o+'>'
			print('{} {} {} .'.format(s,p,o))