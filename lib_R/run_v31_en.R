library(r2ddi)

dir2xml(
    "temp/v31/en/",
    "r2ddi/v31/en/",
    missing_codes=-9:-1,
    my_cores=30)
