#!/usr/bin/env python3

from time import strptime, mktime
from math import inf
import datetime

records = list()

statistics_time_processing = {
  "minimum": +inf,
  "maximum": 0,
  "average": 0,
  "median": 0
}

with open("input.txt") as input:
  line = str()

  while line := input.readline():
    components_line = line.split(" | ")
    record = dict()

    record["start_time"] = strptime(components_line[0], "%d.%m.%Y %H:%M:%S")
    record["end_time"] = strptime(components_line[1], "%d.%m.%Y %H:%M:%S")
    record["req_path"] = components_line[2]
    record["resp_code"] = int(components_line[3])
    record["resp_body"] = components_line[4]

    records.append(record)

sum_time_processing = 0
list_time_processing = list()

for record in records:
  time_processing = mktime(record["end_time"]) - mktime(record["start_time"])
  sum_time_processing += time_processing

  if time_processing > statistics_time_processing["maximum"]:
    statistics_time_processing["maximum"] = time_processing

  if time_processing < statistics_time_processing["minimum"]:
    statistics_time_processing["minimum"] = time_processing

  list_time_processing.append(time_processing)

statistics_time_processing["average"] = sum_time_processing / len(records)
half = len(list_time_processing) // 2

list_time_processing.sort()

if len(list_time_processing) % 2 == 0:
  statistics_time_processing["median"] = (list_time_processing[half] + list_time_processing[half - 1]) / 2

else:
  statistics_time_processing["median"] = list_time_processing[half]

print(statistics_time_processing)