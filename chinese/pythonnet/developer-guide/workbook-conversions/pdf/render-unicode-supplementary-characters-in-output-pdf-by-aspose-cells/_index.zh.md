---
title: 使用Aspose.Cells for Python via .NET API，将输出PDF中的Unicode补充字符渲染。
type: docs
weight: 350
url: /zh/python-net/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/
description: 学习如何在将Excel转换为PDF时使用Aspose.Cells for Python via .NET API渲染Unicode补充字符。
keywords: 使用Python将Unicode补充字符渲染到PDF文件并将Excel保存为PDF文件时打印Unicode补充字符，Python在将Excel转换为PDF时显示Unicode补充字符，输出Excel文件为PDF文件的Unicode补充字符
---

{{% alert color="primary" %}}

普通的Unicode字符为2字节长，而Unicode补充字符为4字节长。Aspose.Cells for Python via .NET现在支持渲染这些4字节Unicode字符。

在Unicode字符标准中，补充字符是指分配的代码点范围从U+10000到U+10FFFF。换句话说，这些是大于U+FFFF的Unicode字符。

- 在UTF-8中，这些字符每个都是4个字节长。
- 在UTF-16中，这些字符需要2个代理对（16位单位）。

{{% /alert %}}

## 使用Aspose.Cells for Python via .NET将输出PDF中的Unicode补充字符渲染

以下屏幕截图显示了Aspose.Cells for Python via .NET如何将[源Excel文件](5115563.xlsx)渲染为[输出PDF](5115564.pdf)。如您所见，所有三个Unicode补充字符的渲染方式与Microsoft Excel相同。

![todo:image_alt_text](output.png)

## 示例代码

您可以使用此示例代码将[源Excel文件](5115563.xlsx)转换为[输出PDF](5115564.pdf)。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-RenderUnicodeInOutput.py" >}}
{{< app/cells/assistant language="python-net" >}}
