---
title: 使用 Golang 通过 C++ 生成条件格式化数据条的图像
linktitle: 生成条件格式数据条形图像
description: Aspose.Cells是一个用于操作电子表格文件的C++库。它支持生成条件格式化的数据条和图像，允许用户根据单元格的值自定义电子表格的显示。这篇文章将介绍如何使用Aspose.Cells库生成条件格式化的数据条和图像。
keywords: Aspose.Cells，条件格式，数据条，图像，电子表格
type: docs
weight: 40
url: /zh/go-cpp/generate-conditional-formatting-databars-images/
---

{{% alert color="primary" %}}

有时，您需要生成条件格式数据条的图像。您可以使用Aspose.Cells的[**DataBar.ToImage()**](https://reference.aspose.com/cells/go-cpp/databar/toimage/)方法生成这些图像。本文展示了如何使用Aspose.Cells生成DataBar图像。

{{% /alert %}}

 以下示例代码生成单元格C1的DataBar图片。首先，它访问单元格的格式条件对象，然后从该对象访问 [**DataBar**](https://reference.aspose.com/cells/go-cpp/databar/) ，并使用其 [**ToImage()**](https://reference.aspose.com/cells/go-cpp/databar/toimage/) 方法生成单元格的图片。最后，它将图片保存到磁盘上。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GenerateConditionalFormattingDatabarsImages.go" >}}
