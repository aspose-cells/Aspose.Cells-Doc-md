---
title: 刷新链接形状的值
type: docs
weight: 3000
url: /zh/java/refresh-values-of-linked-shapes/
---

{{% alert color="primary" %}}

有时，在您的Excel文件中有一个链接的形状，该形状链接到某个单元格。在Microsoft Excel中，更改链接单元格的值也会更改链接形状的值。如果您想以XLS或XLSX格式保存工作簿，使用Aspose.Cells也可以正常工作。但是，如果您想将工作簿保存为PDF或HTML格式，那么您将需要调用 [**Worksheet.getShapes().updateSelectedValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection/#updateSelectedValue--) 方法来刷新链接形状的值。

{{% /alert %}}

## 示例

以下屏幕截图显示了下面的示例代码中使用的源Excel文件。它有一个链接的**Picture 1**与单元格A1相连。我们将使用Aspose.Cells更改单元格A1的值，然后调用[**Worksheet.getShapes().updateSelectedValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection/#updateSelectedValue--) 方法来刷新**Picture 1**的值，并以PDF格式保存。

![todo:image_alt_text](refresh-values-of-linked-shapes_1.png)

您可以从以下链接下载 [源Excel文件](5472956.xlsx) 和 [输出PDF](5472955.pdf)。

### 刷新工作表中链接形状的值的Java代码

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RefreshValuesOfLinkedShapes-RefreshValuesOfLinkedShapes.java" >}}
{{< app/cells/assistant language="java" >}}
