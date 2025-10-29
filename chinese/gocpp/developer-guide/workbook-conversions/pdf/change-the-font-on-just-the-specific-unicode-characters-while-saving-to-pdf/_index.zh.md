---
title: 在保存为 PDF 时，仅更改特定 Unicode 字符的字体，使用 Golang 通过 C++
linktitle: 更改Unicode字符的字体
type: docs
weight: 260
url: /zh/go-cpp/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/
description: 了解如何在使用 Golang 通过 C++ 和 Aspose.Cells 保存为 PDF 时更改特定 Unicode 字符的字体。
---

{{% alert color="primary" %}}

一些Unicode字符无法使用用户指定的字体显示。其中一个这样的Unicode字符是**非间断连字**（U+2011），其Unicode编号为8209。这个字符不能用**Times New Roman**显示，但可以用其他字体如**Arial Unicode MS**显示。

 当某个字符出现在使用特定字体（如Times New Roman）的单词或句子中时，Aspose.Cells会将整个单词或句子的字体更改为可以显示该字符的字体（如Arial Unicode MS）。

 但对于一些用户来说，这是不理想的行为，他们只希望更改特定字符的字体，而不是整个单词或句子的字体。

 为了解决这个问题，Aspose.Cells提供了`PdfSaveOptions.IsFontSubstitutionCharGranularity`属性，应将其设置为`true`，这样只有无法显示的特定字符的字体会被更换为可显示的字体，其余部分保持原字体。

{{% /alert %}}

## **示例**

以下屏幕截图比较了以下示例代码生成的两个输出PDF。

 一个没有设置`PdfSaveOptions.IsFontSubstitutionCharGranularity`属性的生成结果，另一个在将该属性设置为`true`之后生成。

 如第一个PDF所示，由于非断行连字符，整个句子的字体从Times New Roman变为了Arial Unicode MS。而在第二个PDF中，只有非断行连字符的字体发生了变化。

|**第一个PDF文件**|
| :- |
|![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_1.png)|

|**第二个PDF文件**|
| :- |
|![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_2.png)|

### **示例代码**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChangeTheFontOnJustTheSpecificUnicodeCharactersWhileSavingToPdf.go" >}}
