---  
title: استبدال النص في الفن الذكي باستخدام Node.js عبر C++  
linktitle: استبدال النص في شكل ذكاء ذكي  
type: docs  
weight: 1200  
url: /ar/nodejs-cpp/replace-text-in-smart-art/  
description: تعلم كيفية استبدال النص في الفن الذكي باستخدام Aspose.Cells for Node.js via C++.  
---  

## **سيناريوهات الاستخدام المحتملة**  

الفن الذكي هو أحد الكائنات الرئيسية في دفتر العمل. في كثير من الأحيان، هناك حاجة لتحديث النص في الفن الذكي. يوفر Aspose.Cells for Node.js via C++ هذه الميزة من خلال ضبط الخاصية [**Shape.getText()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getText--).  

يمكن تنزيل ملف المصدر من الرابط التالي:  

[SmartArt.xlsx](77496338.xlsx)  

## **الكود المثالي**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceFilePath = path.join(dataDir, "SmartArt.xlsx");

// Loads the workbook which contains hidden external links
const wb = new AsposeCells.Workbook(sourceFilePath);

const worksheets = wb.getWorksheets();
for (let i = 0; i < worksheets.getCount(); i++) 
{
const worksheet = worksheets.get(i);
const shapes = worksheet.getShapes();
for (let j = 0; j < shapes.getCount(); j++) 
{
const shape = shapes.get(j);
shape.setAlternativeText("ReplacedAlternativeText"); // This works fine just as the normal Shape objects do.
if (shape.isSmartArt()) 
{
const smartArtShapes = shape.getResultOfSmartArt().getGroupedShapes();
for (let k = 0; k < smartArtShapes.length; k++) 
{
const smartart = smartArtShapes[k];
smartart.setText("ReplacedText"); // This doesn't update the text in Workbook which I save to the another file.
}
}
}
}

const options = new AsposeCells.OoxmlSaveOptions();
options.setUpdateSmartArt(true);
const outputFilePath = path.join(dataDir, "outputSmartArt.xlsx");
wb.save(outputFilePath, options);
```  

