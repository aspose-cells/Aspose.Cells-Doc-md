---
title: Format Pivot Table Cells
type: docs
weight: 20
url: /java/format-pivot-table-cells/
---

{{% alert color="primary" %}}

Sometimes, you want to format pivot table cells. For example, you want to apply a background color to pivot table cells. Aspose.Cells provides two methods [**PivotTable.formatAll()**](https://apireference.aspose.com/cells/java/com.aspose.cells/pivottable#formatAll(com.aspose.cells.Style)) and [**PivotTable.format()**](https://apireference.aspose.com/cells/java/com.aspose.cells/pivottable#format(int,%20int,%20com.aspose.cells.Style)), which you can use for this purpose.

[**PivotTable.formatAll()**](https://apireference.aspose.com/cells/java/com.aspose.cells/pivottable#formatAll(com.aspose.cells.Style)) applies the style to the entire pivot table while [**PivotTable.format()**](https://apireference.aspose.com/cells/java/com.aspose.cells/pivottable#format(int,%20int,%20com.aspose.cells.Style)) applies the style to a single cell of the pivot table.

{{% /alert %}}

The following sample code formats the entire pivot table with a light blue color and then formats the second table row yellow.

**The input pivot table, before executing the code**

![todo:image_alt_text](format-pivot-table-cells_1.png)

**The ouput pivot table, after the executing the code**

![todo:image_alt_text](format-pivot-table-cells_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FormatPivotTableCells-FormatPivotTableCells.java" >}}
