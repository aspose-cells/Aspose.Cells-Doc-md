---
title: Создавать рабочие книги и рабочие листы с именами диапазонов с помощью Node.js через C++
linktitle: Именованный диапазон
type: docs
weight: 40
url: /ru/nodejs-cpp/create-workbook-and-worksheet-scoped-named-ranges/
description: Узнайте, как создавать именованные диапазоны с областью действия рабочей книги и листа, используя Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}} 

Microsoft Excel позволяет пользователям определить именованные диапазоны с двумя различными областями: книга (также известная как глобальная область) и лист.

- Именованные диапазоны с глобальной областью могут быть доступны с любого листа внутри этой книги, просто используя его имя.
- Именованные диапазоны с областью листа доступны с помощью ссылки на конкретный лист, на котором он был создан.

Aspose.Cells for Node.js via C++ предоставляет ту же функциональность, что и Microsoft Excel для добавления именованных диапазонов с областью действия книги и листа. При создании именованного диапазона с областью действия листа, следует использовать ссылку на лист в именованном диапазоне, чтобы указать его как диапазон с областью действия листа.

{{% /alert %}} 
## **Добавление именованного диапазона с областью видимости рабочей книги**


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a new Workbook object
const workbook = new AsposeCells.Workbook();

// Get first worksheet of the workbook
const sheet = workbook.getWorksheets().get(0);

// Get worksheet's cells collection
const cells = sheet.getCells();

// Create a range of Cells from Cell A1 to C10
const workbookScope = cells.createRange("A1", "C10");

// Assign the name to workbook scope named range
workbookScope.setName("workbookScope");

// Save the workbook
workbook.save(path.join(dataDir, "WorkbookScope.out.xlsx"));
```
## **Добавление Именованного Диапазона с Областью Листа**


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a new Workbook object
const workbook = new AsposeCells.Workbook();

// Get first worksheet of the workbook
const sheet = workbook.getWorksheets().get(0);

// Get worksheet's cells collection
const cells = sheet.getCells();
// Create a range of Cells
const localRange = cells.createRange("A1", "C10");

// Assign name to range with sheet reference
localRange.setName("Sheet1!local");

// Save the workbook
workbook.save(path.join(dataDir, "output.out.xls"));
```

## **Продвинутые темы**
- [Создание доступа и копирование именованных диапазонов](/cells/ru/nodejs-cpp/create-access-and-copy-named-ranges/)
- [Форматирование и изменение именованных диапазонов](/cells/ru/nodejs-cpp/format-and-modify-named-ranges/)
- [Получить диапазон с внешними ссылками](/cells/ru/nodejs-cpp/get-range-with-external-links/)
- [Реализация не последовательных диапазонов](/cells/ru/nodejs-cpp/implementing-non-sequential-ranges/)


