use temp/v31/en/pl.dta, clear
keep cid-plb0400
saveold temp/v31/en/plxxxxx1.dta, replace

use temp/v31/en/pl.dta, clear
keep plb0401-plc0320
saveold temp/v31/en/plxxxxx2.dta, replace

use temp/v31/en/pl.dta, clear
keep plc0321-ple0090
saveold temp/v31/en/plxxxxx3.dta, replace

use temp/v31/en/pl.dta, clear
keep ple0091-plh0247
saveold temp/v31/en/plxxxxx4.dta, replace

use temp/v31/en/pl.dta, clear
keep plh0248-fpop
saveold temp/v31/en/plxxxxx5.dta, replace
