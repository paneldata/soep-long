import os
import sys

import pandas as pd
from ddi.onrails.repos import convert_r2ddi

sys.path.append(os.path.expanduser("~/github/ddi.py/"))


def main():
    print("[INFO] Read datasets...")
    data = convert_r2ddi.Parser(version="v32")
    print("[INFO] Write JSON file...")
    data.write_json()
    print("[INFO] Write YAML file...")
    data.write_yaml()


if __name__ == "__main__":
    main()
