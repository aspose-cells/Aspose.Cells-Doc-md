---
title: 保存为 PDF 时仅更改特定 Unicode 字符的字体
type: docs
weight: 260
url: /zh/net/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/
---
{{% alert color="primary" %}} 

某些 Unicode 字符无法通过用户指定的字体显示。一个这样的 Unicode 字符是**不间断连字符**(U+2011) 其 Unicode 编号为 8209。此字符无法显示为**英语字体格式一种** 但它可以用其他字体显示，例如**宋体 Unicode MS**.

当这样的字符出现在某些特定字体（如 Times New Roman）的单词或句子中时，Aspose.Cells 将整个单词或句子的字体更改为可以显示此字符的字体，如 Arial Unicode 到 MS。

然而，这对某些用户来说是不受欢迎的行为，他们只想更改特定字符的字体，而不是更改整个单词或句子的字体。

为了解决这个问题，Aspose.Cells 提供了 PdfSaveOptions.IsFontSubstitutionCharGranularity 属性，该属性应设置为 true，以便只有不可显示的特定字符的字体更改为可显示的字体，其余单词或句子应保留原始字体。

{{% /alert %}} 
## **例子**
下面的屏幕截图比较了下面示例代码生成的两个输出 PDF。

一个是在未设置 PdfSaveOptions.IsFontSubstitutionCharGranularity 属性的情况下生成的，另一个是在将 PdfSaveOptions.IsFontSubstitutionCharGranularity 属性设置为 true 后生成的。

正如您在第一个 Pdf 中看到的那样，由于不间断连字符，整个句子的字体已从 Times New Roman 更改为 Arial Unicode MS。而在第二个 Pdf 中，只有 Non-Breaking Hyphen 的字体发生了变化。

|**第一个 PDF 文件**|
|:- |
|![待办事项：图像_替代_文本](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_1.png)|


|**第二个 PDF 文件**|
|:- |
|![待办事项：图像_替代_文本](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_2.png)|
### **示例代码**


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-ChangeFontUnicodeCharacterToPdf-ChangeFontUnicodeCharacterWhileSavingToPdf.cs" >}}



