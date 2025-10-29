---  
title: Создание объединенного диапазона с помощью Node.js через C++  
linktitle: Создать объединенный диапазон  
type: docs  
weight: 360  
url: /ru/nodejs-cpp/create-union-range/  
description: Узнайте, как создать объединенный диапазон с помощью Aspose.Cells for Node.js via C++.  
keywords: Создайте объединенный диапазон Node.js через C++, Объединенный диапазон Aspose.Cells Node.js, Создание объединенного диапазона WorksheetCollection Node.js  
---  

## **Создать объединенный диапазон**  
Aspose.Cells позволяет создавать объединенный диапазон с помощью метода [WorksheetCollection.createUnionRange](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#createUnionRange-string-number-). Метод [WorksheetCollection.createUnionRange](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#createUnionRange-string-number-) принимает два параметра: адрес для создания объединенного диапазона и индекс листа. Метод возвращает объект [UnionRange](https://reference.aspose.com/cells/nodejs-cpp/unionrange).  

Следующий пример кода демонстрирует создание объединенного диапазона, используя метод [WorksheetCollection.createUnionRange](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#createUnionRange-string-number-). Генерируемый этим кодом файл прилагается для справки.  

- [Выходной файл](106364952.xlsx)  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Create union range
const unionRange = workbook.getWorksheets().createUnionRange("sheet1!A1:A10,sheet1!C1:C10", 0);

// Put value "ABCD" in the range
unionRange.setValue("ABCD");

// Save the output workbook.
workbook.save("CreateUnionRange_out.xlsx");
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
