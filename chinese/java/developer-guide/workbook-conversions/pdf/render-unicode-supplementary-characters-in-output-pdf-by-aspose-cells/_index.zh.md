---
title: 通过 Aspose.Cells 在输出 PDF 中渲染 Unicode 增补字符
type: docs
weight: 690
url: /zh/java/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/
---
{{% alert color="primary" %}} 

普通 Unicode 字符的长度为 2 个字节，而 Unicode 增补字符的长度为 4 个字节。 Aspose.Cells 现在支持渲染这些 4 字节的 Unicode 字符。

在 Unicode 字符标准中，增补字符是分配了代码点从 U+10000 到 U+10FFFF 的字符。换句话说，这些是大于 U+FFFF 的 Unicode 字符。

- 在 UTF-8 中，这些字符每个都是 4 个字节长。
- 在 UTF-16 中，这些字符需要 2 个代理项（16 位单元）。

{{% /alert %}} 
## **通过 Aspose.Cells 在输出 PDF 中渲染 Unicode 增补字符**
以下屏幕截图显示了 Aspose.Cells 如何呈现[源文件](5473390.xlsx)进入[输出PDF](5473391.pdf).如您所见，所有三个 Unicode 增补字符的呈现方式与 Microsoft Excel 完全相同。

![待办事项：图像_替代_文本](render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells_1.png)

您可以使用此示例代码将[源文件](5473390.xlsx)进入[输出PDF](5473391.pdf).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-utility-RenderUnicodeSupplimentaryCharacterToPDF-1.java" >}}
