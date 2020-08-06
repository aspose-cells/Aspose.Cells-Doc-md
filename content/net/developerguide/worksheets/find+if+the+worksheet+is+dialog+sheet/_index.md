---
title : "Find if the Worksheet is Dialog Sheet" 
description : "" 
weight : 12168 
toc : false
type: docs
url: /net/developerguide/worksheets/find+if+the+worksheet+is+dialog+sheet/
---

# Aspose.Cells for .NET : Find if the Worksheet is Dialog Sheet


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Possible Usage Scenarios](#possible-usage-scenarios)
*   2 [Find if the Worksheet is Dialog Sheet](#find-if-the-worksheet-is-dialog-sheet)
*   3 [Sample Code](#sample-code)
*   4 [Console Output](#console-output)
{{< /panel >}}
 

## Possible Usage Scenarios

Dialog Sheet is an old format of sheet that contains a dialog box. Such sheet could be inserted by an older version of Microsoft Excel e.g. 2003 as shown in this screenshot. It can also be inserted with VBA in newer versions e.g. Microsoft Excel 2016.

![image](64716826.png)

You can find if the sheet is a dialog sheet or some other type of sheet with [Worksheet.Type](https://apireference.aspose.com/net/cells/aspose.cells/worksheet/properties/type) property provided by Aspose.Cells. If it returns enumeration value [SheetType.Dialog](https://apireference.aspose.com/net/cells/aspose.cells/sheettype), then it means, you are dealing with dialog sheet.

## Find if the Worksheet is Dialog Sheet

The following sample code loads the [sample Excel file](https://docs2.aspose.com/cells/net/attachments/64454872/64716820.xlsx) that contains a dialog sheet. It checks the [Worksheet.Type](https://apireference.aspose.com/net/cells/aspose.cells/worksheet/properties/type) property compares it with [SheetType.Dialog ](https://apireference.aspose.com/net/cells/aspose.cells/sheettype)and then prints the message. Please see the console output of the sample code given below for more help.

## Sample Code

## Console Output

{{< code lang="cs" >}}
Worksheet is a Dialog Sheet.
{{< /code >}}

