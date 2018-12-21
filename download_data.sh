#!/bin/bash

# This script will run in parallel all the

for i in 158 159 160; do
  for j in 1 2 3 4; do
    for k in 100; do
      if ([ ${i} -eq 158 ] && [ ${j} -eq 2 ]) || ([ ${i} -eq 159 ] && [ ${j} -eq 1 ]) || ([ ${i} -eq 159 ] && [ ${j} -eq 2 ]) || ([ ${i} -eq 160 ] && [ ${j} -eq 1 ]); then
        data=("../sim/parent_model_${i}_${j}_gaps${k}_0050/" "MSC${i}-T-stack${j}-Nov29-2018_iso" "particles_trimmed.tif" "gaps_actual.tif" "gaps_100x.tif" "thresh_vessels.tif" "tissue_boundary.tif" ${k} 2.234)
      else
        data=("../sim/parent_model_${i}_${j}_gaps${k}_0050/" "MSC${i}-T-stack${j}-Nov29-2018_iso" "particles_trimmed.tif" "gaps_actual.tif" "gaps_100x.tif" "thresh_vessels.tif" "tissue_boundary.tif" ${k} 2.0)
      fi
      (python2 main.py -m parent_model -p ${data[@]}) &
    done
  done
done

wait
