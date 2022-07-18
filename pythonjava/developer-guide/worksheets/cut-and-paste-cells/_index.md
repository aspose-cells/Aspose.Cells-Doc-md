---
title: Cut and Paste Cells
type: docs
weight: 30
url: /python-java/cut-and-paste-cells/
---

## **Cut and Paste Cells**
Aspose.Cells for Python via Java provides the ability to cut and paste cells. For this, the API provides the [insertCutCells](https://reference.aspose.com/cells/python/asposecells.api/cells#insertCutCells\(com.aspose.cells.Range,%20int,%20int,%20int\)) method of the [Cells](https://reference.aspose.com/cells/python/asposecells.api/Cells) collection. The [insertCutCells](https://reference.aspose.com/cells/python/asposecells.api/cells#insertCutCells\(com.aspose.cells.Range,%20int,%20int,%20int\)) method accepts the following parameters.

- [Range](https://reference.aspose.com/cells/python/asposecells.api/Range): The range of cells to be cut.
- Row Index: The index of the row to insert cells.
- Column Index: The index of the column to insert cells.
- [ShiftType](https://reference.aspose.com/cells/python/asposecells.api/ShiftType): The shift direction of the columns.

The following code snippet demonstrates how to cut and paste cells within a worksheet.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-CutAndPasteCells.py" >}}
