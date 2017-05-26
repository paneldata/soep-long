---
name: soep-long
label: SOEPlong
config:
    variables:
        label-table: True
---

# SOEPlong

## Citation

* **Title:** SOEPlong
* **Label:** Long format of the German Socio-Economic Panel Study (SOEP)
* **Citation guideline:** see SOEP-Core
* **Persistent identifier:** 10.5684/soep.v32.1
* **Investigators/authors:** Jürgen Schupp; Peter Krause; Jan Goebel; Martin Kroh; Carsten
  Schröder; Charlotte Bartels; Klaudia Erhardt; Alexandra Fedorets; Marco
  Giesselmann; Markus Grabka; Simon Kühne; David Richter; Rainer
  Siegers; Paul Schmelzer; Christian Schmitt; Daniel Schnitzlein; Knut Wenzig

## Study info

SOEPlong is a complete and user-friendly data format for all wave-specific data, primary and generated, from SOEPcore. In the classic delivery, the data are provided annually as individual files and.  Ppriority is given to faithful reproduction of the data and the original sequence based on the respective survey instrument. On the basis of structured programmes, SOEPlong includes all SOEPcore data as timely and consistent long-variables. 
The time-consuming data preparation required for analyses is facilitated by SOEPlong in many ways: (1) SOEPlong provides all variables as time-consistent long-variables – this makes individual collecting, renaming, and recoding of variables in the time course unnecessary. (2) If required, the long-variables are already recoded (e.g., changing categories in the time course or income data in euro) and integrated (i.e. variables from P/H-OST / PAUSL / P_MIG datasets).  All changed variables are additionally provided as original coded  long-variables for the respective years for alternative recoding. (3) Moreover, figures for all long-variables are provided which document temporal monitoring, time-course distribution (bar charts and violin plots), acquisition and consistency of the population (missings) in the time course.
Provenance details infrom the biography and life history dataquestionnaires are only shared in SOEPlong (BIO). Moreover, the variables partner-status and partner-ID – also for non-realised household members – as well as enumerated weights are only available in SOEPlong (P/H-PFADL).
Specifically, the following files are provided in SOEPlong Version v301 (prepared biography and spell data are already available as long or spell format in SOEPcore and can be linked in the same way in SOEPlong)

A more detailled overview can be found in the [Desktop Companion](http://about.paneldata.org/soep/dtc/) in chapter [Principles of data structure](http://about.paneldata.org/soep/dtc/data-structure.html).

## Missings

|Code | Meaning|
|:----:|-----|
|-1|no answer /don`t know|
|-2|does not apply|
|-3|implausible value|
|-4|inadmissible multiple response|
|-5|not included in this version of the questionnaire|
|-6|version of questionnaire with modified filtering|
|-8|question not part of the survey programm this year*

*Only applicable for datasets in long format.

## Data set

Table  Matching of SOEPlong and cross-sectional datasets from SOEP-CORE

| SOEPlong | SOEPcore                                         |
|----------|--------------------------------------------------|
|_Tracking Files_|
| ppfadl   | ppfad, phrf                                      |
| hpfadl   | hpfad, hhrf                                      |
|_Register-Files_|
| pbrutto  | bpbrutto, ..., zpbrutto, bapbrutto, bbpbrutto, ... |
| hbrutto  | bhbrutto, ..., zhbrutto, bahbrutto, bbhbrutto, ... |
|_Respondents-Files_|
| pl       | ap, ..., zp, bap, bbp, ...                       |
| hl       | ah, ..., zh, bah, bbh, ...                       |
| kidl     | kidlong (akind, ..., zkind, bakind, bbkind, ...) |
| bio      | biolela, mlela, ..., zlela, balela, bblela, ...  |
| jugend   | qjugend, ..., zjugend, bajugend, bbjugend, ...   |
|_Generated Files_|
| pgen     | apgen, ..., zpgen, bapgen, bbpgen, ...           |
| hgen     | ahgen, ..., zhgen, bahgen, bbhgen, ...           |
| pkal     | apkal, ..., zpkal, bapkal, bbpkal, ...           |
| pequiv   | apequiv, ..., zpequiv, bapequiv, bbpequiv, ...   |


