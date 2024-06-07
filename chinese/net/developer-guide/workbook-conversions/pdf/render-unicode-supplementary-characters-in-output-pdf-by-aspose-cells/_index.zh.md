---
title: 通过 Aspose.Cells 在输出 PDF 中呈现 Unicode 补充字符
type: docs
weight: 350
url: /zh/net/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/
---

{{% alert color="primary" %}}

普通的 Unicode 字符长度为2个字节，而 Unicode 补充字符长度为4个字节。Aspose.Cells 现在支持呈现这些4个字节的 Unicode 字符。

在 Unicode 字符标准中，补充字符是指代码点从U+10000到U+10FFFF的字符。换句话说，这些是大于 U+FFFF 的 Unicode 字符。

- 在 UTF-8 中，这些字符每个都是4个字节长。
- 在 UTF-16 中，这些字符需要2个代理对（16位单位）。

{{% /alert %}}

## 通过 Aspose.Cells 在输出 PDF 中呈现 Unicode 补充字符

以下截图展示了 Aspose.Cells 将 [源 Excel 文件](5115563.xlsx) 渲染到 [输出 PDF](5115564.pdf) 中。您可以看到所有三个 Unicode 补充字符的呈现效果与 Microsoft Excel 相同。

![todo:image_alt_text](output.png)

## 示例代码

您可以使用这个示例代码将 [源 Excel 文件](5115563.xlsx) 转换为 [输出 PDF](5115564.pdf)。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderUnicodeInOutput-RenderUnicodeInOutput.cs" >}}
