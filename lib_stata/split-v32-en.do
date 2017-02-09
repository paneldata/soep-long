use temp/v32/en/pl.dta, clear
keep cid-plb0593
saveold temp/v32/en/plxxxxx1.dta, replace

use temp/v32/en/pl.dta, clear
keep plb0594-pld0136
saveold temp/v32/en/plxxxxx2.dta, replace

use temp/v32/en/pl.dta, clear
keep pld0137-plg0100
saveold temp/v32/en/plxxxxx3.dta, replace

use temp/v32/en/pl.dta, clear
keep plg0101-pli0130
saveold temp/v32/en/plxxxxx4.dta, replace

use temp/v32/en/pl.dta, clear
keep pli0131-fpop
saveold temp/v32/en/plxxxxx5.dta, replace
