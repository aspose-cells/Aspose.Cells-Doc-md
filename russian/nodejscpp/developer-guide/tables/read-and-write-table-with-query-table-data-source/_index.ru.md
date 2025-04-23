---
title: Чтение и запись таблиц с источником данных QueryTable через Node.js
linktitle: Чтение и запись таблицы с источником данных таблицы запросов
type: docs
weight: 30
url: /ru/nodejs-cpp/read-and-write-table-with-query-table-data-source/
description: Узнайте, как читать и писать таблицу с источником данных QueryTable с помощью Aspose.Cells for Node.js via C++. 
---

## **Чтение и запись таблицы с источником данных из запроса к таблице**
С помощью Aspose.Cells for Node.js via C++ вы можете читать и записывать таблицу, которая имеет QueryTable в качестве источника данных. Поддержка этой функции также доступна для XLS-файлов. Следующий фрагмент кода демонстрирует чтение и запись такой таблицы путем сначала чтения таблицы, а затем ее изменения для добавления итоговой строки.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the source directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Load workbook object
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "SampleTableWithQueryTable.xls"));

const worksheet = workbook.getWorksheets().get(0);

const table = worksheet.getListObjects().get(0);

// Check the data source type if it is query table
if (table.getDataSourceType() === AsposeCells.TableDataSourceType.QueryTable) {
table.setShowTotals(true);
}

// Save the file
workbook.save(path.join(outputDir, "SampleTableWithQueryTable_out.xls"));
```

Исходный и выходной файлы Excel прикреплены для справки.

[Исходный файл](96928091.xls)

[Выходной файл](96928092.xls)
