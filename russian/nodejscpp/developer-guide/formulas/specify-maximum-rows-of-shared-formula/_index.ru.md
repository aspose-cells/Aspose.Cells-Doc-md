---  
title: Укажите максимальное количество строк для общей формулы с помощью Node.js через C++  
linktitle: Укажите максимальное количество строк общей формулы  
type: docs  
weight: 40  
url: /ru/nodejs-cpp/specify-maximum-rows-of-shared-formula/  
description: Узнайте, как указывать максимальное число строк для общих формул с помощью Aspose.Cells for Node.js via C++.  
---  

## **Возможные сценарии использования**  

Максимальное количество строк для общей формулы по умолчанию — 64. Оно может быть любым числом, например, 1000. Производительность общей формулы зависит от этого числа. Поэтому Aspose.Cells предоставляет свойство [**WorkbookSettings.getMaxRowsOfSharedFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getMaxRowsOfSharedFormula--), которое можно использовать для задания максимального количества строк. Общая формула будет разбита на несколько частей, если общее число строк превысит указанное значение, как показано на следующем скриншоте.  

![todo:image_alt_text](specify-maximum-rows-of-shared-formula_1.png)  

## **Укажите максимальное количество строк общей формулы**  

Следующий пример кода демонстрирует использование свойства [**WorkbookSettings.getMaxRowsOfSharedFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getMaxRowsOfSharedFormula--). Он устанавливает максимум в 5 строк для общей формулы и добавляет общую формулу в ячейку D1 для 100 строк, сохраняет файл и выводит его как [выходной Excel-файл](61767856.xlsx). Если раскрыть содержимое файла и проверить *sheet1.xml*, увидите, что разделение общей формулы происходит каждые 5 строк, что выделено на скриншоте выше.  

## **Образец кода**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Create a new workbook
const wb = new AsposeCells.Workbook();

// Set the max rows of shared formula to 5
wb.getSettings().setMaxRowsOfSharedFormula(5);

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Access cell D1
const cell = ws.getCells().get("D1");

// Set the shared formula in 100 rows
cell.setSharedFormula("=Sum(A1:A2)", 100, 1);

// Save the output Excel file
wb.save("outputSpecifyMaximumRowsOfSharedFormula.xlsx");
```  

