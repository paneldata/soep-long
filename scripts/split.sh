rm -r temp/*
cp -r /home/soepdist/ddionrails/soep-long/v31 temp/
stata-se -b lib_stata/split_de.do
stata-se -b lib_stata/split_en.do
rm temp/v31/*/pl.dta
