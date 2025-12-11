---
title: Managing Ranges
linktitle: Ranges
type: docs
weight: 105
url: /python-net/managing-ranges/
description: This article shows how to manage ranges by the Aspose.Cells for Python via .NET API.
keywords: Python Excel Library, Python manage ranges, Create range in Python, Python Put value into the Cells of the Range, Python Set style of the Cells of the Range, Python Get CurrentRegion of the Range.
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Introduction**

In Excel, you can select multiple cells with a mouse‑box selection; the set of selected cells is called a **Range**.

For example, you can click the left mouse button in cell **A1** of the worksheet and then drag to cell **C4**. The rectangular area you selected can also be easily created as an object by using Aspose.Cells for Python via .NET.

Here is how to create a range, put values, set style, and perform more operations on the **Range** object.

## **Managing Ranges Using Aspose.Cells for Python Excel Library**

Aspose.Cells for Python via .NET provides a class, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) class contains a **Worksheets** collection that allows access to each worksheet in an Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) class. The [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) class provides a [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) collection.

## **How to Create Range**

When you want to create a rectangular area that extends over **A1:C4**, you can use the following code:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-Create.py" >}}

## **How to Put Value into the Cells of the Range**

Say you have a range of cells that extends over **A1:C4**. The matrix has **4 × 3 = 12** cells. The individual range cells are arranged sequentially.

The following example shows how to input some values into the cells of the **Range**.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-PutValue.py" >}}

## **How to Set Style of the Cells of the Range**

The following example shows how to set the style of the cells of the **Range**.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-SetStyle.py" >}}

## **How to Get CurrentRegion of the Range**

**CurrentRegion** is a property that returns a **Range** object that represents the current region.  

The current region is a range bounded by any combination of blank rows and blank columns. It is read‑only.

In Excel, you can obtain the CurrentRegion area by:
1. Selecting an area (**range1**) with the mouse box.
2. Clicking **Home → Editing → Find & Select → Go To Special → Current region**, or using **Ctrl+Shift+***. Excel will automatically expand the selection to **range2**, which is the CurrentRegion of **range1**.

Using Aspose.Cells for Python via .NET, you can use the `Range.current_region` property to perform the same function.

Please download the following test file, open it in Excel, use the mouse box to select an area **A1:D7**, then press **Ctrl+Shift+***; you will see area **A1:C3** selected.

[current_region.xlsx](current_region.xlsx)

Now please run the following example to see how it works in Aspose.Cells for Python via .NET:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-CurrentRegion.py" >}}

## **Advanced topics**
- [AutoFill range of Excel file](/cells/python-net/autofill-ranges/)
- [Copy Ranges of Excel](/cells/python-net/copy-ranges-of-excel/)
- [Copy Range Data Only](/cells/python-net/copy-range-data-only/)
- [Copy Range Data with Style](/cells/python-net/copy-range-data-with-style/)
- [Copy Range Style Only](/cells/python-net/copy-range-style-only/)
- [Create Union Range](/cells/python-net/create-union-range/)
- [Cut and Paste Range](/cells/python-net/cut-and-paste-cells/)
- [Delete Ranges](/cells/python-net/delete-ranges-from-excel/)
- [Get Address Cell Count Offset Entire Column and Entire Row of the Range](/cells/python-net/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/)
- [Insert Ranges](/cells/python-net/insert-ranges-to-excel/)
- [Merge or Unmerge Range of Cells](/cells/python-net/merge-or-unmerge-range-of-cells/)
- [Move Range of Cells in a Worksheet](/cells/python-net/move-range-of-cells-in-a-worksheet/)
- [Create Workbook and Worksheet Scoped Named Ranges](/cells/python-net/create-workbook-and-worksheet-scoped-named-ranges/)
- [Search and Replace Data in a Range](/cells/python-net/search-and-replace-data-in-a-range/)

{{< app/cells/assistant language="python-net" >}}
