---
title: Filter VBA Project while loading a workbook
type: docs
weight: 140
url: /net/filter-vba-project-while-loading-a-workbook/
---

## **Possible Usage Scenarios**

Some .xlsm/.xslb files have an extremely large amount of macros (or very, very long macros). Aspose.Cells will unconditionally load this (meta) data when opening such workbooks. You may require to control this though [**LoadDataFilterOptions**](https://apireference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions) when you really only need to extract sheet names for a large number of workbooks thus skipping over such unneeded content. This filter is provided by introducing a new option, [**LoadDataFilterOptions.VBA**](https://apireference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions).

## **Sample Code**

The following sample code loads a workbook such that only VBA is filtered. A sample file for testing this feature can be downloaded from the following link:

[sampleMacroEnabledWorkbook.xlsm](79527938.xlsm)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FilterVBAMacrosWhileLoadingWorkbook-1.cs" >}}
