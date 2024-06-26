#!/usr/bin/env python3

from time import strptime, mktime
from math import inf
import sys

records = list()

statistics_time_processing = {
  "minimum": +inf,
  "maximum": 0,
  "average": 0,
  "median": 0
}

number_requests_resource = dict()

with open(sys.argv[1]) as input:
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
counter_responses_error = 0

for record in records:
  time_processing = mktime(record["end_time"]) - mktime(record["start_time"])
  sum_time_processing += time_processing

  if time_processing > statistics_time_processing["maximum"]:
    statistics_time_processing["maximum"] = time_processing

  if time_processing < statistics_time_processing["minimum"]:
    statistics_time_processing["minimum"] = time_processing

  list_time_processing.append(time_processing)

  if (record["resp_code"] > 400) or ("error" in record["resp_body"]):
    counter_responses_error += 1

  resource = record["req_path"]

  if resource in number_requests_resource:
    number_requests_resource[resource] += 1

  else:
    number_requests_resource[resource] = 1

statistics_time_processing["average"] = sum_time_processing / len(records)
half = len(list_time_processing) // 2

list_time_processing.sort()

if len(list_time_processing) % 2 == 0:
  statistics_time_processing["median"] = (list_time_processing[half] + list_time_processing[half - 1]) / 2

else:
  statistics_time_processing["median"] = list_time_processing[half]

for characteristic in statistics_time_processing:
  print(characteristic, statistics_time_processing[characteristic])

print(f'Процент ошибочных запросов: {counter_responses_error / len(records) * 100}')

for resource in number_requests_resource:
  print(resource, number_requests_resource[resource])