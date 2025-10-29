---
title: 将单元格范围显示为数据标签
description: 学习如何使用 Aspose.Cells for Python via .NET 在图表中将一范围的单元格显示为数据标签。我们的指南将展示如何将标签链接到您的数据源，并进行格式化，以在图表中提供准确且有意义的信息。
keywords: Aspose.Cells for Python via .NET，绘图，数据标签，单元格范围，数据源，格式化，准确性，有意义的信息。
type: docs
weight: 130
url: /zh/python-net/showing-cell-range-as-the-data-labels/
---

{{% alert color="primary" %}}

在 Microsoft Excel 2013 中，您可以显示数据标签的单元格范围。Aspose.Cells for Python via .NET 支持此功能。

{{% /alert %}}

## **复选框显示单元格范围作为数据标签**

在Microsoft Excel中显示单元格范围作为数据标签：

1. 选择系列数据标签，右键单击以打开上下文菜单。
1. 选择**格式数据标签**。标签选项会显示。
1. 选择或清除选项 **标签包含 - 来自单元格的值**。

下面的示例代码访问图表系列数据标签，并将 [**DataLabels.show_cell_range**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/datalabels/show_cell_range) 属性设置为 **true** 以选择 **标签包含 - 来自单元格的值** 选项。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ShowCellRangeAsDataLabels.py" >}}
{{< app/cells/assistant language="python-net" >}}
