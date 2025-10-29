---
title: 生成条件格式数据条形图像
description: Aspose.Cells for Python via .NET 是一个用于处理电子表格文件的 Python 库。它支持生成条件格式化的数据条和图片，使用户可以根据单元格的值自定义电子表格的显示方式。本文将介绍如何使用 Aspose.Cells for Python 生成条件格式化的数据条和图片。
keywords: Aspose.Cells for Python via .NET、条件格式、数据条、图片、电子表格
type: docs
weight: 40
url: /zh/python-net/generate-conditional-formatting-databars-images/
---

{{% alert color="primary" %}}

有时，您需要生成条件格式化 DataBars 的图片。可以使用 Aspose.Cells [**DataBar.to_image()**](https://reference.aspose.com/cells/python-net/aspose.cells/databar/to_image) 方法生成这些图片。本文展示了如何使用 Aspose.Cells for Python via .NET 生成 DataBar 图片。

{{% /alert %}}

以下示例代码生成了单元格 C1 的 DataBar 图像。首先，它访问了单元格的格式条件对象，然后从该对象访问[**DataBar**](https://reference.aspose.com/cells/python-net/aspose.cells/databar)对象，并使用其 [**to_image()**](https://reference.aspose.com/cells/python-net/aspose.cells/databar/to_image) 方法生成单元格的图像。最后，将图像保存在磁盘上。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-GenerateDatabarImage-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
