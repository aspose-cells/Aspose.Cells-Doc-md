---
title: 生成条件格式数据条形图像
type: docs
weight: 170
url: /zh/java/generate-conditional-formatting-databars-images/
---

{{% alert color="primary" %}}

有时，您需要生成条件格式数据条的图像。您可以使用Aspose.Cells [**DataBar.toImage()**](https://reference.aspose.com/cells/java/com.aspose.cells/databar#toImage(com.aspose.cells.Cell,%20com.aspose.cells.ImageOrPrintOptions)）方法生成这些图像。本文显示了如何使用Aspose.Cells生成数据条图像。

{{% /alert %}}

## **示例**

以下示例代码生成单元格C1的数据条图像。首先，它访问单元格的格式条件对象，然后从该对象中访问数据条对象，并使用其[**DataBar.toImage()**](https://reference.aspose.com/cells/java/com.aspose.cells/databar#toImage(com.aspose.cells.Cell,%20com.aspose.cells.ImageOrPrintOptions)）方法生成单元格的图像，最后将图像保存到磁盘。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-GenerateDatabarImage-1.java" >}}
