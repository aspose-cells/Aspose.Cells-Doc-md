---
title: Filter VBA Project while loading a workbook
type: docs
weight: 70
url: /java/filter-vba-project-while-loading-a-workbook/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**
Some .xlsm/.xlsb files have an extremely large amount of macros (or very, very long macros). Aspose.Cells will unconditionally load this (meta) data when opening such workbooks. You may need to control this through `LoadDataFilterOptions` when you really only need to extract sheet names for a large number of workbooks, thus skipping such unneeded content. This filter is provided by introducing a new option `LoadDataFilterOptions.VBA`.

## **Sample Code**
The following sample code loads a workbook such that VBA is filtered out. A sample file for testing this feature can be downloaded from the following link:

[sampleMacroEnabledWorkbook.xlsm](79527951.xlsm)

// Set the load options; we do not want to load VBA
LoadOptions loadOptions = new LoadOptions(LoadFormat.AUTO);
loadOptions.setLoadFilter(new LoadFilter(LoadDataFilterOptions.ALL & ~LoadDataFilterOptions.VBA));

// Create a workbook object from the sample Excel file using the load options
Workbook book = new Workbook(srcDir + "sampleMacroEnabledWorkbook.xlsm", loadOptions);

// Save the workbook
book.save(outDir + "OutputSampleMacroEnabledWorkbook.xlsm", SaveFormat.XLSM);
{{< app/cells/assistant language="java" >}}
