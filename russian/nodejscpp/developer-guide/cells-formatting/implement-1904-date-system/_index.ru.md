---
title: Реализуйте систему дат 1904 с помощью Node.js и C++
description: Aspose.Cells — это библиотека Node.js для работы с файлами электронных таблиц. Она поддерживает реализацию системы дат 1904, позволяя пользователям выполнять вычисления и форматировать данные на основе системы дат 1 января 1904 года. В этой статье описывается, как реализовать систему дат 1904 с использованием библиотеки Aspose.Cells.
keywords: Aspose.Cells, система дат 1904, электронная таблица, вычисления, форматирование, Node.js через C++
type: docs
weight: 7000
url: /ru/nodejs-cpp/implement-1904-date-system/
---

{{% alert color="primary" %}} 

Microsoft Excel поддерживает две системы дат: систему дат 1900 (используемая как по умолчанию в Excel для Windows) и систему дат 1904. Система дат 1904 обычно используется для обеспечения совместимости с файлами Excel для Macintosh и является системой по умолчанию, если вы используете Excel для Macintosh. Вы можете установить систему дат 1904 для файлов Excel, используя Aspose.Cells for Node.js via C++. 

{{% /alert %}} 

Для реализации системы дат 1904 в Microsoft Excel (например, Microsoft Excel 2003):

1. В меню **Инструменты** выберите **Параметры**, а затем выберите вкладку **Расчет**.
1. Выберите опцию **1904 годовая система**.
1. Нажмите **ОК**.

|**Выбор 1904-ой годовой системы в Microsoft Excel**|
| :- |
|![todo:image_alt_text](implement-1904-date-system_1.png)|

См. следующий образец кода о том, как это сделать с использованием API Aspose.Cells.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xlsx");
// Initialize a new Workbook
// Open an excel file
const workbook = new AsposeCells.Workbook(filePath);

// Implement 1904 date system
workbook.getSettings().setDate1904(true);

// Save the excel file
workbook.save(path.join(dataDir, "Mybook.out.xlsx"));
```
