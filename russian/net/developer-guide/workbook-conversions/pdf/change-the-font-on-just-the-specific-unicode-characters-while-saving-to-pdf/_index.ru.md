---
title: Изменение шрифта только для определенных символов Unicode при сохранении в PDF
type: docs
weight: 260
url: /ru/net/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/
---

{{% alert color="primary" %}} 

Некоторые символы Unicode не могут быть отображены выбранным пользователем шрифтом. Один из таких символов Unicode - **Неразрывной дефис** (U+2011), его код Unicode - 8209. Этот символ нельзя отобразить шрифтом **Times New Roman**, но его можно отобразить другими шрифтами, например, **Arial Unicode MS**.

Если такой символ встречается внутри какого-либо слова или предложения, которое использует определенный шрифт, например, Times New Roman, то Aspose.Cells изменяет шрифт всего слова или предложения на шрифт, который может отобразить этот символ, например, Arial Unicode MS.

Однако это нежелательное поведение для некоторых пользователей, и они хотят, чтобы поменялся только шрифт этого конкретного символа, а не всего слова или предложения.

Для решения этой проблемы Aspose.Cells предоставляет свойство PdfSaveOptions.IsFontSubstitutionCharGranularity, которое должно быть установлено в true, чтобы только шрифт конкретного символа, который не может отобразиться, был изменен на отображаемый шрифт, а остальное слово или предложение должно оставаться в оригинальном шрифте.

{{% /alert %}} 
## **Пример**
На следующем скриншоте сравниваются два выходных PDF-файла, сгенерированных примерным кодом ниже.

Один сгенерирован без установки свойства PdfSaveOptions.IsFontSubstitutionCharGranularity, а другой - с установкой свойства PdfSaveOptions.IsFontSubstitutionCharGranularity в true.

Как видно на первом PDF, шрифт всего предложения изменился с Times New Roman на Arial Unicode MS из-за  Non-Breaking Hyphen. В то время как на втором PDF, изменился только шрифт Non-Breaking Hyphen.

|**Первый файл PDF**|
| :- |
|![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_1.png)|


|**Второй файл PDF**|
| :- |
|![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_2.png)|
### **Образец кода**


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-ChangeFontUnicodeCharacterToPdf-ChangeFontUnicodeCharacterWhileSavingToPdf.cs" >}}



