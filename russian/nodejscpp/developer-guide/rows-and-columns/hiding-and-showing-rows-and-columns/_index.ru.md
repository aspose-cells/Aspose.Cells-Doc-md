---
title: Скрытие и отображение строк и столбцов с помощью Node.js через C++
linktitle: Скрытие и отображение строк и столбцов
type: docs
weight: 60
url: /ru/nodejs-cpp/hiding-and-showing-rows-and-columns/
description: Научитесь скрывать и показывать строки и столбцы в рабочем листе с помощью Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}}

Иногда имеет смысл скрывать определенные строки или столбцы на листе и показывать их позже. Эту возможность предоставляет Microsoft Excel, также как и Aspose.Cells.

{{% /alert %}}

## **Управление видимостью строк и столбцов**

Aspose.Cells for Node.js via C++ предоставляет класс [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) содержит [**WorksheetCollection**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection), позволяющий разработчикам получать доступ к каждому рабочему листу в файле Excel. Рабочий лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) предоставляет коллекцию [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells), которая содержит все ячейки рабочего листа. Коллекция [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) предоставляет несколько методов для управления строками или столбцами в рабочем листе. Некоторые из них рассматриваются ниже.

### **Скрытие строк и столбцов**

Разработчики могут скрывать строки или столбцы, вызвав методы [**hideRow(number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#hideRow-number-) и [**hideColumn(number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#hideColumn-number-) коллекции [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) соответственно. Оба метода требуют индекс строки или столбца, чтобы скрыть конкретный элемент.

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Reading the Excel file into a buffer
const fileBuffer = fs.readFileSync(filePath);

// Instantiating a Workbook object with Uint8Array
const workbook = new AsposeCells.Workbook(new Uint8Array(fileBuffer));

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Hiding the 3rd row of the worksheet
worksheet.getCells().hideRow(2);

// Hiding the 2nd column of the worksheet
worksheet.getCells().hideColumn(1);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.out.xls"));
```

{{% alert color="primary" %}}

Также можно скрыть строку или столбец, установив высоту строки или ширину столбца равным 0 соответственно.

{{% /alert %}}

### **Показ строк и столбцов**

Разработчики могут отображать любой скрытый ряд или столбец, вызвав методы [**unhideRow(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#unhideRow-number-number-) и [**unhideColumn(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#unhideColumn-number-number-) коллекции [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) соответственно. Оба метода требуют два параметра:

- **Индекс строки или столбца** - индекс строки или столбца, который используется для отображения конкретной строки или столбца.
- **Высота строки или ширина столбца** - высота строки или ширина столбца, назначенные строке или столбцу после отображения.

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");
// Read the Excel file into a Buffer (Uint8Array)
const fileBuffer = fs.readFileSync(filePath);

// Instantiating a Workbook object with file buffer
const workbook = new AsposeCells.Workbook(fileBuffer);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Unhiding the 3rd row and setting its height to 13.5
worksheet.getCells().unhideRow(2, 13.5);

// Unhiding the 2nd column and setting its width to 8.5
worksheet.getCells().unhideColumn(1, 8.5);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

{{% alert color="primary" %}}

При отображении скрытого столбца, если вам нужно восстановить его исходную или ранее установленную ширину, пожалуйста, сделайте это, развернув столбец с отрицательной шириной. Например: worksheet.cells.unhideColumn(5, -1)

{{% /alert %}}

### **Скрытие нескольких строк и столбцов**

Разработчики могут скрывать несколько строк или столбцов одновременно, вызвав методы [**hideRows(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#hideRows-number-number-) и [**hideColumns(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#hideColumns-number-number-) коллекции [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) соответственно. Оба метода требуют начальный индекс строки или столбца и количество скрываемых строк или столбцов в качестве параметров.

```javascript
const fs = require("fs");
const path = require("path");
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

// Hiding 3, 4, and 5 rows in the worksheet
worksheet.getCells().hideRows(2, 3);

// Hiding 2 and 3 columns in the worksheet
worksheet.getCells().hideColumns(1, 2);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "outputxls"));
```

{{% alert color="primary" %}}

Также возможно использовать методы [**unhideRows(number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#unhideRows-number-number-number-) и [**unhideColumns(number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#unhideColumns-number-number-number-) класса [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) для отображения нескольких строк и столбцов.

{{% /alert %}}
