---
title: Accessing Cells of a Worksheet
type: docs
weight: 10
url: /cpp/accessing-cells-of-a-worksheet/
---

{{% alert color="primary" %}} 

We know that all worksheets may contain data that is basically stored in cells (with which a worksheet is made up of). A cell is a basic part of a worksheet that is used to construct the whole worksheet as a sequence of rows and columns. Before we try to access data from a worksheet, we would need to get access to its cells. So, in this topic, we will discuss some basic approaches to access worksheet cells at runtime using Aspose.Cells.

{{% /alert %}} 
## **Accessing Cells**
Aspose.Cells provides a class [IWorkbook](https://apireference.aspose.com/cells/cpp/class/aspose.cells.i_workbook/) that represents an Excel file. The [IWorkbook](https://apireference.aspose.com/cells/cpp/class/aspose.cells.i_workbook/) class contains a [Worksheets](https://apireference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection/) collection that allows to access each worksheet in the Excel file. A worksheet is represented by the [IWorksheet](https://apireference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet/) class. The [IWorksheet](https://apireference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet/) class provides a [Cells](https://apireference.aspose.com/cells/cpp/class/aspose.cells.i_cells/) collection that represents all cells in the worksheet.

We can use [Cells](https://apireference.aspose.com/cells/cpp/class/aspose.cells.i_cells/) collection to access cells in a worksheet. Aspose.Cells provides three basic approaches to access cells in a worksheet:

1. Using cell name.
1. Using a cell's row and column index.
1. Using a cell index in the [Cells](https://apireference.aspose.com/cells/cpp/class/aspose.cells.i_cells/) collection

{{% alert color="primary" %}} 

We have mentioned that the 3rd approach is the fastest and the 1st approach is the slowest one. The performance difference between the approaches is very small so don't worry about performance degradation, whichever approach you use.

{{% /alert %}} 
### **Using Cell Name**
Developers can access any specific cell by passing its cell name to the [Cells](https://apireference.aspose.com/cells/cpp/class/aspose.cells.i_cells/) collection of the [IWorksheet](https://apireference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet/) class as an index.

If you create a blank worksheet at start, the count of [Cells](https://apireference.aspose.com/cells/cpp/class/aspose.cells.i_cells/) collection is zero. When you use this approach to access a cell, it will check whether this cell exists in the collection or not. If yes, it returns the cell object in the collection otherwise, it creates a new [ICell](https://apireference.aspose.com/cells/cpp/class/aspose.cells.i_cell/) object, adds the object to the [Cells](https://apireference.aspose.com/cells/cpp/class/aspose.cells.i_cells/) collection and then returns that object. This approach is the easiest way to access the cell if you are familiar with Microsoft Excel but it's the slowest one as compared to other approaches.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AccessingCellsOfWorksheet-AccessingCellsUsingCellName.cpp" >}}
### **Using Row & Column Index of the Cell**
Developers can access any specific cell by passing the indices of its row and column to the [Cells](https://apireference.aspose.com/cells/cpp/class/aspose.cells.i_cells/) collection of the [IWorksheet](https://apireference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet/) class. This approach works in the same way as that of the first approach.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AccessingCellsOfWorksheet-AccessingCellsUsingRowAndColumnIndexOfTheCell.cpp" >}}
## **Accessing Maximum Display Range of Worksheet**
Aspose.Cells allows developers to access a worksheet's maximum display range. The maximum display range - the range of cells between the first and last cell with content - is useful when you need to copy, select or display the entire contents of a worksheet in an image.

You can access a worksheet's maximum display range using [MaxDisplayIRange](https://apireference.aspose.com/cells/cpp/class/aspose.cells.i_cells/#ad351277ccaa0a4e1e8cd0693a1e2e988) method of the [Cells](https://apireference.aspose.com/cells/cpp/class/aspose.cells.i_cells/) collection.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AccessingCellsOfWorksheet-AccessingMaximumDisplayRangeOfWorksheet.cpp" >}}
