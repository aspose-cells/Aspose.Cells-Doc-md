---  
title: رسم المخطط الزمني أثناء تحويل Excel إلى PDF باستخدام Node.js عبر C++  
linktitle: رسم الجدول الزمني أثناء تحويل إكسيل إلى PDF  
type: docs  
weight: 60  
url: /ar/nodejs-cpp/draw-timeline-while-rendering-excel-to-pdf/  
description: إدارة جداول زمنية لملفات Excel مع Aspose.Cells for Node.js via C++.  
keywords: تحويل المخطط الزمني إلى PDF بدون Office 2013، Office 2016، Office 2019 وOffice 365 باستخدام Node.js عبر C++  
---  

## **رسم الجدول الزمني أثناء تحويل Excel إلى PDF**  
إذا كان لديك ملف Excel مضاف إليه جدول زمني وترغب في تصديره إلى PDF مع إعدادات الجدول الزمني، يدعم Aspose.Cells for Node.js via C++ ذلك الآن بشكل افتراضي. ببساطة صدّر ملف Excel مع جدول زمني إلى PDF، وسيظهر ملف PDF الناتج الجدول الزمني المطبق.  

الكود النموذجي التالي يحمل [ملف Excel عيني](input.xlsx) الذي يحتوي على جدول زمني موجود. ثم يحفظ المصنف كـ [ملف PDF الناتج](out.pdf). اللقطة الشاشية التالية تقارن ملف Excel المصدر بالملف PDF المعدل.  

<img src="out.png" width="60%">  

## **الكود المثالي**  
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "input.xlsx");
// Load sample Excel file
const workbook = new AsposeCells.Workbook(filePath);
// Save file to pdf
workbook.save("out.pdf", AsposeCells.SaveFormat.Pdf);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
