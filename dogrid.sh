#!/bin/bash
rm -rf self_loop_scale.txt

for i in `seq 25 40`;
do
	python change_run_sh.py $i
	echo "$i*100" | bc >> self_loop_scale.txt
	./run.sh > a.out
	tail -n 1 a.out >> self_loop_scale.txt
done