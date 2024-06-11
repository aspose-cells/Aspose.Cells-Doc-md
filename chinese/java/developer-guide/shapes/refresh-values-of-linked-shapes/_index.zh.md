---
title: 刷新链接形状的值
type: docs
weight: 3000
url: /zh/java/refresh-values-of-linked-shapes/
---

{{% alert color="primary" %}}

有时，您的Excel文件中有一个链接到某个单元格的链接形状。在Microsoft Excel中，更改链接单元格的值也会更改链接形状的值。如果要以XLS或XLSX格式保存工作簿，则Aspose.Cells将可以正常工作。然而，如果要以PDF或HTML格式保存工作簿，那么就必须调用 [**Worksheet.getShapes().updateSelectedValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#updateSelectedValue() 方法来刷新链接形状的值。

{{% /alert %}}

## 示例

以下屏幕截图显示了下面示例代码中使用的源Excel文件。它有一个称为 **Picture 1** 的链接到单元格 A1 的链接。我们将使用Aspose.Cells更改单元格 A1 的值，然后调用 [**Worksheet.getShapes().updateSelectedValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#updateSelectedValue() 方法来刷新 **Picture 1** 的值并将其保存为PDF格式。

![todo:image_alt_text](refresh-values-of-linked-shapes_1.png)

您可以从以下链接下载 [源Excel文件](5472956.xlsx) 和 [输出PDF](5472955.pdf)。

### 刷新工作表中链接形状的值的Java代码

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RefreshValuesOfLinkedShapes-RefreshValuesOfLinkedShapes.java" >}}
