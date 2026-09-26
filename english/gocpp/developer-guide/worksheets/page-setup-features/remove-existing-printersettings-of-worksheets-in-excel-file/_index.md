---
title: Remove Existing PrinterSettings of Worksheets in Excel file with Golang via C++
linktitle: Remove Existing PrinterSettings of Worksheets
type: docs
weight: 60
url: /go-cpp/remove-existing-printersettings-of-worksheets-in-excel-file/
description: Learn how to remove existing PrinterSettings of a worksheet inside the Excel file through the Page Setup object programmatically using Aspose.Cells with Golang via C++.
keywords: remove printer settings of worksheet c++, remove printer settings of excel worksheet c++
---

## **Possible Usage Scenarios**
Sometimes developers want to prevent Excel from including *.bin* files of printer settings in the saved XLSX files. Printer settings files are located under *“[file "root"]\xl\printerSettings”.* This document explains how to remove existing printer settings using Aspose.Cells APIs.

## **Remove Existing PrinterSettings of Worksheets in Excel file**
Aspose.Cells allows you to remove existing printer settings specified for different sheets in the Excel file. The following sample code illustrates how to remove existing printer settings for all the worksheets in the workbook. Please see its [sample Excel file](45056020.xlsx), [output Excel file](45056021.xlsx), console output as well as the screenshot for a reference.

## **Screenshot**
![todo:image_alt_text](remove-existing-printersettings-of-worksheets-in-excel-file_1.png)

## **Sample Code**
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RemoveExistingPrintersettingsOfWorksheetsInExcelFile.go" >}}

## **Console Output**
{{< highlight java >}}

PrinterSettings of this worksheet exist.

Sheet Name: Sheet1

Paper Size: PaperLegal

Printer settings of this worksheet are now removed by setting it to null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet2

Paper Size: PaperEnvelopeB5

Printer settings of this worksheet are now removed by setting it to null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet3

Paper Size: PaperA6

Printer settings of this worksheet are now removed by setting it to null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet4

Paper Size: PaperA3

Printer settings of this worksheet are now removed by setting it to null.

{{< /highlight >}}
{{< app/cells/assistant language="go" >}}
