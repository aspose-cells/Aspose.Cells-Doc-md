---  
title: Создать и скопировать именованные диапазоны с помощью Node.js и C++  
linktitle: Создание доступа и копирование именованных диапазонов  
type: docs  
weight: 200  
url: /ru/nodejs-cpp/create-access-and-copy-named-ranges/  
description: Узнайте, как создавать, получать доступ и копировать именованные диапазоны в Excel с помощью Aspose.Cells for Node.js via C++.  
---  

## **Введение**  

Обычно метки столбцов и строк используются для ссылки на отдельные ячейки. Можно создавать описательные имена для представления ячеек, диапазонов ячеек, формул или постоянных значений. слово **имя** может относиться к строке символов, которая представляет ячейку, диапазон ячеек, формулу или постоянное значение. Назначение имени диапазону означает, что этот диапазон ячеек можно ссылаться по имени. Используйте легкие для понимания имена, такие как Products, чтобы обозначать сложные диапазоны, такие как Sales!C20:C30. Метки можно использовать в формулах, ссылающихся на данные на той же рабочей странице; если хотите представить диапазон на другой странице, можно использовать имя. *Именованные диапазоны — одна из самых мощных функций Microsoft Excel, особенно при использовании в качестве исходных диапазонов для списков, сводных таблиц, графиков и т. д.*  

## **Работа с именованным диапазоном с помощью Microsoft Excel**  

### **Создание именованных диапазонов**  

Следующие шаги описывают, как назвать ячейку или диапазон ячеек с помощью **MS Excel**. Этот метод применяется к **Microsoft Office Excel 2003**, **Microsoft Excel 97**, **2000** и **2002**.  

1. Выберите ячейку или диапазон ячеек, которые хотите назвать.  
2. Нажмите **Пакетное имя** слева на строке формул.  
3. Введите название для ячеек.  
4. Нажмите ENTER.  

{{% alert color="primary" %}}  
Вы не можете называть ячейку, когда вы изменяете содержимое ячейки.  
{{% /alert %}}  

## **Работа с именованным диапазоном с использованием Aspose.Cells**  

Здесь мы используем API Aspose.Cells для выполнения этой задачи.  
Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) содержит коллекцию [**getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--), которая позволяет получить доступ к каждому листу в файле Excel. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) предоставляет коллекцию [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells).  

### **Создание именованного диапазона**  

Можно создать именованный диапазон, вызвав перегруженный метод [**createRange(string, string)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#createRange-string-string-) коллекции [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells). Типичная версия метода [**createRange(string)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#createRange-string-) принимает следующие параметры:  

- Имя верхней левой ячейки, имя верхней левой ячейки в диапазоне.  
- Имя нижней правой ячейки, имя нижней правой ячейки в диапазоне.  

Когда вызывается метод [**createRange(string)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#createRange-string-), он возвращает только что созданный диапазон в виде экземпляра класса [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range). Используйте этот объект [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range), чтобы настроить именованный диапазон. Например, установите имя диапазона, используя свойство [**getName()**](https://reference.aspose.com/cells/nodejs-cpp/range/#getName--). В следующем примере показано, как создать именованный диапазон ячеек, который простирается от B4:G14.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1.xls"));

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Creating a named range
const range = worksheet.getCells().createRange("B4", "G14");

// Setting the name of the named range
range.setName("TestRange");

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.out.xls"));
```  

### **Ввод данных в ячейки именованного диапазона**  

Можно вставить данные в отдельные ячейки диапазона, следуя образцу  

- **JavaScript**: Диапазон[строка, столбец]  

Предположим, у вас есть именованный диапазон ячеек, который охватывает A1:C4. Матрица состоит из 4 * 3 = 12 ячеек. Отдельные ячейки диапазона упорядочены последовательно: Диапазон[0,0], Диапазон[0,1], Диапазон[0,2], Диапазон[1,0], Диапазон[1,1], Диапазон[1,2], Диапазон[2,0], Диапазон[2,1], Диапазон[2,2], Диапазон[3,0], Диапазон[3,1], Диапазон[3,2].  

Используйте следующие свойства для определения ячеек в диапазоне:  

- firstRow возвращает индекс первой строки в именованном диапазоне.  
- firstColumn возвращает индекс первого столбца в именованном диапазоне.  
- rowCount возвращает общее количество строк в именованном диапазоне.  
- columnCount возвращает общее количество столбцов в именованном диапазоне.  

В следующем примере показано, как ввести некоторые значения в ячейки указанного диапазона.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook();

// Get the first worksheet in the workbook.
const worksheet1 = workbook.getWorksheets().get(0);

// Create a range of cells based on H1:J4.
const range = worksheet1.getCells().createRange("H1", "J4");

// Name the range.
range.setName("MyRange");

// Input some data into cells in the range.
range.get(0, 0).setValue("USA");
range.get(0, 1).setValue("SA");
range.get(0, 2).setValue("Israel");
range.get(1, 0).setValue("UK");
range.get(1, 1).setValue("AUS");
range.get(1, 2).setValue("Canada");
range.get(2, 0).setValue("France");
range.get(2, 1).setValue("India");
range.get(2, 2).setValue("Egypt");
range.get(3, 0).setValue("China");
range.get(3, 1).setValue("Philipine");
range.get(3, 2).setValue("Brazil");

// Save the excel file.
workbook.save(path.join(dataDir, "rangecells.out.xls"));
```  

### **Определение ячеек в именованном диапазоне**  

Вы можете вставить данные в отдельные ячейки диапазона, следуя шаблону:  

- **JavaScript**: Диапазон[строка, столбец]  

Если у вас есть именованный диапазон, который охватывает A1:C4. Матрица делает 4 * 3 = 12 ячеек. Отдельные ячейки диапазона упорядочены последовательно: Диапазон[0,0], Диапазон[0,1], Диапазон[0,2], Диапазон[1,0], Диапазон[1,1], Диапазон[1,2], Диапазон[2,0], Диапазон[2,1], Диапазон[2,2], Диапазон[3,0], Диапазон[3,1], Диапазон[3,2].  

Используйте следующие свойства для определения ячеек в диапазоне:  

- firstRow возвращает индекс первой строки в именованном диапазоне.  
- firstColumn возвращает индекс первого столбца в именованном диапазоне.  
- rowCount возвращает общее количество строк в именованном диапазоне.  
- columnCount возвращает общее количество столбцов в именованном диапазоне.  

В следующем примере показано, как ввести некоторые значения в ячейки указанного диапазона.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1_testrange.xls"));

// Getting the specified named range
const range = workbook.getWorksheets().getRangeByName("TestRange");

// Identify range cells.
console.log("First Row : " + range.getFirstRow());
console.log("First Column : " + range.getFirstColumn());
console.log("Row Count : " + range.getRowCount());
console.log("Column Count : " + range.getColumnCount());
```  

### **Доступ к именованным диапазонам**  

#### **Доступ к конкретному именованному диапазону**  

Вызовите метод [**getRangeByName(string)**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#getRangeByName-string-) коллекции [**worksheets**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection), чтобы получить диапазон по указанному имени. Типичный метод [**getRangeByName(string)**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#getRangeByName-string-) принимает имя именованного диапазона и возвращает указанный именованный диапазон как экземпляр класса [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range). В следующем примере показано, как получить доступ к указанному диапазону по его имени.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1_testrange.xls"));

// Getting the specified named range
const range = workbook.getWorksheets().getRangeByName("TestRange");

if (range !== null) 
{
console.log("Named Range : " + range.getRefersTo());
}
```  

#### **Доступ ко всем именованным диапазонам в электронной таблице**  

Вызовите метод [**getNamedRanges()**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#getNamedRanges--) коллекции [**worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection), чтобы получить все именованные диапазоны в электронной таблице. Метод [**getNamedRanges()**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#getNamedRanges--) возвращает массив всех именованных диапазонов в коллекции [**worksheets**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection).  

В следующем примере показано, как получить доступ ко всем именованным диапазонам в книге.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1.xls"));

// Getting all named ranges
const ranges = workbook.getWorksheets().getNamedRanges();

if (ranges != null) {
console.log("Total Number of Named Ranges: " + ranges.length);
}
```  

### **Копировать именованные диапазоны**  

Aspose.Cells предоставляет метод [**range.copy(Range, PasteOptions)**](https://reference.aspose.com/cells/nodejs-cpp/range/#copy-range-pasteoptions-) для копирования диапазона ячеек с форматированием в другой диапазон.  

В следующем примере показано, как скопировать исходный диапазон ячеек в другой именованный диапазон.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook();

// Get all the worksheets in the book.
const worksheets = workbook.getWorksheets();

// Get the first worksheet in the worksheets collection.
const worksheet = workbook.getWorksheets().get(0);

// Create a range of cells.
const range1 = worksheet.getCells().createRange("E12", "I12");

// Name the range.
range1.setName("MyRange");

// Set the outline border to the range.
range1.setOutlineBorder(AsposeCells.BorderType.TopBorder, AsposeCells.CellBorderType.Medium, new AsposeCells.Color(0, 0, 128));
range1.setOutlineBorder(AsposeCells.BorderType.BottomBorder, AsposeCells.CellBorderType.Medium, new AsposeCells.Color(0, 0, 128));
range1.setOutlineBorder(AsposeCells.BorderType.LeftBorder, AsposeCells.CellBorderType.Medium, new AsposeCells.Color(0, 0, 128));
range1.setOutlineBorder(AsposeCells.BorderType.RightBorder, AsposeCells.CellBorderType.Medium, new AsposeCells.Color(0, 0, 128));

// Input some data with some formattings into
// A few cells in the range.
range1.get(0, 0).putValue("Test");
range1.get(0, 4).putValue("123");

// Create another range of cells.
const range2 = worksheet.getCells().createRange("B3", "F3");

// Name the range.
range2.setName("testrange");

// Copy the first range into second range.
range2.copy(range1);

// Save the excel file.
workbook.save(path.join(dataDir, "copyranges.out.xls"));
```  

