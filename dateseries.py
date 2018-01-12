


from datetime import datetime

def dateseries(yyyymmddhhmmss)

	timestamp = str(yyyymmddhhmmss)
	yyyy = timestamp[0:4]
	mm = timestamp[4:6]
	dd = timestamp[6:8]
	hh = timestamp[8:10]
	mm = timestamp[10:12]
	ss = timestamp[12:14]
	
	# Use existing function from datetime module to convert strings in date
	# i.e. 
	# dateseries = datetime.datetime(yyyy,mm,dd,hh,mm,ss)
	
	return dataseries
	
