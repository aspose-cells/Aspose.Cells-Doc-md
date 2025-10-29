---  
title: كيفية تعيين نقطة كإجمالي باستخدام Node.js عبر C++  
linktitle: كيفية تعيين نقطة كمجموع  
description: تعلم كيفية تعيين النقاط كمجموع في مخططات WaterFall باستخدام Aspose.Cells for Node.js via C++.  
keywords: مخطط WaterFall، نقطة، تعيين كمجموع، Node.js عبر C++  
type: docs  
weight: 72  
url: /ar/nodejs-cpp/how-to-set-point-as-total/  
---  

## ما هو "تعيين نقطة كمجموع" في مخطط إكسل

في بعض مخططات إكسل، مثل مخطط WaterFall، تكون بعض نقاط البيانات مجموع النقاط السابقة، وقد تحتاج إلى "تعيين نقطة كمجموع". سنوضح رمز النموذج والتوضيح أدناه.

## يحتاج مخطط WaterFall إلى "تعيين نقطة كمجموع" 

![todo:image_alt_text](set-as-total1.png)

يعرض هذا الصورة مخطط WaterFall في إكسل. نرى أن هناك أربع نقاط بيانات تبدأ بـ "مجموع"، وتُستخدم لحساب جميع النقاط السابقة. في هذه الصورة، الإعدادات ليست صحيحة تمامًا. عندما نختار نقطة "مجموع 2024"، نلاحظ أن خيار "تعيين كإجمالي" غير محدد في إكسل. مرفق أدناه ملف إكسل النموذجي الذي يحتاج إلى تعديل، وسنستخدم Aspose.Cells for Node.js via C++ لضبطه بشكل صحيح.

## استخدام Aspose.Cells for Node.js via C++ لتعيين نقطة كمجموع 

نستخدم الكود التالي لضبط الملف بشكل صحيح:

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "SampleSheet.xlsx");

const workbook = new AsposeCells.Workbook(filePath);
const worksheet = workbook.getWorksheets().get(0);
const chart = worksheet.getCharts().get("Graphiq5");

// set some points as total column 
// In this example, we set points 0, 4, 8, 12 as total
chart.getNSeries().get(0).getLayoutProperties().setSubtotals([0, 4, 8, 12]);
workbook.save(path.join(dataDir, "output.xlsx"));
```

يمكنك الحصول على [ملف الناتج الصحيح](output.xlsx) التالي

كما هو موضح في الشكل أدناه، تم ضبط النقاط الأربعة "مجموع" بشكل صحيح، ويمكنك رؤية الفرق عن المخطط السابق.

![todo:image_alt_text](set-as-total2.png)  
{{< app/cells/assistant language="nodejs-cpp" >}}
