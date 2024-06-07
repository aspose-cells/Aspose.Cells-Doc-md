---
title: 通过 Aspose.Cells 在输出 PDF 中呈现 Unicode 补充字符
type: docs
weight: 690
url: /zh/java/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/
---

{{% alert color="primary" %}} 

普通的 Unicode 字符长度为2个字节，而 Unicode 补充字符长度为4个字节。Aspose.Cells 现在支持呈现这些4个字节的 Unicode 字符。

在 Unicode 字符标准中，补充字符是指代码点从U+10000到U+10FFFF的字符。换句话说，这些是大于 U+FFFF 的 Unicode 字符。

- 在 UTF-8 中，这些字符每个都是4个字节长。
- 在 UTF-16 中，这些字符需要2个代理对（16位单位）。

{{% /alert %}} 
## **通过Aspose.Cells在输出PDF中呈现Unicode补充字符**
以下屏幕截图显示了 Aspose.Cells 将 [源 Excel 文件](5473390.xlsx) 渲染到 [输出 PDF](5473391.pdf)。正如您所见，所有三个 Unicode Supplementary 字符都与 Microsoft Excel 完全相同地呈现。

![todo:image_alt_text](render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells_1.png)

您可以使用此示例代码将源 Excel 文件转换为输出 PDF 文件。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-utility-RenderUnicodeSupplimentaryCharacterToPDF-1.java" >}}
