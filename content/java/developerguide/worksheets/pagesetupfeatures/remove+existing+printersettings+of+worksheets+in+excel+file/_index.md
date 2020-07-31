---
title : "Remove Existing PrinterSettings of Worksheets in Excel file" 
description : "" 
weight : 16134 
toc : false
type: docs
url: /java/developerguide/worksheets/pagesetupfeatures/remove+existing+printersettings+of+worksheets+in+excel+file/
---

# Aspose.Cells for Java : Remove Existing PrinterSettings of Worksheets in Excel file


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Possible Usage Scenarios](#possible-usage-scenarios)
*   2 [Remove Existing PrinterSettings of Worksheets in Excel file](#remove-existing-printersettings-of-worksheets-in-excel-file)
*   3 [Screenshot](#screenshot)
*   4 [Sample Code](#sample-code)
*   5 [Console Output](#console-output)
{{< /panel >}}
 

## Possible Usage Scenarios

Sometimes developers want to prevent Excel from including *.bin* files of printer settings in the saved XLSX files. Printer settings files are located under *“\[file "root"\]\\xl\\printerSettings”*. This document explains how to remove existing printer settings using Aspose.Cells APIs.

## Remove Existing PrinterSettings of Worksheets in Excel file

Aspose.Cells allows you to remove existing printer settings specified for different sheets in the Excel file. The following sample code illustrates how to remove existing printer settings for all the worksheets in the workbook. Please see its[sample Excel file](https://docs2.aspose.com/cells/java/attachments/44860273/45056023.xlsx), [output Excel file](https://docs2.aspose.com/cells/java/attachments/44860273/45056024.xlsx), console output as well as a screenshot for a reference.

## Screenshot

![](https://docs2.aspose.com/cells/java/attachments/44860273/45056022.png)

## Sample Code

## Console Output

{{< code lang="cs" >}}
PrinterSettings of this worksheet exist.
Sheet Name: Sheet1
Paper Size: 5
Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.
Sheet Name: Sheet2
Paper Size: 34
Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.
Sheet Name: Sheet3
Paper Size: 70
Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.
Sheet Name: Sheet4
Paper Size: 8
Printer settings of this worksheet are now removed by setting it null.
{{< /code >}}

