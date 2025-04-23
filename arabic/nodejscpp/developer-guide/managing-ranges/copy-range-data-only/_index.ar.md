---  
title: نسخ بيانات النطاق فقط باستخدام Node.js عبر C++  
linktitle: نسخ بيانات النطاق فقط  
type: docs  
weight: 600  
url: /ar/nodejs-cpp/copy-range-data-only/  
description: تعلم كيفية نسخ البيانات من مدى خلايا إلى آخر باستخدام Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
في بعض الأحيان، قد تحتاج إلى نسخ البيانات من نطاق خلايا إلى آخر، نسخ البيانات فقط، دون التنسيق. تقدم Aspose.Cells هذه الميزة.  

تقدم هذه المقالة كود عينة تستخدم Aspose.Cells لنسخ نطاق البيانات.  
{{% /alert %}}  

يوضح هذا المثال كيف:  

1. إنشاء دفتر عمل.  
1. إضافة بيانات إلى الخلايا في ورقة العمل الأولى.  
1. إنشاء [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range).  
1. إنشاء [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) object باستخدام سمات التنسيق المحددة.  
1. تطبيق تنسيق النمط على النطاق.  
1. إنشاء نطاق آخر من الخلايا.  
1. نسخ بيانات النطاق الأول إلى هذا النطاق الثاني.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook();

// Get the first Worksheet Cells.
const cells = workbook.getWorksheets().get(0).getCells();

// Fill some sample data into the cells.
for (let i = 0; i < 50; i++) {
for (let j = 0; j < 10; j++) {
cells.get(i, j).putValue(`${i},${j}`);
}
}

// Create a range (A1:D3).
const range = cells.createRange("A1", "D3");

// Create a style object.
const style = workbook.createStyle();
// Specify the font attribute.
style.getFont().setName("Calibri");
// Specify the shading color.
style.setForegroundColor(AsposeCells.Color.Yellow);
style.setPattern(AsposeCells.BackgroundType.Solid);
// Specify the border attributes.
style.getBorders().get(AsposeCells.BorderType.TopBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
style.getBorders().get(AsposeCells.BorderType.TopBorder).setColor(AsposeCells.Color.Blue);
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setColor(AsposeCells.Color.Blue);
style.getBorders().get(AsposeCells.BorderType.LeftBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
style.getBorders().get(AsposeCells.BorderType.LeftBorder).setColor(AsposeCells.Color.Blue);
style.getBorders().get(AsposeCells.BorderType.RightBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
style.getBorders().get(AsposeCells.BorderType.RightBorder).setColor(AsposeCells.Color.Blue);

// Create the style flag object.
const flag1 = new AsposeCells.StyleFlag();
// Implement font attribute
flag1.setFontName(true);
// Implement the shading / fill color.
flag1.setCellShading(true);
// Implement border attributes.
flag1.setBorders(true);
// Set the Range style.
range.applyStyle(style, flag1);

// Create a second range (C10:F12).
const range2 = cells.createRange("C10", "F12");

// Copy the range data only.
range2.copyData(range);

const outputFilePath = path.join(dataDir, "CopyRangeData.out.xlsx");
// Save the excel file.
workbook.save(outputFilePath);
```  

