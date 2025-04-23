---  
title: Форматирование строк и столбцов с помощью Node.js через C++  
linktitle: Строки и столбцы  
type: docs  
weight: 100  
url: /ru/nodejs-cpp/adjusting-row-height-and-column-width/  
description: Aspose.Cells for Node.js via C++ может поддерживать изменение высоты строки или ширины столбца, а также применять форматирование к строкам или столбцам.  
keywords: Настройте высоту строки и ширину столбца, отрегулируйте высоту строки и ширину столбца, измените высоту строки или ширину столбца, форматируйте строки и столбцы, как установить высоту строки и ширину столбца.  
---  

{{% alert color="primary" %}}  
При работе с электронными таблицами и добавлении данных в строки или столбцы, возможно, потребуется изменить высоту строк или ширину столбцов. Иногда применение форматирования к строкам или столбцам означает, что текущая высота или ширина должны измениться для отображения данных. Обычно пользователи регулируют высоту строк и ширину столбцов в WYSIWYG-редакторе с помощью Microsoft Excel. Но с Aspose.Cells разработчики могут выполнять эти операции во время выполнения.  
{{% /alert %}}  

## **Работа со строками**  

### **Как настроить высоту строки**  

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) содержит [**WorksheetCollection**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection), позволяющий получать доступ к каждому листу в файле Excel. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) предоставляет коллекцию [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells), которая представляет все ячейки на листе.  

Коллекция [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) предоставляет несколько методов для управления строками или столбцами на листе. Некоторые из них рассмотрены далее более подробно.  

### **Как установить высоту строки**  

Можно установить высоту отдельной строки, вызвав метод [**setRowHeight(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#setRowHeight-number-number-) коллекции [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells). Метод [**setRowHeight(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#setRowHeight-number-number-) принимает следующие параметры:

- **Индекс строки**, индекс строки, высоту которой вы изменяете.  
- **Высота строки**, высота строки, применяемая к строке.

```javascript
try {
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");
// Creating a file stream containing the Excel file to be opened
const fstream = fs.createReadStream(filePath);

// Reading the file stream into a buffer
const chunks = [];
fstream.on('data', chunk => chunks.push(chunk));
fstream.on('end', () => {
const buffer = Buffer.concat(chunks);

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(buffer);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Setting the height of the second row to 13
worksheet.getCells().setRowHeight(1, 13);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.out.xls"));

// Closing the file stream to free all resources
fstream.close();
```  

### **Как установить высоту всех строк на листе**  

Если разработчики хотят установить одинаковую высоту для всех строк на листе, они могут сделать это, используя свойство [**getStandardHeight()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getStandardHeight--) коллекции [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells).  

**Пример:**  

```javascript
const fs = require("fs");
const path = require("path");
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

// Setting the height of all rows in the worksheet to 15
worksheet.getCells().setStandardHeight(15);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.out.xls"));

// Closing the file stream to free all resources
// (Note: Closing the file stream is unnecessary in this context as it's a 
// synchronous read performed using fs.readFileSync, which does not require
// explicit closure, but if using fs.createReadStream, you would handle it accordingly)
```  

## **Работа с колонками**  

### **Как установить ширину столбца**  

Установите ширину столбца, вызвав метод [**setColumnWidth(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#setColumnWidth-number-number-) коллекции [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells). Метод [**setColumnWidth(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#setColumnWidth-number-number-) принимает следующие параметры:  

- **Индекс колонки**, индекс колонки, ширину которой вы изменяете.  
- **Ширина колонки**, желаемая ширина колонки.  

```javascript
const fs = require("fs");
const path = require("path");
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

// Setting the width of the second column to 17.5
worksheet.getCells().setColumnWidth(1, 17.5);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.out.xls"));

// Closing the file stream to free all resources
fstream; // Note: No explicit close needed for fs.readFileSync
```  

### **Как установить ширину столбца в пикселях**  

Установите ширину столбца, вызвав метод [**setColumnWidthPixel(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#setColumnWidthPixel-number-number-) коллекции [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells). Метод [**setColumnWidthPixel(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#setColumnWidthPixel-number-number-) принимает следующие параметры:  

- **Индекс колонки**, индекс колонки, ширину которой вы изменяете.  
- **Ширина столбца**, желаемая ширина столбца в пикселях.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
const outDir = path.join(__dirname, "output");

// Load source Excel file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "Book1.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Set the width of the column in pixels
worksheet.getCells().setColumnWidthPixel(7, 200);

workbook.save(path.join(outDir, "SetColumnWidthInPixels_Out.xlsx"));
```  

### **Как установить ширину всех столбцов в листе Excel**  

Чтобы установить одинаковую ширину столбцов для всех столбцов на листе, используйте свойство [**getStandardWidth()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getStandardWidth--) коллекции [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells).  

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Creating a file stream containing the Excel file to be opened
const filePath = path.join(dataDir, "book1.xls");

// Instantiating a Workbook object
// Opening the Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Setting the width of all columns in the worksheet to 20.5
worksheet.getCells().setStandardWidth(20.5);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.out.xls"));

// Closing the file stream to free all resources
// No explicit close needed in Node.js
```  

## **Продвинутые темы**  
- [Автоподгонка строк и столбцов](/cells/ru/nodejs-cpp/autofit-rows-and-columns/)  
- [Преобразование текста в столбцы с использованием Aspose.Cells](/cells/ru/nodejs-cpp/convert-text-to-columns-using-aspose-cells/)  
- [Копирование строк и столбцов](/cells/ru/nodejs-cpp/copying-rows-and-columns/)  
- [Удаление пустых строк и столбцов в листе Excel](/cells/ru/nodejs-cpp/delete-blank-rows-and-columns-in-a-worksheet/)  
- [Группировка и разгруппировка строк и столбцов](/cells/ru/nodejs-cpp/grouping-and-ungrouping-rows-and-columns/)  
- [Скрытие и отображение строк и столбцов](/cells/ru/nodejs-cpp/hiding-and-showing-rows-and-columns/)  
- [Вставка или удаление строк в листе Excel](/cells/ru/nodejs-cpp/insert-or-delete-rows-in-an-excel-worksheet/)  
- [Вставка и удаление строк и столбцов в файле Excel](/cells/ru/nodejs-cpp/inserting-and-deleting-rows-and-columns/)  
- [Удалить дублирующиеся строки в рабочем листе](/cells/ru/nodejs-cpp/remove-duplicate-rows-in-a-worksheet/)  
- [Обновление ссылок в других листах при удалении пустых столбцов и строк на листе](/cells/ru/nodejs-cpp/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/)  

