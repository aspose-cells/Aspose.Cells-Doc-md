---
title: 格式化数据透视表单元格
type: docs
weight: 20
url: /zh/python-java/format-pivot-table-cells/
---

{{% alert color="primary" %}}

有时，您希望格式化数据透视表单元格。例如，您希望为数据透视表单元格应用背景颜色。Aspose.Cells提供两种方法[**PivotTable.formatAll()**](https://reference.aspose.com/cells/python-java/asposecells.api/pivottable#formatAll(com.aspose.cells.Style)）和[**PivotTable.format()**](https://reference.aspose.com/cells/python-java/asposecells.api/pivottable#format(int,%20int,%20com.aspose.cells.Style)），您可以用于此目的。

[**PivotTable.formatAll()**](https://reference.aspose.com/cells/python-java/asposecells.api/pivottable#formatAll(com.aspose.cells.Style)）为整个数据透视表应用样式，而[**PivotTable.format()**](https://reference.aspose.com/cells/python-java/asposecells.api/pivottable#format(int,%20int,%20com.aspose.cells.Style)）为数据透视表的单个单元格应用样式。

{{% /alert %}}

以下示例代码为整个数据透视表设置浅蓝色，并为第二表行设置黄色。

**执行代码前的输入数据透视表**

![todo:image_alt_text](format-pivot-table-cells_1.png)

**执行代码后的输出数据透视表**

![todo:image_alt_text](format-pivot-table-cells_2.png)

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "PivotTables-FormatCells.py" >}}
