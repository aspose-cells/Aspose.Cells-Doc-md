---  
title: Tile Picture as a Texture inside the Shape with Node.js via C++  
linktitle: صورة البلاط كقشرة داخل الشكل  
type: docs  
weight: 1700  
url: /ar/nodejs-cpp/tile-picture-as-a-texture-inside-the-shape/  
description: تعلم كيفية تجانس صورة صغيرة كملمس داخل شكل باستخدام Aspose.Cells for Node.js via C++.  
---  

## **سيناريوهات الاستخدام المحتملة**  

عندما تكون الصورة صغيرة ولا تغطي السطح بأكمله للشكل دون فقدان جودتها ، فإن لديك خيار تبطينها. يملأ التبطين سطح الشكل بصورة صغيرة عن طريق تكرارها كما لو أنها بلاط.  

## **صورة البلاط كقشرة داخل الشكل**  

يمكنك ملء سطح الشكل بصورة محددة وتجانسها باستخدام خاصية [**Shape.isTiling()**](https://reference.aspose.com/cells/nodejs-cpp/texturefill/#isTiling--) وتعيينها إلى **true**. يرجى مراجعة الكود النموذجي التالي، وملف Excel النموذجي ([ملف Excel](46465050.xlsx))، والصورة المصغرة كمثال.  

## **لقطة شاشة**  

![todo:image_alt_text](tile-picture-as-a-texture-inside-the-shape_1.png)  

## **الكود المثالي**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Load sample Excel file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleTextureFill_IsTiling.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first shape inside the worksheet
const shape = worksheet.getShapes().get(0);

// Tile Picture as a Texture inside the Shape 
shape.getFill().getTextureFill().setIsTiling(true);

// Save the output Excel file
workbook.save(path.join(outputDir, "outputTextureFill_IsTiling.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
