---
title: Конвертация Excel в CSV, TSV и Txt через Node.js с помощью C++
linktitle: Сохранить как CSV, TSV и Txt
type: docs
weight: 40
url: /ru/nodejs-cpp/convert-excel-to-csv-tsv-and-txt/
description: Узнайте, как конвертировать файлы Excel в форматы CSV, TSV и TXT с помощью Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}}

Aspose.Cells позволяет конвертировать файлы Excel, ODS, JSON и другие форматы в CSV, TSV и TXT.

{{% /alert %}}

## **Сохранение рабочей книги в текстовом или CSV формате**

Иногда вам нужно конвертировать или сохранить рабочую книгу с несколькими рабочими листами в текстовом формате. Для текстовых форматов (например, TXT, TabDelim, CSV и др.) по умолчанию как Microsoft Excel, так и Aspose.Cells сохраняют только содержимое активного листа.

Следующий пример кода объясняет, как сохранить всю книгу в текстовом формате. Загрузите исходную книгу, которая может быть любым файлом таблицы Microsoft Excel или OpenOffice (например, XLS, XLSX, XLSM, XLSB, ODS и т. д.) с любым количеством листов.

При выполнении кода он преобразует данные всех листов рабочей книги в формат TXT

Вы можете изменить тот же пример, чтобы сохранить свой файл в CSV. По умолчанию, [**TxtSaveOptions.getSeparator()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getSeparator--) это запятая, поэтому не указывайте разделитель при сохранении в формат CSV.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Load your source workbook
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1.xls"));

// Text save options. You can use any type of separator
const opts = new AsposeCells.TxtSaveOptions();
opts.setSeparator('\t');
opts.setExportAllSheets(true);

// Save entire workbook data into file
workbook.save(path.join(dataDir, "out.txt"), opts);
```

## **Сохранение текстовых файлов с пользовательским разделителем**

Текстовые файлы содержат данные электронных таблиц без форматирования. Файл представляет собой своего рода обычный текстовый файл, который может содержать некоторые настраиваемые разделители между его данными.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Create a Workbook object and opening the file from its path
const wb = new AsposeCells.Workbook(filePath);

// Instantiate Text File's Save Options
const options = new AsposeCells.TxtSaveOptions();

// Specify the separator
options.setSeparator(";");

// Save the file with the options
wb.save(path.join(dataDir, "output.csv"), options);
```


## **Продвинутые темы**
- [Сохранять разделители для пустых строк при экспорте таблиц в формат CSV](/cells/ru/nodejs-cpp/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/)
- [Обрезать ведущие пустые строки и столбцы при экспорте электронных таблиц в формат CSV](/cells/ru/nodejs-cpp/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)
{{< app/cells/assistant language="nodejs-cpp" >}}
