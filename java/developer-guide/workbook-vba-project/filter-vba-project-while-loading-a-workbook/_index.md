---
title: Filter VBA Project while loading a workbook
type: docs
weight: 70
url: /java/filter-vba-project-while-loading-a-workbook/
---

## **Possible Usage Scenarios**
Some .xlsm/.xslb files have extremely large amount of macros (or very, very long macros). Aspose.Cells will unconditionally load this (meta) data when opening such workbooks. You may require to control this though LoadDataFilterOptions, when you really only need to extract sheet names for a large number of workbooks thus skipping over such unneeded content. This filter is provided by introducing new option LoadDataFilterOptions.VBA.
## **Sample Code**
The following sample code loads a workbook such that only VBA is filtered. Sample file for testing this feature can be downloaded from the following link:

[sampleMacroEnabledWorkbook.xlsm](attachments/79331431/79527951.xlsm)

// Set the load options, we do not want to load VBA
LoadOptions loadOptions = new LoadOptions(LoadFormat.AUTO);
loadOptions.setLoadFilter(new LoadFilter(LoadDataFilterOptions.ALL & ~LoadDataFilterOptions.VBA));

// Create workbook object from sample excel file using load options
Workbook book = new Workbook(srcDir + "sampleMacroEnabledWorkbook.xlsm", loadOptions);

// Save the output in pdf format
book.save(outDir + "OutputSampleMacroEnabledWorkbook.xlsm", SaveFormat.XLSM);
