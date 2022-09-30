import datetime
import os

date = datetime.datetime.now()
d_m = date.month
d_y = date.year
d_d = date.day

def main():
	try:
		os.mkdir(f"{d_y}")
	except Exception as e:
		pass
	try:
		open(f'{d_y}/{d_m}.txt','r')
	except Exception as e:
		file = open(f'{d_y}/{d_m}.txt','w')
		for i in range(33):
			file.write("\n")
		file.close()
#if __name__=="__main__":
#	main()