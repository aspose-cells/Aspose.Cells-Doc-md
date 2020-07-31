---
title : "Accessing Cells of a Worksheet" 
description : "" 
weight : 12160 
toc : false
type: docs
url: /java/developerguide/data/accessing+cells+of+a+worksheet/
---

# Aspose.Cells for Java : Accessing Cells of a Worksheet


We know that all worksheets may contain data that is basically stored in cells (with which a worksheet is made up of). A cell is a basic part of a worksheet that is used to construct the whole worksheet as a sequence of rows and columns. Before we try to access data from a worksheet, we would need to get access to its cells. So, in this topic, we will discuss some basic approaches to access worksheet cells at runtime using Aspose.Cells.

{{< panel title="Contents Summary" style="primary" >}}
*   1 [Accessing Cells](#accessing-cells)
    *   1.1 [Using Cell Name](#using-cell-name)
    *   1.2 [Using Row & Column Index of the Cell](#using-row-&-column-index-of-the-cell)
    *   1.3 [Related Articles](#related-articles)
*   2 [Accessing Maximum Display Range of Worksheet](#accessing-maximum-display-range-of-worksheet)
{{< /panel >}}
 

## Accessing Cells

Aspose.Cells provides a class, [Workbook](https://apireference.aspose.com/java/cells/com.aspose.cells/workbook) that represents a Microsoft Excel file. The [Workbook](https://apireference.aspose.com/java/cells/com.aspose.cells/workbook) class contains a [WorksheetCollection](https://apireference.aspose.com/java/cells/com.aspose.cells/WorksheetCollection) collection that allows access to each worksheet in the Excel file. A worksheet is represented by the [Worksheet](https://apireference.aspose.com/java/cells/com.aspose.cells/Worksheet) class. The [Worksheet](https://apireference.aspose.com/java/cells/com.aspose.cells/Worksheet) class provides a [Cells](https://apireference.aspose.com/java/cells/com.aspose.cells/Cells) collection that represents all the cells in the worksheet.

We can use the [Cells](https://apireference.aspose.com/java/cells/com.aspose.cells/Cells) collection to access cells in a worksheet. Aspose.Cells provides different basic approaches for accessing cells:

1.  [Using cell name](https://docs2.aspose.com/cells/java/developerguide/data/accessing+cells+of+a+worksheet).
2.  [Using row & column index](https://docs2.aspose.com/cells/java/developerguide/data/accessing+cells+of+a+worksheet).

### Using Cell Name

Developers can access any specific cell by passing its cell name to the [Cells](https://apireference.aspose.com/java/cells/com.aspose.cells/Cells) collection of the [Worksheet](https://apireference.aspose.com/java/cells/com.aspose.cells/Worksheet) class.

If you create a blank worksheet at the start, the count of [Cells](https://apireference.aspose.com/java/cells/com.aspose.cells/Cells) collection is zero. When you use this approach to access a cell, it will check whether this cell exists in the collection or not. If yes, it returns the cell object in the collection otherwise, it creates a new [Cell](https://apireference.aspose.com/java/cells/com.aspose.cells/Cell) object, adds the object to the [Cells](https://apireference.aspose.com/java/cells/com.aspose.cells/Cells) collection and then returns the object. This approach is the easiest way to access the cell if you are familiar with Microsoft Excel but it's slower than other approaches.


  

### Using Row & Column Index of the Cell

Developers can access any specific cell by passing the indices of its row and column to the [Cells](https://apireference.aspose.com/java/cells/com.aspose.cells/Cells) collection of the [Worksheet](https://apireference.aspose.com/java/cells/com.aspose.cells/Worksheet) class.

This approach works in the same way as that of the first approach.

### Related Articles

*   [Named Ranges](https://docs2.aspose.com/cells/java/developerguide/data/named+ranges)
*   [Create Workbook (Global) and Worksheet Scoped Named Ranges](https://docs2.aspose.com/cells/java/developerguide/technicalarticles/mngworkbooksandworksheets/create+workbook+global+and+worksheet+scoped+named+ranges)

## Accessing Maximum Display Range of Worksheet

Aspose.Cells allows developers to access a worksheet's maximum display range. The maximum display range - the range of cells between the first and last cell with content - is useful when you need to copy, select, or display the entire contents of a worksheet in an image.

You can access a worksheet's maximum display range using [Worksheet.getCells().getMaxDisplayRange()](https://apireference.aspose.com/java/cells/com.aspose.cells/cells#MaxDisplayRange).

In the following figure, the selected worksheet' maximum display range is A1:G15.

**Showing the maximum display range of this worksheet**  
![](https://docs2.aspose.com/cells/java/attachments/5276742/5472473.png)

The following sample code illustrates how to access the [MaxDisplayRange](https://apireference.aspose.com/java/cells/com.aspose.cells/cells#MaxDisplayRange) property. The code generates the following output.

{{< code lang="cs" >}}
Maximum Display Range: =Sheet1!$A$1:$G$15
{{< /code >}}

