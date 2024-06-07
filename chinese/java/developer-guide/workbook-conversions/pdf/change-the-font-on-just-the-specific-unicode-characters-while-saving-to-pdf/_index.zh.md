---
title: 在保存为PDF时仅更改特定Unicode字符的字体
type: docs
weight: 150
url: /zh/java/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/
---

{{% alert color="primary" %}}

一些Unicode字符无法由用户指定的字体显示。这样的Unicode字符之一是**不换行连字符**（U+2011），其Unicode号为8209。不能使用**Times New Roman**显示此字符，但可以使用**Arial Unicode MS**等其他字体显示此字符。

当这样的字符出现在某一特定字体（例如Times New Roman）的单词或句子中时，Aspose.Cells会将整个单词或句子的字体更改为可以显示此字符的字体，例如Arial Unicode MS。

然而，这对一些用户来说是不希望的行为，他们只希望特定字符的字体被更改，而不是更改整个单词或句子的字体。

为解决此问题，Aspose.Cells提供了[**PdfSaveOptions.setFontSubstitutionCharGranularity()**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IsFontSubstitutionCharGranularity)属性，应将其设置为**true**，这样只有无法显示的特定字符的字体才会更改，而其他单词或句子的字体保持不变。

{{% /alert %}}

## **例子**

以下屏幕截图比较了以下示例代码生成的两个输出PDF。一个是在未设置[**PdfSaveOptions.setFontSubstitutionCharGranularity()**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IsFontSubstitutionCharGranularity)属性的情况下生成的，另一个是在将[**PdfSaveOptions.setFontSubstitutionCharGranularity()**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IsFontSubstitutionCharGranularity)属性设置为**true**后生成的。如您在第一个PDF中所见，由于不换行连字符，整个句子的字体已从Times New Roman更改为Arial Unicode MS。而在第二个PDF中，只有不换行连字符的字体已更改。

![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ChangeFontonspecificUnicodecharacters-ChangeFontonspecificUnicodecharacters.java" >}}
