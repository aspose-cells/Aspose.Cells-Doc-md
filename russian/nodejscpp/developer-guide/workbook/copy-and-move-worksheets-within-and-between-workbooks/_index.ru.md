---
title: Копирование и перемещение листов внутри и между книгами с помощью Node.js через C++
linktitle: Копирование и перемещение листов внутри и между книгами
type: docs
weight: 80
url: /ru/nodejs-cpp/copy-and-move-worksheets-within-and-between-workbooks/
description: Узнайте, как копировать и перемещать листы внутри и между книгами, используя Aspose.Cells for Node.js via C++. Эффективно управляйте структурой вашей книги.
---

{{% alert color="primary" %}}

Иногда вам требуется несколько листов с общим форматированием и вводом данных. Например, если вы работаете с квартальными бюджетами, вам может понадобиться создать книгу с листами, содержащими одни и те же заголовки столбцов, заголовки строк и формулы. Есть способ сделать это: создав один лист, а затем скопировав его три раза.

Aspose.Cells for Node.js via C++ поддерживает копирование или перемещение листов внутри или между книгами. Листы, включая данные, форматирование, таблицы, матрицы, диаграммы, изображения и другие объекты, копируются с максимально возможной точностью.

{{% /alert %}}

## **Копирование и перемещение листов**

### **Копирование листа внутри книги**

Начальные шаги одинаковы для всех примеров.

1. Создайте две книги с некоторыми данными в Microsoft Excel. Для целей этого примера мы создали две новые книги в Microsoft Excel и ввели некоторые данные на листах.

- FirstWorkbook.xlsx (3 листа).
- SecondWorkbook.xlsx (1 лист).

1. Скачайте и установите Aspose.Cells:
   1. [Скачайте Aspose.Cells for Node.js via C++](https://downloads.aspose.com/cells/nodejs-cpp).
   1. Установите его на вашем компьютере для разработки.
      Все [Aspose](http://www.aspose.com/) компоненты при установке работают в режиме оценки. Режим оценки не имеет временных ограничений и вставляет только водяные знаки в созданные документы.
1. Создайте проект:
   1. Начните свой рабочий окружение.
   1. Создайте новое консольное приложение.
1. Добавьте ссылки:
   1. Добавьте ссылку на Aspose.Cells в проект.
      Например, добавьте ссылку на ...\Program Files\Aspose\Aspose.Cells\Bin\NodeJs\Aspose.Cells.dll
1. Скопируйте лист в книге.
   Первый пример копирует первый лист (Copy) внутри FirstWorkbook.xlsx.

При выполнении кода лист с именем Copy копируется внутри FirstWorkbook.xlsx с именем Последний лист.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open a file into the first book.
const excelWorkbook1 = new AsposeCells.Workbook(path.join(dataDir, "FirstWorkbook.xlsx"));

// Copy the first sheet of the first book within the workbook
excelWorkbook1.getWorksheets().get(2).copy(excelWorkbook1.getWorksheets().get("Copy"));

// Save the file.
excelWorkbook1.save(path.join(dataDir, "FirstWorkbookCopied_out.xlsx"));
```

### **Перемещение листа внутри книги**

Приведенный ниже код показывает, как переместить лист с одной позиции в книге на другую. При выполнении кода лист с именем Move из индекса 1 перемещается на индекс 2 внутри FirstWorkbook.xlsx.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "FirstWorkbook.xlsx");
// Open a file into the first book.
const excelWorkbook2 = new AsposeCells.Workbook(filePath);

// Move the sheet
const worksheets = excelWorkbook2.getWorksheets();
const worksheet = worksheets.get(0);
worksheet.moveTo(1);

// Save the file.
excelWorkbook2.save(path.join(dataDir, "FirstWorkbookMoved_out.xlsx"));
```

### **Копирование листа между книгами Excel**

Выполнение кода копирует лист с именем Copy в SecondWorkbook.xlsx с именем Sheet2.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const excelWorkbook3 = new AsposeCells.Workbook();
const excelWorkbook4 = new AsposeCells.Workbook();

// Create source worksheet
excelWorkbook3.getWorksheets().add("Copy");

// Add new worksheet into second Workbook
excelWorkbook4.getWorksheets().add();

// Copy the first sheet of the first book into second book.
excelWorkbook4.getWorksheets().get(1).copy(excelWorkbook3.getWorksheets().get("Copy"));

// Save the file.
excelWorkbook4.save(path.join(dataDir, "CopyWorksheetsBetweenWorkbooks_out.xlsx"));
```

### **Перемещение листа между книгами Excel**

При выполнении кода лист с именем Move перемещается из FirstWorkbook.xlsx в SecondWorkbook.xlsx с именем Sheet3.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create new workbooks instead of opening existing files
const excelWorkbook5 = new AsposeCells.Workbook();
const excelWorkbook6 = new AsposeCells.Workbook();

// Add New Worksheet
excelWorkbook6.getWorksheets().add();

// Copy the sheet from first book into second book.
excelWorkbook6.getWorksheets().get(0).copy(excelWorkbook5.getWorksheets().get(0));

// Remove the copied worksheet from first workbook
excelWorkbook5.getWorksheets().removeAt(0);

// Save the file.
excelWorkbook5.save(path.join(dataDir, "FirstWorkbookWithMove_out.xlsx"));

// Save the file.
excelWorkbook6.save(path.join(dataDir, "SecondWorkbookWithMove_out.xlsx"));
```
