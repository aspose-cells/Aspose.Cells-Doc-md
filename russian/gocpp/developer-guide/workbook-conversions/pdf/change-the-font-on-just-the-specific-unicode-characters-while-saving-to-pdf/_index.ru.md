---
title: Измените шрифт только для конкретных символов Юникода при сохранении в PDF с помощью Golang через C++
linktitle: Изменить шрифт для символов Юникода
type: docs
weight: 260
url: /ru/go-cpp/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/
description: Узнайте, как изменить шрифт конкретных символов Юникода при сохранении в PDF с помощью Aspose.Cells и Golang через C++.
---

{{% alert color="primary" %}}

Некоторые символы Unicode не могут быть отображены заданным пользователем шрифтом. Один из таких символов Unicode - это **Неразрывный дефис** (U+2011) и его Unicode-номер 8209. Этот символ не может быть отображен шрифтом **Times New Roman**, но его можно отобразить другими шрифтами, такими как **Arial Unicode MS**.

Когда внутри слова или предложения появляется такой символ, который в шрифте, например Times New Roman, отображается неправильно, Aspose.Cells меняет шрифт всего слова или предложения на шрифт, который может отображать этот символ, например Arial Unicode MS.

Однако это нежелательное поведение для некоторых пользователей, и они хотят, чтобы изменялся только шрифт этого конкретного символа, а не всего слова или предложения.

Чтобы решить эту проблему, Aspose.Cells предоставляет свойство `PdfSaveOptions.IsFontSubstitutionCharGranularity`, которое должно быть установлено в `true`, чтобы изменялся только шрифт конкретного неподдерживаемого символа, а остальной текст оставался в исходном шрифте.

{{% /alert %}}

## **Пример**

На следующем скриншоте сравниваются два выходных PDF-файла, сгенерированных примерным кодом ниже.

Один файл генерируется без установки свойства `PdfSaveOptions.IsFontSubstitutionCharGranularity`, а другой — после установки этого свойства в `true`.

Как видно на первом PDF, шрифт всего предложения изменился с Times New Roman на Arial Unicode MS из-за тире без разрывов. Во втором PDF изменился только шрифт тире без разрывов.

|**Первый PDF файл**|
| :- |
|![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_1.png)|

|**Второй PDF файл**|
| :- |
|![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_2.png)|

### **Образец кода**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChangeTheFontOnJustTheSpecificUnicodeCharactersWhileSavingToPdf.go" >}}
