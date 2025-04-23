---
title: Скрытие отображения нулевых значений на рабочем листе с помощью Node.js через C++
linktitle: Скрытие отображения нулевых значений в таблице
type: docs
weight: 50
url: /ru/nodejs-cpp/hiding-the-display-of-zero-values-in-the-worksheet/
description: Эта статья покажет вам пример кода, объясняющий, как программно скрыть нулевые значения в электронной таблице Excel с помощью библиотеки Node.js через C++.
keywords: скрыть нулевые значения в листе Excel в Node.js через C++
---

{{% alert color="primary" %}} 

Иногда вам нужно скрывать нулевые значения в электронной таблице. Это может быть личным предпочтением или стандартом форматирования.

{{% /alert %}} 

Чтобы скрыть нулевые значения в таблице Microsoft Excel (например, Microsoft Excel 2003):

1. В меню **Инструменты** выберите **Параметры**, затем выберите вкладку **Вид**.
1. Отмените выбор опции **Нулевые значения**.
1. Нажмите **ОК**.

Обратите внимание на следующий пример кода, демонстрирующий скрытие нулей с помощью Aspose.Cells for Node.js via C++.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xlsx");
// Create a new Workbook object
const workbook = new AsposeCells.Workbook(filePath);

// Get First worksheet of the workbook
const sheet = workbook.getWorksheets().get(0);

// Hide the zero values in the sheet
sheet.setDisplayZeros(false);

// Save the workbook
workbook.save(path.join(dataDir, "outputfile.out.xlsx"));
```
