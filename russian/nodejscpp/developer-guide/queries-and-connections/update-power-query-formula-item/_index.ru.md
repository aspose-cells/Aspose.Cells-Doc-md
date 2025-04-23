---
title: Обновление элемента формулы Power Query с помощью Node.js через C++
linktitle: Обновление элемента формулы Power Query
type: docs
weight: 120
url: /ru/nodejs-cpp/update-power-query-formula-item/
description: Узнайте, как обновить источник данных элемента формулы Power Query в файле Excel с помощью Aspose.Cells for Node.js via C++.
---

## **Сценарий использования**

Возможны случаи, когда файлы источника данных перемещаются, и файл Excel не может найти файл. В таких случаях API Aspose.Cells предоставляет возможность обновлять элемент формулы Power Query, используя класс [*PowerQueryFormulaItem*](https://reference.aspose.com/cells/nodejs-cpp/powerqueryformulaitem) для обновления пути к файлу источника.

## **Обновление элемента формулы Power Query**

API Aspose.Cells позволяет обновлять элементы формулы Power Query. Следующий пример кода демонстрирует обновление местоположения файла источника данных в файле Excel с помощью свойства [**PowerQueryFormulaItem.getValue()**](https://reference.aspose.com/cells/nodejs-cpp/powerqueryformulaitem/#getValue--). В файлы для примера приложены исходный и итоговый файлы.

- [Исходный файл 1](106364953.xlsx)
- [Исходный файл 2](106364954.xlsx)
- [Выходной файл](106364955.xlsx)

## **Образец кода**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Working directories
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

const workbook = new AsposeCells.Workbook(path.join(sourceDir, "SamplePowerQueryFormula.xlsx"));
const mashupData = workbook.getDataMashup();

const powerQueryFormulas = mashupData.getPowerQueryFormulas();
const count = powerQueryFormulas.getCount();
for (let i = 0; i < count; i++) 
{
const formula = powerQueryFormulas.get(i);
const items = formula.getPowerQueryFormulaItems();
const itemsCount = items.getCount();
for (let j = 0; j < itemsCount; j++) 
{
const item = items.get(j);
if (item.getName() === "Source") 
{
item.setValue(`Excel.Workbook(File.Contents("${path.join(sourceDir, "SamplePowerQueryFormulaSource.xlsx")}", null, true)`);
}
}
}

// Save the output workbook.
workbook.save(outputDir + "SamplePowerQueryFormula_out.xlsx");
```
