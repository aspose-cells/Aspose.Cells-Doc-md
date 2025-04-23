---
title: Различные способы сохранения файлов с помощью Node.js через C++
linktitle: Сохранить файлы
type: docs
weight: 40
url: /ru/nodejs-cpp/different-ways-to-save-files/
description: Aspose.Cells for Node.js via C++ может сохранять файлы в разные форматы, включая PDF, HTML, DOCX, PPTX, JSON и MHTML.
keywords: Aspose.Cells сохраняет Excel в PDF, HTML, JSON, CSV, TXT, XML, DOCX, PPTX, MHT, MHTML и другие с помощью Node.js через C++.
---

{{% alert color="primary" %}}

Aspose.Cells делает возможным создание и сохранение файлов. В этой статье объясняются различные способы сохранения файлов.

{{% /alert %}}

## **Различные способы сохранения файлов**

Aspose.Cells предоставляет [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), который представляет файл Microsoft Excel и содержит свойства и методы, необходимые для работы с файлами Excel. Класс [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) обеспечивает метод [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-), используемый для сохранения файлов Excel. Метод [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-) имеет множество перегрузок, которые позволяют сохранять файлы различными способами.

Формат файла, в который сохраняется файл, определяется перечислением [**SaveFormat**](https://reference.aspose.com/cells/nodejs-cpp/saveformat)

|**Типы форматов файлов**|**Описание**|
| :- | :- |
|CSV|Представляет собой файл CSV|
|Excel97To2003|Представляет файл Excel 97 - 2003|
|Xlsx|Представляет файл Excel 2007 XLSX|
|Xlsm|Представляет файл Excel 2007 XLSM|
|Xltx|Представляет шаблон файла Excel 2007 XLTX|
|Xltm|Представляет макросов Excel 2007 XLTM|
|Xlsb|Представляет двоичный файл Excel 2007 XLSB|
|SpreadsheetML|Представляет файл XML электронной таблицы|
|TSV|Представляет собой файл значений, разделенных табуляцией|
|TabDelimited|Представляет файл текста с табуляцией|
|ODS|Представляет собой файл ODS|
|Html|Представляет файл(ы) HTML|
|MHtml|Представляет файл(ы) MHTML|
|Pdf|Представляет файл PDF|
|XPS|Представляет документ XPS|
|TIFF|Представляет файл формата Tagged Image File Format (TIFF)|

## **Как сохранить файл в разных форматах**

Чтобы сохранить файлы в хранилище, укажите имя файла (с полным путем хранения) и желаемый формат файла (из перечисления [**SaveFormat**](https://reference.aspose.com/cells/nodejs-cpp/saveformat)) при вызове метода [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-) объекта [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xls");

// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Save in Excel 97 to 2003 format
workbook.save(path.join(dataDir, ".output.xls"));
// OR
workbook.save(path.join(dataDir, ".output.xls"), new AsposeCells.XlsSaveOptions());

// Save in Excel 2007 xlsx format
workbook.save(path.join(dataDir, ".output.xlsx"), AsposeCells.SaveFormat.Xlsx);

// Save in Excel 2007 xlsb format
workbook.save(path.join(dataDir, ".output.xlsb"), AsposeCells.SaveFormat.Xlsb);

// Save in ODS format
workbook.save(path.join(dataDir, ".output.ods"), AsposeCells.SaveFormat.Ods);

// Save in Pdf format
workbook.save(path.join(dataDir, ".output.pdf"), AsposeCells.SaveFormat.Pdf);

// Save in Html format
workbook.save(path.join(dataDir, ".output.html"), AsposeCells.SaveFormat.Html);

// Save in SpreadsheetML format
workbook.save(path.join(dataDir, ".output.xml"), AsposeCells.SaveFormat.SpreadsheetML);
```

## **Как сохранить книгу в Pdf**
Формат документа Portable Document Format (PDF) — это тип документа, созданный Adobe в 1990-х годах. Цель этого формата — внедрить стандарт для представления документов и другого справочного материала в формате, независимом от программного обеспечения, аппаратных средств и операционной системы. Формат PDF полностью способен содержать информацию, такую как текст, изображения, гиперссылки, поля формы, богатые медиа, цифровые подписи, вложения, метаданные, геопространственные функции и 3D-объекты, которые могут стать частью исходного документа.

Следующий код показывает, как сохранить рабочую книгу в формате PDF с помощью Aspose.Cells:
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Set value to Cell.
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Hello World!");

const saveFilePath = path.join(dataDir, "pdf1.pdf");
workbook.save(saveFilePath);

// Save as Pdf format compatible with PDFA-1a
const saveOptions = new AsposeCells.PdfSaveOptions();
saveOptions.setCompliance(AsposeCells.PdfCompliance.PdfA1a);

const pdfAFilePath = path.join(dataDir, "pdfa1a.pdf");
workbook.save(pdfAFilePath, saveOptions);
```

## **Как сохранить книгу в формате текста или CSV**

Иногда вам может потребоваться конвертировать или сохранить книгу с несколькими листами в текстовом формате. Для текстовых форматов (например, TXT, TabDelim, CSV и т. д.) как Microsoft Excel, так и Aspose.Cells по умолчанию сохраняют только содержимое активного листа.

Следующий пример кода показывает, как сохранить всю рабочую книгу в текстовом формате. Загрузите исходную рабочую книгу, которая может быть любым файлом таблицы Microsoft Excel или OpenOffice (например, XLS, XLSX, XLSM, XLSB, ODS и др.) с любым количеством листов.

При выполнении кода он преобразует данные всех листов рабочей книги в формат TXT

Вы можете изменить тот же пример для сохранения файла в формате CSV. По умолчанию [**TxtSaveOptions.getSeparator()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getSeparator--) — запятая, поэтому не указывайте разделитель при сохранении в CSV. Обратите внимание: если вы используете версию для оценки, и даже если свойство [**TxtSaveOptions.getExportAllSheets()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getExportAllSheets--) установлено в true, программа все равно экспортирует только один лист.

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

## **Как сохранить файл в текстовые файлы с пользовательским разделителем**

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

## **Как сохранить файл в поток**

Чтобы сохранить файлы в поток, создайте объект *MemoryStream* или *FileStream* и сохраните файл в этот поток, вызвав метод [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-) объекта [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook). Укажите желаемый формат файла с помощью перечисления [**SaveFormat**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) при вызове метода [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

async function downloadExcel(req, res) {
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);
// Save the workbook to a memory stream
const stream = workbook.save(AsposeCells.SaveFormat.Xlsx);

// Set the content type and file name
const contentType = "application/octet-stream";
const fileName = "output.xlsx";

// Set the response headers
res.setHeader("Content-Disposition", `attachment; filename="${fileName}"`);
res.setHeader("Content-Type", contentType);

// Write the file contents to the response body stream
res.send(stream);
}
```

## **Как сохранить файл Excel в файлы Html и Mht**
Aspose.Cells может просто сохранять файл Excel, JSON, CSV или другие файлы, которые можно загрузить с помощью Aspose.Cells как .html и .mht файлы.
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Save file to mhtml format
workbook.save("out.mht");
```


## **Как сохранить файл Excel в форматы OpenOffice (ODS, SXC, FODS, OTS)**
Мы можем сохранять файлы в формат OpenOffice: ODS, SXC, FODS, OTS и др.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Load your source workbook
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1.xlsx"));
// Save as ods file 
workbook.save("Out.ods");
// Save as sxc file 
workbook.save("Out.sxc");
// Save as fods file 
workbook.save("Out.fods");
```

## **Как сохранить файл Excel в формат JSON или XML**

JSON (JavaScript Object Notation) – это открытый стандартный файловый формат для обмена данными, который использует удобочитаемый текст для хранения и передачи данных. JSON-файлы сохраняются с расширением .json. JSON требует меньше форматирования и является хорошей альтернативой XML. JSON происходит из JavaScript, но является независимым от языка форматом данных. Создание и разбор JSON поддерживается многими современными языками программирования. application/json – это тип медиа-формат, используемый для JSON.

Aspose.Cells поддерживает сохранение файлов в форматах JSON или XML.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Convert the workbook to json file.
workbook.save(path.join(dataDir, "book1.json"));
```


## **Продвинутые темы**
- [Настройка уровня сжатия книги Excel](/cells/ru/nodejs-cpp/adjust-workbook-compression-level/)
- [Сохранить книгу в формате Strict Open XML Spreadsheet](/cells/ru/nodejs-cpp/save-workbook-to-strict-open-xml-spreadsheet-format/)
- [Сохранение файла в объект ответа](/cells/ru/nodejs-cpp/saving-file-to-response-object/)
