---
title: 将带有图片或图表的XLS文件转换为PDF
type: docs
weight: 50
url: /zh/python-net/convert-xls-file-with-images-or-charts-to-pdf/
description: 了解如何使用Aspose.Cells for Python通过.NET API将带有图像或图表的XLS文件转换为PDF
keywords: Python将带图像或图表的XLS文件转换为PDF，在Python中使用Python将xls转换为pdf，带有图像的Python XLS文件转换为pdf，带有图表的xls文件通过python转换为pdf，Python xls转换为pdf
---

{{% alert color="primary" %}} 

Aspose.Cells for Python通过.NET支持将包含图像和图表的XLS文件转换为PDF文档。Aspose.Cells for Python通过.NET API可以独立工作以将电子表格转换为PDF：不需要Aspose.PDF for .NET进行转换。该过程可以在内存中完成，因为该过程不依赖于临时或中介XML文件。这意味着大型Excel文件，例如包含图像、图表和其他绘图对象的文件，可以快速高效地转换。

{{% /alert %}} 
## **示例代码**


{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-ConvertXLSFileToPDF-1.py" >}}

{{% alert color="primary" %}} 

如果电子表格包含公式，在渲染为PDF之前最好调用[Workbook.calculate_formula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#)方法。这样可以确保重新计算依赖于公式的值，并在PDF中呈现正确的值。

{{% /alert %}}
