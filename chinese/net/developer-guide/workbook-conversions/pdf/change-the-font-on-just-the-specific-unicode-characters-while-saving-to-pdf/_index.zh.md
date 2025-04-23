---
title: 在保存为PDF时仅更改特定Unicode字符的字体
type: docs
weight: 260
url: /zh/net/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/
---

{{% alert color="primary" %}} 

一些Unicode字符无法由用户指定的字体显示。 其中一个Unicode字符是**非断开连字符**（U+2011），其Unicode编号为8209。 Times New Roman不能显示此字符，但Arial Unicode MS等其他字体可以显示。

当此类字符出现在使用特定字体（如Times New Roman）的某个词或句子中时，Aspose.Cells会将整个单词或句子的字体更改为可以显示此字符的字体，如Arial Unicode to MS。

但对一些用户来说，这是不希望的行为，并且他们希望只更改特定字符的字体，而不是更改整个单词或句子的字体。

为了解决这个问题，Aspose.Cells提供了PdfSaveOptions.IsFontSubstitutionCharGranularity属性，该属性应设置为true，以便只更改无法显示的特定字符的字体为可显示的字体，并使剩余的单词或句子保持在原始字体中。

{{% /alert %}} 
## **示例**
以下屏幕截图比较了以下示例代码生成的两个输出PDF。

一个是在不设置PdfSaveOptions.IsFontSubstitutionCharGranularity属性的情况下生成的，另一个是在将PdfSaveOptions.IsFontSubstitutionCharGranularity属性设置为true后生成的。

如您在第一个PDF中看到的，整个句子的字体已从Times New Roman更改为Arial Unicode MS，因为有非断开连字符。 而在第二个PDF中，只更改了非断开连字符的字体。

| **第一个PDF文件** |
| :- |
|![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_1.png)|


| **第二个PDF文件** |
| :- |
|![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_2.png)|
### **示例代码**


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-ChangeFontUnicodeCharacterToPdf-ChangeFontUnicodeCharacterWhileSavingToPdf.cs" >}}



{{< app/cells/assistant language="csharp" >}}
