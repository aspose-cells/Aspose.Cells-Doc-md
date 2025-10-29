---
title: 指定如何在输出PDF和图像中交叉字符串，使用Golang通过C++实现
linktitle: 指定输出PDF和图像中如何跨越字符串
type: docs
weight: 120
url: /zh/go-cpp/specify-how-to-cross-string-in-output-pdf-and-image/
description: 学习如何使用 Aspose.Cells for C++ 控制 PDF 和图片输出中的文本溢出。
---

## **可能的使用场景**

当单元格包含的文本或字符串超过单元格宽度时，如果下一列的单元格为空或没有内容，文本会溢出。在将Excel文件保存为PDF或图片时，可以通过指定-[**TextCrossType**](https://reference.aspose.com/cells/go-cpp/textcrosstype/) 枚举的交叉类型来控制溢出。它具有以下值：

- **TextCrossType.Default**：显示文本如 MS Excel，其是否溢出取决于下一单元格。如果下一单元格为空，字符串会溢出或者被截断。

- **TextCrossType.CrossKeep**：像 MS Excel 导出PDF/图片时那样显示字符串。

- **TextCrossType.CrossOverride**：允许文本跨越其他单元格显示，并覆盖被跨越单元格中的文本。

- **TextCrossType.StrictInCell**: 仅在单元格宽度内显示字符串。

## **使用TextCrossType指定输出PDF/图像中如何跨越字符串**

以下示例代码加载示例Excel文件，并通过指定不同的 [**TextCrossType**](https://reference.aspose.com/cells/go-cpp/textcrosstype/) 来保存为PDF/图片格式。示例Excel文件和输出文件可以从以下链接下载：

[sampleCrossType.xlsx](81920905.xlsx)

[outputCrossType.pdf](81920903.pdf)

[outputCrossType.png](81920904.png)

### 示例代码

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SpecifyHowToCrossStringInOutputPdfAndImage.go" >}}
