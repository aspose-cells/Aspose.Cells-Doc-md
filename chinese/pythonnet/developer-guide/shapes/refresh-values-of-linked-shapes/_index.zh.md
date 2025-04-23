---
title: 刷新链接形状的值
type: docs
weight: 3200
url: /zh/python-net/refresh-values-of-linked-shapes/
---

{{% alert color="primary" %}}

有时候，您的Excel文件中会有一个链接形状，该形状链接到某个单元格。在Microsoft Excel中，更改链接单元格的值也会更改链接形状的值。如果您想以XLS或XLSX格式保存工作簿，Aspose.Cells for Python via .NET也能正常工作。这也适用于Aspose.Cells for Python via .NET。如果您希望将工作簿保存为PDF或HTML格式，则必须调用[**Worksheet.Shapes.update_selected_value()**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/update_selected_value)方法来刷新链接形状的值。

{{% /alert %}}

## 示例

下图显示了下方示例代码中使用的源Excel文件。它包含一个链接到单元格A1至E4的图片。我们将用Aspose.Cells for Python via .NET更改单元格B4的值，然后调用[**Worksheet.Shapes.update_selected_value()**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/update_selected_value)方法来刷新图片的值并以PDF格式保存。

![todo:image_alt_text](refresh-values-of-linked-shapes_1.jpg)

您可以从以下链接下载源Excel文件和输出PDF。

### C#代码来刷新链接形状的值

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-RefreshValueOfLinkedShapes-1.py" >}}
