---
title: إرسال شكل في مقدمة أو خلفية داخل ورقة العمل باستخدام Node.js عبر C++
linktitle: إرسال الشكل إلى الأمام أو الوراء داخل ورقة العمل
type: docs
weight: 3400
url: /ar/nodejs-cpp/send-shape-front-or-back-inside-the-worksheet/
description: تعلم كيفية إرسال شكل إلى الأمام أو الخلف في ورقة العمل باستخدام Aspose.Cells for Node.js via C++. 
---

## **سيناريوهات الاستخدام المحتملة**

عندما تتواجد أشكال متعددة في نفس الموقع، يتم تحديد رؤيتها حسب مواقع ترتيب z. توفر Aspose.Cells طريقة [**Shape.toFrontOrBack()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#toFrontOrBack-number-)، التي تغير موضع ترتيب z للشكل. لإرسال شكل إلى الخلف، ستستخدم رقمًا سالبًا مثل -1، -2، -3، وهكذا، ولإحضار شكل إلى الأمام، ستستخدم رقمًا موجبًا مثل 1، 2، 3، وهكذا.

## **إرسال الشكل إلى الأمام أو الوراء داخل ورقة العمل**

يوضح رمز العينة التالي استخدام طريقة [**Shape.toFrontOrBack()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#toFrontOrBack-number-). الرجاء مراجعة ملف Excel النموذجي (50528330.xlsx) المستخدم في الكود وملف Excel الناتج (50528331.xlsx) الذي تم إنشاؤه به. تُظهر لقطة الشاشة تأثير الكود على ملف Excel النموذجي عند التشغيل.

![todo:image_alt_text](send-shape-front-or-back-inside-the-worksheet_1.png)

## **الكود المثالي**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceFilePath = path.join(dataDir, "sampleToFrontOrBack.xlsx");

// Load source Excel file
const workbook = new AsposeCells.Workbook(sourceFilePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first and fourth shape
const shape1 = worksheet.getShapes().get(0);
const shape4 = worksheet.getShapes().get(3);

// Print the Z-Order position of the shape
console.log("Z-Order Shape 1: " + shape1.getZOrderPosition());

// Send this shape to front
shape1.toFrontOrBack(2);

// Print the Z-Order position of the shape
console.log("Z-Order Shape 4: " + shape4.getZOrderPosition());

// Send this shape to back
shape4.toFrontOrBack(-2);

// Save the output Excel file
const outputFilePath = path.join(dataDir, "outputToFrontOrBack.xlsx");
workbook.save(outputFilePath);
```
