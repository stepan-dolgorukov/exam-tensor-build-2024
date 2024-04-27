#!/usr/bin/env bash

IFS=$'\n'

while read -r host; do
  echo ${host}

  # rsync [OPTION...] [USER@]HOST:SRC... [DEST]
  # rsync [OPTION...] SRC... [USER@]HOST:DEST
done