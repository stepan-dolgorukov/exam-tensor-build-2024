#!/usr/bin/env bash

directory_target=${1}

directories=\
"$(find ${directory_target}\
  -mindepth 1\
  -maxdepth 1\
  -type d)"

for directory in ${directories}; do
  files_directory=$(find ${directory} -type f)

  for file in ${files_directory}; do
    file_removed_tail=$(cut -d "." -f 1,2 <<< ${file})

    # Если файл является основным
    if [ ${file_removed_tail} = ${file} ]; then
      files_extra_file=$(find ${directory} -wholename "${file}.*" -type f)

      size_file_extra_maximum=$(( $(stat --printf="%s" ${file}) ))
      file_extra_replace_main=${file}

      for file_extra in ${files_extra_file}; do
        size_file_extra=$(( $(stat --printf="%s" ${file_extra}) ))

        if [ ${size_file_extra_maximum} -lt ${size_file_extra} ]; then
          file_extra_replace_main=${file_extra}
          size_file_extra_maximum=${size_file_extra}
        fi
      done

      if [ ${file} != ${file_extra_replace_main} ]; then
        echo 'mv' ${file_extra_replace_main} ${file}
      fi

      length=$(( $(wc -w <<< ${files_extra_file}) ))

      if [ ${length} -ne 0 ]; then
        echo 'rm' ${files_extra_file}
      fi

    # Если файл является дополнительным
    else
      files_extra_file=$(find ${directory} -wholename "${file_removed_tail}.*" -type f)
      length=$(( $(wc -w <<< ${files_extra_file}) ))

      if [ ${length} -gt 1 ] && [ ! -f ${file_removed_tail} ]; then
          echo 'У файла' ${file_removed_tail} 'дополнительных файлов:' ${length}
          exit 1
        fi

      if [ ! -f ${file_removed_tail} ]; then
        echo 'mv' ${file} ${file_removed_tail}
      fi
    fi
  done
done