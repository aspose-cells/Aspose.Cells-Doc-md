---  
title: Управление листами Excel файлов Microsoft с помощью Node.js через C++  
linktitle: Рабочие листы  
type: docs  
weight: 90  
url: /ru/nodejs-cpp/manage-worksheets/  
description: Добавляйте, удаляйте и активируйте листы с помощью Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
Разработчики могут легко создавать и управлять листами в файлах Microsoft Excel программно, используя гибкий API Aspose.Cells. В этой теме описываются подходы к добавлению и удалению листов в файлах Microsoft Excel.  
{{% /alert %}}  

Aspose.Cells предоставляет класс, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), который представляет файл Excel. Класс [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) содержит коллекцию [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--), позволяющую получить доступ к каждому листу в файле Excel.  

Лист представляет класс [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) предоставляет широкий спектр свойств и методов для управления листами.  

## **Добавление рабочих листов в новый файл Excel**  

Для создания нового файла Excel программно:  

1. Создайте объект класса [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook).  
1. Вызовите метод [**WorksheetCollection.add(SheetType)**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#add-sheettype-) класса [**WorksheetCollection**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection). В файл Excel автоматически добавляется пустой лист. Его можно получить, передав индекс листа в коллекцию [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--).  
3. Получите ссылку на рабочий лист.  
1. Выполнение работы с рабочими листами.  
1. Сохраните новый файл Excel с новыми листами, вызвав метод [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-) класса [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook).  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Workbook object
const i = workbook.getWorksheets().getCount();
workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(i);

// Setting the name of the newly added worksheet
worksheet.setName("My Worksheet");

// Saving the Excel file
workbook.save(path.join(dataDir, "output.out.xls"));
```  

## **Добавление листов в дизайнерскую электронную таблицу**  

Процесс добавления листов в дизайн-таблицу совпадает с добавлением нового листа, за исключением того, что файл Excel уже существует и должен быть открыт перед добавлением листов. Дизайн-таблицу можно открыть с помощью класса [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook).  

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "book1.xlsx");

// Creating a file stream containing the Excel file to be opened
const fstream = fs.readFileSync(inputPath);

// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fstream);

// Adding a new worksheet to the Workbook object
const i = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(i);

// Setting the name of the newly added worksheet
worksheet.setName("My Worksheet");

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xlsx"));
```  

## **Доступ к листам с использованием имени листа**  

Получите доступ к любому листу, указав его имя или индекс.  

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "book1.xlsx");

// Creating a file stream containing the Excel file to be opened
const fstream = fs.readFileSync(inputPath);

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fstream);

// Accessing a worksheet using its sheet name
const worksheet = workbook.getWorksheets().get("Sheet1");
const cell = worksheet.getCells().get("A1");
console.log(cell.getValue());
```  

## **Удаление листов с использованием имени листа**  

Чтобы удалить листы из файла, вызовите метод [**WorksheetCollection.removeAt(string)**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#removeAt-string-) класса [**WorksheetCollection**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection). Передайте имя листа в метод [**WorksheetCollection.removeAt(string)**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#removeAt-string-), чтобы удалить конкретный лист.  

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

// Removing a worksheet using its sheet name
workbook.getWorksheets().removeAt("Sheet1");

// Save workbook
workbook.save(path.join(dataDir, "output.out.xls"));
```  

## **Удаление рабочих листов с использованием индекса листа.**  

Удаление листов по имени хорошо работает, когда известно имя листа. Если имя листа неизвестно, используйте перегруженную версию метода [**WorksheetCollection.removeAt(string)**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#removeAt-string-), которая принимает индекс листа вместо его имени.  

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

// Removing a worksheet using its sheet index
workbook.getWorksheets().removeAt(0);

// Save workbook
workbook.save(path.join(dataDir, "output.out.xls"));
```  

## **Активация листов и установка активной ячейки на листе**  

Иногда необходимо, чтобы определенный лист был активен и отображался при открытии файла Microsoft Excel. Аналогично, можно активировать конкретную ячейку и настроить прокрутки для отображения активной ячейки. Aspose.Cells способен выполнять все эти задачи.  

Активный лист - это лист, над которым вы работаете: имя активного листа на вкладке жирным шрифтом по умолчанию.  

Активная ячейка - это выбранная ячейка, в которую вводятся данные при начале набора текста. Одновременно может быть активна только одна ячейка. Активная ячейка выделяется толстой границей.  

### **Активация листов и установка активной ячейки**  

Aspose.Cells предоставляет конкретные вызовы API для активации листа и ячейки. Например, свойство [**WorksheetCollection.getActiveSheetIndex()**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#getActiveSheetIndex--) полезно для установки активного листа в книге. Аналогично, свойство [**Worksheet.getActiveCell()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getActiveCell--) используется для установки и получения активной ячейки в листе.  

Чтобы убедиться, что горизонтальные или вертикальные полосы прокрутки находятся в нужной позиции по индексам строк и столбцов для отображения определенных данных, используйте свойства [**Worksheet.getFirstVisibleRow()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getFirstVisibleRow--) и [**Worksheet.getFirstVisibleColumn()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getFirstVisibleColumn--).  

В следующем примере показано, как активировать лист и сделать активной ячейку. В сгенерированном выводе полосы прокрутки будут прокручены, чтобы сделать 2-ю строку и 2-й столбец первой видимой строкой и столбцом.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook();

// Add a worksheet if collection is empty
const worksheets = workbook.getWorksheets();
if (worksheets.getCount() === 0) {
worksheets.add();
}

// Get the first worksheet in the workbook.
const worksheet1 = worksheets.get(0);

// Get the cells in the worksheet.
const cells = worksheet1.getCells();

// Input data into B2 cell.
cells.get(1, 1).putValue("Hello World!");

// Set the first sheet as an active sheet.
workbook.getWorksheets().setActiveSheetIndex(0);

// Set B2 cell as an active cell in the worksheet.
worksheet1.setActiveCell("B2");

// Set the B column as the first visible column in the worksheet.
worksheet1.setFirstVisibleColumn(1);

// Set the 2nd row as the first visible row in the worksheet.
worksheet1.setFirstVisibleRow(1);

// Save the excel file.
workbook.save(path.join(dataDir, "output.xls"));
```  

## **Продвинутые темы**  
- [Копирование и перемещение листов](/cells/ru/nodejs-cpp/copying-and-moving-worksheets/)  
- [Посчитать количество ячеек в листе](/cells/ru/nodejs-cpp/count-number-of-cells-in-the-worksheet/)  
- [Обнаружение пустых листов](/cells/ru/nodejs-cpp/detecting-empty-worksheets/)  
- [Определить, является ли рабочий лист диалоговым листом](/cells/ru/nodejs-cpp/find-if-the-worksheet-is-dialog-sheet/)  
- [Получить уникальный идентификатор листа](/cells/ru/nodejs-cpp/get-worksheet-unique-id/)  
- [Создание, изменение или удаление сценариев из листов](/cells/ru/nodejs-cpp/create-manipulate-or-remove-scenarios-from-worksheets/)  
- [Управление разрывами страницы](/cells/ru/nodejs-cpp/managing-page-breaks/)  
- [Возможности настройки страницы](/cells/ru/nodejs-cpp/page-setup-features/)   
- [Использование свойства Sheet.SheetId из OpenXml с помощью Aspose.Cells](/cells/ru/nodejs-cpp/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/)  
- [Просмотр листов](/cells/ru/nodejs-cpp/worksheet-views/)  


{{< app/cells/assistant language="nodejs-cpp" >}}
