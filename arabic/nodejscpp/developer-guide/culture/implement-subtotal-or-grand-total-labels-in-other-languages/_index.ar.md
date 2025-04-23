---  
title: تنفيذ تسميات Subtotal أو Grand Total بلغات أخرى باستخدام Node.js عبر C++  
linktitle: تنفيذ تسميات Subtotal أو Grand Total بلغات أخرى  
type: docs  
weight: 50  
url: /ar/nodejs-cpp/implement-subtotal-or-grand-total-labels-in-other-languages/  
---  

## **سيناريوهات الاستخدام المحتملة**  

أحيانًا، ترغب في عرض تسميات المجموع الفرعي والإجمالي النهائي بلغات غير الإنجليزية مثل الصينية، اليابانية، العربية، الهندية، وغيرها. يسمح لك Aspose.Cells for Node.js via C++ بفعل ذلك باستخدام فئة [**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings) وخصائص [**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/). يرجى مراجعة هذه المقالة لمعرفة كيفية استخدام فئة [**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings).  

- [استخدام فئة GlobalizationSettings لتحديد تسميات الإجمالي الفرعي المخصصة وتسمية أخرى لمخطط القطاع](/cells/ar/nodejs-cpp/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/)  

## ** تنفيذ تسميات Subtotal أو Grand Total بلغات أخرى**  

 يحمّل الكود النموذجي التالي ملف Excel [العينة](5115151.xlsx) ويُنفذ أسماء المجموع الفرعي والإجمالي النهائي باللغة الصينية. يرجى مراجعة ملف Excel الناتج [5115152.xlsx] الذي يُولده هذا الكود للمرجعية. نقوم أولاً بإنشاء فئة من [**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings) ثم نستخدمها في الكود الخاص بنا.  

```javascript
const AsposeCells = require("aspose.cells.node");

class GlobalizationSettingsImp extends AsposeCells.GlobalizationSettings {
// This function will return the sub total name
getTotalName(functionType) {
return "Chinese Total - 可能的用法";
}

// This function will return the grand total name
getGrandTotalName(functionType) {
return "Chinese Grand Total - 可能的用法";
}
}
```  

الآن استخدم الفئة التي أنشأتها أعلاه في الكود كما يلي:  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Load your source workbook
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xlsx"));

// Set the globalization setting to change subtotal and grand total names
const globalizationSettings = new AsposeCells.GlobalizationSettings();
workbook.getSettings().setGlobalizationSettings(globalizationSettings);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Apply subtotal on A1:B10
const cellArea = AsposeCells.CellArea.createCellArea("A1", "B10");
worksheet.getCells().subtotal(cellArea, 0, AsposeCells.ConsolidationFunction.Sum, [2, 3, 4]);

// Set the width of the first column
worksheet.getCells().setColumnWidth(0, 40);

// Save the output excel file
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

