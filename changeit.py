import sys

f = open("./steps/train_mono.sh","r").readlines()
num_int = 0
if int(sys.argv[1]) == 0:
	num_int = 1
else:
	num_int = float(sys.argv[1])*0.02
f[12] = 'scale_opts="--transition-scale=1.0 --acoustic-scale=0.1 --self-loop-scale=' + str(num_int) + '"\n'
#f[12] = 'totgauss=' +str(num_int) + ' # Target #Gaussians.\n'
f1 = open("./steps/train_mono.sh","w")
for line in f:
	f1.write(line)