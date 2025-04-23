---  
title: Конвертация Excel в JSON с помощью Node.js через C++  
linktitle: Конвертировать Excel в JSON  
type: docs  
weight: 300  
url: /ru/nodejs-cpp/convert-excel-to-json/  
description: Узнайте, как конвертировать файл Excel в JSON с помощью Aspose.Cells for Node.js via C++.  
keywords: Экспорт рабочей книги в JSON с помощью Node.js через C++, преобразование Excel в JSON через Node.js с помощью C++  
---  

{{% alert color="primary" %}}  
Aspose.Cells поддерживает преобразование рабочей книги в файл JSON (JavaScript Object Notation).  
{{% /alert %}}  

## **Конвертировать книгу Excel в JSON**  

Нет необходимости гадать, как преобразовать рабочую книгу Excel в JSON, потому что библиотека Aspose.Cells for Node.js via C++ предлагает лучшее решение. API Aspose.Cells поддерживает преобразование таблиц в формат JSON. Чтобы экспортировать рабочую книгу в JSON, передайте [**SaveFormat.Json**](https://reference.aspose.com/cells/nodejs-cpp/saveformat/) как второй параметр метода [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-). Также можно использовать класс [**JsonSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/jsonsaveoptions/), чтобы задать дополнительные параметры для экспорта листа в JSON.  

Следующий пример кода демонстрирует экспорт рабочей книги Excel в JSON. Ознакомьтесь с кодом для преобразования [исходного файла](sample.xlsx) в JSON-файл, сгенерированный кодом, для справки.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Convert the workbook to json file.
workbook.save("sample_out.json");
```  

Следующий пример кода использует класс JsonSaveOptions для задания дополнительных настроек и демонстрирует экспорт рабочей книги Excel в JSON. Ознакомьтесь с кодом для преобразования [исходного файла](sample.xlsx) в JSON-файл, сгенерированный кодом, для справки.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create an options of saving the file.
const options = new AsposeCells.JsonSaveOptions();

// Set the exporting range.
options.setExportArea(AsposeCells.CellArea.createCellArea("B1", "C4"));

// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Convert the workbook to json file.
workbook.save("sample_out.json", options);
```  


