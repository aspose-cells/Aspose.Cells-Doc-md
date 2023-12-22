---
title: 通过 Aspose.Cells for Python via .NET 渲染输出中的 Unicode 增补字符 PDF
type: docs
weight: 350
url: /zh/python-net/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/
description: 了解如何在使用 Aspose.Cells for Python via .NET API 将 Excel 转换为 PDF 时呈现 Unicode 增补字符。
keywords: Python Render Unicode Supplementary characters while saving file to PDF, Print Unicode Supplementary characters while saving Excel to PDF using Python, Python Show Unicode Supplementary characters when converting Excel to PDF, Output Unicode Supplementary characters for excel to pdf
---
{{% alert color="primary" %}}

普通 Unicode 字符的长度为 2 个字节，而 Unicode 补充字符的长度为 4 个字节。 Aspose.Cells for Python via .NET 现在支持这些 4 字节 Unicode 字符的呈现。

在 Unicode 字符标准中，补充字符是分配从 U+10000 到 U+10FFFF 的代码点的字符。换句话说，这些是大于 U+FFFF 的 Unicode 字符。

- 在 UTF-8 中，这些字符每个长度为 4 个字节。
- 在 UTF-16 中，这些字符需要 2 个代理项（16 位单元）。

{{% /alert %}}

## 通过 Aspose.Cells for Python via .NET 渲染输出中的 Unicode 增补字符 PDF

下面的截图显示了 Aspose.Cells for Python via .NET 如何渲染[源 Excel 文件](5115563.xlsx)进入[输出PDF](5115564.pdf)。正如您所看到的，所有三个 Unicode 补充字符的呈现方式与 Microsoft Excel 的呈现方式完全相同。

![待办事项：图像_替代_文本](output.png)

## 示例代码

您可以使用此示例代码进行转换[源 Excel 文件](5115563.xlsx)进入[输出PDF](5115564.pdf).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-RenderUnicodeInOutput.py" >}}
