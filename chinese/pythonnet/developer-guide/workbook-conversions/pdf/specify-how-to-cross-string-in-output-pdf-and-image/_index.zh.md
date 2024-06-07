---
title: 指定输出PDF和图像中如何跨越字符串
type: docs
weight: 120
url: /zh/python-net/specify-how-to-cross-string-in-output-pdf-and-image/
description: 学习如何在使用Aspose.Cells for Python通过.NET API将字符串跨越输出PDF和图像
keywords: Python将输出PDF和图像中的字符串跨越
---

## **可能的使用场景**

当单元格包含文本或字符串但超过了单元格的宽度时，如果下一列中的单元格为null或空，则字符串会溢出。当将Excel文件保存为PDF/Image时，您可以通过指定交叉类型来控制此溢出，该枚举具有以下值

- **TextCrossType.DEFAULT**：显示类似于MS Excel的文本，取决于下一个单元格。如果下一个单元格为空，则字符串将跨越或将被截断。

- **TextCrossType.CROSS_KEEP**：显示字符串类似于MS Excel导出的PDF/图像

- **TextCrossType.CROSS_OVERRIDE**：通过跨越其他单元格并覆盖经过的单元格的文本来显示所有文本

- **TextCrossType.STRICT_IN_CELL**：仅在单元格宽度内显示字符串

## **使用TextCrossType指定输出PDF/Image中的字符串如何跨越**

下面的示例代码加载示例Excel文件，并通过指定不同的[**TextCrossType**](https://reference.aspose.com/cells/python-net/aspose.cells/textcrosstype/)将其保存为PDF/Image格式。示例Excel文件和输出文件可从以下链接下载：

[sampleCrossType.xlsx](81920905.xlsx)

[outputCrossType.pdf](81920903.pdf)

[outputCrossType.png](81920904.png)

###示例代码

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-RenderUsingTextCrossType-1.py" >}}
