# 20180113031506, AmaralC
# This function convert a sequence of characteres in date format using the module datetime

from datetime import datetime

def sequence_to_date(yyyyMMddhhmmss)

	timestamp = str(yyyyMMddhhmmss)
	yyyy = int(timestamp[0:4])
	MM = int(timestamp[4:6])
	dd = int(timestamp[6:8])
	hh = int(timestamp[8:10])
	mm = int(timestamp[10:12])
	ss = int(timestamp[12:14])

  # Use existing function from datetime module to convert strings in date	
	return datetime(yyyy,MM,dd,hh,mm,ss)
	
