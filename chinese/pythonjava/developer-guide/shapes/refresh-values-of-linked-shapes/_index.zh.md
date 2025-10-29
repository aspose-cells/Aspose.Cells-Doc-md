---
title: 刷新链接形状的值
type: docs
weight: 3200
url: /zh/python-java/refresh-values-of-linked-shapes/
---

{{% alert color="primary" %}}

有时，您的Excel文件中有一个链接的形状，该形状链接到某个单元格。在Microsoft Excel中，更改链接单元格的值也会更改链接形状的值。如果要以XLS或XLSX格式保存工作簿，则使用Aspose.Cells也起作用。但是，如果要将工作簿保存为PDF或HTML格式，则必须调用[**Worksheet.getShapes().updateSelectedValue()**](https://reference.aspose.com/cells/python-java/asposecells.api/shapecollection#updateSelectedValue())方法刷新链接形状的值。

{{% /alert %}}

## 示例

以下截图显示了下面示例代码中使用的源Excel文件。其有一个链接图片链接到单元格A1到E4。我们将更改单元格B4的值用Aspose.Cells，然后调用[**Worksheet.getShapes().updateSelectedValue()**](https://reference.aspose.com/cells/python-java/asposecells.api/shapecollection#updateSelectedValue())方法刷新图片的值并将其保存为PDF格式。

![todo:image_alt_text](refresh-values-of-linked-shapes_1.jpg)

您可以从提供的链接下载[源Excel文件](sampleRefreshValueOfLinkedShapes.xlsx)和[输出PDF](95584292.pdf)。

### C#代码来刷新链接形状的值

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Examples-pythonjava-Shapes-RefreshValueOfLinkedShapes-1.py" >}}
{{< app/cells/assistant language="csharp" >}}
