---
title: Find if the Worksheet is Dialog Sheet
type: docs
weight: 100
url: /java/find-if-the-worksheet-is-dialog-sheet/
---

## **Possible Usage Scenarios**

Dialog Sheet is an old format of the sheet that contains a dialog box. Such a sheet could be inserted by an older version of Microsoft Excel e.g. 2003 as shown in this screenshot. It can also be inserted with VBA in newer versions e.g. Microsoft Excel 2016.

![todo:image_alt_text](find-if-the-worksheet-is-dialog-sheet_1.png)

You can find if the sheet is a dialog sheet or some other type of sheet with [**Worksheet.Type**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Type) property provided by Aspose.Cells. If it returns enumeration value [**SheetType.DIALOG**](https://reference.aspose.com/cells/java/com.aspose.cells/sheettype#DIALOG), then it means, you are dealing with a dialog sheet.

## **Find if the Worksheet is Dialog Sheet**

The following sample code loads the [sample Excel file](64716841.xlsx) that contains a dialog sheet. It checks the [**Worksheet.Type**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Type) property compares it with [**SheetType.DIALOG**](https://reference.aspose.com/cells/java/com.aspose.cells/sheettype#DIALOG) and then prints the message. Please see the console output of the sample code given below for more help.

## **Sample Code**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Worksheets-FindIfWorksheetIsDialogSheet.java" >}}

## **Console Output**

{{< highlight java >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}
