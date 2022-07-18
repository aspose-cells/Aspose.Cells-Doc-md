---
title: Accessing Cells of a Worksheet
type: docs
weight: 10
url: /net/accessing-cells-of-a-worksheet/
---

{{% alert color="primary" %}}

We know that all worksheets may contain data that is basically stored in cells (with which a worksheet is made up of). A cell is a basic part of a worksheet that is used to construct the whole worksheet as a sequence of rows and columns. Before we try to access data from a worksheet, we would need to get access to its cells. So, in this topic, we will discuss some basic approaches to access worksheet cells at runtime using Aspose.Cells.

{{% /alert %}}

## **Accessing Cells**

Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) that represents an Excel file. The [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) class contains a [**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) that allows access to each worksheet in the Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) class. The [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) class provides a [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) collection that represents all cells in the worksheet.

We can use [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) collection to access cells in a worksheet. Aspose.Cells provides three basic approaches to access cells in a worksheet:

1. Using the cell name.
1. Using a cell's row and column index.
1. Using a cell index in the [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) collection

**IMPORTANT:** We have mentioned that the 3rd approach is the fastest and the 1st approach is the slowest one. The performance difference between the approaches is very small so don't worry about performance degradation, whichever approach you use.

### **Using Cell Name**

Developers can access any specific cell by passing its cell name to the [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) collection of the [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) class as an index.

If you create a blank worksheet at the start, the count of [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) collection is zero. When you use this approach to access a cell, it will check whether this cell exists in the collection or not. If yes, it returns the cell object in the collection otherwise, it creates a new [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) object, adds the object to the [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) collection and then returns the object. This approach is the easiest way to access the cell if you are familiar with Microsoft Excel but it's the slowest one as compared to other approaches.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-UsingCellName-1.cs" >}}

### **Using Row & Column Index of the Cell**

Developers can access any specific cell by passing the indices of its row and column to the [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) collection of the [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) class.

This approach works in the same way as that of the first approach.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-UsingRowAndColumnIndexOfCell-1.cs" >}}

### **Using Cell Index in Cells Collection**

A cell can also be accessed by passing the cell's numeric index to the [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) collection.

If you use this approach to access cells, an exception can be thrown if the numeric index of the cell is out of range. This approach is the fastest one to access the cells but an important thing to know is that if you use this approach to access a cell object, the numeric index may change after new cells are added to the [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) collection. The cell objects in the [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) collection are internally sorted by row and column indices.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-UsingCellIndexInCellsCollection-1.cs" >}}

## **Accessing Maximum Display Range of Worksheet**

Aspose.Cells allows developers to access a worksheet's maximum display range. The maximum display range - the range of cells between the first and last cell with content - is useful when you need to copy, select, or display the entire contents of a worksheet in an image.

You can access a worksheet's maximum display range using [**Worksheet.Cells.MaxDisplayRange**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdisplayrange). The following sample code illustrates how to access the [**MaxDisplayRange**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdisplayrange) property.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-AccessingMaximumDisplayRangeofWorksheet-1.cs" >}}
