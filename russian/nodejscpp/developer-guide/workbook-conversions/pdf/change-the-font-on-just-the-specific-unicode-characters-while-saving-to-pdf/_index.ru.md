---
title: Изменение шрифта только для отдельных Юникод символов при сохранении в PDF с помощью Node.js через C++
linktitle: Изменение шрифта только для определенных символов Unicode при сохранении в PDF
type: docs
weight: 260
url: /ru/nodejs-cpp/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/
description: Узнайте, как изменять шрифт конкретных Юникод символов при сохранении в PDF с помощью Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}} 

Некоторые символы Unicode не могут быть отображены заданным пользователем шрифтом. Один из таких символов Unicode - это **Неразрывный дефис** (U+2011) и его Unicode-номер 8209. Этот символ не может быть отображен шрифтом **Times New Roman**, но его можно отобразить другими шрифтами, такими как **Arial Unicode MS**.

Когда такой символ встречается внутри слова или предложения, которое использует шрифт Times New Roman, Aspose.Cells меняет шрифт всего слова или предложения на шрифт, который может отображать этот символ, например Arial Unicode или MS.

Однако такое поведение нежелательно для некоторых пользователей, и они хотят менять шрифт только для конкретного символа, а не для всего слова или предложения.

Для решения этой проблемы Aspose.Cells предоставляет свойство `PdfSaveOptions.isFontSubstitutionCharGranularity`, которое нужно установить в true, чтобы изменялся шрифт только для тех символов, которые нельзя отобразить, а остальные оставались в исходном шрифте.

{{% /alert %}} 

## **Пример**
На следующем скриншоте сравниваются два выходных PDF-файла, сгенерированных примерным кодом ниже.

Один PDF создается без установки свойства `PdfSaveOptions.isFontSubstitutionCharGranularity`, а другой — после установки этого свойства в true.

Как видно в первом PDF, шрифт всего предложения изменен с Times New Roman на Arial Unicode MS из-за тире, неразрывного. Во втором PDF изменен только шрифт этого тире.

|**Первый файл PDF**|
| :- |
|![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_1.png)|


|**Второй файл PDF**|
| :- |
|![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_2.png)|
### **Образец кода**


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object
const workbook = new AsposeCells.Workbook();

// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access cells
const cell1 = worksheet.getCells().get("A1");
const cell2 = worksheet.getCells().get("B1");

// Set the styles of both cells to Times New Roman
let style = cell1.getStyle();
style.getFont().setName("Times New Roman");
cell1.setStyle(style);
cell2.setStyle(style);

// Put the values inside the cell
cell1.putValue("Hello without Non-Breaking Hyphen");
cell2.putValue("Hello" + String.fromCharCode(8209) + " with Non-Breaking Hyphen");

// Autofit the columns
worksheet.autoFitColumns();

// Save to Pdf without setting PdfSaveOptions.IsFontSubstitutionCharGranularity
workbook.save(path.join(dataDir, "SampleOutput_out.pdf"));

// Save to Pdf after setting PdfSaveOptions.IsFontSubstitutionCharGranularity to true
const opts = new AsposeCells.PdfSaveOptions();
opts.setIsFontSubstitutionCharGranularity(true);
workbook.save(path.join(dataDir, "SampleOutput2_out.pdf"), opts);
```



