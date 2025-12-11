---
title: Remove Existing Printer Settings of Worksheets in an Excel File
type: docs
weight: 40
url: /java/remove-existing-printersettings-of-worksheets-in-excel-file/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**
Sometimes developers want to prevent Excel from including *.bin* files of printer settings in the saved XLSX files. Printer settings files are located under *“[file "root"]\xl\printerSettings”*. This document explains how to remove existing printer settings using Aspose.Cells APIs.

## **Remove Existing Printer Settings of Worksheets in an Excel File**
Aspose.Cells allows you to remove existing printer settings specified for different sheets in the Excel file. The following sample code illustrates how to remove existing printer settings for all the worksheets in the workbook. Please see its [sample Excel file](45056023.xlsx), [output Excel file](45056024.xlsx), console output as well as a screenshot for reference.

## **Screenshot**
![todo:image_alt_text](remove-existing-printersettings-of-worksheets-in-excel-file_1.png)

## **Sample Code**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-PageSetupFeatures-RemoveExistingPrinterSettingsOfWorksheets.java" >}}

## **Console Output**
{{< highlight java >}}

PrinterSettings for this worksheet exist.
Sheet Name: Sheet1
Paper Size: 5
Printer settings of this worksheet are now removed by setting it to null.

PrinterSettings for this worksheet exist.
Sheet Name: Sheet2
Paper Size: 34
Printer settings of this worksheet are now removed by setting it to null.

PrinterSettings for this worksheet exist.
Sheet Name: Sheet3
Paper Size: 70
Printer settings of this worksheet are now removed by setting it to null.

PrinterSettings for this worksheet exist.
Sheet Name: Sheet4
Paper Size: 8
Printer settings of this worksheet are now removed by setting it to null.

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
