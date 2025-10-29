---
title: Чтение таблиц Numbers, разработанных Apple Inc., с помощью Aspose.Cells for Node.js via C++
linktitle: Чтение Numbers Spreadsheet разработанный Apple Inc. с использованием Aspose.Cells
type: docs
weight: 140
url: /ru/nodejs-cpp/read-numbers-spreadsheet-developed-by-apple-inc-using-aspose-cells/
description: Узнайте, как читать таблицы Numbers, созданные Apple Inc., с помощью Aspose.Cells for Node.js via C++. 
---

## **Возможные сценарии использования**

Numbers — это приложение для работы с таблицами, разработанное Apple Inc. Aspose.Cells может читать таблицы Numbers, но не поддерживает запись в них. Оно может читать данные, стили и формулы таблиц Numbers.

## **Чтение таблиц Numbers, разработанных Apple Inc., с помощью Aspose.Cells for Node.js via C++**

Следующий пример кода загружает [Пример таблицы Numbers](sampleNumbersByAppleInc.numbers) и конвертирует его в [Выходной PDF формат](outputNumbersByAppleInc.pdf). Для успешной загрузки необходимо использовать класс [**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions) и указать [**LoadFormat.Numbers**](https://reference.aspose.com/cells/nodejs-cpp/loadformat) в качестве параметра в его конструкторе. Скачать оба файла можно по предоставленным ссылкам. Можно попробовать код с любой таблицей Numbers. Также рекомендуется ознакомиться с комментариями к коду для получения дополнительной информации.

## **Образец кода**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceFilePath = path.join(dataDir, "sampleNumbersByAppleInc.numbers");
const outputFilePath = path.join(dataDir, "outputNumbersByAppleInc.pdf");

// Specify load options, we want to load Numbers spreadsheet
const opts = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Numbers);

// Load the Numbers spreadsheet in workbook with above load options
const wb = new AsposeCells.Workbook(sourceFilePath, opts);

// Save the workbook to pdf format
wb.save(outputFilePath, AsposeCells.SaveFormat.Pdf);
```

{{< app/cells/assistant language="nodejs-cpp" >}}
