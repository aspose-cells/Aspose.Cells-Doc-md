---
title: Получить ширину и высоту бумаги настройки страницы листа с помощью Node.js через C++
linktitle: Получить ширину и высоту бумаги параметров страницы листа
type: docs
weight: 50
url: /ru/nodejs-cpp/get-paper-width-and-height-of-page-setup-of-worksheet/
description: Узнайте, как программно получить ширину и высоту бумаги настройки страницы Excel листа с помощью Node.js через C++.
keywords: ширина и высота бумаги настройки страницы Excel с помощью Node.js через C++
---

## **Возможные сценарии использования**

Иногда необходимо знать ширину и высоту бумаги, установленную в настройке страницы листа. Для этого используйте свойства [**PageSetup.getPaperWidth()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPaperWidth--) и [**PageSetup.getPaperHeight()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPaperHeight--). 

## **Получение ширины и высоты бумаги на листе Excel**

Следующий пример кода объясняет использование свойств [**PageSetup.getPaperWidth()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPaperWidth--) и [**PageSetup.getPaperHeight()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPaperHeight--). Сначала он изменяет размер бумаги на *A2*, затем ищет ширину и высоту бумаги, затем меняет его на *A3*, *A4*, *Letter* и соответственно находит ширину и высоту бумаги.

### **Образец кода**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Create an instance of Workbook class
const book = new AsposeCells.Workbook();

// Access first worksheet
const sheet = book.getWorksheets().get(0);

// Set paper size to A2 and print paper width and height in inches
sheet.getPageSetup().setPaperSize(AsposeCells.PaperSizeType.PaperA2);
console.log("PaperA2: " + sheet.getPageSetup().getPaperWidth() + "x" + sheet.getPageSetup().getPaperHeight());

// Set paper size to A3 and print paper width and height in inches
sheet.getPageSetup().setPaperSize(AsposeCells.PaperSizeType.PaperA3);
console.log("PaperA3: " + sheet.getPageSetup().getPaperWidth() + "x" + sheet.getPageSetup().getPaperHeight());

// Set paper size to A4 and print paper width and height in inches
sheet.getPageSetup().setPaperSize(AsposeCells.PaperSizeType.PaperA4);
console.log("PaperA4: " + sheet.getPageSetup().getPaperWidth() + "x" + sheet.getPageSetup().getPaperHeight());

// Set paper size to Letter and print paper width and height in inches
sheet.getPageSetup().setPaperSize(AsposeCells.PaperSizeType.PaperLetter);
console.log("PaperLetter: " + sheet.getPageSetup().getPaperWidth() + "x" + sheet.getPageSetup().getPaperHeight());
```

### **Вывод в консоль**

Вот вывод в консоль вышеуказанного образца кода.

{{< highlight java >}}

PaperA2: 16.54x23.39

PaperA3: 11.69x16.54

PaperA4: 8.27x11.69

PaperLetter: 8.5x11

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
