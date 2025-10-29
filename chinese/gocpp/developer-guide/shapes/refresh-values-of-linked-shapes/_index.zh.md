---
title: 用Golang通过C++刷新链接形状的值
linktitle: 刷新链接形状的值
type: docs
weight: 3200
url: /zh/go-cpp/refresh-values-of-linked-shapes/
description: 学习如何使用 Aspose.Cells for C++ 在Excel文件中刷新关联形状的值。
---

{{% alert color="primary" %}}

有时，您的Excel文件中有一个链接的形状，该形状链接到某个单元格。在Microsoft Excel中，更改链接单元格的值也会更改链接形状的值。如果要以XLS或XLSX格式保存工作簿，则使用Aspose.Cells也起作用。但是，如果要将工作簿保存为PDF或HTML格式，则必须调用[**Worksheet.Shapes.UpdateSelectedValue()**](https://reference.aspose.com/cells/go-cpp/shapecollection/updateselectedvalue/)方法刷新链接形状的值。

{{% /alert %}}

## 示例

下图显示了示例代码所使用的源Excel文件。它包含一个链接到单元格A1到E4的图片。我们将用 Aspose.Cells 改变B4单元格的值，然后调用 [**Worksheet.Shapes.UpdateSelectedValue()**](https://reference.aspose.com/cells/go-cpp/shapecollection/updateselectedvalue/) 方法刷新图片的值，并将其保存为PDF格式。

![todo:image_alt_text](refresh-values-of-linked-shapes_1.jpg)

您可以从给定链接下载 [源Excel文件](95584291.xlsx) 和 [输出PDF](95584292.pdf)。

### 用C++刷新关联形状值的代码示例

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RefreshValuesOfLinkedShapes.go" >}}
