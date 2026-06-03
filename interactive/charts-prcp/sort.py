import collections
with open ("pythonsort.txt", "r") as myfile:
    for line in myfile.readlines():
		if line.find('": {') > 0:
			string = line.replace('": {', ' - Rain": {')
			print string			
		if line.find('label') > 0:
			string = line.replace('",', ' - Rain",')
			print string
		if line.find('data') == -1 and line.find('label') == -1 and line.find('": {') == -1:
			print line
		print 'lines: { show: true },points: { show: true },'
		if line.find('data') > 0:
			string = line.replace('data: [[', '{')
			string = string.replace(']]},', '}')
			string = string.replace(',', ':')
			string = string.replace(': ', ', ')
			string = string.replace('[', '')
			string = string.replace(']', '')
			tempco = eval(string)
			od = collections.OrderedDict(sorted(tempco.items()))
			string = str(od)
			string = string.replace('OrderedDict([(', 'data: [[')
			string = string.replace(')])', ']]},')
			string = string.replace('(', '[')
			string = string.replace(')', ']')
			print string
with open ("pythonsort.txt", "r") as myfile:
    for line in myfile.readlines():
		if line.find('": {') > 0:
			string = line.replace('": {', ' - Rain trend": {')
			print string	
		if line.find('label') > 0:
			string = line.replace('",', ' - Rain trend",')
			print string
		if line.find('data') == -1 and line.find('label') == -1 and line.find('": {') == -1:
			print line
		print 'lines: { show: true },points: { show: true },'
		if line.find('data') > 0:
			string = line.replace('data: [[', '{')
			string = string.replace(']]},', '}')
			string = string.replace(',', ':')
			string = string.replace(': ', ', ')
			string = string.replace('[', '')
			string = string.replace(']', '')
			tempco = eval(string)
			od = collections.OrderedDict(sorted(tempco.items()))
			y = od.values()
			N = len(y)
			x = range(N)
			B = (sum(x[i] * y[i] for i in xrange(N)) - 1./N*sum(x)*sum(y)) / (sum(x[i]**2 for i in xrange(N)) - 1./N*sum(x)**2)
			A = 1.*sum(y)/N - B * 1.*sum(x)/N
			string = 'data: ['
			for key, value in od.iteritems(): 	
			    string+=("[%s, %s], " % (key, A+B*key))
			string+=']},'
			string = string.replace(', ]},', ']},')
			print string