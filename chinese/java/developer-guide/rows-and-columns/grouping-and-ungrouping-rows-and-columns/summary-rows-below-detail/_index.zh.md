---
title: 应用小计和更改明细下方大纲汇总行的方向
type: docs
weight: 100
url: /zh/java/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/
---
{{% alert color="primary" %}}

本文将说明如何将小计应用于数据以及更改明细下方大纲汇总行的方向。

您可以使用将小计应用于数据[**工作表.Cells.小计（）**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#subtotal(com.aspose.cells.CellArea,%20int,%20int,%20int[])） 方法。它采用以下参数。

- **单元格区域** - 应用小计的范围
- **通过...分组** 分组依据的字段，作为从零开始的整数偏移量
- **功能** 小计功能。
- **总表** 一个从零开始的字段偏移数组，指示要添加小计的字段。
- **代替** 表示是否替换当前小计
- **分页符** 表示是否在组间添加分页符
- **汇总以下数据** 指示是否在数据下方添加摘要。

此外，您还可以控制 Outline 的方向**详细信息下方的摘要行**如以下屏幕截图所示，使用[**工作表.getOutline().SummaryRowBelow**](https://reference.aspose.com/cells/java/com.aspose.cells/outline#SummaryRowBelow)财产。您可以使用 Microsoft Excel 打开此设置**数据 > 大纲 > 设置**

![待办事项：图片_替代_文本](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_1.png)

{{% /alert %}}

## 例子

### 比较源文件和输出文件的屏幕截图

以下屏幕截图显示了以下示例代码中使用的源 Excel 文件，其中包含 A 列和 B 列中的一些数据。

![待办事项：图片_替代_文本](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_2.png)

以下屏幕截图显示了示例代码生成的输出 Excel 文件。如您所见，小计已应用于范围**A2:B11**大纲的方向是详细信息下方的摘要行。

![待办事项：图片_替代_文本](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_3.png)

### Java 应用小计和更改大纲摘要行方向的代码

这是实现如上所示输出的示例代码。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ApplyingSubtotal-1.java" >}}
