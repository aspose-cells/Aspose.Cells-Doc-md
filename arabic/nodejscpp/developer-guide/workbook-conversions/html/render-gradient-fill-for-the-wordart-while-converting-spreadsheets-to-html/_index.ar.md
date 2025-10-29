---  
title: عرض تدرج التعبئة لنص WordArt أثناء تحويل أوراق العمل إلى HTML باستخدام Node.js عبر C++  
linktitle: عرض تعبئة التدرج لـ WordArt أثناء تحويل جداول البيانات إلى صيغة HTML  
type: docs  
weight: 90  
url: /ar/nodejs-cpp/render-gradient-fill-for-the-wordart-while-converting-spreadsheets-to/  
description: تعلم كيفية عرض تدرج التعبئة لنص WordArt عند تحويل أوراق العمل إلى HTML باستخدام Aspose.Cells for Node.js via C++.  
---  

## **سيناريوهات الاستخدام المحتملة**  
قبل إصدار Aspose.Cells 17.1، لم يكن يدعم عرض تدرج ملء WordArt عند تحويل ملف إكسل إلى تنسيق HTML. منذ إصدار Aspose.Cells 17.1، يُدعم تدرج ملء WordArt. تُقارن لقطة الشاشة التالية تأثير التدرج عند تحويل ملف إكسل باستخدام Aspose.Cells 17.1 والإصدار الأقدم.  

![todo:image_alt_text](render-gradient-fill-for-the-wordart-while-converting-spreadsheets-to-html_1.png)  

## **عرض تعبئة التدرج لكلمة WordArt أثناء تحويل جداول البيانات إلى صيغة HTML**  
يُحوِّل الكود النموذجي التالي [ملف الإكسل المصدر](22774111.xlsx) إلى [صيغة HTML المخرجة](22774109.zip) إنّ مصدر ملف الإكسل يتضمن كائن WordArt مع تدرج ملء كما هو موضح في لقطة الشاشة أعلاه.  

## **الكود المثالي**  
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sourceGradientFill.xlsx");

// Read the source excel file having text with gradient fill
const workbook = new AsposeCells.Workbook(filePath);

// Save workbook to html format
workbook.save(path.join(dataDir, "out_sourceGradientFill.html"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
