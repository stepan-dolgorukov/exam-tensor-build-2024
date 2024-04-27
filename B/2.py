#!/usr/bin/env python3

import sys
from os import walk, remove, rmdir
from time import sleep

directory_to_clean = sys.argv[1]
count_type_files_deleted = {
  "unknown": 0,
  "directory": 0
}

total_files = 0
counter_deleted = 0
progress = 0

for prefix, directories, regulars in walk(directory_to_clean):
  total_files += len(directories) + len(regulars)

for prefix, _, regulars in walk(directory_to_clean):

  for regular in regulars:
    parts = regular.split(".")

    if len(parts) < 2:
      count_type_files_deleted["unknown"] += 1

    else:
      extension = parts[-1]

      if not extension in count_type_files_deleted:
        count_type_files_deleted[extension] = 0

      count_type_files_deleted[extension] += 1

    if prefix[-1] != ('/'):
      prefix += '/'

    # print(prefix + regular)
    remove(prefix + regular)
    counter_deleted += 1

    progress += 24 / total_files

    print("#" * int(progress) + "." * (24 - int(progress)), end="\r")
    sleep(1)


for prefix, directories, _ in walk(directory_to_clean, topdown=False):

  for directory in directories:
    count_type_files_deleted["directory"] += 1

    if prefix[-1] != ('/'):
      prefix += '/'

    # print(prefix + directory)
    rmdir(prefix + directory)

    counter_deleted += 1
    progress += 24 / total_files

    print("#" * int(progress) + "." * (24 - int(progress)), end="\r")
    sleep(1)

print()

for type in count_type_files_deleted:
  if count_type_files_deleted[type] > 0:
    print(f"{type}: {count_type_files_deleted[type]}")
