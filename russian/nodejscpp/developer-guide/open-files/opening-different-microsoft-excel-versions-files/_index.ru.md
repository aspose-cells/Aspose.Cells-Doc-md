---
title: Открывать файлы Microsoft Excel разных версий с помощью Node.js через C++
linktitle: Открыть файлы разных версий Microsoft Excel
type: docs
weight: 20
url: /ru/nodejs-cpp/opening-different-microsoft-excel-versions-files/
description: В этой статье объясняется, как открывать файлы Excel разных версий с помощью Aspose.Cells for Node.js via C++.
keywords: Открытие различных файлов Microsoft Excel с помощью Node.js через C++ как открыть зашифрованные файлы Excel в Node.js через C++
---

{{% alert color="primary" %}}

Aspose.Cells может открывать файлы разных версий Microsoft Excel, такие как Microsoft Excel 95/97 - 2003, SpreadsheetML, открытие файлов Microsoft Excel 2007/2010/2013/2016/2019 и Office 365 XLSX или зашифрованных файлов Excel.

{{% /alert %}}

## **Как открыть файлы разных версий Microsoft Excel**

Приложение часто должно уметь открывать файлы Microsoft Excel, созданные в разных версиях, например, Microsoft Excel 95, 97 или Microsoft Excel 2007/2010/2013/2016/2019 и Office 365. Возможно, вам нужно загрузить файл в любом из нескольких форматов, включая XLS, XLSX, XLSM, XLSB, SpreadsheetML, TabDelimited или TSV, CSV, ODS и другие. Используйте конструктор или укажите атрибут [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) класса с типом [**getFileFormat()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getFileFormat--), который определяет формат с помощью перечисления [**FileFormatType**](https://reference.aspose.com/cells/nodejs-cpp/fileformattype).

Перечисление [**FileFormatType**](https://reference.aspose.com/cells/nodejs-cpp/fileformattype) содержит множество предопределенных форматов файлов, некоторые из которых приведены ниже.

|**Типы форматов файлов**|**Описание**|
| :- | :- |
|Csv|Представляет файл CSV|
|Excel97To2003|Представляет файл Excel 97 - 2003|
|Xlsx|Представляет файл Excel 2007/2010/2013/2016/2019 и Office 365 XLSX|
|Xlsm|Представляет файл Excel 2007/2010/2013/2016/2019 и Office 365 XLSM|
|Xltx|Представляет файл шаблон Excel 2007/2010/2013/2016/2019 и Office 365 XLTX|
|Xltm|Представляет макрос-возможный файл Excel 2007/2010/2013/2016/2019 и Office 365 XLTM|
|Xlsb|Представляет бинарный файл Excel 2007/2010/2013/2016/2019 и Office 365 XLSB|
|SpreadsheetML|Представляет файл SpreadsheetML|
|Tsv|Представляет файл со значениями, разделенными знаком табуляции|
|TabDelimited|Представляет файл текста с табуляцией|
|Ods|Представляет файл ODS|
|Html|Представляет файл HTML|
|Mhtml|Представляет файл MHTML|

### **Открыть файлы Microsoft Excel 95/5.0**

Чтобы открыть файл Microsoft Excel 95/5.0, используйте [**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions) и установите соответствующий атрибут для класса [**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions) для загружаемого файла шаблона. Пример файла для тестирования этой функции можно скачать по следующей ссылке:

[Файл Excel95](Excel95.xls)

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Excel95_5.0.xls");

// Get the Excel file into stream
const stream = fs.readFileSync(filePath);

// Instantiate LoadOptions specified by the LoadFormat.
const loadOptions1 = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Auto);

// Create a Workbook object and opening the file from the stream
const wbExcel95 = new AsposeCells.Workbook(stream, loadOptions1);
console.log("Microsoft Excel 95/5.0 workbook opened successfully!");
```

### **Открыть файлы Microsoft Excel 97 - 2003**

Чтобы открыть файл Microsoft Excel 97 - 2003, используйте [**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions) и установите соответствующий атрибут для класса [**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions) для загружаемого файла шаблона.

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book_Excel97_2003.xls");
// Get the Excel file into stream
const stream = fs.readFileSync(filePath);

// Instantiate LoadOptions specified by the LoadFormat.
const loadOptions1 = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Excel97To2003);

// Create a Workbook object and opening the file from the stream
const wbExcel97 = new AsposeCells.Workbook(stream, loadOptions1);
console.log("Microsoft Excel 97 - 2003 workbook opened successfully!");
```

### **Открыть файлы Microsoft Excel 2007/2010/2013/2016/2019 и Office 365 XLSX**

Для открытия файла в форматах Microsoft Excel 2007/2010/2013/2016/2019 и Office 365, то есть XLSX или XLSB, укажите путь к файлу. Также можно использовать [**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions) и установить соответствующие атрибуты/опции класса [**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions) для загружаемого шаблона файла.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Opening Microsoft Excel 2007 Xlsx Files
// Instantiate LoadOptions specified by the LoadFormat.
const loadOptions = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx);

// Create a Workbook object and opening the file from its path
const workbook = new AsposeCells.Workbook(path.join(dataDir, "Book_Excel2007.xlsx"), loadOptions);
console.log("Microsoft Excel 2007 - Office365 workbook opened successfully!");
```

### **Открыть зашифрованные файлы Excel**

Возможна создание зашифрованных файлов Excel с помощью Microsoft Excel. Для открытия зашифрованного файла используйте [**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions) и укажите его атрибуты и опции (например, задайте пароль) для загружаемого файла шаблона.
Образец файла для тестирования этой функции может быть загружен по следующей ссылке:

[Encrypted Excel](EncryptedExcel.xlsx)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "encryptedBook.xls");

// Instantiate LoadOptions
const loadOptions = new AsposeCells.LoadOptions();

// Specify the password
loadOptions.setPassword("1234");

// Create a Workbook object and opening the file from its path
const wbEncrypted = new AsposeCells.Workbook(filePath, loadOptions);
console.log("Encrypted excel file opened successfully!");
```

Aspose.Cells также поддерживает открытие защищенных паролем файлов Microsoft Excel 2007, 2010, 2013, 2016, 2019, Office 365.


{{< app/cells/assistant language="nodejs-cpp" >}}
