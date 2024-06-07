---
title: 在保存为PDF时仅更改特定Unicode字符的字体
type: docs
weight: 260
url: /zh/net/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/
---

{{% alert color="primary" %}} 

用户指定字体无法显示一些Unicode字符。这样一个Unicode字符是**连字符**（U+2011），其Unicode编号为8209。这个字符不能用**Times New Roman**显示，但可以用其他字体如**Arial Unicode MS**显示。

当这样一个字符出现在某个特定字体的单词或句子中，比如在Times New Roman字体中，那么Aspose.Cells会将整个单词或句子的字体更改为可显示这个字符的字体，比如Arial Unicode MS。

然而，对一些用户而言，这种行为是不希望的，他们只希望更改特定字符的字体，而不是更改整个单词或句子的字体。

为了解决这个问题，Aspose.Cells提供了PdfSaveOptions.IsFontSubstitutionCharGranularity属性，应将其设置为true，以便仅更改无法显示的特定字符的字体以显示的字体，而单词或句子的其余部分应保持原始字体。

{{% /alert %}} 
## **例子**
以下屏幕截图比较了以下示例代码生成的两个输出PDF。

一个是在没有设置PdfSaveOptions.IsFontSubstitutionCharGranularity属性的情况下生成的Pdf，另一个是在将PdfSaveOptions.IsFontSubstitutionCharGranularity属性设置为true后生成的。

正如您在第一个Pdf中所看到的，由于连字符发生了变化，整个句子的字体已从Times New Roman更改为Arial Unicode MS。而在第二个Pdf中，只有连字符的字体发生了变化。

|**第一个Pdf文件**|
| :- |
|![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_1.png)|


|**第二个Pdf文件**|
| :- |
|![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_2.png)|
### **示例代码**


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-ChangeFontUnicodeCharacterToPdf-ChangeFontUnicodeCharacterWhileSavingToPdf.cs" >}}



