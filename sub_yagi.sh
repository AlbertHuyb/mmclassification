export yagi=25
export pcts=(1.0)
export ports=(29500 29501 29502 29503 29504)

for((i=0;i<${#pcts[@]};i++)) do

    pct=${pcts[i]}
    port=${ports[i]}
    config=sss_fruit_${pct}_pretrain

    qsub -N CP${pct} \
         -o /home/zhijie/logs/SonyAI/${config}.log \
         -q main.q@yagi${yagi}.vision.is.tohoku \
         -v config=$config -v port=$port \
         train_sss.sh

done;
