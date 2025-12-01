---
title: Remove Existing PrinterSettings of Worksheets in Excel file
type: docs
weight: 60
url: /python-net/remove-existing-printersettings-of-worksheets-in-excel-file/
description: In this article, you will learn how to remove existing PrinterSettings of Worksheet inside the Excel file through Page Setup object programmatically with sample code using Aspose.Cells for Python Excel Library.
keywords: Python Excel Library, Python remove printer settings of worksheet, Python remove printer settings of excel worksheet.
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**
Sometimes developers want to prevent Excel from including *.bin* files of printer settings in the saved XLSX files. Printer settings files are located under *“[file "root"]\xl\printerSettings”.* This document explains how to remove existing printer settings using Aspose.Cells for Python via .NET APIs.

## **Remove Existing PrinterSettings of Worksheets in Excel file**
Aspose.Cells for Python via .NET allows you to remove existing printer settings specified for different sheets in the Excel file. The following sample code illustrates how to remove existing printer settings for all the worksheets in the workbook. Please see its [sample Excel file](45056020.xlsx), [output Excel file](45056021.xlsx), console output as well as the screenshot for a reference.

## **Screenshot**
![todo:image_alt_text](remove-existing-printersettings-of-worksheets-in-excel-file_1.png)

## **Sample Code**
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-RemoveExistingPrinterSettingsOfWorksheets.py" >}}

## **Console Output**
{{< highlight java >}}

 PrinterSettings of this worksheet exist.

Sheet Name: Sheet1

Paper Size: PaperLegal

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet2

Paper Size: PaperEnvelopeB5

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet3

Paper Size: PaperA6

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet4

Paper Size: PaperA3

Printer settings of this worksheet are now removed by setting it null.

{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
