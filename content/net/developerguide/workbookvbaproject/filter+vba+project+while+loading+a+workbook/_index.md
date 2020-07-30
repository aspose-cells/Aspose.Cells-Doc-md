---
title : "Filter VBA Project while loading a workbook" 
description : "" 
weight : 12326 
toc : false
type: docs
url: /net/developerguide/workbookvbaproject/filter+vba+project+while+loading+a+workbook/
---

# Aspose.Cells for .NET : Filter VBA Project while loading a workbook


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Possible Usage Scenarios](#possible-usage-scenarios)
*   2 [Sample Code](#sample-code)
{{< /panel >}}
 

 

## Possible Usage Scenarios

Some .xlsm/.xslb files have an extremely large amount of macros (or very, very long macros). Aspose.Cells will unconditionally load this (meta) data when opening such workbooks. You may require to control this though [LoadDataFilterOptions](https://apireference.aspose.com/net/cells/aspose.cells/loaddatafilteroptions) when you really only need to extract sheet names for a large number of workbooks thus skipping over such unneeded content. This filter is provided by introducing a new option, [LoadDataFilterOptions.VBA](https://apireference.aspose.com/net/cells/aspose.cells/loaddatafilteroptions).

## Sample Code

The following sample code loads a workbook such that only VBA is filtered. A sample file for testing this feature can be downloaded from the following link:

[sampleMacroEnabledWorkbook.xlsm](https://docs2.aspose.com/cells/net/attachments/79331346/79527938.xlsm)

## Attachments:

![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [sampleMacroEnabledWorkbook.xlsm](https://docs2.aspose.com/cells/net/attachments/79331346/79527938.xlsm) (application/vnd.ms-excel.sheet.macroenabled.12)  

