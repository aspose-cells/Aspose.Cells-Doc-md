---
title: Установка параметров печати с помощью Node.js через C++
linktitle: Настройка параметров печати
type: docs
weight: 40
url: /ru/nodejs-cpp/setting-print-options/
description: В этой статье показано, как программно установить параметры печати функции настройки страницы Excel с помощью API Node.js и библиотеки C++. Можно установить область печати, заголовки печати и порядок страниц.
keywords: установка области печати Excel через Node.js с помощью C++, установка заголовков печати Excel через Node.js, установка порядка страниц Excel через Node.js с помощью C++
---

{{% alert color="primary" %}}

Настройки страницы установки Microsoft Excel предоставляют несколько параметров печати (также называемых параметрами листа), которые позволяют пользователям контролировать порядок печати листов рабочей книги.

{{% /alert %}}

## **Установка параметров печати**

Эти параметры печати позволяют пользователям:

- Выбрать конкретную область печати на рабочем листе.
- Напечатать заголовки.
- Напечатать сетку.
- Печать верхних заголовков строк / столбцов.
- Достичь чернового качества.
- Напечатать примечания.
- Напечатать ошибки ячеек.
- Определить порядок страниц.

Aspose.Cells for Node.js via C++ поддерживает все параметры печати, предлагаемые Microsoft Excel, и разработчики могут легко настроить эти параметры для рабочих листов, используя свойства класса [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup). Ниже подробно обсуждается, как использовать эти свойства.

### **Установка области печати**

По умолчанию область печати включает все области листа, содержащие данные. Разработчики могут установить конкретную область печати листа.

Чтобы выбрать конкретную область печати, используйте свойство [**PageSetup.getPrintArea()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintArea--) класса [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup). Назначьте этому свойству диапазон ячеек, определяющий область печати.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the PageSetup of the worksheet
const pageSetup = workbook.getWorksheets().get(0).getPageSetup();

// Specifying the cells range (from A1 cell to T35 cell) of the print area
pageSetup.setPrintArea("A1:T35");

// Save the workbook.
workbook.save(path.join(dataDir, "SetPrintArea_out.xls"));
```

### **Установка заголовков для печати**

Aspose.Cells позволяет назначить заголовки строк и столбцов для повторения на всех страницах напечатанного листа. Для этого используйте свойства [**PageSetup.getPrintTitleColumns()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintTitleColumns--) и [**PageSetup.getPrintTitleRows()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintTitleRows--) класса [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup).

Строки или столбцы, которые будут повторяться, определяются путем передачи их номеров строки или столбца. Например, строки определяются как $1:$2, а столбцы определяются как $A:$B.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the PageSetup of the worksheet
const pageSetup = workbook.getWorksheets().get(0).getPageSetup();

// Defining column numbers A & B as title columns
pageSetup.setPrintTitleColumns("$A:$B");

// Defining row numbers 1 & 2 as title rows
pageSetup.setPrintTitleRows("$1:$2");

// Save the workbook.
workbook.save(path.join(dataDir, "SetPrintTitle_out.xls"));
```

### **Настройка Других Опций Печати**

Класс [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup) также предоставляет несколько других свойств для установки общих параметров печати следующим образом:

- [**PageSetup.getPrintGridlines()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintGridlines--): логическое свойство, определяющее, следует ли печатать сетки или нет.
- [**PageSetup.getPrintHeadings()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintHeadings--): логическое свойство, определяющее, следует ли печатать заголовки строк и столбцов или нет.
- [**PageSetup.getBlackAndWhite()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getBlackAndWhite--): логическое свойство, определяющее, следует ли печатать рабочий лист в чёрно-белом режиме или нет.
- [**PageSetup.getPrintComments()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintComments--): определяет, отображать ли комментарии для печати на рабочем листе или в конце рабочего листа.
- [**PageSetup.getPrintDraft()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintDraft--): логическое свойство, определяющее, следует ли печатать лист без графики.
- [**PageSetup.getPrintErrors()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintErrors--): определяет, следует ли печатать ошибки ячейки как отображаемые, пустые, тире или N/A.

Для установления свойств [**PageSetup.getPrintComments()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintComments--) и [**PageSetup.getPrintErrors()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintErrors--) Aspose.Cells for Node.js via C++ также предоставляет два перечисления, [**PrintCommentsType**](https://reference.aspose.com/cells/nodejs-cpp/printcommentstype) и [**PrintErrorsType**](https://reference.aspose.com/cells/nodejs-cpp/printerrorstype), содержащие предопределённые значения для назначения свойствам [**PageSetup.getPrintComments()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintComments--) и [**PageSetup.getPrintErrors()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintErrors--) соответственно.

Предопределённые значения в перечислении [**PrintCommentsType**](https://reference.aspose.com/cells/nodejs-cpp/printcommentstype) перечислены ниже с их описаниями.

|**Типы Примечаний к Печати**|**Описание**|
| :- | :- |
|PrintInPlace|Указывает на печать комментариев как отображаемых в таблице.|
|PrintNoComments|Указывает, что комментарии не нужно печатать.|
|PrintSheetEnd|Указывает на печать комментариев в конце таблицы.|

Предопределённые значения перечисления [**PrintErrorsType**](https://reference.aspose.com/cells/nodejs-cpp/printerrorstype) перечислены ниже с их описаниями.

|**Типы Ошибок Печати**|**Описание**|
| :- | :- |
|PrintErrorsBlank|Указывает, что ошибки не нужно печатать.|
|PrintErrorsDash|Указывает на печать ошибок как "--".|
|PrintErrorsDisplayed|Указывает на печать ошибок как отображаемых.|
|PrintErrorsNA|Указывает на печать ошибок как "#N/A".|

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the PageSetup of the worksheet
const pageSetup = workbook.getWorksheets().get(0).getPageSetup();

// Allowing to print gridlines
pageSetup.setPrintGridlines(true);

// Allowing to print row/column headings
pageSetup.setPrintHeadings(true);

// Allowing to print worksheet in black & white mode
pageSetup.setBlackAndWhite(true);

// Allowing to print comments as displayed on worksheet
pageSetup.setPrintComments(AsposeCells.PrintCommentsType.PrintInPlace);

// Allowing to print worksheet with draft quality
pageSetup.setPrintDraft(true);

// Allowing to print cell errors as N/A
pageSetup.setPrintErrors(AsposeCells.PrintErrorsType.PrintErrorsNA);

// Save the workbook.
workbook.save(path.join(dataDir, "OtherPrintOptions_out.xls"));
```

### **Установить порядок страниц**

Класс [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup) предоставляет свойство [**PageSetup.getOrder()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getOrder--), которое используется для сортировки нескольких страниц вашего рабочего листа для печати. Есть два варианта порядка страниц.

- **Сначала вниз, затем вправо:** печатает все страницы вниз до печати любых страниц вправо.
- **Сначала вправо, затем вниз:** печатает страницы слева направо до печати страниц ниже.

Aspose.Cells предоставляет перечисление [**PrintOrderType**](https://reference.aspose.com/cells/nodejs-cpp/printordertype), которое содержит все предопределённые типы порядка.

Предопределённые значения перечисления [**PrintOrderType**](https://reference.aspose.com/cells/nodejs-cpp/printordertype) приведены ниже.

|**Типы порядка печати**|**Описание**|
| :- | :- |
|DownThenOver|Представляет порядок печати как сначала вниз, затем вправо.|
|OverThenDown|Представляет порядок печати как сначала вправо, затем вниз.|

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the PageSetup of the worksheet
const pageSetup = workbook.getWorksheets().get(0).getPageSetup();

// Setting the printing order of the pages to over then down
pageSetup.setOrder(AsposeCells.PrintOrderType.OverThenDown);

// Save the workbook.
workbook.save(path.join(dataDir, "SetPageOrder_out.xls"));
```
