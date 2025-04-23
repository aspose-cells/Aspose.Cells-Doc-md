---
title: Вычисление функции IFNA с помощью Aspose.Cells for Node.js via C++
description: Как вычислить функции IFNA с использованием библиотеки Aspose.Cells для Node.js через C++. Загрузите существующий файл Excel или создайте новый и вычислите функцию IFNA для получения результата. В конце сохраните изменённый файл Excel на диск.
keywords: Aspose.Cells, Excel, функции IFNA, вычисления Node.js через C++
type: docs
weight: 40
url: /ru/nodejs-cpp/calculating-ifna-function-using-aspose-cells/
---

{{% alert color="primary" %}} 

Aspose.Cells поддерживает вычисление функции Excel IFNA. Функция IFNA возвращает значение, которое вы указываете, если формула возвращает ошибку #N/A; в противном случае она возвращает результат формулы.

{{% /alert %}} 
## **Вычисление функции IFNA с помощью Aspose.Cells for Node.js via C++**
Следующий пример иллюстрирует вычисление функции IFNA с помощью Aspose.Cells for Node.js via C++.


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Create new workbook
// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Add data for VLOOKUP
worksheet.getCells().get("A1").putValue("Apple");
worksheet.getCells().get("A2").putValue("Orange");
worksheet.getCells().get("A3").putValue("Banana");

// Access cell A5 and A6
const cellA5 = worksheet.getCells().get("A5");
const cellA6 = worksheet.getCells().get("A6");

// Assign IFNA formula to A5 and A6
cellA5.setFormula('=IFNA(VLOOKUP("Pear",$A$1:$A$3,1,0),"Not found")');
cellA6.setFormula('=IFNA(VLOOKUP("Orange",$A$1:$A$3,1,0),"Not found")');

// Calculate the formula of workbook
workbook.calculateFormula();

// Print the values of A5 and A6
console.log(cellA5.getStringValue());
console.log(cellA6.getStringValue());
```
## **Вывод в консоль**
Вот вывод в консоль вышеуказанного образца кода.

{{< highlight javascript >}}
 Not found

Orange
{{< /highlight >}}
