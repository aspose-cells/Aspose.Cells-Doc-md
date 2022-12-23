---
title: Измените шрифт только на определенные символы Unicode при сохранении на PDF.
type: docs
weight: 260
url: /ru/net/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/
---
{{% alert color="primary" %}} 

 Некоторые символы Unicode не отображаются шрифтом, указанным пользователем. Одним из таких символов Unicode является**Неразрывный дефис** (U+2011), а его номер Unicode – 8209. Этот символ нельзя отобразить с**Таймс Нью Роман** , но он может отображаться с другими шрифтами, такими как**Ариал Юникод МС**.

Когда такой символ встречается внутри какого-либо слова или предложения, написанного определенным шрифтом, например Times New Roman, тогда Aspose.Cells изменяет шрифт всего слова или предложения на шрифт, который может отображать этот символ, например Arial Unicode, на MS.

Однако это нежелательное поведение для некоторых пользователей, и они хотят, чтобы был изменен только шрифт этого конкретного символа, а не изменение шрифта всего слова или предложения.

Чтобы решить эту проблему, Aspose.Cells предоставляет свойство PdfSaveOptions.IsFontSubstitutionCharGranularity, которое должно быть установлено в значение true, чтобы только шрифт определенного символа, который не отображается, был изменен на отображаемый шрифт, а остальная часть слова или предложения должна оставаться в исходном шрифте.

{{% /alert %}} 
## **Пример**
На следующем снимке экрана сравниваются два выходных PDF-файла, созданных с помощью приведенного ниже примера кода.

Один создается без установки свойства PdfSaveOptions.IsFontSubstitutionCharGranularity, а другой создается после установки для свойства PdfSaveOptions.IsFontSubstitutionCharGranularity значения true.

Как вы можете видеть в первом PDF-файле, шрифт всего предложения изменился с Times New Roman на Arial Unicode MS из-за неразрывного дефиса. В то время как во втором Pdf изменился только шрифт Non-Breaking Hyphen.

|**Первый PDF-файл**|
|:- |
|![дело:изображение_альтернативный_текст](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_1.png)|


|**Второй PDF-файл**|
|:- |
|![дело:изображение_альтернативный_текст](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_2.png)|
### **Образец кода**


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-ChangeFontUnicodeCharacterToPdf-ChangeFontUnicodeCharacterWhileSavingToPdf.cs" >}}



