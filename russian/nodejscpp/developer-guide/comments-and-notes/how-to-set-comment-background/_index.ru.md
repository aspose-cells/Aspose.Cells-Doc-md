---
title: Как изменить фон комментария в Excel с помощью Node.js через C++
linktitle: Фон комментария
type: docs
weight: 190
url: /ru/nodejs-cpp/how-to-set-comment-background/
description: Как изменить цвет комментария и вставить картинку или изображение в комментарий в Excel с помощью Aspose.Cells for Node.js via C++.
keywords: Добавление изображения как фона комментария в Excel с Node.js через C++
---

{{% alert color="primary" %}}
Комментарии добавляются к ячейкам для записи замечаний, любой информации о работе формулы, источнике данных или вопросах рецензентов. Комментарии играют важную роль при обсуждении или проверке документа несколькими людьми. Как различать комментарии разных пользователей? Да, можно установить разный фон у каждого комментария. Но при обработке большого количества документов и комментариев вручную это невозможно. К счастью, [**Aspose.Cells**](https://products.aspose.com/cells/nodejs-cpp/) предоставляет API, который позволяет делать это автоматически в коде.
{{% /alert %}}

## **Как изменить цвет комментария в Excel**

Если вам не нужен стандартный фон у комментариев, вы можете заменить его на интересующий вас цвет. Как изменить цвет фона для области комментария в Excel?

Нижеследующий код поможет вам разобраться, как использовать [**Aspose.Cells**](https://products.aspose.com/cells/nodejs-cpp/), чтобы добавить фоновый цвет комментариев по вашему выбору.

Здесь подготовлен [пример файла](exmaple.xlsx) для вас. Этот файл используется для инициализации объекта Workbook в приведенном ниже коде.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Initialize a new workbook.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "example.xlsx"));

// Accessing the newly added comment
const comment = workbook.getWorksheets().get(0).getComments().get(0);

// change background color
const shape = comment.getCommentShape();
shape.getFill().getSolidFill().setColor(AsposeCells.Color.Red);

// Save the Excel file
workbook.save(path.join(dataDir, "result.xlsx"));
```

Выполните указанный выше код, и вы получите [выходной файл](result.xlsx).

## **Как вставить изображение в комментарий в Excel**

Microsoft Excel позволяет настраивать внешний вид таблиц практически по всему спектру. Можно даже добавить фоновое изображение к комментариям. Добавление фона может быть эстетичным выбором или способствовать укреплению бренда.

Пример ниже создает XLSX-файл с нуля с помощью API [**Aspose.Cells**](https://products.aspose.com/cells/nodejs-cpp/) и добавляет комментарий с фоновым изображением в ячейку A1.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

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
const fs = require("fs");
const bmp = fs.readFileSync(path.join(dataDir, "image2.jpg"));
const ms = Buffer.from(bmp);

// Set image data to the shape associated with the comment
comment.getCommentShape().getFill().setImageData(ms);

// Save the workbook
const outputFilePath = path.join(dataDir, "commentwithpicture1.out.xlsx");
workbook.save(outputFilePath, AsposeCells.SaveFormat.Xlsx);
```

{{< app/cells/assistant language="nodejs-cpp" >}}
