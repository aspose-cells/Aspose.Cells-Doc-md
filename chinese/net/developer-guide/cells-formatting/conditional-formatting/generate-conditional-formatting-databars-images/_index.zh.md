---
title: 生成条件格式 DataBars 图像
description: Aspose.Cells 是一个用于处理电子表格文件的 .NET 库。它支持生成有条件格式化的数据条和图像，允许用户根据单元格的值自定义电子表格的显示。本文将介绍如何使用Aspose.Cells库生成条件格式的数据条和图像。
keywords: Aspose.Cells, Conditional Formatting, Data Bars, Images, Spreadsheets
type: docs
weight: 40
url: /zh/net/generate-conditional-formatting-databars-images/
---
{{% alert color="primary" %}}

有时，您需要生成条件格式 DataBar 的图像。您可以使用Aspose.Cells[**DataBar.ToImage()**](https://reference.aspose.com/cells/net/aspose.cells/databar/methods/toimage)生成这些图像的方法。本文介绍如何使用 Aspose.Cells 生成 DataBar 图像。

{{% /alert %}}

以下示例代码生成单元格 C1 的 DataBar 图像。首先，它访问单元格的格式条件对象，然后从该对象访问[**数据栏**](https://reference.aspose.com/cells/net/aspose.cells/databar)对象并使用它的[**ToImage()**](https://reference.aspose.com/cells/net/aspose.cells/databar/methods/toimage)生成细胞图像的方法。最后，它将图像保存在磁盘上。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageConditionalFormatting-GenerateDatabarImage-1.cs" >}}
