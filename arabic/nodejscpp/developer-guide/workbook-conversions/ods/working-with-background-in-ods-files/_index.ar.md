---  
title: العمل مع الخلفية في ملفات ODS مع Node.js عبر C++  
linktitle: العمل مع الخلفية في ملفات ODS  
type: docs  
weight: 150  
url: /ar/nodejs-cpp/working-with-background-in-ods-files/  
description: تعلم كيفية إدارة الخلفيات في ملفات ODS باستخدام Aspose.Cells for Node.js via C++.  
---  

## **الخلفية في ملفات ODS**  

يمكن إضافة خلفية إلى الأوراق في ملفات ODS. يمكن أن تكون الخلفية خلفية ملونة أو خلفية رسومية. الخلفية ليست مرئية عند فتح الملف ولكن إذا تمت طباعة الملف كملف PDF، فإن الخلفية مرئية في الملف PDF الناتج. الخلفية أيضًا مرئية في حوار معاينة الطباعة.  

 توفر Aspose.Cells for Node.js via C++ القدرة على قراءة معلومات الخلفية وإضافة الخلفية في ملفات ODS.  

## **قراءة معلومات الخلفية من ملف ODS**  

 توفر Aspose.Cells for Node.js via C++ فئة [**OdsPageBackground**](https://reference.aspose.com/cells/nodejs-cpp/odspagebackground) لإدارة الخلفية في ملفات ODS. يوضح مثال الكود التالي استخدام فئة [**OdsPageBackground**](https://reference.aspose.com/cells/nodejs-cpp/odspagebackground) بتحميل ملف مصدر ODS وقراءة معلومات الخلفية. يرجى مراجعة المخرجات المعروضة في وحدة التحكم كمصدر مرجعي.  

### **الكود المثالي**  

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// Source and output directories
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Load source Excel file
const filePath = path.join(sourceDir, "GraphicBackground.ods");
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

const background = worksheet.getPageSetup().getODSPageBackground();

console.log("Background Type: " + background.getType().toString());
console.log("Background Position: " + background.getGraphicPositionType().toString());

// Save background image
const imagePath = outputDir + "background.jpg";
fs.writeFileSync(imagePath, Buffer.from(background.getGraphicData()));
```  

### **مخرجات الوحدة**  

{{< highlight javascript >}}  
Background Type: Graphic  
Background Position: CenterCenter  
{{< /highlight >}}  

## **إضافة خلفية ملونة إلى ملف ODS**  

 توفر Aspose.Cells for Node.js via C++ فئة [**OdsPageBackground**](https://reference.aspose.com/cells/nodejs-cpp/odspagebackground) لإدارة الخلفية في ملفات ODS. يوضح المثال التالي استخدام الخاصية [**OdsPageBackground.getColor()**](https://reference.aspose.com/cells/nodejs-cpp/odspagebackground/#getColor--) لإضافة خلفية لون إلى ملف ODS. يرجى مراجعة ملف [الإخراج ODS](90112031.ods) الناتج عن الكود للمرجعية.  

### **الكود المثالي**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

worksheet.getCells().get(0, 0).putValue(1);
worksheet.getCells().get(1, 0).putValue(2);
worksheet.getCells().get(2, 0).putValue(3);
worksheet.getCells().get(3, 0).putValue(4);
worksheet.getCells().get(4, 0).putValue(5);
worksheet.getCells().get(5, 0).putValue(6);
worksheet.getCells().get(0, 1).putValue(7);
worksheet.getCells().get(1, 1).putValue(8);
worksheet.getCells().get(2, 1).putValue(9);
worksheet.getCells().get(3, 1).putValue(10);
worksheet.getCells().get(4, 1).putValue(11);
worksheet.getCells().get(5, 1).putValue(12);

const background = worksheet.getPageSetup().getODSPageBackground();

background.setColor(AsposeCells.Color.Azure);
background.setType(AsposeCells.OdsPageBackgroundType.Color);

workbook.save(outputDir + "ColoredBackground.ods", AsposeCells.SaveFormat.Ods);
```  

## **إضافة خلفية رسومية إلى ملف ODS**  

 توفر Aspose.Cells for Node.js via C++ فئة [**OdsPageBackground**](https://reference.aspose.com/cells/nodejs-cpp/odspagebackground) لإدارة الخلفية في ملفات ODS. يوضح المثال التالي استخدام الخاصية [**OdsPageBackground.getGraphicData()**](https://reference.aspose.com/cells/nodejs-cpp/odspagebackground/#getGraphicData--) لإضافة خلفية رسومية إلى ملف ODS. يرجى مراجعة ملف [الإخراج ODS](90112030.ods) الناتج عن الكود للمرجعية.  

### **الكود المثالي**  

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

worksheet.getCells().get(0, 0).putValue(1);
worksheet.getCells().get(1, 0).putValue(2);
worksheet.getCells().get(2, 0).putValue(3);
worksheet.getCells().get(3, 0).putValue(4);
worksheet.getCells().get(4, 0).putValue(5);
worksheet.getCells().get(5, 0).putValue(6);
worksheet.getCells().get(0, 1).putValue(7);
worksheet.getCells().get(1, 1).putValue(8);
worksheet.getCells().get(2, 1).putValue(9);
worksheet.getCells().get(3, 1).putValue(10);
worksheet.getCells().get(4, 1).putValue(11);
worksheet.getCells().get(5, 1).putValue(12);

const background = worksheet.getPageSetup().getODSPageBackground();

background.setType(AsposeCells.OdsPageBackgroundType.Graphic);
background.setGraphicData(fs.readFileSync(path.join(sourceDir, "background.jpg")));
background.setGraphicType(AsposeCells.OdsPageBackgroundGraphicType.Area);

workbook.save(outputDir + "GraphicBackground.ods", AsposeCells.SaveFormat.Ods);
```  

