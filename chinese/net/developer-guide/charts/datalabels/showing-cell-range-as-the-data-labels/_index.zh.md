---
title: 将单元格范围显示为数据标签
description: 学习如何使用 Aspose.Cells for .NET 在图表中显示一系列单元格作为数据标签。我们的指南将演示如何将标签链接到数据源并格式化它们，以在图表中提供准确和有意义的信息。
keywords: Aspose.Cells for .NET，图表，数据标签，单元格范围，数据源，格式化，准确性，有意义的信息。
type: docs
weight: 130
url: /zh/net/showing-cell-range-as-the-data-labels/
---

{{% alert color="primary" %}}

在 Microsoft Excel 2013 中，您可以显示数据标签的单元格范围。Aspose.Cells 支持此功能。

{{% /alert %}}

## **复选框显示单元格范围作为数据标签**

在 Microsoft Excel 中显示单元格范围作为数据标签:

1. 选择系列数据标签，单击右键打开上下文菜单。
1. 选择 **格式数据标签**。标签选项将显示。
1. 选择或取消选中选项 **标签包含 - 来自单元格的值**。

以下示例代码访问图表系列数据标签，并将 [**DataLabels.ShowCellRange**](https://reference.aspose.com/cells/net/aspose.cells.charts/datalabels/properties/showcellrange) 属性设置为 **true**，以选择 **标签包含 - 来自单元格的值** 选项。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-ShowCellRangeAsDataLabels-ShowCellRangeAsDataLabels.cs" >}}
