---
title: Find if the Worksheet is Dialog Sheet
type: docs
weight: 90
url: /python-net/find-if-the-worksheet-is-dialog-sheet/
description: Dialog Sheet is an old format of sheet. This article provides instructions and sample code for determining programmatically whether an Excel worksheet is a Dialog Sheet using Aspose.Cells for Python via .NET Library.
keywords: Python Excel Library, Python find excel worksheet dialog type, worksheet dialog in python.
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

Dialog Sheet is an old sheet format that contains a dialog box. Such a sheet could be inserted by an older version of Microsoft Excel, e.g., 2003, as shown in this screenshot. It can also be inserted with VBA in newer versions, e.g., Microsoft Excel 2016.

![todo:image_alt_text](find-if-the-worksheet-is-dialog-sheet_1.png)

You can find out if the sheet is a dialog sheet or some other type of sheet with **[Worksheet.type](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/type/)**, a property provided by Aspose.Cells for Python via .NET. If it returns the enumeration value **[SheetType.DIALOG](https://reference.aspose.com/cells/python-net/aspose.cells/sheettype/)**, then it means you are dealing with a dialog sheet.

## **Find if the Worksheet is Dialog Sheet**

The following sample code loads the [sample Excel file](64716820.xlsx) that contains a dialog sheet. It checks the **Worksheet.type** property, compares it with **SheetType.DIALOG**, and then prints the message. Please see the console output of the sample code given below for more help.

## **Sample Code**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-FindIfWorksheetIsDialogSheet.py" >}}

## **Console Output**

{{< highlight java >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
