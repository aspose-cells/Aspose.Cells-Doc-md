---
title: Find if the Worksheet is Dialog Sheet with Go
linktitle: Find if the Worksheet is Dialog Sheet
type: docs
weight: 90
url: /gocpp/find-if-the-worksheet-is-dialog-sheet/
description: Dialog Sheet is an older sheet format. This article provides instructions and sample code for determining programmatically whether an Excel worksheet is a Dialog Sheet using the Go API.
keywords: find excel worksheet dialog type go, worksheet dialog go
ai_search_scope: cells_go
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

Dialog Sheet is an older sheet format that contains a dialog box. Such a sheet could be inserted by an earlier version of Microsoft Excel, e.g., 2003, as shown in this screenshot. It can also be inserted with VBA in newer versions, e.g., Microsoft Excel 2016.

![todo:image_alt_text](find-if-the-worksheet-is-dialog-sheet_1.png)

You can find if the sheet is a dialog sheet or some other type of sheet with the [**Worksheet.GetType()**](https://reference.aspose.com/cells/go/aspose.cells/worksheet/gettype/) property provided by Aspose.Cells. If it returns the enumeration value [**SheetType.Dialog**](https://reference.aspose.com/cells/go/aspose.cells/sheettype/), then it means you are dealing with a dialog sheet.

## **Find if the Worksheet is Dialog Sheet**

The following sample code loads the [sample Excel file](64716820.xlsx) that contains a dialog sheet. It checks the [**Worksheet.GetType()**](https://reference.aspose.com/cells/go/aspose.cells/worksheet/gettype/) property, compares it with [**SheetType.Dialog**](https://reference.aspose.com/cells/go/aspose.cells/sheettype/), and then prints the message. Please see the console output of the sample code given below for more help.

## **Sample Code**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FindIfWorksheetIsDialogSheet.go" >}}

## **Console Output**

{{< highlight go >}}
Worksheet is a Dialog Sheet.
{{< /highlight >}}