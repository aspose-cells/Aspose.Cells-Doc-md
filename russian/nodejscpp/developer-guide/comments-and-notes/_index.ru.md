---
title: Управление комментариями и заметками с помощью Node.js через C++
linktitle: Комментарии и заметки
type: docs
weight: 128
url: /ru/nodejs-cpp/comments-and-notes/
description: Вставляйте и управляйте комментариями или заметками с помощью Aspose.Cells for Node.js via C++.
keywords: вставка комментариев, вставка заметок Node.js через C++
---

## **Введение**

Комментарии используются для добавления дополнительной информации в ячейки. Aspose.Cells for Node.js via C++ предоставляет два метода для добавления комментариев к ячейкам. Первый — создание комментариев вручную в дизайнерском файле. Эти комментарии затем импортируются с помощью Aspose.Cells. Второй — добавление комментариев с помощью API Aspose.Cells во время выполнения. В этой теме обсуждается добавление комментариев к ячейкам с помощью API Aspose.Cells. Также будет объяснено форматирование комментариев.

## **Добавление комментария**

Добавьте комментарий к ячейке, вызвав метод [**CommentCollection.add(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#add-number-number-) коллекции [**Comments**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection) (инкапсулированный в объект [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)). Новый объект [**Comment**](https://reference.aspose.com/cells/nodejs-cpp/comment) можно получить из коллекции [**Comments**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection), передав индекс комментария. После получения объекта [**Comment**](https://reference.aspose.com/cells/nodejs-cpp/comment) настройте заметку комментария с помощью свойства [**getNote()**](https://reference.aspose.com/cells/nodejs-cpp/comment/#getNote--).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Workbook object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding a comment to "F5" cell
const commentIndex = worksheet.getComments().add("F5");

// Accessing the newly added comment
const comment = worksheet.getComments().get(commentIndex);

// Setting the comment note
comment.setNote("Hello Aspose!");

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

## **Форматирование комментариев**

Также возможно форматировать внешний вид комментариев, настроив их высоту, ширину и параметры шрифта.

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Workbook object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding a comment to "F5" cell
const commentIndex = worksheet.getComments().add("F5");

// Accessing the newly added comment
const comment = worksheet.getComments().get(commentIndex);

// Setting the comment note
comment.setNote("Hello Aspose!");

// Setting the font size of a comment to 14
comment.getFont().setSize(14);

// Setting the font of a comment to bold
comment.getFont().setIsBold(true);

// Setting the height of the font to 10
comment.setHeightCM(10);

// Setting the width of the font to 2
comment.setWidthCM(2);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

## **Добавить изображение в комментарий**

С помощью Microsoft Excel 2007 также возможно иметь изображение в качестве фона комментария к ячейке. В Excel 2007 это можно сделать, выполнив следующие шаги. (Предполагается, что вы уже добавили комментарий к ячейке.)

1. Щелкните правой кнопкой мыши ячейку, содержащую комментарий.
1. Выберите **Показать/скрыть комментарии** и очистите любой текст из комментария.
1. Щелкните по границе комментария, чтобы выбрать его.
1. Выберите **Формат**, затем **Комментарий**.
1. На вкладке **Цвета и линии** разверните список **Цвет**.
1. Нажмите **Изменение заливки**.
1. На вкладке **Изображение** нажмите **Выбрать изображение**.
1. Найдите и выберите изображение.
1. Нажмите **ОК**, пока все диалоговые окна не закроются.

Aspose.Cells также предоставляет эту функцию. Ниже приведен пример кода, который создает файл XLSX с нуля, добавляя комментарий в ячейку "A1" с установленным изображением в качестве его фона.

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a Workbook
const workbook = new AsposeCells.Workbook();

// Get a reference of comments collection with the first sheet
const comments = workbook.getWorksheets().get(0).getComments();

// Add a comment to cell A1
const commentIndex = comments.add(0, 0);
const comment = comments.get(commentIndex);
comment.setNote("First note.");
comment.getFont().setName("Times New Roman");

// Load an image into stream
const bmpPath = path.join(dataDir, "logo.jpg");
const bmpData = fs.readFileSync(bmpPath);

// Set image data to the shape associated with the comment
comment.getCommentShape().getFill().setImageData(bmpData);

// Save the workbook
workbook.save(path.join(dataDir, "book1.out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```

## **Продвинутые темы**
- [Изменение направления текста комментария](/cells/ru/nodejs-cpp/change-text-direction-of-the-comment/)
- [Как изменить цвет шрифта комментария](/cells/ru/nodejs-cpp/how-to-change-the-comment-font-color/)
- [Как установить фон комментария](/cells/ru/nodejs-cpp/how-to-set-comment-background/)
- [Комментарии с цепочкой](/cells/ru/nodejs-cpp/threaded-comments/)

{{< app/cells/assistant language="nodejs-cpp" >}}
