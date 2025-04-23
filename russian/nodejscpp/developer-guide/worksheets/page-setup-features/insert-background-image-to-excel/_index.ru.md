---
title: Вставить фоновое изображение в Excel с помощью Node.js через C++
linktitle: Вставить фоновое изображение в Excel
type: docs
weight: 90
url: /ru/nodejs-cpp/insert-background-image-to-excel/
description: "Как вставить фоновое изображение в Excel, используя Aspose.Cells for Node.js via C++."
---

{{% alert color="primary" %}} 

Вы можете сделать лист более привлекательным, добавив изображение в качестве фонового изображения рабочего листа. Эта функция может быть довольно эффективной, если у вас есть специальная корпоративная графика, которая добавляет намек на фон, не заслоняя данные на листе. Вы можете установить фоновое изображение для листа с помощью API Aspose.Cells.

{{% /alert %}} 

## **Установка фонового изображения на листе в Microsoft Excel**

Чтобы установить фоновое изображение листа в Microsoft Excel (например, Microsoft Excel 2019):

1. Из меню **Макет страницы** найдите опцию **Настройка страницы**, затем щелкните опцию **Фон**.
1. Выберите изображение для установки фонового изображения листа.

   **Установка фона листа**

![todo:image_alt_text](insert-background-to-excel.jpg)

## **Установка фона листа с помощью Aspose.Cells for Node.js via C++**

Приведенный ниже код устанавливает фоновое изображение с использованием изображения из потока.

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const backgroundImagePath = path.join(dataDir, "background.jpg");

// Create a new Workbook.
const workbook = new AsposeCells.Workbook();

// Get the first worksheet.
const sheet = workbook.getWorksheets().get(0);

// Set the background image for the worksheet.
sheet.setBackgroundImage(fs.readFileSync(backgroundImagePath).buffer);

// Save the Excel file
workbook.save("outputBackImageSheet.xlsx");

// Save the HTML file
workbook.save("outputBackImageSheet.html", AsposeCells.SaveFormat.Html);
```

## Связанные статьи

- [Работа с фоном в файлах ODS](/cells/ru/nodejs-cpp/working-with-background-in-ods-files/)

