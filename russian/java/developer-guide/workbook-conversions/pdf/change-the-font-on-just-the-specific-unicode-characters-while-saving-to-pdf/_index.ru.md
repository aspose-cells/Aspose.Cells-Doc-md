---
title: Измените шрифт только на определенные символы Unicode при сохранении в PDF
type: docs
weight: 150
url: /ru/java/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/
---
{{% alert color="primary" %}}

 Некоторые символы Юникода не отображаются с помощью указанного пользователем шрифта. Одним из таких символов Unicode является**Неразрывный дефис** (U+2011), а его номер Unicode – 8209. Этот символ нельзя отобразить с**Таймс Нью Роман** , но он может отображаться с другими шрифтами, такими как**Ариал Юникод МС**.

Когда такой символ встречается внутри какого-либо слова или предложения, написанного определенным шрифтом, например Times New Roman, тогда Aspose.Cells изменяет шрифт всего слова или предложения на шрифт, который может отображать этот символ, например Arial Unicode, на MS.

Однако это нежелательное поведение для некоторых пользователей, и они хотят, чтобы был изменен только шрифт конкретного символа, а не изменение шрифта всего слова или предложения.

 Чтобы решить эту проблему, Aspose.Cells предоставляет[**PdfSaveOptions.setFontSubstitutionCharGranularity()**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IsFontSubstitutionCharGranularity) свойство, которое должно быть установлено**истинный**так что изменяется только шрифт конкретного символа, который не отображается, а шрифт для остальной части слова или предложения остается прежним.

{{% /alert %}}

## **Пример**

 На следующем снимке экрана сравниваются два выходных PDF-файла, созданных с помощью приведенного ниже примера кода. Один был сгенерирован без установки[**PdfSaveOptions.setFontSubstitutionCharGranularity()**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IsFontSubstitutionCharGranularity) свойство, а другое было создано после установки[**PdfSaveOptions.setFontSubstitutionCharGranularity()**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IsFontSubstitutionCharGranularity) собственность на**истинный**. Как вы можете видеть в первом PDF-файле, шрифт всего предложения изменился с Times New Roman на Arial Unicode MS из-за неразрывного дефиса. В то время как во втором PDF изменился только шрифт Non-Breaking Hyphen.

![дело:изображение_альтернативный_текст](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ChangeFontonspecificUnicodecharacters-ChangeFontonspecificUnicodecharacters.java" >}}
