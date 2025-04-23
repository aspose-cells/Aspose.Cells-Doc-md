---  
title: Добавление или удаление строк в рабочем листе Excel с помощью Node.js через C++  
linktitle: Вставка или удаление строк в рабочем листе Excel  
type: docs  
weight: 20  
url: /ru/nodejs-cpp/insert-or-delete-rows-in-an-excel-worksheet/  
description: Этот статья предоставляет код Node.js с использованием C++, чтобы вставлять и удалять строки в рабочем листе Excel.  
keywords: node.js вставка или удаление строк в Excel, node.js вставка или удаление строк в Excel, node.js вставка строк в Excel, node.js удаление строк в Excel, вставка или удаление строк в рабочем листе Excel с помощью node.js, вставка или удаление строк в Excel с помощью node.js, вставка строк в Excel с помощью node.js, удаление строк в Excel с помощью node.js  
---  

{{% alert color="primary" %}}  

Когда создаёте новый рабочий лист или работаете с существующим, вам может понадобиться добавить дополнительные строки или столбцы для размещения данных. В других случаях, необходимо удалить строки или столбцы из указанных позиций в рабочем листе.  

{{% /alert %}}  

Aspose.Cells for Node.js via C++ предоставляет два метода для вставки и удаления строк: [**Cells.insertRows(number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRows-number-number-boolean-) и [**Cells.deleteRows(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteRows-number-number-). Эти методы оптимизированы по производительности и выполняют работу очень быстро.  

Для вставки или удаления определённого количества строк рекомендуется всегда использовать методы [**Cells.insertRows(number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRows-number-number-boolean-) и [**Cells.deleteRows(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteRows-number-number-), а не в цикле методы [**Cells.insertRow(number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRow-number-) или [**Cells.deleteRow(number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteRow-number-).  

Aspose.Cells работает так же, как и Microsoft Excel. При добавлении строк или столбцов содержимое рабочего листа сдвигается вниз и вправо. При удалении строк или столбцов содержимое рабочего листа сдвигается вверх или влево. Ссылки в других рабочих листах и ячейках обновляются при добавлении или удалении строк.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate a Workbook object.
// Load a template file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1.xlsx"));

// Get the first worksheet in the book.
const sheet = workbook.getWorksheets().get(0);

// Insert 10 rows at row index 2 (insertion starts at 3rd row)
sheet.getCells().insertRows(2, 10);

// Delete 5 rows now. (8th row - 12th row)
sheet.getCells().deleteRows(7, 5);

// Save the excel file.
workbook.save(path.join(dataDir, "out_book1.out.xlsx"));
```  

