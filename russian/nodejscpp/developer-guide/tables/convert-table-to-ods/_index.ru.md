---  
title: Конвертировать таблицу в ODS с помощью Node.js и C++  
linktitle: Преобразование таблицы в формат ODS  
type: docs  
weight: 70  
url: /ru/nodejs-cpp/convert-table-to-ods/  
description: Узнайте, как конвертировать Excel файл с таблицей в формат ODS с помощью Aspose.Cells for Node.js via C++.  
---  

Aspose.Cells поддерживает преобразование файла Excel с таблицей в формат ODS. Просто сохраните файл в формате ODS, и сгенерированный файл ODS будет содержать работоспособную таблицу.

## Образец кода

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

// Open an existing file that contains a table/list object in it
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "SampleTable.xlsx"));

// Save the file
workbook.save(path.join(outputDir, "ConvertTableToOds_out.ods"));
```

Выходной файл ODS, сгенерированный образцовым кодом, прикреплен для вашего ознакомления.

[**Output ODS File**](ConvertTableToOds_out.ods)  

