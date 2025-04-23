---
title: تدوير النص مع الشكل داخل ورقة العمل باستخدام Node.js عبر C++
linktitle: تدوير النص مع الشكل داخل ورقة العمل
type: docs
weight: 1300
url: /ar/nodejs-cpp/rotate-text-with-shape-inside-the-worksheet/
description: تعلم كيف تدور النص مع الشكل داخل ورقة العمل في إكسل باستخدام Aspose.Cells for Node.js via C++.
---

## **سيناريوهات الاستخدام المحتملة**

يمكنك إضافة نص داخل أي شكل باستخدام مايكروسوفت إكسل. إذا أضفت شكلاً باستخدام إصدار مايكروسوفت إكسل 2003 القديم جداً، فلن يدور النص مع الشكل. ولكن إذا أضفت شكلاً باستخدام إصدارات أحدث من مايكروسوفت إكسل مثل 2007، 2010، 2013 أو 2016، فسيتم تدوير النص مع الشكل. يمكنك التحكم في ما إذا كان النص ينبغي أن يدور مع الشكل أم لا باستخدام خاصية [**ShapeTextAlignment.getRotateTextWithShape()**](https://reference.aspose.com/cells/nodejs-cpp/shapetextalignment/#getRotateTextWithShape--). القيمة الافتراضية لها هي **true**، مما يعني أن النص سيدور مع الشكل، ولكن إذا قمت بضبطها على **false**، فلن يدور النص مع الشكل.

## **تدوير النص مع الشكل داخل ورقة العمل**

يحمّل الكود النموذجي التالي ملف إكسل عينة الذي يحتوي على شكل مثلث والنص يتغير مع دوران الشكل. عند فتح الملف في إكسل، ودوران الشكل، سيدور النص معه. ثم يتم ضبط خاصية [**ShapeTextAlignment.getRotateTextWithShape()**](https://reference.aspose.com/cells/nodejs-cpp/shapetextalignment/#getRotateTextWithShape--) على **false** ويحفظ الملف باسم ملف إكسل الناتج. عند فتح الملف الناتج في إكسل، ودوران الشكل، لن يدور النص معه. الرجاء الاطلاع على لقطة الشاشة التالية التي تظهر تأثير الكود على ملف الإكسل العينة كمرجع.

![todo:image_alt_text](rotate-text-with-shape-inside-the-worksheet_1.png)

## **الكود المثالي**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceFilePath = path.join(dataDir, "sampleRotateTextWithShapeInsideWorksheet.xlsx");

// Load sample Excel file.
const workbook = new AsposeCells.Workbook(sourceFilePath);

// Access first worksheet.
const worksheet = workbook.getWorksheets().get(0);

// Access cell B4 and add message inside it.
const cellB4 = worksheet.getCells().get("B4");
cellB4.putValue("Text is not rotating with shape because RotateTextWithShape is false.");

// Access first shape.
const shape = worksheet.getShapes().get(0);

// Access shape text alignment.
const shapeTextAlignment = shape.getTextBody().getTextAlignment();

// Do not rotate text with shape by setting RotateTextWithShape as false.
shapeTextAlignment.setRotateTextWithShape(false);

// Save the output Excel file.
const outputFilePath = path.join(dataDir, "outputRotateTextWithShapeInsideWorksheet.xlsx");
workbook.save(outputFilePath);
```
