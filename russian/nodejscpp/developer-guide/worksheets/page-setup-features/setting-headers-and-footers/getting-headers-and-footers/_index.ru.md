---
title: Получение заголовков или нижних колонтитулов с помощью Node.js через C++
linktitle: Получение заголовков или нижних колонтитулов
type: docs
weight: 30
url: /ru/nodejs-cpp/get-headers-or-footers/
description: В этой статье объясняется, как программно получать заголовки и нижние колонтитулы из файлов Excel или OpenOffice через API Node.js через C++.
---

{{% alert color="primary" %}}

Заголовки и нижние колонтитулы отображаются только в представлении макета страницы, предварительном просмотре и на распечатанных страницах. 

Также вы можете использовать диалоговое окно настройки страницы, если хотите просмотреть заголовки или нижние колонтитулы для более чем одного листа одновременно. 

Для других типов листов, таких как листы диаграмм или диаграммы, вы можете вставлять заголовки и нижние колонтитулы только с помощью диалогового окна настройки страницы.

{{% /alert %}}

## **Получение заголовков и нижних колонтитулов в MS Excel**
1. Нажмите на лист, где вы хотите просмотреть или изменить заголовки или нижние колонтитулы.
2. На вкладке Вид в группе Просмотры рабочей книги щёлкните «Разметка страницы».
   Excel отображает лист в режиме макета страницы.
3. Чтобы просмотреть или отредактировать заголовок или нижний колонтитул, щелкните на текстовом поле заголовка или колонтитула слева, по центру или справа вверху или внизу страницы листа (под заголовком или над колонтитулом).


## **Получение заголовков и нижних колонтитулов с помощью Aspose.Cells for Node.js via C++**
С помощью методов [**PageSetup.getHeader(number)**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getHeader-number-) и [**PageSetup.getFooter(number)**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getFooter-number-) разработчики на Node.js могут просто получать заголовки или нижние колонтитулы из файла.

1. Создайте рабочую книгу для открытия файла.
2. Получите лист, из которого необходимо получить заголовки или нижний колонтитул.
3. Получите заголовок или нижний колонтитул с конкретным ID раздела.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "HeaderFooter.xlsx");

// Instantiate a new Workbook
const workbook = new AsposeCells.Workbook(filePath);
const sheet = workbook.getWorksheets().get(0);

// Gets left section of header
console.log(sheet.getPageSetup().getHeader(0));
// Gets center section of header
console.log(sheet.getPageSetup().getHeader(1));
// Gets right section of header
console.log(sheet.getPageSetup().getHeader(2));
// Gets center section of footer
console.log(sheet.getPageSetup().getFooter(1));
```

## **Разбор заголовков и колонтитулов в список команд**
Текст заголовка или нижнего колонтитула может содержать специальные команды, например, заполнители для номера страницы, текущей даты или атрибутов форматирования текста.

Специальные команды представлены одним символом с ведущим амперсандом ("&").

Строки заголовка и нижнего колонтитула создаются с использованием грамматики ABNF. Без просмотрщика их понять сложно.

Aspose.Cells for Node.js via C++ предоставляет метод [**PageSetup.getCommands(string)**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getCommands-string-) для парсинга заголовков и нижних колонтитулов как списка команд.

Следующий код показывает, как парсить заголовок или нижний колонтитул как список команд и обрабатывать команды:

```javascript
try {
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "HeaderFooter.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);
const sheet = workbook.getWorksheets().get(0);

// Gets left section of header
const headerSection = sheet.getPageSetup().getHeader(0);
const commands = sheet.getPageSetup().getCommands(headerSection) || [];

commands.forEach(c => {
switch (c.getType()) {
case AsposeCells.HeaderFooterCommandType.SheetName:
// embedded the name of the sheet to header or footer
break;
}
```
