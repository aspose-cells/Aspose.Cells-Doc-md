---
title: 生成条件格式数据条形图像
linktitle: 生成条件格式数据条形图像
description: Aspose.Cells 是一个用于操作电子表格文件的 Node.js 库。它支持生成条件格式化的数据条和图像，允许用户根据单元格的值自定义电子表格的显示方式。本文将介绍如何使用 Aspose.Cells 生成条件格式的数据条和图像。
keywords: Aspose.Cells，条件格式，数据条，图像，电子表格，Node.js via C++
type: docs
weight: 40
url: /zh/nodejs-cpp/generate-conditional-formatting-databars-images/
---

{{% alert color="primary" %}}

有时，您需要生成条件格式数据条的图像。您可以使用Aspose.Cells的[**DataBar.toImage(Cell, ImageOrPrintOptions)**](https://reference.aspose.com/cells/nodejs-cpp/databar/#toImage-cell-imageorprintoptions-)方法生成这些图像。本文展示了如何使用Aspose.Cells生成DataBar图像。

{{% /alert %}}

 以下示例代码生成单元格C1的DataBar图片。首先，它访问单元格的格式条件对象，然后从该对象访问 [**DataBar**](https://reference.aspose.com/cells/nodejs-cpp/databar) ，并使用其 [**DataBar.toImage(Cell, ImageOrPrintOptions)**](https://reference.aspose.com/cells/nodejs-cpp/databar/#toImage-cell-imageorprintoptions-) 方法生成单元格的图片。最后，它将图片保存到磁盘上。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ConditionalFormatting-GenerateConditionalFormattingDataBars.js" >}}

