import glob
import os
import re

import pandas as pd
from ddi.onrails.repos import convert_r2ddi, copy, dor1, merge_instruments


def datasets():
    x = pd.read_csv("metadata/datasets.csv")
    x.rename(
        columns={
            "study": "study_name",
            "dataset": "dataset_name",
            "period": "period_name",
            "analysis_unit": "analysis_unit_name",
            "conceptual_dataset": "conceptual_dataset_name",
        },
        inplace=True,
    )
    dor1.lower_all_names(x)
    x.to_csv("ddionrails/datasets.csv", index=False)


def variables():
    x = pd.read_csv("metadata/variables.csv")
    x.rename(
        columns={
            "study": "study_name",
            "dataset": "dataset_name",
            "varname": "variable_name",
            "concept": "concept_name",
        },
        inplace=True,
    )
    valid = (
        x.ix[:, ("study_name", "dataset_name", "variable_name")].duplicated() == False
    )
    x = x.ix[valid]
    dor1.lower_all_names(x)
    x.to_csv("ddionrails/variables.csv", index=False)


def concepts():
    x = pd.read_csv("metadata/concepts.csv")
    x.rename(columns={"concept": "concept_name"}, inplace=True)
    valid = x.ix[:, "concept_name"].duplicated() == False
    x = x.ix[valid]
    dor1.lower_all_names(x)
    x.to_csv("ddionrails/concepts.csv", index=False)


def fix_pl():
    os.system(
        """
        rm -rf temp/r2ddi
        mkdir -p temp
        cp -r r2ddi temp
    """
    )
    for name in glob.glob("temp/r2ddi/*/*/plxxx*"):
        print(name)
        with open(name, "r") as f:
            text = f.read()
        with open(name, "w") as f:
            text = re.sub(r"plxxxxx[0-9]", "pl", text)
            f.write(text)


def main():
    copy.study()
    datasets()
    variables()
    dor1.transformations()
    fix_pl()
    convert_r2ddi.Parser(
        "soep-long", version="v32", r2ddi_path="temp/r2ddi"
    ).write_json()
    try:
        os.system(
            """
            rm -r ddionrails/topics
            cp -r ../soep-core/ddionrails/topics/ ddionrails/
        """
        )
        print("[INFO] Copy topics from soep-core")
    except:
        print("[ERROR] Couldn't copy topics from soep-core")


if __name__ == "__main__":
    main()
