---  
title: نسخ بيانات النطاق مع نمط باستخدام Node.js عبر C++  
linktitle: نسخ بيانات النطاق مع النمط  
type: docs  
weight: 610  
url: /ar/nodejs-cpp/copy-range-data-with-style/  
description: تعلم كيفية نسخ مجموعة من الخلايا مع التنسيق باستخدام Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

[نسخ بيانات النطاق فقط](/cells/ar/nodejs-cpp/copy-range-data-only/) شرح كيفية نسخ البيانات من مدى خلايا إلى آخر. على وجه التحديد، يطبق مجموعة جديدة من الأنماط على الخلايا المنسوخة. يمكن لـ Aspose.Cells أيضًا نسخ نطاق كامل مع التنسيق. يوضح هذا المقال كيفية ذلك.  

{{% /alert %}}  

 توفر Aspose.Cells مجموعة من الفئات والطرق للعمل مع النطاقات، على سبيل المثال، [**createRange(string, string)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#createRange-string-string-)، [**StyleFlag**](https://reference.aspose.com/cells/nodejs-cpp/styleflag/) و [**applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#applyStyle-style-styleflag-).  

هذا المثال:  

1. ينشئ دفتر عمل.  
2. يملأ عددًا من الخلايا في الورقة الأولى بالبيانات.  
3. ينشئ [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range/).  
4. ينشئ كائن [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style/) بصفات تنسيق محددة.  
5. يطبق النمط على مدى البيانات.  
6. ينشئ مدى ثاني من الخلايا.  
7. ينسخ البيانات مع التنسيق من النطاق الأول إلى النطاق الثاني.  

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
for (let i = 0; i < 50; i++)
{
for (let j = 0; j < 10; j++) 
{
cells.get(i, j).putValue(`${i},${j}`);
}
}

// Create a range (A1:D3).
const range = cells.createRange("A1", "D3");

// Create a style object.
let style = workbook.createStyle();
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

// Create the styleflag object.
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

// Copy the range data with formatting.
range2.copy(range);

const outputFilePath = path.join(dataDir, "CopyRange.out.xlsx");
// Save the excel file.
workbook.save(outputFilePath);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
