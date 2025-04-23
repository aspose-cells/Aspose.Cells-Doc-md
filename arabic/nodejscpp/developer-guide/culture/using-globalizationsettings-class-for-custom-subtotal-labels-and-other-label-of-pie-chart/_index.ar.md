---
title: استخدام فئة GlobalizationSettings لتخصيص تسميات المجموع الفرعي والتسميات الأخرى لرسوم بيانية الفطيرة عبر Node.js و C++
linktitle: استخدام فئة GlobalizationSettings لتخصيص علامات مجموع جزئي مخصصة وعلامة أخرى لمخطط البيت
type: docs
weight: 70
url: /ar/nodejs-cpp/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/
description: تعلم كيفية تخصيص تسميات المجموع الفرعي والتسميات الأخرى للرسوم البيانية الفطيرة باستخدام فئة GlobalizationSettings في Aspose.Cells for Node.js via C++.
---

## **سيناريوهات الاستخدام المحتملة**

 قدمت واجهات برمجة التطبيقات Aspose.Cells فئة [**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings) للتعامل مع السيناريوهات التي يرغب فيها المستخدم في استخدام تسميات مخصصة للمجاميع الفرعية في جدول البيانات. علاوة على ذلك، يمكن أيضًا استخدام فئة [**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings) لتعديل تسمية **Other** لرسوم بيانية الفطيرة عند عرض الورقة أو الرسم.

## **مقدمة في فئة GlobalizationSettings**

 تقدم فئة [**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings) حاليًا الطرق الثلاثة التالية التي يمكن تجاوزها في فئة مخصصة للحصول على التسميات المطلوبة للمجاميع الفرعية أو لعرض نص مخصص لتسمية **Other** في رسم فطيرة.

1. [**GlobalizationSettings.getTotalName(ConsolidationFunction)**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/#getTotalName-consolidationfunction-): يحصل على الاسم الكامل للوظيفة.
1. [**GlobalizationSettings.getGrandTotalName(ConsolidationFunction)**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/#getGrandTotalName-consolidationfunction-): يستلم اسم المجموع الكلي للوظيفة.


### **علامات مخصصة للمجاميع الجزئية**

 يمكن استخدام فئة [**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings) لتخصيص تسميات المجموع الفرعي من خلال تجاوز الطرق [**GlobalizationSettings.getTotalName(ConsolidationFunction)**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/#getTotalName-consolidationfunction-) و [**GlobalizationSettings.getGrandTotalName(ConsolidationFunction)**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/#getGrandTotalName-consolidationfunction-) كما هو موضح أدناه.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// Defines a custom class derived from GlobalizationSettings class
class CustomSettings extends AsposeCells.GlobalizationSettings {
// Overrides the GetTotalName method
getTotalName(functionType) {
// Checks the function type used to add the subtotals
switch (functionType) {
// Returns custom value based on the function type used to add the subtotals
case AsposeCells.ConsolidationFunction.Average:
return "AVG";
// Handle other cases as per requirement
default:
return super.getTotalName(functionType);
}
}

// Overrides the GetGrandTotalName method
getGrandTotalName(functionType) {
// Checks the function type used to add the subtotals
switch (functionType) {
// Returns custom value based on the function type used to add the subtotals
case AsposeCells.ConsolidationFunction.Average:
return "GRD AVG";
// Handle other cases as per requirement
default:
return super.getGrandTotalName(functionType);
}
}
}
```

 من أجل إدخال تسميات مخصصة، من الضروري تعيين الخاصية [**WorkbookSettings.getGlobalizationSettings()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getGlobalizationSettings--) إلى مثيل من فئة **CustomSettings** المعرفة أعلاه قبل إضافة المجاميع الفرعية إلى الورقة.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");
// Defines a custom class derived from GlobalizationSettings class
class CustomSettings extends AsposeCells.GlobalizationSettings {
// Overrides the GetTotalName method
getTotalName(functionType) {
// Checks the function type used to add the subtotals
switch (functionType) {
// Returns custom value based on the function type used to add the subtotals
case AsposeCells.ConsolidationFunction.Average:
return "AVG";
// Handle other cases as per requirement
default:
return super.getTotalName(functionType);
}
}

// Overrides the GetGrandTotalName method
getGrandTotalName(functionType) {
// Checks the function type used to add the subtotals
switch (functionType) {
// Returns custom value based on the function type used to add the subtotals
case AsposeCells.ConsolidationFunction.Average:
return "GRD AVG";
// Handle other cases as per requirement
default:
return super.getGrandTotalName(functionType);
}
}
}

try {
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Loads an existing spreadsheet containing some data
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xlsx"));

// Assigns the GlobalizationSettings property of the WorkbookSettings class to a custom class created
workbook.getSettings().setGlobalizationSettings(new CustomSettings());

// Accesses the 1st worksheet from the collection which contains data that resides in the cell range A2:B9
const sheet = workbook.getWorksheets().get(0);

// Adds Subtotal of type Average to the worksheet
sheet.getCells().subtotal(AsposeCells.CellArea.createCellArea("A2", "B9"), 0, AsposeCells.ConsolidationFunction.Average, [1]);

// Calculates Formulas
workbook.calculateFormula();

// Auto fits all columns
sheet.autoFitColumns();

// Saves the workbook on disc
workbook.save(path.join(dataDir, "output_out.xlsx"));
} catch (error) {
console.error(`Test failed: ${error.message}`);
throw error;
}
```

{{% alert color="primary" %}}

 تعمل فئة [**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings) فقط على إضافة مجاميع فرعية جديدة. إذا كانت ورقة البيانات تحتوي على مجاميع فرعية بالفعل، فلا يمكن تعديل تسمياتها.

{{% /alert %}}

