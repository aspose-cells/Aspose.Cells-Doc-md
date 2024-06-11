---
title: 在保存为PDF时仅更改特定Unicode字符的字体
type: docs
weight: 150
url: /zh/java/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/
---

{{% alert color="primary" %}}

一些Unicode字符无法使用用户指定的字体显示。其中一个这样的Unicode字符是**非间断连字**（U+2011），其Unicode编号为8209。这个字符不能用**Times New Roman**显示，但可以用其他字体如**Arial Unicode MS**显示。

当这样一个字符出现在某个特定字体（如Times New Roman）的单词或句子中时，Aspose.Cells会将整个单词或句子的字体更改为可显示此字符的字体，如Arial Unicode MS。

然而，这对一些用户来说是不希望的行为，他们只希望特定字符的字体更改，而不是更改整个单词或句子的字体。

为了解决这个问题，Aspose.Cells提供了[**PdfSaveOptions.setFontSubstitutionCharGranularity()**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IsFontSubstitutionCharGranularity)属性，应设置为**true**，以便仅更改无法显示的特定字符的字体，而保持单词或句子的其余部分的字体不变。

{{% /alert %}}

## **示例**

以下屏幕截图比较了以下样本代码生成的两个输出PDF。一个是在未设置[**PdfSaveOptions.setFontSubstitutionCharGranularity()**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IsFontSubstitutionCharGranularity)属性的情况下生成的，另一个是在将[**PdfSaveOptions.setFontSubstitutionCharGranularity()**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IsFontSubstitutionCharGranularity)属性设置为**true**后生成的。如您在第一个PDF中可以看到，由于非间断连字，整个句子的字体已从Times New Roman更改为Arial Unicode MS。而在第二个PDF中，仅非间断连字的字体已更改。

![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ChangeFontonspecificUnicodecharacters-ChangeFontonspecificUnicodecharacters.java" >}}
