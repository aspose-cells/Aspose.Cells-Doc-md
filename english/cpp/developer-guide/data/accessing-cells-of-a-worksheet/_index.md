---
title: Accessing Cells of a Worksheet
type: docs
weight: 10
url: /cpp/accessing-cells-of-a-worksheet/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

We know that all worksheets contain data that is stored in cells, which make up a worksheet. A cell is a basic part of a worksheet that is used to construct the whole worksheet as a sequence of rows and columns. Before we try to access data from a worksheet, we need to get access to its cells. So, in this topic, we will discuss some basic approaches to access worksheet cells at runtime using Aspose.Cells.

{{% /alert %}} 

## **Accessing Cells**
Aspose.Cells provides a class [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) that represents an Excel file. The [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) class contains a [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) collection that allows access to each worksheet in the Excel file. A worksheet is represented by the [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) class. The [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) class provides a [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) collection that represents all cells in the worksheet.

We can use the [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) collection to access cells in a worksheet. Aspose.Cells provides three basic approaches to access cells in a worksheet:

1. Using the cell name.  
2. Using a cell's row and column index.  
3. Using a cell index in the [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) collection.

{{% alert color="primary" %}} 

We have mentioned that the third approach is the fastest and the first approach is the slowest. The performance difference between the approaches is very small, so don't worry about performance degradation, whichever approach you use.

{{% /alert %}} 

### **Using Cell Name**
Developers can access any specific cell by passing its cell name to the [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) collection of the [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) class as an index.

If you create a blank worksheet at the start, the count of the [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) collection is zero. When you use this approach to access a cell, it checks whether the cell exists in the collection. If it does, the method returns the existing cell object; otherwise, it creates a new [Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) object, adds it to the [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) collection, and then returns that object. This approach is the easiest way to access a cell if you are familiar with Microsoft Excel, but it is the slowest compared with the other approaches.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AccessingCellsOfWorksheet-AccessingCellsUsingCellName-new.cpp" >}}

### **Using Row & Column Index of the Cell**
Developers can access any specific cell by passing the indices of its row and column to the [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) collection of the [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) class. This approach works in the same way as the first approach.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AccessingCellsOfWorksheet-AccessingCellsUsingRowAndColumnIndexOfTheCell-new.cpp" >}}

## **Accessing the Maximum Display Range of a Worksheet**
Aspose.Cells allows developers to access a worksheet's maximum display range. The maximum display range—the range of cells between the first and last cell with content—is useful when you need to copy, select, or display the entire contents of a worksheet in an image.

You can access a worksheet's maximum display range using the [MaxDisplayRange](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdisplayrange/) method of the [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) collection.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AccessingCellsOfWorksheet-AccessingMaximumDisplayRangeOfWorksheet-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
