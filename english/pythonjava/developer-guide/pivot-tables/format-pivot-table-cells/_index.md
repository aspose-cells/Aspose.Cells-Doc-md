---
title: Format Pivot Table Cells
type: docs
weight: 20
url: /python-java/format-pivot-table-cells/
---

{{% alert color="primary" %}}

Sometimes, you want to format pivot table cells. For example, you want to apply a background color to pivot table cells. Aspose.Cells provides two methods [**PivotTable.formatAll()**](https://reference.aspose.com/cells/python-java/asposecells.api/pivottable#formatAll(com.aspose.cells.Style)) and [**PivotTable.format()**](https://reference.aspose.com/cells/python-java/asposecells.api/pivottable#format(int,%20int,%20com.aspose.cells.Style)), which you can use for this purpose.

[**PivotTable.formatAll()**](https://reference.aspose.com/cells/python-java/asposecells.api/pivottable#formatAll(com.aspose.cells.Style)) applies the style to the entire pivot table while [**PivotTable.format()**](https://reference.aspose.com/cells/python-java/asposecells.api/pivottable#format(int,%20int,%20com.aspose.cells.Style)) applies the style to a single cell of the pivot table.

{{% /alert %}}

The following sample code formats the entire pivot table with a light blue color and then formats the second table row yellow.

**The input pivot table, before executing the code**

![todo:image_alt_text](format-pivot-table-cells_1.png)

**The ouput pivot table, after the executing the code**

![todo:image_alt_text](format-pivot-table-cells_2.png)

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "PivotTables-FormatCells.py" >}}
