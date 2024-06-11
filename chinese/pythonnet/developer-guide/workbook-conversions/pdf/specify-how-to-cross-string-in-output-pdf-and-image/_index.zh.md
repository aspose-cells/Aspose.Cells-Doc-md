---
title: 指定输出PDF和图像中如何跨越字符串
type: docs
weight: 120
url: /zh/python-net/specify-how-to-cross-string-in-output-pdf-and-image/
description: 了解如何使用Aspose.Cells for Python via .NET API在输出PDF和图像中跨字符串。
keywords: Python跨字符串在输出PDF和图像中
---

## **可能的使用场景**

当单元格包含文本或字符串但大于单元格宽度时，如果下一列的单元格为空，则字符串会溢出。当您将Excel文件保存为PDF / 图像时，您可以通过使用[**TextCrossType**](https://reference.aspose.com/cells/python-net/aspose.cells/textcrosstype/)枚举指定交叉类型来控制此溢出。它具有以下值

- **TextCrossType.DEFAULT**：像MS Excel一样显示文本，这取决于下一单元格。如果下一个单元格为null，字符串将会跨越或者被截断。

- **TextCrossType.CROSS_KEEP**：像MS Excel一样显示字符串导出为PDF/图像

- **TextCrossType.CROSS_OVERRIDE**：通过跨越其他单元格显示所有文本并覆盖交叉单元格的文本

- **TextCrossType.STRICT_IN_CELL**: 仅在单元格宽度内显示字符串。

## **使用TextCrossType指定输出PDF/图像中如何跨越字符串**

以下示例代码加载示例Excel文件，并通过指定不同的[**TextCrossType**](https://reference.aspose.com/cells/python-net/aspose.cells/textcrosstype/)将其保存为PDF/图像格式。可以从以下链接下载示例Excel文件和输出文件：

[sampleCrossType.xlsx](81920905.xlsx)

[outputCrossType.pdf](81920903.pdf)

[outputCrossType.png](81920904.png)

### 示例代码

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-RenderUsingTextCrossType-1.py" >}}
