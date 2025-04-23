---
title: Вставка и удаление строк и столбцов файлов Excel
linktitle: Вставка и удаление строк и столбцов
type: docs
weight: 70
url: /ru/nodejs-cpp/inserting-and-deleting-rows-and-columns/
description: В этой статье показано, как вставлять и удалять строки и столбцы с помощью API Aspose.Cells for Node.js via C++.
keywords: Aspose.Cells Node.js через C++ управляет строками и столбцами, вставляет и удаляет строки и столбцы
---

## **Введение**

При создании нового листа Excel с нуля или работе с существующим листом нам может потребоваться добавить дополнительные строки или столбцы для размещения большего объема данных. Напротив, также может потребоваться удалить строки или столбцы из указанных позиций в листе. 
Чтобы выполнить эти требования, Aspose.Cells for Node.js via C++ предоставляет очень простые классы и методы, рассмотренные ниже.

### **Управлять строками и столбцами**

Aspose.Cells for Node.js via C++ предоставляет класс [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) содержит коллекцию [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection), позволяющую получать доступ к каждому рабочему листу в файле Excel. Рабочий лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) предоставляет коллекцию [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--), которая содержит все ячейки рабочего листа.

Коллекция [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) предоставляет несколько методов для управления строками и столбцами в рабочем листе. Некоторые из них рассматриваются ниже.

{{% alert color="primary" %}}

При добавлении строк или столбцов содержимое листа смещается вниз или вправо, а при удалении — вверх или влево.

{{% /alert %}}


## **Вставить строки и столбцы**

### **Как вставить строку**

Вставьте строку на листе в любом месте, вызвав метод [**insertRow(number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRow-number-) коллекции [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--). Метод [**insertRow(number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRow-number-) принимает индекс строки, куда будет вставлена новая строка.

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Creating a file stream containing the Excel file to be opened
const fstream = fs.readFileSync(filePath);

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fstream);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Inserting a row into the worksheet at 3rd position
worksheet.getCells().insertRow(2);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.out.xls"));
```

### **Как вставить несколько строк**

Для вставки нескольких строк на лист, вызовите метод [**insertRows(number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRows-number-number-boolean-) коллекции [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--). Метод [**insertRows(number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRows-number-number-boolean-) принимает два параметра:

- Индекс строки, индекс строки, с которой будут вставлены новые строки.
- Количество строк, общее количество строк, которые необходимо вставить.

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

const fileData = fs.readFileSync(filePath);
const workbook = new AsposeCells.Workbook(fileData);

const worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().insertRows(2, 10);

workbook.save(path.join(dataDir, "output.out.xls"));
```

### **Как вставить строку с форматированием**

Чтобы вставить строку с параметрами форматирования, используйте перегрузку [**insertRows(number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRows-number-number-boolean-), которая принимает [**InsertOptions**](https://reference.aspose.com/cells/nodejs-cpp/insertoptions) в качестве параметра. Установите свойство [**CopyFormatType**](https://reference.aspose.com/cells/nodejs-cpp/copyformattype/) класса [**InsertOptions**](https://reference.aspose.com/cells/nodejs-cpp/insertoptions) с перечислением [**CopyFormatType**](https://reference.aspose.com/cells/nodejs-cpp/copyformattype/). Перечисление [**CopyFormatType**](https://reference.aspose.com/cells/nodejs-cpp/copyformattype/) имеет три элемента, перечисленные ниже.

- SameAsAbove: Форматирует строку так же, как и строка выше.
- SameAsBelow: Форматирует строку так же, как и строка ниже.
- Очистить: Очищает форматирование.

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Creating a file stream containing the Excel file to be opened
const filePath = path.join(dataDir, "book1.xls");
const fstream = fs.readFileSync(filePath);

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fstream);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Setting Formatting options
const insertOptions = new AsposeCells.InsertOptions();
insertOptions.setCopyFormatType(AsposeCells.CopyFormatType.SameAsAbove);

// Inserting a row into the worksheet at 3rd position
worksheet.getCells().insertRows(2, 1, insertOptions);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "InsertingARowWithFormatting.out.xls"));
```

### **Как вставить столбец**

Разработчики также могут вставлять столбец в лист на любой позиции, вызвав метод [**insertColumn(number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertColumn-number-boolean-) коллекции [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--). Метод [**insertColumn(number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertColumn-number-boolean-) принимает индекс столбца, куда будет вставлен новый столбец.

```javascript
const fs = require('fs');
const path = require('path');
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Creating a file stream containing the Excel file to be opened
const fileStream = fs.readFileSync(filePath);

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fileStream);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Inserting a column into the worksheet at 2nd position
worksheet.getCells().insertColumn(1);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.out.xls"));
```

## **Удалить строки и столбцы**

### **Как удалить несколько строк**

Чтобы удалить несколько строк из листа, вызовите метод [**deleteRows(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteRows-number-number-) коллекции [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--). Метод [**deleteRows(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteRows-number-number-) принимает два параметра:

- Индекс строки, индекс строки, с которой строки будут удалены.
- Количество строк, общее количество строк, которые нужно удалить.

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Read file contents as Uint8Array
const fileContent = fs.readFileSync(filePath);
const fileBuffer = new Uint8Array(fileContent);

// Instantiating a Workbook object with file buffer
const workbook = new AsposeCells.Workbook(fileBuffer);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Deleting 10 rows from the worksheet starting from 3rd row
worksheet.getCells().deleteRows(2, 10);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xlsx"));
```


### **Как удалить столбец**

Чтобы удалить столбец из листа в любом месте, вызовите метод [**deleteColumn(number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteColumn-number-boolean-) коллекции [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--). Метод [**deleteColumn(number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteColumn-number-boolean-) принимает индекс удаляемого столбца.

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Creating a file stream containing the Excel file to be opened
const filePath = path.join(dataDir, "Book1.xlsx");

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fs.readFileSync(filePath));

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Deleting a column from the worksheet at 5th position
worksheet.getCells().deleteColumn(4);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xlsx"));

// Closing resources is handled automatically by Node.js, no specific close needed.
```
