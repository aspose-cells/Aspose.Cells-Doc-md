---
title: Изменение шрифта только для определенных символов Unicode при сохранении в PDF
type: docs
weight: 150
url: /ru/java/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/
---

{{% alert color="primary" %}}

Некоторые символы Unicode не могут быть отображены заданным пользователем шрифтом. Один из таких символов Unicode - это **Неразрывный дефис** (U+2011) и его Unicode-номер 8209. Этот символ не может быть отображен шрифтом **Times New Roman**, но его можно отобразить другими шрифтами, такими как **Arial Unicode MS**.

Когда такой символ встречается внутри слова или предложения, который находится в определенном шрифте, например Times New Roman, то Aspose.Cells изменяет шрифт всего слова или предложения на шрифт, который может отобразить этот символ, например Arial Unicode MS.

Однако это нежелательное поведение для некоторых пользователей и они хотят, чтобы шрифт только конкретного символа был изменен, а не весь шрифт слова или предложения.

Чтобы решить эту проблему, Aspose.Cells предоставляет свойство [**PdfSaveOptions.setFontSubstitutionCharGranularity()**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IsFontSubstitutionCharGranularity), которое должно быть установлено на **true**, чтобы изменить только шрифт конкретного символа, который не отображается, остальной текст оставался с тем же шрифтом.

{{% /alert %}}

## **Пример**

Следующий снимок экрана сравнивает два сгенерированных PDF, сгенерированных образцовым кодом ниже. Один был сгенерирован без установки свойства [**PdfSaveOptions.setFontSubstitutionCharGranularity()**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IsFontSubstitutionCharGranularity), а другой был сгенерирован после установки свойства [**PdfSaveOptions.setFontSubstitutionCharGranularity()**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IsFontSubstitutionCharGranularity) в **true**. Как видно на первом PDF, шрифт всего предложения изменился с Times New Roman на Arial Unicode MS из-за Неразрывного дефиса. В то время как на втором PDF, изменен только шрифт неразрывного дефиса.

![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ChangeFontonspecificUnicodecharacters-ChangeFontonspecificUnicodecharacters.java" >}}
