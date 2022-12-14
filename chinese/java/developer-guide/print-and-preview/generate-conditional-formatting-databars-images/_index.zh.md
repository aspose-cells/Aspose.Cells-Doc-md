---
title: 生成条件格式 DataBars 图像
type: docs
weight: 170
url: /zh/java/generate-conditional-formatting-databars-images/
---
{{% alert color="primary" %}}

有时，您需要生成条件格式数据条的图像。您可以使用 Aspose.Cells[**DataBar.toImage()**](https://reference.aspose.com/cells/java/com.aspose.cells/databar#toImage(com.aspose.cells.Cell,%20com.aspose.cells.ImageOrPrintOptions)方法来生成这些图像。本文介绍如何使用 Aspose.Cells 生成 DataBar 图像。

{{% /alert %}}

## **例子**

以下示例代码生成单元格 C1 的 DataBar 图像。首先，它访问单元格的格式条件对象，然后从该对象访问 DataBar 对象并使用其[**DataBar.toImage()**](https://reference.aspose.com/cells/java/com.aspose.cells/databar#toImage(com.aspose.cells.Cell,%20com.aspose.cells.ImageOrPrintOptions)方法来生成细胞的图像。最后，它将图像保存在磁盘上。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-GenerateDatabarImage-1.java" >}}
