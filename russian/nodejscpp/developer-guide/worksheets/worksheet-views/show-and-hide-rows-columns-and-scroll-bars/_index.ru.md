---  
title: Показать и скрывать строки, столбцы и полосы прокрутки с помощью Node.js через C++  
linktitle: Показать и скрыть строки, столбцы и полосы прокрутки  
type: docs  
weight: 20  
url: /ru/nodejs-cpp/show-and-hide-rows-columns-and-scroll-bars/  
description: В этой статье показано, как программно отображать и скрывать строки и столбцы листа Excel, используя Node.js через C++. Управляйте видимостью полос прокрутки и эффективно скрывайте несколько строк и столбцов.  
---  

{{% alert color="primary" %}}  
Aspose.Cells предоставляет способы управления видимостью строк, столбцов и полос прокрутки листа.  
{{% /alert %}}  

## **Показ и скрытие строк и столбцов**  

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), представляющий файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) содержит коллекцию [**getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--), позволяющую разработчикам получать доступ к каждому листу Excel. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) обеспечивает коллекцию [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--), которая отображает все ячейки листа. Коллекция [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) предоставляет несколько методов для управления строками или столбцами листа. Некоторые из них обсуждены ниже.  

### **Показать строки и столбцы**  

Разработчики могут отображать любой скрытый ряд или столбец, вызвав методы [**unhideRow(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#unhideRow-number-number-) и [**unhideColumn(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#unhideColumn-number-number-) коллекции [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) соответственно. Оба метода требуют два параметра:  

- **Индекс строки или столбца** - индекс строки или столбца, который используется для отображения конкретной строки или столбца.  
- **Высота строки или ширина столбца** - высота строки или ширина столбца, назначенные строке или столбцу после отображения.  

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Reading the Excel file into a buffer
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
При восстановлении скрытого столбца, если необходимо вернуть его к ранее назначенной ширине или к исходной ширине, пожалуйста, сделайте его неподсвеченным с отрицательной шириной. Например: worksheet.Cells.unhideColumn(5, -1)  
{{% /alert %}}  

### **Скрыть строки и столбцы**  

Разработчики могут скрывать строки или столбцы, вызвав методы [**hideRow(number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#hideRow-number-) и [**hideColumn(number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#hideColumn-number-) коллекции [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) соответственно. Оба метода требуют индекс строки или столбца, чтобы скрыть конкретный элемент.  

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

const fileBuffer = fs.readFileSync(filePath);

const workbook = new AsposeCells.Workbook(fileBuffer);

const worksheet = workbook.getWorksheets().get(0);

worksheet.getCells().hideRow(2);

worksheet.getCells().hideColumn(1);

workbook.save(path.join(dataDir, "output.out.xls"));
```  

{{% alert color="primary" %}}  
Также можно скрыть строку или столбец, установив высоту строки или ширину столбца равным 0 соответственно.  
{{% /alert %}}  

### **Скрыть несколько строк и столбцов**  

Разработчики могут скрывать несколько строк или столбцов одновременно, вызвав методы [**hideRows(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#hideRows-number-number-) и [**hideColumns(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#hideColumns-number-number-) коллекции [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) соответственно. Оба метода требуют начальный индекс строки или столбца и количество скрываемых строк или столбцов в качестве параметров.  

```javascript
const fs = require('fs');
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

// Hiding 3, 4 and 5 rows in the worksheet
worksheet.getCells().hideRows(2, 3);

// Hiding 2 and 3 columns in the worksheet
worksheet.getCells().hideColumns(1, 2);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "outputxls"));

// No explicit close needed for file stream as we're working with in-memory data
```  

## **Показывать и скрывать полосы прокрутки**  

Полосы прокрутки используются для навигации по содержимому любого файла. Обычно существует два типа полос прокрутки:  

- Вертикальные полосы прокрутки  
- Горизонтальные полосы прокрутки  

Microsoft Excel также предоставляет горизонтальные и вертикальные полосы прокрутки, чтобы пользователи могли пролистывать содержимое листа Excel. Используя Aspose.Cells, разработчики могут контролировать видимость обоих типов полос прокрутки в файлах Excel.  

### **Управление видимостью полос прокрутки**  

Aspose.Cells предоставляет класс, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), который представляет файл Excel. Класс [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) содержит широкий спектр свойств и методов для управления файлом Excel. Для управления видимостью полос прокрутки используйте свойства [**WorkbookSettings.isVScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isVScrollBarVisible--) и [**WorkbookSettings.isHScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isHScrollBarVisible--). [**WorkbookSettings.isVScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isVScrollBarVisible--) и [**WorkbookSettings.isHScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isHScrollBarVisible--) — логические свойства, означающие, что эти свойства могут хранить только значения **true** или **false**.  

#### **Отображение полос прокрутки**  

Делайте полосы прокрутки видимыми, устанавливая свойства [**WorkbookSettings.isVScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isVScrollBarVisible--) или [**WorkbookSettings.isHScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isHScrollBarVisible--) класса [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) в **true**.  

#### **Скрытие полос прокрутки**  

Скрыть полосы прокрутки, установив свойства [**WorkbookSettings.isVScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isVScrollBarVisible--) или [**WorkbookSettings.isHScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isHScrollBarVisible--) класса [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) в **false**.  

**Пример кода**  

Ниже приведен полный код, который открывает файл Excel, book1.xls, скрывает оба ползунка прокрутки, а затем сохраняет измененный файл как output.xls.  

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

// Hiding the vertical scroll bar of the Excel file
workbook.getSettings().setIsVScrollBarVisible(false);

// Hiding the horizontal scroll bar of the Excel file
workbook.getSettings().setIsHScrollBarVisible(false);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```  

