---
title: 保存为 PDF 时仅更改特定 Unicode 字符的字体
type: docs
weight: 150
url: /zh/java/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/
---
{{% alert color="primary" %}}

某些 Unicode 字符无法通过用户指定的字体显示。一个这样的 Unicode 字符是**不间断连字符**(U+2011) 其 Unicode 编号为 8209。此字符无法显示为**英语字体格式一种** 但它可以用其他字体显示，例如**宋体 Unicode MS**.

当这样的字符出现在某些特定字体（如 Times New Roman）的单词或句子中时，Aspose.Cells 将整个单词或句子的字体更改为可以显示此字符的字体，如 Arial Unicode 到 MS。

然而，这对某些用户来说是不受欢迎的行为，他们只希望必须更改特定字符的字体，而不是更改整个单词或句子的字体。

针对这个问题，Aspose.Cells提供[**PdfSaveOptions.setFontSubstitutionCharGranularity()**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IsFontSubstitutionCharGranularity)应该设置的属性**真的**这样只有无法显示的特定字符的字体发生变化，而其余单词或句子的字体保持不变。

{{% /alert %}}

## **例子**

下面的屏幕截图比较了下面示例代码生成的两个输出 PDF。一个没有设置就生成了[**PdfSaveOptions.setFontSubstitutionCharGranularity()**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IsFontSubstitutionCharGranularity)属性，另一个是在设置后生成的[**PdfSaveOptions.setFontSubstitutionCharGranularity()**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IsFontSubstitutionCharGranularity)财产给**真的**.正如您在第一个 PDF 中看到的那样，由于不间断连字符，整个句子的字体已从 Times New Roman 更改为 Arial Unicode MS。而在第二个 PDF 中，只有 Non-Breaking Hyphen 的字体发生了变化。

![待办事项：图像_替代_文本](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ChangeFontonspecificUnicodecharacters-ChangeFontonspecificUnicodecharacters.java" >}}
