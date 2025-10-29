---  
title: تحديد الحد الأقصى لصفوف الصيغة المشتركة باستخدام Node.js عبر C++  
linktitle: كما يمكن استخدام الخاصية {0} لتحديد الصفوف القصوى للصيغة المشتركة.  
type: docs  
weight: 40  
url: /ar/nodejs-cpp/specify-maximum-rows-of-shared-formula/  
description: تعلم كيفية تحديد الحد الأقصى لصفوف الصيغ المشتركة باستخدام Aspose.Cells for Node.js via C++.  
---  

## **سيناريوهات الاستخدام المحتملة**  

الحد الأقصى الافتراضي لصفوف الصيغة المشتركة هو 64. يمكن أن يكون أي رقم مثل 1000. تتغير أداء الصيغة المشتركة مع اختلاف عدد الصفوف. لذلك، يوفر Aspose.Cells الخاصية [**WorkbookSettings.getMaxRowsOfSharedFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getMaxRowsOfSharedFormula--) التي يمكن استخدامها لتحديد الحد الأقصى لصفوف الصيغة المشتركة. سيتم تقسيم الصيغة المشتركة إلى عدة صيغ مشتركة إذا كان إجمالي صفوفها أكبر من ذلك، كما هو موضح في لقطة الشاشة التالية.  

![todo:image_alt_text](specify-maximum-rows-of-shared-formula_1.png)  

## **تحديد الصفوف القصوى للصيغة المشتركة**  

يفسر الرمز النموذجي التالي استخدام الخاصية [**WorkbookSettings.getMaxRowsOfSharedFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getMaxRowsOfSharedFormula--). حيث يحدد الحد الأقصى لصفوف الصيغة المشتركة إلى 5 ويضيف الصيغة المشتركة في الخلية D1 لعشرة صفوف ويحفظها إلى [ملف إكسل الناتج](61767856.xlsx). إذا قمت باستخراج محتويات الملف وفحص *sheet1.xml*، سترى أن الصيغة المشتركة تنقسم بعد كل 5 صفوف كما هو موضح في لقطة الشاشة السابقة.  

## **الكود المثالي**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Create a new workbook
const wb = new AsposeCells.Workbook();

// Set the max rows of shared formula to 5
wb.getSettings().setMaxRowsOfSharedFormula(5);

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Access cell D1
const cell = ws.getCells().get("D1");

// Set the shared formula in 100 rows
cell.setSharedFormula("=Sum(A1:A2)", 100, 1);

// Save the output Excel file
wb.save("outputSpecifyMaximumRowsOfSharedFormula.xlsx");
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
