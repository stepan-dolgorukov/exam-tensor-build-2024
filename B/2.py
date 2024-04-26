#!/usr/bin/env python3

import sys
from os import walk, remove, rmdir

directory_to_clean = sys.argv[1]
count_type_files_deleted = {
  "unknown": 0,
  "directory": 0
}

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

    remove(prefix + regular)
    # print(prefix + regular)

for prefix, directories, _ in walk(directory_to_clean, topdown=False):

  for directory in directories:
    count_type_files_deleted["directory"] += 1

    if prefix[-1] != ('/'):
      prefix += '/'

    rmdir(prefix + directory)
    # print(prefix + directory)

for type in count_type_files_deleted:
  if count_type_files_deleted[type] > 0:
    print(f"{type}: {count_type_files_deleted[type]}")
