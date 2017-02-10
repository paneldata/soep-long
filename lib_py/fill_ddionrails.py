import os, sys, re, glob
import pandas as pd

sys.path.append(os.path.expanduser("~/github/ddi.py/"))

from ddi.onrails.repos import merge_instruments, dor1, copy, convert_r2ddi

def datasets():
    x = pd.read_csv("metadata/datasets.csv")
    x.rename(columns={
        "study":"study_name",
        "dataset":"dataset_name",
        "period":"period_name",
        "analysis_unit":"analysis_unit_name",
        "conceptual_dataset":"conceptual_dataset_name",
    }, inplace=True)
    dor1.lower_all_names(x)
    x.to_csv("ddionrails/datasets.csv", index=False)

def variables():
    x = pd.read_csv("metadata/variables.csv")
    x.rename(columns={
        "study":"study_name",
        "dataset":"dataset_name",
        "varname":"variable_name",
        "concept":"concept_name",
    }, inplace=True)
    valid = x.ix[ : , ("study_name", "dataset_name", "variable_name")].duplicated() == False
    x = x.ix[valid]
    dor1.lower_all_names(x)
    x.to_csv("ddionrails/variables.csv", index=False)

def concepts():
    x = pd.read_csv("metadata/concepts.csv")
    x.rename(columns={
        "concept":"concept_name",
    }, inplace=True)
    valid = x.ix[ : , "concept_name"].duplicated() == False
    x = x.ix[valid]
    dor1.lower_all_names(x)
    x.to_csv("ddionrails/concepts.csv", index=False)

def fix_pl():
    os.system("""
        rm -rf temp/r2ddi
        mkdir -p temp
        cp -r r2ddi temp
    """)
    for name in glob.glob("temp/r2ddi/*/*/plxxx*"):
        print(name)
        with open(name, "r") as f:
            text = f.read()
        with open(name, "w") as f:
            text = re.sub(r'plxxxxx[0-9]', "pl", text)
            f.write(text)

def main():
    copy.study()
    datasets()
    variables()
    fix_pl()
    convert_r2ddi.Parser(version="v32", r2ddi_path="temp/r2ddi").write_json()

if __name__ == "__main__":
    main()
