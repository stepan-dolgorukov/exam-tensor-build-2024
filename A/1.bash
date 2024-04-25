#!/usr/bin/env bash

directory_target=$1
version_bound=$2

directories=\
"$(find ${directory_target}\
  -mindepth 1\
  -maxdepth 1\
  -type d)"

version_bound_x=$(( $(cut -d "." -f 1 <<< ${version_bound}) ))
version_bound_y=$(( $(cut -d "." -f 2 <<< ${version_bound}) ))
version_bound_z=$(( $(cut -d "." -f 3 <<< ${version_bound}) ))
version_bound_tail=$(cut -d "." -f 4 <<< ${version_bound})

for directory in ${directories}; do

  product=$(basename $(cut -d "_" -f 1 <<< ${directory}))
  version=$(cut -d "_" -f 2 <<< ${directory})

  if [ ${version} == ${directory} ]; then
    continue
  fi

  version_x=$(( $(cut -d "." -f 1 <<< ${version}) ))
  version_y=$(( $(cut -d "." -f 2 <<< ${version}) ))
  version_z=$(( $(cut -d "." -f 3 <<< ${version}) ))
  version_tail=$(cut -d "." -f 4 <<< ${version})

  if [ -z ${version} ]; then
    continue
  fi

  # X_b < X
  if [ ${version_bound_x} -lt ${version_x} ]; then
    continue
  fi

  # X_b > X
  if [ ${version_bound_x} -gt ${version_x} ]; then
    rm -r ${directory}
    continue
  fi

  # X_b == X

  # Y_b < Y
  if [ ${version_bound_y} -lt ${version_y} ]; then
    continue
  fi

  # Y_b > Y
  if [ ${version_bound_y} -gt ${version_y} ]; then
    rm -r ${directory}
    continue
  fi

  # X_b == X, Y_b == Y

  # Z_b < Z
  if [ ${version_bound_y} -lt ${version_bound_z} ]; then
    continue
  fi

  # Z_b > Z
  if [ ${version_bound_z} -gt ${version_z} ]; then
    rm -r ${directory}
    continue
  fi

  # T_b >_{lex} T
  if [[ ${version_bound_tail} > ${version_tail} ]]; then
    rm -r ${directory}
    continue
  fi

done