---
title: Managing Ranges with Golang via C++
linktitle: Ranges
type: docs
weight: 105
url: /go-cpp/managing-ranges/
description: Learn how to manage ranges in Excel files using Aspose.Cells with Golang via C++. Create, modify, and style ranges programmatically.
---

## **Introduction**

In Excel, you can select multiple cells with a mouse box selection; the set of selected cells is called a **Range**.

For example, you can click the left mouse button in cell **A1** of the workbook and then drag to cell **C4**. The rectangular area you selected can also be easily created as an object by using Aspose.Cells.

Here is how to create a range, put values, set styles, and perform more operations on the **Range** object.

## **Managing Ranges Using Aspose.Cells**

Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) class contains a [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) collection that allows access to each worksheet in an Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/go-cpp/worksheet/) class. The [**Worksheet**](https://reference.aspose.com/cells/go-cpp/worksheet/) class provides a [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) collection.

### **Create Range**

When you want to create a rectangular area that extends over **A1:C4**, you can use the following code:

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ManagingRanges.go" >}}

### **Put values into the cells of the range**

Say you have a range of cells that extends over **A1:C4**. The matrix contains 4 × 3 = 12 cells. The individual range cells are arranged sequentially: `Range[0,0]`, `Range[0,1]`, `Range[0,2]`, `Range[1,0]`, `Range[1,1]`, `Range[1,2]`, `Range[2,0]`, `Range[2,1]`, `Range[2,2]`, `Range[3,0]`, `Range[3,1]`, `Range[3,2]`.

The following example shows how to input some values into the cells of the range.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ManagingRanges-1.go" >}}

### **Set the style of the cells of the range**

The following example shows how to set the style of the cells of the range.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ManagingRanges-2.go" >}}

### **Get CurrentRegion of the range**

`CurrentRegion` is a property that returns a **Range** object that represents the current region.  

The current region is a range bounded by any combination of blank rows and blank columns. It is read‑only.

In Excel, you can get the CurrentRegion area by:

1. Selecting an area (**range1**) with the mouse box.  
2. Clicking **Home → Editing → Find & Select → Go To Special → Current region**, or using **Ctrl+Shift+\***. Excel will automatically select an area (**range2**); now you have it—**range2** is the CurrentRegion of **range1**.

Using Aspose.Cells, you can use the `Range.CurrentRegion` property to perform the same function.

Please **download** the following test file, open it in Excel, use the mouse box to select an area **A1:D7**, then press **Ctrl+Shift+\***; you will see area **A1:C3** selected.

[current_region.xlsx](current_region.xlsx)

Now please run the following example to see how it works in Aspose.Cells:

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ManagingRanges-3.go" >}}

## **Advanced topics**
- [AutoFill range of Excel file](/cells/cpp/autofill-ranges/)
- [Copy Ranges of Excel](/cells/cpp/copy-ranges-of-Excel/)
- [Copy Range Data Only](/cells/cpp/copy-range-data-only/)
- [Copy Range Data with Style](/cells/cpp/copy-range-data-with-style/)
- [Copy Range Style Only](/cells/cpp/copy-range-style-only/)
- [Create Union Range](/cells/cpp/create-union-range/)
- [Cut and Paste Range](/cells/cpp/cut-and-paste-cells/)
- [Delete Ranges](/cells/cpp/delete-ranges-from-Excel/)
- [Get Address Cell Count Offset Entire Column and Entire Row of the Range](/cells/cpp/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/)
- [Insert Ranges](/cells/cpp/insert-ranges-to-Excel/)
- [Merge or Unmerge Range of Cells](/cells/cpp/merge-or-unmerge-range-of-cells/)
- [Move Range of Cells in a Worksheet](/cells/cpp/move-range-of-cells-in-a-worksheet/)
- [Create Workbook and Worksheet Scoped Named Ranges](/cells/cpp/create-workbook-and-worksheet-scoped-named-ranges/)
- [Search and Replace Data in a Range](/cells/cpp/search-and-replace-data-in-a-range/)