---  
title: Переместить диапазон ячеек в листе с помощью Node.js через C++  
linktitle: Перемещение диапазона ячеек на листе  
type: docs  
weight: 370  
url: /ru/nodejs-cpp/move-range-of-cells-in-a-worksheet/  
description: Узнайте, как перемещать диапазон ячеек в листе с помощью Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
В этой статье показано, как перемещать диапазон ячеек на листе.  
{{% /alert %}}  

## **Перемещение диапазона ячеек на листе**  
В примере кода используется файл-шаблон для демонстрации задачи.  

**Входной файл**  

![todo:image_alt_text](move-range-of-cells-in-a-worksheet_1.png)  

Пожалуйста, ознакомьтесь с созданным файлом с перемещением диапазона A1:B5 в C1:D5.  

**Выходной файл**  

![todo:image_alt_text](move-range-of-cells-in-a-worksheet_2.png)  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xlsx");
// Instantiate the workbook object. Open the Excel file
const workbook = new AsposeCells.Workbook(filePath);

const cells = workbook.getWorksheets().get(0).getCells();

const range = cells.createRange("A1", "B5");
//move the range to right.
range.moveTo(0, 2);
```  

