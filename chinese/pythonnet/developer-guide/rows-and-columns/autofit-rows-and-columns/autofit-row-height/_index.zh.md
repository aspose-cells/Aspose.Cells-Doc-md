---
title: 加载文件时自动调整行高
type: docs
weight: 120
url: /zh/python-net/autofit-row-height/
description: 通过 Aspose.Cells for Python 的 .NET API，学习如何调整行高度，使其不是自定义的。
keywords: Python Excel 库，Python 加载文件时自适应行高，Python 打开 Excel 文件时自动调整行高。 
---

## **可能的使用场景**
行的高度会自动匹配内容的字体，但是当缓存行的高度与文件中的内容高度不匹配时，MS Excel 会在加载文件时自动调整行高度，而 Aspose.Cells for Python 的 .NET 版本不会自动调整以提高性能。如果您需要使用 Aspose.Cells for Python 的 .NET 程序在加载文件时自动匹配行高度，您可以通过参数 [LoadOptions.AutoFitterOptions.only_auto](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions/only_auto/) 来实现目标。

请参考以下图像数据。我们可以看到第11行的缓存行高为15，但Excel在加载文件时会自动调整行高。
<br>
<img src="1.png" width=70% />

## **使用 Aspose.Cells for Python Excel 库调整行高度**
如果直接加载文件并将其保存为PDF，则PDF文件中的数据将无法完全显示，因为其缓存行高仅为15。
<br>
<img src="2.png" width=70% />
<br>
如果在加载文件时将参数 [LoadOptions.AutoFitterOptions.only_auto](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions/only_auto/) 设置为 true，则 Aspose.Cells for Python 的 .NET 版本会自动调整行高度。调整后的行高度可以有效满足文本显示要求。
<br>
<img src="3.png" width=70% />

## **Python 代码示例**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Rows-autofit-row-height.py" >}}
