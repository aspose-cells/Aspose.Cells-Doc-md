---
title: Автоподгонка столбцов и строк при загрузке HTML в рабочую книгу с помощью Node.js через C++
linktitle: Автоматическое подгонка столбцов и строк при загрузке HTML в Рабочей книге
type: docs
weight: 120
url: /ru/nodejs-cpp/autofit-columns-and-rows-while-loading-html-in-workbook/
description: Узнайте, как автоматически подгонять столбцы и строки при загрузке HTML файлов в рабочую книгу с помощью Aspose.Cells for Node.js via C++.
---

## **Возможные сценарии использования**

Вы можете автоматически подгонять столбцы и строки при загрузке вашего HTML-файла внутри объекта Рабочая книга. Для этого установите свойство [**HtmlLoadOptions.getAutoFitColsAndRows()**](https://reference.aspose.com/cells/nodejs-cpp/htmlloadoptions/#getAutoFitColsAndRows--) в значение **true**.

## **Автоматическая подгонка столбцов и строк при загрузке HTML в Рабочей книге**

Следующий пример кода сначала загружает пример HTML в рабочую книгу без параметров загрузки и сохраняет его в формате XLSX. Затем повторно загружает HTML в рабочую книгу, на этот раз установив свойство [**HtmlLoadOptions.getAutoFitColsAndRows()**](https://reference.aspose.com/cells/nodejs-cpp/htmlloadoptions/#getAutoFitColsAndRows--) в **true**, и сохраняет в формате XLSX. Загрузите оба файла Excel: [Выходной файл Excel без AutoFitColsAndRows](outputWithout_AutoFitColsAndRows.xlsx) и [Выходной файл Excel с AutoFitColsAndRows](outputWith_AutoFitColsAndRows.xlsx). Следующий скриншот показывает эффект от свойства [**HtmlLoadOptions.getAutoFitColsAndRows()**](https://reference.aspose.com/cells/nodejs-cpp/htmlloadoptions/#getAutoFitColsAndRows--) на обоих выходных файлах Excel.

![todo:image_alt_text](autofit-columns-and-rows-while-loading-html-in-workbook_1.png)

## **Образец кода**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Sample HTML.
const sampleHtml = "<html><body><table><tr><td>This is sample text.</td><td>Some text.</td></tr><tr><td>This is another sample text.</td><td>Some text.</td></tr></table></body></html>";

// Load HTML string into memory stream.
const ms = Uint8Array.from(sampleHtml, c => c.charCodeAt(0));

// Load memory stream into workbook.
let wb = new AsposeCells.Workbook(ms);

// Save the workbook in xlsx format.
wb.save(path.join(dataDir, "outputWithout_AutoFitColsAndRows.xlsx"));

// Specify the HTMLLoadOptions and set AutoFitColsAndRows = true.
const opts = new AsposeCells.HtmlLoadOptions();
opts.setAutoFitColsAndRows(true);

// Load memory stream into workbook with the above HTMLLoadOptions.
wb = new AsposeCells.Workbook(ms, opts);

// Save the workbook in xlsx format.
wb.save(path.join(dataDir, "outputWith_AutoFitColsAndRows.xlsx"));
```

{{< app/cells/assistant language="nodejs-cpp" >}}
