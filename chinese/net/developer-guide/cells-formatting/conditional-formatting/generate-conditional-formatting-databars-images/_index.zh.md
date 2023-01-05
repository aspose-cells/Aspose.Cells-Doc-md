---
title: 生成条件格式 DataBars 图像
type: docs
weight: 40
url: /zh/net/generate-conditional-formatting-databars-images/
---
{{% alert color="primary" %}}

有时，您需要生成条件格式数据条的图像。您可以使用 Aspose.Cells[**数据条.ToImage()**](https://reference.aspose.com/cells/net/aspose.cells/databar/methods/toimage)生成这些图像的方法。本文介绍如何使用 Aspose.Cells 生成 DataBar 图像。

{{% /alert %}}

以下示例代码生成单元格 C1 的 DataBar 图像。首先，它访问单元格的格式条件对象，然后从该对象访问[**数据条**](https://reference.aspose.com/cells/net/aspose.cells/databar)对象并使用其[**印象（）**](https://reference.aspose.com/cells/net/aspose.cells/databar/methods/toimage)生成细胞图像的方法。最后，它将图像保存在磁盘上。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageConditionalFormatting-GenerateDatabarImage-1.cs" >}}
