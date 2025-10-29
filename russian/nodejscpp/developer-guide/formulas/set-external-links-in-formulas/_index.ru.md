---
title: Установка внешних связей в формулах с помощью Node.js через C++
linktitle: Установка внешних ссылок в формулах
type: docs
weight: 20
url: /ru/nodejs-cpp/set-external-links-in-formulas/
description: Узнайте, как установить внешние связи в формулах с помощью Aspose.Cells for Node.js via C++. 
keywords: Установка внешних связей в формулах Node.js через C++, включение внешних файлов в формулы Node.js через C++ 
---

{{% alert color="primary" %}} 

Иногда необходимо включать ссылки на внешние файлы в формулы, например, для оценки значения ячейки или диапазона относительно них. Aspose.Cells for Node.js via C++ предоставляет эту возможность, и этот документ объясняет, как ее использовать.

{{% /alert %}} 

Ниже приведен пример кода, показывающий, как включить внешние файлы в формулы.



```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook();

// Get first Worksheet
const sheet = workbook.getWorksheets().get(0);

// Get Cells collection
const cells = sheet.getCells();

// Set formula with external links
cells.get("A1").setFormula(`=SUM('[${filePath}]Sheet1'!A2, '[${filePath}]Sheet1'!A4)`);

// Set formula with external links
cells.get("A2").setFormula(`='[${filePath}]Sheet1'!A8`);

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
