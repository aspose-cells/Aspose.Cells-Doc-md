---
title: 刷新链接形状的值
type: docs
weight: 3200
url: /zh/net/refresh-values-of-linked-shapes/
---

{{% alert color="primary" %}}

有时，您的Excel文件中有一个链接形状，它链接到某个单元格。在Microsoft Excel中，更改链接单元格的值也会更改链接形状的值。如果要将工作簿保存为XLS或XLSX格式，则Aspose.Cells也支持这一点。但是，如果要将工作簿保存为PDF或HTML格式，则需要调用[**Worksheet.Shapes.UpdateSelectedValue()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/updateselectedvalue)方法来刷新链接形状的值。

{{% /alert %}}

## 示例

以下屏幕截图显示了示例代码中使用的源Excel文件。它有一个链接图片链接到单元格A1至E4。我们将使用Aspose.Cells更改单元格B4的值，然后调用[**Worksheet.Shapes.UpdateSelectedValue()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/updateselectedvalue)方法来刷新图片的值并以PDF格式保存。

![todo:image_alt_text](refresh-values-of-linked-shapes_1.jpg)

您可以从给定链接处下载[源Excel文件](95584291.xlsx)和[输出PDF](95584292.pdf)。

### 刷新链接形状的值的C#代码

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-RefreshValueOfLinkedShapes-1.cs" >}}
