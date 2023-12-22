---
title: 应用小计并更改详细信息下方大纲汇总行的方向
type: docs
weight: 100
url: /zh/net/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/
description: 了解如何使用 Aspose.Cells for .NET API 应用小计并更改详细信息下方大纲汇总行的方向。
keywords: Apply subtotal, Add subtotal, change direction of outline summary Rows below Detail, change direction of outline summary Columns to right of Detail, Create subtotal and change direction of outline summary Rows below Detail
---
{{% alert color="primary" %}}

本文将解释如何将小计应用于数据以及更改详细信息下方的大纲汇总行的方向。

您可以使用以下方法将小计应用于数据[**工作表.Cells.Subtotal()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/subtotal/index)方法。它采用以下参数。

- **细胞区域** 应用小计的范围
- **通过...分组** 分组依据的字段，作为从零开始的整数偏移量
- **功能** 小计功能。
- **总列表** 从零开始的字段偏移量数组，指示添加小计的字段。
- **代替** - 表示是否替换当前小计
- **分页符** 指示是否在组之间添加分页符
- **总结如下数据** 指示是否在数据下方添加摘要。

此外，您还可以控制轮廓的方向**详细信息下方的摘要行**如以下屏幕截图所示，使用 Worksheet.Outline.SummaryRowBelow 属性。您可以使用以下命令在 Microsoft Excel 中打开此设置**数据 > 大纲 > 设置**

![待办事项：图像_替代_文本](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_1.png)

{{% /alert %}}

## 源文件和输出文件的图像

以下屏幕截图显示了下面示例代码中使用的源 Excel 文件，其中包含 A 列和 B 列中的一些数据。

![待办事项：图像_替代_文本](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_2.png)

以下屏幕截图显示了示例代码生成的输出 Excel 文件。如您所见，小计已应用于范围 A2:B11，大纲的方向是详细信息下方的汇总行。

![待办事项：图像_替代_文本](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_3.png)

## C# 应用小计并更改大纲汇总行方向的代码

这是实现如上所示输出的示例代码。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-ApplyingSubtotalChangeSummaryDirection-1.cs" >}}
