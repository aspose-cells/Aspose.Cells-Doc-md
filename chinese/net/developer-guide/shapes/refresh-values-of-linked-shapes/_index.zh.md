---
title: 刷新链接形状的值
type: docs
weight: 3200
url: /zh/net/refresh-values-of-linked-shapes/
---
{{% alert color="primary" %}}

有时，您的 Excel 文件中有一个链接形状，该形状链接到某个单元格。在 Microsoft Excel 中，更改链接单元格的值也会更改链接形状的值。如果您想以 XLS 或 XLSX 格式保存工作簿，这也适用于 Aspose.Cells。但是，如果您想以 PDF 或 HTML 格式保存工作簿，则必须调用[**工作表.Shapes.UpdateSelectedValue()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/updateselectedvalue)方法刷新链接形状的值。

{{% /alert %}}

## 例子

以下屏幕截图显示了以下示例代码中使用的源 Excel 文件。它具有链接到单元格 A1 到 E4 的链接图片。我们将使用 Aspose.Cells 更改单元格 B4 的值，然后调用[**工作表.Shapes.UpdateSelectedValue()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/updateselectedvalue)方法刷新图片的值，保存为PDF格式。

![待办事项：图片_替代_文本](refresh-values-of-linked-shapes_1.jpg)

您可以下载[源Excel文件](95584291.xlsx)和[输出 PDF](95584292.pdf)从给定的链接。

### C# 刷新链接形状值的代码

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-RefreshValueOfLinkedShapes-1.cs" >}}
