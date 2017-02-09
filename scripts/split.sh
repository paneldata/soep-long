rm -r temp/*
cp -r /home/soepdist/ddionrails/soep-long/v32 temp/
stata-se -b lib_stata/split-v32-de.do
stata-se -b lib_stata/split-v32-en.do
rm temp/v32/*/pl.dta
