---
title : "Find if the Worksheet is Dialog Sheet" 
description : "" 
weight : 12140 
toc : false
type: docs
url: /java/developerguide/worksheets/find+if+the+worksheet+is+dialog+sheet/
---

# Aspose.Cells for Java : Find if the Worksheet is Dialog Sheet


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Possible Usage Scenarios](#possible-usage-scenarios)
*   2 [Find if the Worksheet is Dialog Sheet](#find-if-the-worksheet-is-dialog-sheet)
*   3 [Sample Code](#sample-code)
*   4 [Console Output](#console-output)
{{< /panel >}}
 

## Possible Usage Scenarios

Dialog Sheet is an old format of the sheet that contains a dialog box. Such a sheet could be inserted by an older version of Microsoft Excel e.g. 2003 as shown in this screenshot. It can also be inserted with VBA in newer versions e.g. Microsoft Excel 2016.

![image](64716840.png)

You can find if the sheet is a dialog sheet or some other type of sheet with [Worksheet.Type](https://apireference.aspose.com/java/cells/com.aspose.cells/worksheet#Type) property provided by Aspose.Cells. If it returns enumeration value [SheetType.DIALOG](https://apireference.aspose.com/java/cells/com.aspose.cells/sheettype#DIALOG), then it means, you are dealing with a dialog sheet.

## Find if the Worksheet is Dialog Sheet

The following sample code loads the [sample Excel file](https://docs2.aspose.com/cells/java/attachments/64454897/64716841.xlsx) that contains a dialog sheet. It checks the [Worksheet.Type](https://apireference.aspose.com/java/cells/com.aspose.cells/worksheet#Type) property compares it with [SheetType.DIALOG](https://apireference.aspose.com/java/cells/com.aspose.cells/sheettype#DIALOG) and then prints the message. Please see the console output of the sample code given below for more help.

## Sample Code

## Console Output

{{< code lang="cs" >}}
Worksheet is a Dialog Sheet.
{{< /code >}}

