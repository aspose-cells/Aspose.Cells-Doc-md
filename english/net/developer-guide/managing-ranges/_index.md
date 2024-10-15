---
title: Managing Ranges
linktitle: Ranges
type: docs
weight: 105
url: /net/managing-ranges/
---

## **Introduction**

In Excel, you can select multiple cells with a mouse box selection, the set of selected cells is called "Range".

For example, you can click the left mouse button in Cell "A1" of the Excel and then drag to cell "C4". The rectangular area you selected can also be easily created as an object by using Aspose.Cells.

Here is how to create range, put value, set style, and do more operations to the "Range" object.

## **Managing Ranges Using Aspose.Cells**

Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) class contains a [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) collection that allows access to each worksheet in an Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) class. The [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) class provides a [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) collection.

### **Create Range**

When you want to create a rectangular area that extends over A1:C4, you can use the following code:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Range-Create.cs" >}}

### **Put value into the Cells of the Range**

Say you have a range of cells that extends over A1:C4. The matrix makes 4 * 3 = 12 cells. The individual range cells are arranged sequentially: Range[0,0], Range[0,1], Range[0,2], Range[1,0], Range[1,1], Range[1,2], Range[2,0], Range[2,1], Range[2,2], Range[3,0], Range[3,1], Range[3,2].

The following example shows how to input some values into the cells of the Range.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Range-PutValue.cs" >}}

### **Set style of the Cells of the Range**

The following example shows how to set style of the cells of the Range.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Range-SetStyle.cs" >}}

### **Get CurrentRegion of the Range**

CurrentRegion is a property that returns a Range object that represents the current region. 

The current region is a range bounded by any combination of blank rows and blank columns. Read-only.

In excel, you can get CurrentRegion area by:
1. Select an area(range1) with the mouse box.
2. Click "Home - Editing - Find & Select - Go To Special - Currect region", or use "Ctrl+Shift+*", you will see excel automatically helps you select an area(range2), now you made it, range2 is the CurrentRegion of range1.

Using Aspose.Cells, you can use "Range.CurrentRegion" property to perform the same function.

Please downloaded the following test file, open it in excel, use the mouse box to select an area "A1:D7", then click "Ctrl+Shift+*", you will see area "A1:C3" selected.

[current_region.xlsx](current_region.xlsx)

Now please run the following example, see how it works in Aspose.Cells:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Range-CurrentRegion.cs" >}}


## **Advance topics**
- [AutoFill range of Excel file](/cells/net/autofill-ranges/)
- [Copy Ranges of Excel](/cells/net/copy-ranges-of-Excel/)
- [Copy Range Data Only](/cells/net/copy-range-data-only/)
- [Copy Range Data with Style](/cells/net/copy-range-data-with-style/)
- [Copy Range Style Only](/cells/net/copy-range-style-only/)
- [Create Union Range](/cells/net/create-union-range/)
- [Cut and Paste Range](/cells/net/cut-and-paste-cells/)
- [Delete Ranges](/cells/net/delete-ranges-from-Excel/)
- [Get Address Cell Count Offset Entire Column and Entire Row of the Range](/cells/net/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/)
- [Insert Ranges](/cells/net/insert-ranges-to-Excel/)
- [Merge or Unmerge Range of Cells](/cells/net/merge-or-unmerge-range-of-cells/)
- [Move Range of Cells in a Worksheet](/cells/net/move-range-of-cells-in-a-worksheet/)
- [Create Workbook and Worksheet Scoped Named Ranges](/cells/net/create-workbook-and-worksheet-scoped-named-ranges/)
- [Search and Replace Data in a Range](/cells/net/search-and-replace-data-in-a-range/)
{{< app/cells/assistant language="csharp" >}}