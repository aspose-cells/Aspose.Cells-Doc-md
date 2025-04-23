---
title: Зафиксировать верхнюю строку(и) листа Excel с помощью Node.js и C++
linktitle: Заморозить строки
type: docs
weight: 190
url: /ru/nodejs-cpp/how-to-freeze-rows-of-excel-worksheet
description: В этой статье вы научитесь программно фиксировать верхние строки листа Excel, используя библиотеку Node.js с C++ API.
keywords: Зафиксировать верхние строки, зафиксировать верхнюю строку с помощью Node.js и C++.
---

## **Введение**

В этой статье мы научимся, как зафиксировать верхнюю строку(и). Когда у вас есть огромное количество данных под общим заголовком, вы не можете видеть заголовок при прокрутке вниз по листу. Вы можете зафиксировать верхний(е) строку(и), чтобы видеть зафиксированную часть даже при прокрутке остальной части данных. Вы легко сможете видеть заголовки в верхних строках.

## **Заморозить строки в Excel**

**![Заморозить верхнюю строку(и) в Excel](Freeze-Rows.png)**

1. Если хотите заморозить верхнюю(ие) строку(и), сначала выберите строку под строкой, которую нужно зафиксировать.
2. Нажмите Вид > Заморозка областей.
3. В выпадающем меню нажмите "Заморозить верхнюю строку".
4. Если вы прокрутите вниз, первая строка всегда останется сверху.

**![Замороженная строка](Frozen-Row.png)**

Как видите, 1-я строка зафиксирована; первая строка всегда остаётся вверху при прокрутке.

Фиксация строк позволяет вам просматривать большие данные без отслеживания ярлыка строки.

## **Фиксация строк с помощью Aspose.Cells for Node.js via C++**
Просто зафиксировать строки с помощью Aspose.Cells for Node.js via C++. 
Пожалуйста, используйте метод [**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#freezePanes-number-number-number-number-) для фиксации строки(и) в выбранной строке.
1. Создать рабочую книгу для открытия файла или создать пустой файл.
2. Зафиксируйте первую строку с помощью метода Worksheet.freezePanes().
3. Сохранить файл.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Freeze.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);

// Freezing panes at the cell B2
workbook.getWorksheets().get(0).freezePanes("A2", 1, 0);

// Saving the file
workbook.save("frozen.xlsx");
```

Приложен [образец исходного файла Excel](../Freeze.xlsx).
