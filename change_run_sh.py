import sys

f = open("./run.sh","r").readlines()
num_int = 0
if int(sys.argv[1]) == 0:
	num_int = 1
else:
	num_int = int(sys.argv[1])*100
print(f[54])	
f[54] = "\t" + str(num_int) + ' 30000 data/train data/lang exp/mono_ali exp/tri1' + '\n'
print(f[54])
#f[12] = 'totgauss=' +str(num_int) + ' # Target #Gaussians.\n'
# f1 = open("./steps/train_mono.sh","w")
# for line in f:
# 	f1.write(line)