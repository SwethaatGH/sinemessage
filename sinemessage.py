import math,shutil,sys,time
width,height=shutil.get_terminal_size()
width-=1
print("enter a message with max",width//2,"chars")
while (True):
	message=input("enter your message:")
	if 1<=len(message)<=(width//2):
		print("message must be within 1 to",width//2,"chars")
		break
step=0.0
multiplier=(width-len(message))/2
try:
	while (True):
		sinofstep = math.sin(step)
		padding = ' '*int((sinofstep+1)*multiplier)
		print(padding+message)
		time.sleep(0.1)
		step+=0.25
except KeyboardInterrupt:
	sys.exit()