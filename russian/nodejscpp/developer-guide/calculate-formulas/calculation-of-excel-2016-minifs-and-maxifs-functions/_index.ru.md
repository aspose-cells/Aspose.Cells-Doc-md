---
title: Вырaщивание функций MINIFS и MAXIFS Excel 2016 с Node.js через C++
description: В этой статье описывается, как использовать библиотеку Aspose.Cells для вычисления функций MINIFS и MAXIFS в Microsoft Excel 2016 с помощью Node.js через C++. Загружаем существующий файл Excel или создаем новый, затем используем методы Aspose.Cells для вычисления этих функций и сохранения результатов на диск.
keywords: Aspose.Cells, Excel, 2016, функция MINIFS, функция MAXIFS, вычисление Node.js через C++
type: docs
weight: 300
url: /ru/nodejs-cpp/calculation-of-excel-2016-minifs-and-maxifs-functions/
---

## **Возможные сценарии использования**
Microsoft Excel 2016 поддерживает функции MINIFS и MAXIFS. Эти функции не поддерживаются в Excel 2013 или более ранних версиях. Aspose.Cells for Node.js via C++ также поддерживает вычисление этих функций. Следующий скриншот демонстрирует использование этих функций. Пожалуйста, прочтите красные комментарии внутри скриншота, чтобы понять, как работают эти функции.

![todo:image_alt_text](calculation-of-excel-2016-minifs-and-maxifs-functions_1.png)

## **Расчет функций MINIFS и MAXIFS Excel 2016**
 Следующий пример кода загружает [пример файла excel](5115149.xlsx) и вызывает метод [Workbook.calculateFormula()](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) для выполнения вычислений формулы через Aspose.Cells for Node.js via C++, затем сохраняет результаты в [выходной PDF](5115154.pdf).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceFilePath = path.join(dataDir, "sampleMINIFSAndMAXIFS.xlsx");

// Load your source workbook containing MINIFS and MAXIFS functions
const workbook = new AsposeCells.Workbook(sourceFilePath);

// Perform Aspose.Cells formula calculation
workbook.calculateFormula();

// Save the calculations result in pdf format
const options = new AsposeCells.PdfSaveOptions();
options.setOnePagePerSheet(true);
const outputFilePath = path.join(dataDir, "outputMINIFSAndMAXIFS.pdf");
workbook.save(outputFilePath, options);
```
