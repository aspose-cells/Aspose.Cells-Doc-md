---
title: Как напечатать Excel, чтобы он подходил по ширине и высоте страниц с помощью Node.js через C++
linktitle: Как напечатать Excel так, чтобы страницы были шириной и высотой, подогнанными под страницу
type: docs
weight: 200
url: /ru/nodejs-cpp/how-to-print-excel-as-fitted-pages-wide-and-tall/
description: В этой статье приведён код, объясняющий, как задать параметры FitToPagesWide и FitToPagesTall с помощью Aspose.Cells for Node.js via C++.
keywords: Node.js через C++ как установить FitToPagesWide и FitToPagesTall, как добавить FitToPagesWide и FitToPagesTall в Node.js, как задать FitToPagesWide и FitToPagesTall в Excel, как очистить FitToPagesWide и FitToPagesTall в Excel, как распечатать Excel, чтобы он умещался по ширине и высоте страниц, как напечатать лист как одну страницу, как распечатать все столбцы листа на одной странице.
---

## **Введение**

Настройки FitToPagesWide и FitToPagesTall используются в приложениях для работы с таблицами (таких как Microsoft Excel), чтобы контролировать масштабирование при печати. Эти настройки помогают обеспечить, чтобы напечатанный результат поместился на указанное количество страниц, как по горизонтали, так и по вертикали. Вот разъяснение каждого из параметров:

1. FitToPagesWide: Эта настройка задает количество страниц по ширине, в которые должна поместиться распечатка. Например, установка значения в 1 означает, что содержимое масштабируется для размещения на одной странице по ширине, независимо от ширины таблицы.
2. FitToPagesTall: Эта настройка определяет количество страниц по вертикали, в которые должна поместиться распечатанная часть. Например, установка FitToPagesTall в 1 означает, что содержимое масштабируется для размещения на одной высоте страницы, независимо от количества строк.

## **Зачем использовать FitToPagesWide и FitToPagesTall**
Вот некоторые причины установки FitToPagesWide и FitToPagesTall:
1. Контроль над размещением при печати: задавая количество страниц по ширине и высоте, вы можете убедиться, что ваш печатный документ легко читаем и хорошо отформатирован, без нежелательного переноса столбцов или строк между страницами.
2. Последовательность: Если вы печатаете несколько листов или отчетов, использование этих настроек помогает поддерживать последовательный формат, что облегчает сравнение и анализ печатных документов.
3. Профессиональный вид: Правильное масштабирование и подгонка содержимого под заданное количество страниц могут сделать ваш документ более аккуратным и профессиональным.

## **Как распечатать файл по страницам по ширине и высоте в Excel**

Чтобы установить параметры FitToPagesWide и FitToPagesTall в Microsoft Excel, выполните следующие шаги:

1. Откройте рабочую книгу Excel и перейдите к листу, который хотите распечатать.
2. Перейдите на вкладку Макет страницы на ленте.
3. В группе Настройка страницы щёлкните по маленькой стрелке в правом нижнем углу, чтобы открыть диалоговое окно Настройка страницы.
4. В диалоговом окне Настройка страницы перейдите на вкладку Страница.
5. В разделе Масштабирование выберите опцию "По размеру" и укажите желаемое число страниц по ширине и высоте: Введите желаемое число страниц по ширине в первое поле (по ширине x страниц). Введите желаемое число страниц по высоте во второе поле (по высоте y страниц).
<br>
<img src="2.png" width=60% />

Нажмите OK, чтобы применить настройки.

## **Как напечатать Excel в прикидке страниц по ширине и высоте с помощью Aspose.Cells for Node.js via C++**

Чтобы установить FitToPagesWide и FitToPagesTall в определённом листе: сначала загрузите [пример файла](input.xlsx), затем необходимо изменить свойства [**PageSetup.getFitToPagesTall()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getFitToPagesTall--) и [**PageSetup.getFitToPagesWide()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getFitToPagesWide--) объекта [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/) для нужного листа. Вот пример на Node.js:

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "input.xlsx");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook(filePath);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Setting the number of pages to which the length of the worksheet will be spanned
worksheet.getPageSetup().setFitToPagesTall(1);

// Setting the number of pages to which the width of the worksheet will be spanned
worksheet.getPageSetup().setFitToPagesWide(1);

// Save the workbook
workbook.save("out_net.pdf");
```

Результат вывода:
<br>
<img src="1.png" width=60% />

## **Как напечатать лист как одну страницу с помощью Aspose.Cells for Node.js via C++**

Чтобы напечатать лист как одну страницу: сначала загрузите [пример файла](sample.xlsx), затем нужно установить свойство [**PdfSaveOptions.getOnePagePerSheet()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getOnePagePerSheet--) объекта [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/). Вот пример на Node.js:

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

const options = new AsposeCells.PdfSaveOptions();
options.setOnePagePerSheet(true);

// Save the workbook.
workbook.save("OnePagePerSheet.pdf", options);
```

Результат вывода:
<br>
<img src="3.png" width=60% />

## **Как напечатать все столбцы листа на одной странице с помощью Aspose.Cells for Node.js via C++**

Чтобы напечатать все столбцы листа на одной странице: сначала загрузите [пример файла](sample.xlsx), затем необходимо установить свойство [**PdfSaveOptions.getAllColumnsInOnePagePerSheet()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getAllColumnsInOnePagePerSheet--) объекта [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/). Вот пример на Node.js:

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

const options = new AsposeCells.PdfSaveOptions();
options.setAllColumnsInOnePagePerSheet(true);

// Save the workbook.
workbook.save("AllColumnsInOnePagePerSheet.pdf", options);
```

Результат вывода:
<br>
<img src="4.png" width=60% />
{{< app/cells/assistant language="nodejs-cpp" >}}
