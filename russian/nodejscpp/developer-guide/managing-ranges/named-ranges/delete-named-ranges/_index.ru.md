---
title: Удаление именованных диапазонов с помощью Node.js через C++
linktitle: Удалить именованные диапазоны
type: docs
weight: 90
url: /ru/nodejs-cpp/Delete-named-ranges/
description: Вы можете узнать, как удалить определенные имена или именованные диапазоны из файлов Excel или OpenOffice с помощью Aspose.Cells for Node.js via C++.
---

## **Введение**
Если в файлах Excel слишком много определенных имен или именованных диапазонов, некоторые из них придется очистить, чтобы они больше не использовались.

## **Удалить именованный диапазон в MS Excel**

Для удаления именованного диапазона из Excel следуйте этим шагам:
1. Откройте Microsoft Excel и откройте книгу, которая содержит именованный диапазон.
2. Перейдите на вкладку "Формулы" на ленте Excel.
3. Нажмите кнопку "Менеджер имен" в группе "Определенные имена". Это откроет диалоговое окно Менеджер имен.
4. В диалоговом окне Менеджер имен выберите именованный диапазон, который вы хотите удалить.
5. Нажмите кнопку "Удалить". Подтвердите удаление по запросу.
6. Нажмите кнопку "Закрыть", чтобы закрыть диалоговое окно Менеджер имен.
7. Сохраните книгу, чтобы сохранить внесенные изменения.

## **Удаляет именованный диапазон с помощью Aspose.Cells for Node.js via C++**
С помощью Aspose.Cells for Node.js via C++ вы можете удалить именованные диапазоны или определенные имена по [тексту](https://reference.aspose.com/cells/nodejs-cpp/namecollection/#remove-string-) или [индексу](https://reference.aspose.com/cells/nodejs-cpp/namecollection/#removeAt-number-) из списка.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);

// Get all the worksheets in the book.
const worksheets = workbook.getWorksheets();

// Deleted a named range by text.
worksheets.getNames().remove("NamedRange");

// Deleted a defined name by index. Ensure to check the count before removal.
if (worksheets.getNames().getCount() > 0) {
worksheets.getNames().removeAt(0);
}

// Save the workbook to retain the changes.
workbook.save("Book2.xlsx");
```

Примечание: если определенное имя используется в формулах, его невозможно удалить. Мы можем удалить только формулу определенного имени.

## **Удаляет несколько именованных диапазонов**
При удалении определенного имени нужно проверить, используется ли оно во всех формулах в файле.
Для повышения производительности удаления именованных диапазонов, мы можем удалять некоторые их сразу вместе.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);

// Get all the worksheets in the book.
const worksheets = workbook.getWorksheets();

// Deleted some defined names.
worksheets.getNames().remove(["NamedRange1", "NamedRange2"]);

// Save the workbook to retain the changes.
workbook.save("Book2.xlsx");
```

## **Удаление дублированных определенных имен**
Некоторые файлы Excel повреждаются, потому что некоторые определенные имена дублируются. Поэтому мы можем удалить эти дублирующиеся имена для восстановления файла.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);

// Get all the worksheets in the book.
const worksheets = workbook.getWorksheets();

// Deleted some defined names.
worksheets.getNames().removeDuplicateNames();

// Save the workbook to retain the changes.
workbook.save("Book2.xlsx");
```



