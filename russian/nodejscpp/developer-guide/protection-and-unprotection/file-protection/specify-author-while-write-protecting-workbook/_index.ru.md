---  
title: Укажите автора при защите книги паролем с помощью Node.js через C++  
linktitle: Укажите автора при защите от записи книги  
type: docs  
weight: 40  
url: /ru/nodejs-cpp/specify-author-while-write-protecting-workbook/  
description: Укажите имя автора при защите книги паролем с помощью Aspose.Cells for Node.js via C++.  
---  

## **Возможные сценарии использования**

Вы можете указать имя автора при защите вашей книги паролем с помощью API Aspose.Cells. Пожалуйста, используйте свойство [**Workbook.getAuthor()**](https://reference.aspose.com/cells/nodejs-cpp/writeprotection/#getAuthor--) для этой цели.

## **Укажите автора при защите от записи книги**

Следующий пример кода объясняет использование свойства [**Workbook.getAuthor()**](https://reference.aspose.com/cells/nodejs-cpp/writeprotection/#getAuthor--). Код создает пустую книгу, защищает ее паролем, указывает имя автора и сохраняет как [выходной файл Excel](67338582.xlsx). Ниже приведен снимок экрана, иллюстрирующий эффект этого примера на выходном файле Excel для вашего ознакомления.

![todo:image_alt_text](specify-author-while-write-protecting-workbook_1.png)

## **Образец кода**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Create empty workbook.
const workbook = new AsposeCells.Workbook();

// Write protect workbook with password.
workbook.getSettings().getWriteProtection().setPassword("1234");

// Specify author while write protecting workbook.
workbook.getSettings().getWriteProtection().setAuthor("SimonAspose");

// Save the workbook in XLSX format.
const outputDir = path.join(__dirname, "output");
workbook.save(path.join(outputDir, "outputSpecifyAuthorWhileWriteProtectingWorkbook.xlsx"));
```  

