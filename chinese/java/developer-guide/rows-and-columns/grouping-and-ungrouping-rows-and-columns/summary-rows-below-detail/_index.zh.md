---
title: 应用小计和在详细信息下方更改大纲摘要行的方向
type: docs
weight: 100
url: /zh/java/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/
---

{{% alert color="primary" %}}

本文将解释如何将小计应用于数据并更改详细信息下方的大纲摘要行的方向。

您可以使用[**Worksheet.Cells.subtotal()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#subtotal(com.aspose.cells.CellArea,%20int,%20int,%20int[]))方法对数据应用小计。它需要以下参数。

- **CellArea** - 要应用小计的范围
- **GroupBy** - 按照哪个字段分组，作为从零开始的整数偏移量
- **Function** - 小计函数
- **TotalList** - 一个从零开始的字段偏移量数组，指示添加小计的字段
- **Replace** - 指示是否替换当前小计
- **PageBreaks** - 指示是否在组之间添加分页符
- **SummaryBelowData** - 指示是否在数据下方添加汇总

此外，您可以控制大纲**详细下面的摘要行的方向**，如以下屏幕截图所示，使用此属性。您可以在Microsoft Excel中打开此设置，路径为**数据 > 大纲 > 设置**

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_1.png)

{{% /alert %}}

## 示例

### 源文件和输出文件比较的屏幕截图

以下截图显示了示例代码中使用的源Excel文件，其中在A和B列中包含一些数据。

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_2.png)

以下截图显示了示例代码生成的输出Excel文件。正如您所看到的，小计已应用于范围**A2:B11**，大纲的方向是详细信息下方的摘要行。

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_3.png)

### 使用Java代码应用小计和更改详细信息下方的大纲摘要行的方向

以下是实现上述输出的示例代码。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ApplyingSubtotal-1.java" >}}
