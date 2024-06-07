---
title: 生成条件格式化数据条图像
description: Aspose.Cells是一个用于处理电子表格文件的.NET库。它支持生成具有条件格式化数据条和图像的功能，允许用户根据单元格值自定义电子表格的显示。本文将介绍如何使用Aspose.Cells库生成条件格式化的数据条和图像。
keywords: Aspose.Cells、条件格式、数据条、图像、电子表格
type: docs
weight: 40
url: /zh/net/generate-conditional-formatting-databars-images/
---

{{% alert color="primary" %}}

有时，您需要生成条件格式化数据条的图像。您可以使用Aspose.Cells [**DataBar.ToImage()**](https://reference.aspose.com/cells/net/aspose.cells/databar/methods/toimage) 方法生成这些图像。本文展示了如何使用Aspose.Cells生成数据条图像。

{{% /alert %}}

以下示例代码生成单元格 C1 的数据条图像。首先，它访问单元格的格式条件对象，然后从该对象中访问 [**DataBar**](https://reference.aspose.com/cells/net/aspose.cells/databar) 对象，并使用其 [**ToImage()**](https://reference.aspose.com/cells/net/aspose.cells/databar/methods/toimage) 方法生成单元格的图像。最后，将图像保存在磁盘上。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageConditionalFormatting-GenerateDatabarImage-1.cs" >}}
