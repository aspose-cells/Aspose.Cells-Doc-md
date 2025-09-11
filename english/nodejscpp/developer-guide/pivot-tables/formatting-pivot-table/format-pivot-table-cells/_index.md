---
title: Format Pivot Table Cells
type: docs
weight: 30
url: /nodejs-cpp/format-pivot-table-cells/
description: How to format pivot table cells with Aspose.Cells for Node.js via C++.
keywords: Format pivot table cells.
---

{{% alert color="primary" %}}

Sometimes, you want to format pivot table cells. For example, you want to apply background color to pivot table cells. Aspose.Cells for Node.js via C++ provides two methods [**PivotTable.formatAll(style)**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#formatAll-style-) and [**PivotTable.format(row, column, style)**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#format-number-number-style-), which you can use for this purpose.

[**PivotTable.formatAll(style)**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#formatAll-style-) applies the style to entire pivot table while [**PivotTable.format(row, column, style)**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#format-number-number-style-) applies the style to a single cell of the pivot table.

{{% /alert %}}
The following sample code loads the [sample Excel file](pivot_format.xlsx) that contains two pivot tables, and achieve the operation of formatting the entire pivot table and formatting individual cells in the pivot table.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-FormatPivotTableCells-1.js" >}}

## Related Articles

- [Formatting Pivot Table](/cells/nodejs-cpp/formatting-pivot-table/)
- [Working with data display formats of DataField in Pivot Table](/cells/nodejs-cpp/working-with-data-display-formats-of-datafield-in-pivot-table/)
{{< app/cells/assistant language="nodejs-cpp" >}}