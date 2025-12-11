---
title: Add Cells to Microsoft Excel Formula Watch Window with Golang via C++
linktitle: Add Cells to Formula Watch Window
description: Learn how to use Aspose.Cells for C++ to add cells to the formula watch window in Excel. Load or create an Excel file, manipulate cells, set formulas, and save the modified file.
keywords: Aspose.Cells, Excel, Formula Watch Window, Cells, Adding, C++
type: docs
weight: 60
url: /go-cpp/add-cells-to-microsoft-excel-formula-watch-window/
---

## **Possible Usage Scenarios**

The Microsoft Excel Watch Window is a useful tool that conveniently monitors cell values and their formulas. You can open the *Watch Window* in Microsoft Excel by clicking *Formulas > Watch Window*. It has the *Add Watch* button that can be used to add cells for inspection. Similarly, you can use the [**Worksheet.CellWatches.Add()**](https://reference.aspose.com/cells/go-cpp/cellwatchcollection/add_int_int/) method to add cells to the *Watch Window* using the Aspose.Cells API.

## **Add Cells to Microsoft Excel Formula Watch Window**

The following sample code sets the formula of cells C1 and E1 and adds both of them to the Watch Window. It then saves the workbook as an [output Excel file](67338481.xlsx). If you open the output Excel file and view the *Watch Window*, you will see both cells as shown in this screenshot.

![todo:image_alt_text](add-cells-to-microsoft-excel-formula-watch-window_1.png)

## **Sample Code**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AddCellsToMicrosoftExcelFormulaWatchWindow.go" >}}