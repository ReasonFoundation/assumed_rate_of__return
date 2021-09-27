## Text extraction - Extracting "Assumed Rate of Return" in Municipal Financial Reports

This project's goal is to extract the "assumed rate of return" from about 3000 municipal 2020 financial reports in Michigan state.

The extracted result is then compared against three reported data:

* Actuarial Assumed Rate of Investment Return in "OPEB Summary and UA",
* Discount Rate in "OPEB Summary and UA", and
* Actuarial Assumed Rate of Investment Return in "Pension Summary and UA".

### 1.  Convert the original pdf files to text files

Put all pdf files to folder `MI2020`

Run file `convert.sh` to convert these pdf files into text files.

### 2. Using regular expression to extract the information of interest and the context surrounding these figures.

Run file `carf1.py` to extract all numbers associated with "investment rate of return", "discount rate".

The result is `output1.csv` file.

### 3. Comparing the extracted data against the rate in OPEB and Pension reports.

This analysis is run in `R`.

Using `output1.csv` file above to compare against Actuarial Assumed Rate of Investment Return and Discount rate in "Michigan Pension and OPEB Assumption Data 2020.xlsx".

Run `comparing_with_opeb2.Rmd` inside folder "comparing_extracted_OPEB_pension_RAnalysis".

The final result is output to `comparing_with_opeb2.html`.
