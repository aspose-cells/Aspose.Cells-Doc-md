---
title: Копировать настройки оформления страницы из исходного листа в целевой с помощью Node.js через C++
linktitle: Скопировать настройки страницы из исходного листа в назначенный лист
type: docs
weight: 80
url: /ru/nodejs-cpp/copy-page-setup-settings-from-source-worksheet-into-destination-worksheet/
description: Этот пример показывает, как использовать API Node.js или образец библиотеки C++, чтобы программно скопировать настройки оформления страницы из исходного листа в целевой.
keywords: копировать настройки оформления страницы с помощью Node.js через C++, скопировать настройки оформления страницы в целевой лист с помощью Node.js через C++
---

## **Возможные сценарии использования**

При добавлении нового листа в рабочую книгу он содержит настройки *Page Setup* по умолчанию. Иногда необходимо перенести настройки ([**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup)) с одного листа на другой. Эта документация объясняет, как копировать настройки оформления страницы с одного листа на другой, используя API Aspose.Cells for Node.js via C++.

## **Копирование настроек страницы с исходного листа на целевой лист**

Следующий образец кода иллюстрирует, как скопировать *Параметры страницы* с одного листа на другой с использованием метода [**PageSetup.copy(PageSetup, CopyOptions)**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#copy-pagesetup-copyoptions-). Обратитесь к следующему образцу кода и его выводу консоли для справки.

## **Образец кода**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Create workbook
const wb = new AsposeCells.Workbook();

// Add two test worksheets
wb.getWorksheets().add("TestSheet1");
wb.getWorksheets().add("TestSheet2");

// Access both worksheets as TestSheet1 and TestSheet2
const TestSheet1 = wb.getWorksheets().get("TestSheet1");
const TestSheet2 = wb.getWorksheets().get("TestSheet2");

// Set the Paper Size of TestSheet1 to PaperA3ExtraTransverse
TestSheet1.getPageSetup().setPaperSize(AsposeCells.PaperSizeType.PaperA3ExtraTransverse);

// Print the Paper Size of both worksheets
console.log("Before Paper Size: " + TestSheet1.getPageSetup().getPaperSize());
console.log("Before Paper Size: " + TestSheet2.getPageSetup().getPaperSize());
console.log();

// Copy the PageSetup from TestSheet1 to TestSheet2
TestSheet2.getPageSetup().copy(TestSheet1.getPageSetup(), new AsposeCells.CopyOptions());

// Print the Paper Size of both worksheets
console.log("After Paper Size: " + TestSheet1.getPageSetup().getPaperSize());
console.log("After Paper Size: " + TestSheet2.getPageSetup().getPaperSize());
console.log();
```

## **Вывод в консоль**

{{< highlight java >}}

Before Paper Size: PaperA3ExtraTransverse

Before Paper Size: PaperLetter

After Paper Size: PaperA3ExtraTransverse

After Paper Size: PaperA3ExtraTransverse

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
