#!/usr/bin/env python
"""reducer_ex3.py"""
from itertools import groupby
from operator import itemgetter
import sys

def read_mapper_output(file, separator='\t'):
    for line in file:
        yield line.rstrip().split(separator, 1)

def main(separator='\t'):
    data = read_mapper_output(sys.stdin, separator=separator)
    results = []
    for current_word, group in groupby(data, itemgetter(0)):
        try:
            total_count = sum(int(count) for current_word, count in group)
            results.append((total_count, current_word))
        except ValueError:
            pass

    results.sort(reverse=True)
    for count, word in results[:3]:
        print("%s%s%d" % (word, separator, count))

if __name__ == "__main__":
    main()
