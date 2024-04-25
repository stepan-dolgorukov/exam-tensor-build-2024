#!/usr/bin/env bash

directory_source=${1}
directory_destination=${2}

files_source=$(find ${directory_source} -wholename '*.zip' -o -wholename '*.7z')

for file in ${files_source}; do
  file_removed_prefix=$(sed -e "s/^\///" <<< ${file/#${directory_source}})
  # echo ${file_removed_prefix}

  version=$(cut -d "/" -f 1 <<< ${file_removed_prefix})
  service=$(cut -d "/" -f 2 <<< ${file_removed_prefix})
  number_build=$(cut -d "/" -f 3 <<< ${file_removed_prefix})

  base_name=$(cut -d "/" -f 4 <<< ${file_removed_prefix})
  product=$(cut -d "_" -f 1 <<< ${base_name})
  system_operating=$(cut -d "_" -f 2 <<< ${base_name})
  architecture=$(cut -d "_" -f 3,4 <<< ${base_name} | cut -d "." -f 1)
  type_archieve=$(cut -d "." -f 2 <<< ${base_name})

  # echo ${version} ${service} ${number_build} ${product} ${system_operating} ${architecture}
  # echo ${service}/${version}/${number_build}/${system_operating}_${architecture}/${product}.${type_archieve}

  directory="${directory_destination}/${service}/${version}/${number_build}/${system_operating}_${architecture}"

  mkdir -p ${directory}
  cp ${file} ${directory}/${product}.${type_archieve}
done