import os
import json
import sys
from functools import reduce

def proc_filepath(fp_obj):
    return map(lambda x: os.path.join(fp_obj[0][1:], x), fp_obj[2])

def main(path):
    files = list(reduce(lambda x, y: x + y, map(proc_filepath, os.walk(path))))
    with open("sitemap.json", "w") as f:
        json.dump(files, f)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Insufficient params")
    main(sys.argv[1])
