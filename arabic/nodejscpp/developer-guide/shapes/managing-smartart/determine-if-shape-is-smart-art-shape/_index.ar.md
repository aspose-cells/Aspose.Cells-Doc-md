---  
title: تحديد ما إذا كان الشكل هو شكل فن ذكي باستخدام Node.js عبر C++  
linktitle: تحديد ما إذا كانت الشكل شكل رسوم بيانية ذكية  
type: docs  
weight: 400  
url: /ar/nodejs-cpp/determine-if-shape-is-smart-art-shape/  
description: تعلم كيفية تحديد ما إذا كان الشكل في إكسل هو شكل فن ذكي باستخدام Aspose.Cells for Node.js via C++.  
---  

## **سيناريوهات الاستخدام المحتملة**  

أشكال الفن الذكي هي أشكال خاصة في مايكروسوفت إكسل تتيح لك إنشاء مخططات معقدة تلقائياً. يمكنك معرفة ما إذا كان الشكل هو شكل فن ذكي أو شكل عادي باستخدام خاصية [**Shape.isSmartArt()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#isSmartArt--).  

## **تحديد ما إذا كان الشكل هو شكل ذكاء ذكي**  

الرمز المساعد التالي يقوم بتحميل ملف إكسل (sample.xlsx) الذي يحتوي على شكل فن ذكي كما هو موضح في هذه الصورة. ثم يطبع قيمة خاصية [**Shape.isSmartArt()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#isSmartArt--) لأول شكل. يرجى الاطلاع على مخرجات وحدة التحكم للرمز المساعد المقدم أدناه.  

![todo:image_alt_text](determine-if-shape-is-smart-art-shape_1.png)  

## **الكود المثالي**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleSmartArtShape.xlsx");

// Load the sample smart art shape - Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first shape
const shape = worksheet.getShapes().get(0);

// Determine if shape is smart art
console.log("Is Smart Art Shape: " + shape.isSmartArt());
```  

## **مخرجات الوحدة**  

{{< highlight java >}}  

Is Smart Art Shape: True  

{{< /highlight >}}  

{{< app/cells/assistant language="nodejs-cpp" >}}
