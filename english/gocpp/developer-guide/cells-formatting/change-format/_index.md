---
title: Change the format of a cell with Golang via C++
linktitle: Change the format of a cell
description: How to use Aspose.Cells library in C++ to change the formatting of cells, including font, color, border, etc. By adjusting these properties, you have more control over how cells look and appear.
keywords: Aspose.Cells, cell formatting, C++, font, color, border
type: docs
weight: 20
url: /go-cpp/how-to-change-format-of-cell/
---

## **Possible Usage Scenarios**
When you want to highlight certain data, you can change the style of the cells.

## **How to change the format of a cell in Excel**

To change the format of a single cell in Excel, follow these steps:

1. Open Excel and open the workbook that contains the cell you want to format.

2. Locate the cell you want to format.

3. Right-click on the cell and select "Format Cells" from the context menu. Alternatively, you can select the cell and go to the Home tab in the Excel ribbon, click on the "Format" dropdown in the "Cells" group, and select "Format Cells".

4. The "Format Cells" dialog box will appear. Here, you can choose various formatting options to apply to the selected cell. For example, you can change the font style, font size, font color, number format, borders, background color, etc. Explore the different tabs in the dialog box to access various formatting options.

5. After making the desired formatting changes, click the "OK" button to apply the formatting to the selected cell.

## **How to change the format of a cell Using C++**

To change the format of a cell using Aspose.Cells, you can use the following methods:
1. [Cell.SetStyle(Style style)](https://reference.aspose.com/cells/go-cpp/cell/setstyle_style/)
2. [Cell.SetStyle(Style style, bool explicitFlag)](https://reference.aspose.com/cells/go-cpp/cell/setstyle_style/)
3. [Cell.SetStyle(Style style, StyleFlag flag)](https://reference.aspose.com/cells/go-cpp/cell/setstyle_style/)

## **Sample Code**
In this example, we create an Excel workbook, add some sample data, access the first worksheet, and get two cells("A2" and "B3"). Then, we get the style of the cell, set various formatting options (e.g., font color, bold), and change the format to the cell. Finally, we save the workbook to a new file.
![todo:image_alt_text](change-format.png)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChangeFormat.go" >}}