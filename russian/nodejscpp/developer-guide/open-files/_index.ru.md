---
title: Загрузка и управление файлами Excel, OpenOffice, Json, Csv и Html
linktitle: Открытие файлов
type: docs
weight: 20
url: /ru/nodejs-cpp/loading-saving-and-managing/
description: С Aspose.Cells просто создавать, открывать и управлять файлами Excel, CSV, TSV, ODS, HTML, Numbers, Json, XML, Pdf, Jpg, Tiff, Image, Mht и XPS с помощью Node.js через C++.
---

{{% alert color="primary" %}}

 С Aspose.Cells просто создавать, открывать и управлять файлами Excel, например извлекать данные или использовать дизайн-шаблон для ускорения процесса разработки.

{{% /alert %}}

## **Создание новой книги**
Следующий пример создает новую книгу с нуля.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const licensePath = path.join(dataDir, "Aspose.Cells.lic");

try {
// Create a License object
const license = new AsposeCells.License();

// Set the license of Aspose.Cells to avoid the evaluation limitations
license.setLicense(licensePath);
} catch (ex) {
console.log(ex.message);
}

// Instantiate a Workbook object that represents Excel file.
const wb = new AsposeCells.Workbook();

// When you create a new workbook, a default "Sheet1" is added to the workbook.
const sheet = wb.getWorksheets().get(0);

// Access the "A1" cell in the sheet.
const cell = sheet.getCells().get("A1");

// Input the "Hello World!" text into the "A1" cell
cell.putValue("Hello World!");

// Save the Excel file.
wb.save(path.join(dataDir, "MyBook_out.xlsx"));
```

## **Открытие и сохранение файла**
 С Aspose.Cells просто открывать, сохранять и управлять файлами Excel.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Opening through Path
// Creating a Workbook object and opening an Excel file using its file path
const workbook1 = new AsposeCells.Workbook(path.join(dataDir, "Book1.xlsx"));
// Adding new sheet
const sheet = workbook1.getWorksheets().add("MySheet");
// Setting active sheet
workbook1.getWorksheets().setActiveSheetIndex(1);
// Setting values.
const cells = sheet.getCells();
// Setting text
cells.get("A1").putValue("Hello!");
// Setting number
cells.get("A2").putValue(1000);
// Setting Date Time
const cell = cells.get("A3");
cell.putValue(new Date());
const style = cell.getStyle();
style.setNumber(14);
cell.setStyle(style);
// Setting formula
cells.get("A4").setFormula("=SUM(A1:A3)");
// Saving the workbook to disk.
workbook1.save(path.join(dataDir, "dest.xlsx"));
```

## **Расширенные темы**
- [Различные способы открытия файлов](/cells/ru/nodejs-cpp/different-ways-to-open-files/)
- [Фильтрация заданных имен при загрузке рабочей книги](/cells/ru/nodejs-cpp/filter-defined-names-while-loading-workbook/)
- [Фильтр объектов при загрузке книги или листа](/cells/ru/nodejs-cpp/filter-objects-while-loading-workbook-or-worksheet/)
- [Фильтрация типа данных при загрузке книги из файла шаблона](/cells/ru/nodejs-cpp/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/)
- [Получение предупреждений при загрузке файла Excel](/cells/ru/nodejs-cpp/get-warnings-while-loading-excel-file/)
- [Загрузка исходного файла Excel без диаграмм](/cells/ru/nodejs-cpp/load-source-excel-file-without-charts/)
- [Загрузка конкретных листов в книге](/cells/ru/nodejs-cpp/load-specific-worksheets-in-a-workbook/)
- [Загружать книгу с указанным размером бумаги принтера](/cells/ru/nodejs-cpp/load-workbook-with-specified-printer-paper-size/)
- [Открытие файлов с различными форматами](/cells/ru/nodejs-cpp/opening-different-microsoft-excel-versions-files/)
- [Открытие файлов с различными форматами](/cells/ru/nodejs-cpp/opening-files-with-different-formats/)
- [Оптимизация использования памяти при работе с большими файлами с большими наборами данных](/cells/ru/nodejs-cpp/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)
- [Чтение таблицы чисел, разработанной Apple Inc. с использованием Aspose.Cells](/cells/ru/nodejs-cpp/read-numbers-spreadsheet-developed-by-apple-inc-using-aspose-cells/)
- [Прекратите преобразование или загрузку с использованием объекта InterruptMonitor, если это занимает слишком много времени](/cells/ru/nodejs-cpp/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/)
- [Использование API LightCells](/cells/ru/nodejs-cpp/using-lightcells-api/)
- [Преобразовать CSV в JSON](/cells/ru/nodejs-cpp/convert-csv-to-json/)
- [Преобразование Excel в JSON](/cells/ru/nodejs-cpp/convert-excel-to-json/)
- [Преобразовать JSON в CSV](/cells/ru/nodejs-cpp/convert-json-to-csv/)
- [Преобразовать JSON в Excel](/cells/ru/nodejs-cpp/convert-json-to-excel/)
- [Преобразование Excel в Html](/cells/ru/nodejs-cpp/convert-excel-to-html/)
{{< app/cells/assistant language="nodejs-cpp" >}}
