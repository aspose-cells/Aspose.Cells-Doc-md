---  
title: تحديد الأرقام المهمة التي سيتم تخزينها في ملف Excel باستخدام Node.js عبر C++  
linktitle: تحديد الأرقام البارزة التي يجب تخزينها في ملف Excel  
type: docs  
weight: 30  
url: /ar/nodejs-cpp/specifying-significant-digits-to-be-stored-in-excel-file/  
description: تعلّم كيفية تحديد الأرقام المهمة التي سيتم تخزينها في ملف Excel باستخدام Aspose.Cells for Node.js via C++.  
---  

## **سيناريوهات الاستخدام المحتملة**  

افتراضيًا، يخزن Aspose.Cells for Node.js via C++ 17 رقمًا مهمًا من القيم المزدوجة داخل ملف Excel، على عكس MS-Excel الذي يخزن فقط 15 رقمًا مهمًا. يمكنك تغيير السلوك الافتراضي لـ Aspose.Cells من 17 رقمًا مهمًا إلى 15 باستخدام الخاصية [**CellsHelper.getSignificantDigits()**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#getSignificantDigits--).  

## **تحديد عدد الأرقام المعنوية التي سيتم تخزينها في ملف Excel**  

يعرض رمز النموذج التالي كيف يُجبر Aspose.Cells على استخدام 15 رقمًا مهمًا أثناء تخزين القيم المزدوجة داخل ملف Excel. تحقق من [ملف الإكسل الناتج](22774105.xlsx). غيّر امتداده إلى .zip وفك ضغطه، سترى أن 15 رقمًا مهمًا فقط مخزن داخل ملف الإكسل. يوضح لقطة الشاشة التالية تأثير خاصية [**CellsHelper.getSignificantDigits()**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#getSignificantDigits--) على ملف الإكسل الناتج.  

![todo:image_alt_text](specifying-significant-digits-to-be-stored-in-excel-file_1.png)  

## **الكود المثالي**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// By default, Aspose.Cells stores 17 significant digits unlike
// MS-Excel which stores only 15 significant digits
AsposeCells.CellsHelper.setSignificantDigits(15);

// Create workbook
const workbook = new AsposeCells.Workbook();

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access cell A1
const c = worksheet.getCells().get("A1");

// Put double value, only 15 significant digits as specified by
// CellsHelper.SignificantDigits above will be stored in excel file just like MS-Excel does
c.putValue(1234567890.123451711);

// Save the workbook
workbook.save(path.join(dataDir, "out_SignificantDigits.xlsx"));
```  

