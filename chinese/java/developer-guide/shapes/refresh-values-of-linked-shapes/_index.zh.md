---
title: 刷新链接形状的值
type: docs
weight: 3000
url: /zh/java/refresh-values-of-linked-shapes/
---

{{% alert color="primary" %}}

有时，您的Excel文件中会有一个链接的形状，它链接到某个单元格。在Microsoft Excel中，更改链接单元格的值也会更改链接形状的值。如果您希望将工作簿保存为XLS或XLSX格式，则Aspose.Cells也能很好地处理。但是，如果您想将工作簿保存为PDF或HTML格式，则需要调用[**Worksheet.getShapes().updateSelectedValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#updateSelectedValue()）方法来刷新链接形状的值。

{{% /alert %}}

## 示例

以下屏幕截图显示了在下面的示例代码中使用的源Excel文件。它有一个链接的**Picture 1**链接到单元格A1。我们将改变单元格A1的值，然后调用 [**Worksheet.getShapes().updateSelectedValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#updateSelectedValue()）方法刷新**Picture 1**的值，并将其保存为PDF格式。

![todo:image_alt_text](refresh-values-of-linked-shapes_1.png)

您可以从给定链接中下载[source Excel file](5472956.xlsx)和[output PDF](5472955.pdf)。

### 刷新链接形状值的Java代码

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RefreshValuesOfLinkedShapes-RefreshValuesOfLinkedShapes.java" >}}
