---
title: 生成条件格式数据条形图像
type: docs
weight: 170
url: /zh/java/generate-conditional-formatting-databars-images/
---

{{% alert color="primary" %}}

有时，您需要生成条件格式数据条的图像。您可以使用Aspose.Cells的[**DataBar.toImage()**](https://reference.aspose.com/cells/java/com.aspose.cells/databar#toImage(com.aspose.cells.Cell,%20com.aspose.cells.ImageOrPrintOptions))方法生成这些图像。本文展示了如何使用Aspose.Cells生成DataBar图像。

{{% /alert %}}

## **示例**

下面的示例代码生成了单元格C1的DataBar图像。首先，访问单元格的格式条件对象，然后从该对象访问DataBar对象，并使用其 [**DataBar.toImage()**](https://reference.aspose.com/cells/java/com.aspose.cells/databar#toImage(com.aspose.cells.Cell,%20com.aspose.cells.ImageOrPrintOptions)) 方法生成单元格的图像。最后，将图像保存在磁盘上。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-GenerateDatabarImage-1.java" >}}
