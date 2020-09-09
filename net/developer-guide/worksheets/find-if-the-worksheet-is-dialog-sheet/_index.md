---
title: Find if the Worksheet is Dialog Sheet
type: docs
weight: 90
url: /net/find-if-the-worksheet-is-dialog-sheet/
---

## **Possible Usage Scenarios**

Dialog Sheet is an old format of sheet that contains a dialog box. Such sheet could be inserted by an older version of Microsoft Excel e.g. 2003 as shown in this screenshot. It can also be inserted with VBA in newer versions e.g. Microsoft Excel 2016.

![todo:image_alt_text](find-if-the-worksheet-is-dialog-sheet_1.png)

You can find if the sheet is a dialog sheet or some other type of sheet with [**Worksheet.Type**](https://apireference.aspose.com/cells/net/aspose.cells/worksheet/properties/type) property provided by Aspose.Cells. If it returns enumeration value [**SheetType.Dialog**](https://apireference.aspose.com/cells/net/aspose.cells/sheettype), then it means, you are dealing with dialog sheet.

## **Find if the Worksheet is Dialog Sheet**

The following sample code loads the [sample Excel file](64716820.xlsx) that contains a dialog sheet. It checks the [**Worksheet.Type**](https://apireference.aspose.com/cells/net/aspose.cells/worksheet/properties/type) property compares it with [**SheetType.Dialog**](https://apireference.aspose.com/cells/net/aspose.cells/sheettype) and then prints the message. Please see the console output of the sample code given below for more help.

## **Sample Code**

{{< gist "aspose-com-gists" "922f990b02cf4e04a328bd6f37029af8" "Worksheets-FindIfWorksheetIsDialogSheet.cs" >}}

## **Console Output**

{{< highlight java >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}
