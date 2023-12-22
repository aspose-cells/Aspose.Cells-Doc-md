---
title: 指定如何交叉输出 PDF 和图像中的字符串
type: docs
weight: 120
url: /zh/python-net/specify-how-to-cross-string-in-output-pdf-and-image/
description: 了解如何将输出 PDF 和图像中的字符串与 Aspose.Cells for Python via .NET API 交叉。
keywords: Python Cross String in output PDF and image
---
##  **可能的使用场景**

当单元格包含文本或字符串但大于单元格的宽度时，如果下一列中的下一个单元格为 null 或为空，则字符串会溢出。当您将 Excel 文件保存到 PDF/Image 时，您可以通过使用[**文本交叉类型**](https://reference.aspose.com/cells/python-net/aspose.cells/textcrosstype/)枚举。它具有以下值

- *TextCrossType.DEFAULT**：像 MS Excel 一样显示文本，取决于下一个单元格。如果下一个单元格为空，则字符串将交叉或被截断。

- *TextCrossType.CROSS_KEEP**：像MS Excel导出PDF/Image一样显示字符串

- *TextCrossType.CROSS_OVERRIDE**：通过交叉其他单元格显示所有文本，并覆盖交叉单元格的文本

- *TextCrossType.STRICT_IN_CELL**：仅显示单元格宽度内的字符串。

##  **指定如何使用 TextCrossType 在输出 PDF/Image 中交叉字符串**

以下示例代码加载示例Excel文件，并通过指定不同的值将其保存为PDF/Image格式[**文本交叉类型**](https://reference.aspose.com/cells/python-net/aspose.cells/textcrosstype/)。示例 Excel 文件和输出文件可以从以下链接下载：

[样本CrossType.xlsx](81920905.xlsx)

[输出CrossType.pdf](81920903.pdf)

[输出CrossType.png](81920904.png)

### 示例代码

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-RenderUsingTextCrossType-1.py" >}}
