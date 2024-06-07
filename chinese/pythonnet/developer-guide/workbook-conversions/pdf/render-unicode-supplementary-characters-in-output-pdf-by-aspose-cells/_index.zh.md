---
title: 通过Aspose.Cells for Python通过.NET在输出PDF中呈现Unicode补充字符
type: docs
weight: 350
url: /zh/python-net/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/
description: 学习如何在使用Aspose.Cells for Python通过.NET API将Excel转换为PDF时呈现Unicode补充字符。
keywords: 将文件保存为PDF时使用Python呈现Unicode补充字符，将Excel保存为PDF时使用Python打印Unicode补充字符，将Excel转换为PDF时展示Unicode补充字符，为Excel到PDF输出Unicode补充字符
---

{{% alert color="primary" %}}

普通Unicode字符占2个字节长度，而Unicode补充字符占4个字节长度。Aspose.Cells for Python通过.NET现在支持渲染这些4个字节的Unicode字符。

在 Unicode 字符标准中，补充字符是指代码点从U+10000到U+10FFFF的字符。换句话说，这些是大于 U+FFFF 的 Unicode 字符。

- 在 UTF-8 中，这些字符每个都是4个字节长。
- 在 UTF-16 中，这些字符需要2个代理对（16位单位）。

{{% /alert %}}

## 通过Aspose.Cells for Python通过.NET在输出PDF中呈现Unicode补充字符

以下截图显示了Aspose.Cells for Python通过.NET如何将[源Excel文件](5115563.xlsx)渲染成[输出PDF](5115564.pdf)。正如您所见，所有三个Unicode补充字符都被呈现为与Microsoft Excel相同的方式。

![todo:image_alt_text](output.png)

## 示例代码

您可以使用这个示例代码将 [源 Excel 文件](5115563.xlsx) 转换为 [输出 PDF](5115564.pdf)。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-RenderUnicodeInOutput.py" >}}
