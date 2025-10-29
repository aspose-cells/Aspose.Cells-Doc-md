---  
title: Установка цвета вкладки листа с помощью Node.js через C++  
linktitle: Установка цвета вкладки таблицы  
type: docs  
weight: 120  
url: /ru/nodejs-cpp/set-worksheet-tab-color/  
description: В этой статье представлен пример кода, который устанавливает цвет вкладки Excel таблицы программным путем с помощью Node.js через C++.  
keywords: установка цвета вкладки Excel Node.js через C++, код для установки цвета вкладки Excel Node.js через C++  
---  

{{% alert color="primary" %}}  

Aspose.Cells позволяет изменять цвет отдельных вкладок таблицы, чтобы выделить их из остальных. Например, вы можете сделать вкладку Expenses красной, Sales зеленой, Assets синей и т. д.

{{% /alert %}}  
## **Установка цвета вкладки таблицы в Microsoft Excel**  
1. Щелкните правой кнопкой мыши на вкладке в листе внизу текущей таблицы.  
1. Выберите **Цвет вкладки**.  
1. Выберите цвет из палитры.  
1. Нажмите **ОК**.  
## **Установка цвета вкладки таблицы с помощью Aspose.Cells**  
Приведенный ниже образцовый код показывает, как установить цвет вкладки с помощью Aspose.Cells.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate a new Workbook
// Open an Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "Book1.xlsx"));

// Get the first worksheet in the book
const worksheet = workbook.getWorksheets().get(0);

// Set the tab color
worksheet.setTabColor(AsposeCells.Color.Red);

// Save the Excel file
workbook.save(path.join(dataDir, "worksheettabcolor.out.xls"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
