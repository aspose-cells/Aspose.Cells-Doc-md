---
title: Настройка различных заголовков и колонтитулов для разных страниц с помощью Node.js через C++
linktitle: Установка разных заголовков и нижних колонтитулов для разных страниц
type: docs
weight: 35
url: /ru/nodejs-cpp/setting-different-headers-and-footers-for-pages-to-excel/
description: Эта статья содержит пример кода, показывающий, как программно установить заголовки и колонтитулы страницы листа Excel с помощью Aspose.Cells for Node.js via C++. Установите заголовки и колонтитулы для первых, нечётных и чётных страниц.
keywords: установить заголовки и колонтитулы Excel для первой страницы Node.js через C++, установить заголовки и колонтитулы Excel для нечётных страниц Node.js через C++, установить заголовки и колонтитулы Excel для чётных страниц Node.js через C++
---

{{% alert color="primary" %}}

MS Excel поддерживает установку различных заголовков и нижних колонтитулов для первой страницы, нечетных страниц и четных страниц, начиная с Excel 2007.
Aspose.Cells for Node.js via C++ поддерживает такую же функцию.

{{% /alert %}}

## **Установка разных заголовков и нижних колонтитулов в MS Excel**

**![Установка различных заголовков и нижних колонтитулов](difpage.png)**

1. Нажмите **Разметка страницы > Печать заголовков > Заголовок/нижний колонтитул**.
1. Установите флаги **Different Odd and Even Pages** или **Different first page**.
1. Введите разные заголовки и нижние колонтитулы.

## **Настройка различных заголовков и колонтитулов с помощью Aspose.Cells for Node.js via C++**

Aspose.Cells ведет себя так же, как Excel.
1. Устанавливает флаги [PageSetup.isHFDiffOddEven()](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#isHFDiffOddEven--) и [PageSetup.isHFDiffFirst()](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#isHFDiffFirst--) 
1. Введите разные заголовки и нижние колонтитулы.
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const wb = new AsposeCells.Workbook(filePath);

// Gets the setting of page setup.
const pageSetup = wb.getWorksheets().get(0).getPageSetup();
// Sets different odd and even pages
pageSetup.setIsHFDiffOddEven(true);
pageSetup.setHeader(1, "I am the header of the Odd page.");
pageSetup.setEvenHeader(1, "I am the header of the Even page.");
// Sets different first page
pageSetup.setIsHFDiffFirst(true);
pageSetup.setFirstPageHeader(1, "I am the header of the First page.");
```
