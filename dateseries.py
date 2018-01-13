


import datetime

def dateseries(yyyymmddhhmmss)

	timestamp = str(yyyymmddhhmmss)
	yyyy = dbl(timestamp[0:4])
	mm = dbl(timestamp[4:6])
	dd = dbl(timestamp[6:8])
	hh = dbl(timestamp[8:10])
	mm = dbl(timestamp[10:12])
	ss = dbl(timestamp[12:14])

  # Use existing function from datetime module to convert strings in date	
	dateseries = datetime.datetime(yyyy,mm,dd,hh,mm,ss)
	
	return dataseries
	
