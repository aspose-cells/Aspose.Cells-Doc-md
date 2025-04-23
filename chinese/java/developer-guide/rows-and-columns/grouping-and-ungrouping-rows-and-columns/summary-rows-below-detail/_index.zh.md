---
title: 应用小计并更改大纲摘要行的方向，而不是详细信息下面的行
type: docs
weight: 100
url: /zh/java/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/
---

{{% alert color="primary" %}}

本文将解释如何对数据应用小计并更改大纲摘要行下面的方向。

你可以使用[**Worksheet.Cells.subtotal()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#subtotal-com.aspose.cells.CellArea-int-int-int[]-)方法对数据应用小计。它接受以下参数。

- **单元格区域** - 应用小计的范围
- **按组** - 按零为基础的整数偏移量分组
- **功能** - 小计功能。
- **TotalList** - 一个从零开始的字段偏移量数组，指示要添加小计的字段。
- **Replace** - 指示是否替换当前的小计
- **PageBreaks** - 指示是否在组之间添加分页符
- **SummaryBelowData** - 指示是否在数据下方添加摘要。

此外，您可以使用[**Worksheet.getOutline().SummaryRowBelow**](https://reference.aspose.com/cells/java/com.aspose.cells/outline#SummaryRowBelow)属性来控制大纲**详细下方的摘要行**的方向，如下面的屏幕截图所示。您可以在 Microsoft Excel 中使用**数据 > 大纲 > 设置**打开此设置。

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_1.png)

{{% /alert %}}

## 示例

### 源文件和输出文件的屏幕截图对比

下图显示了示例代码中使用的源Excel文件，其中包含列A和B中的一些数据。

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_2.png)

下面的屏幕截图显示了样例代码生成的输出 Excel 文件。如您所见，小计已应用于范围**A2:B11**，大纲的方向为详细下方的摘要行。

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_3.png)

### Java 代码应用小计并更改大纲摘要行的方向

以下是实现上述输出的示例代码。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ApplyingSubtotal-1.java" >}}
{{< app/cells/assistant language="java" >}}
