---
title: كيفية إضافة PivotChart باستخدام Aspose.Cells for Node.js via C++
linktitle: مخطط محوري
type: docs
weight: 100
url: /ar/nodejs-cpp/how-to-add-pivot-chart/
description: كيفية إضافة PivotChart باستخدام Aspose.Cells for Node.js via C++.
keywords: PivotChart Node.js عبر C++
---
## ما هو PivotChart

المخطط المحوري هو تمثيل بصري للبيانات في جدول محوري. يوفر المخططات المحورية وسيلة لتلخيص، تحليل، استكشاف، وعرض البيانات الملخصة. إليك بعض الميزات والجوانب الرئيسية للمخططات المحورية:

1. تمثيل البيانات ديناميكي: يتم تحديث المخططات المحورية تلقائيًا لتعكس التغييرات في الجدول المحوري. إذا أضفت أو أزلت حقولًا في الجدول، يتم تحديث المخطط المحوري وفقًا لذلك.

1. تفاعلي: المخططات المحورية تفاعلية، تتيح للمستخدمين تصفية وفرز والاستكشاف في البيانات. يسهل ذلك استكشاف جوانب مختلفة من مجموعة البيانات.

1. تصميم مرن: يمكن للمستخدمين تغيير تخطيط مخطط المحور عن طريق سحب وإفلات الحقول، مما يوفر مرونة في كيفية تصور البيانات.

1. أنواع المخططات المختلفة: يمكن إنشاء مخططات Pivot باستخدام أنواع مخططات متنوعة مثل مخططات الأعمدة، الخطوط، الدوائر، والمزيد، اعتمادًا على طبيعة البيانات والرؤى التي ترغب في اكتسابها.

1. التلخيص: تختصر مخططات Pivot كميات كبيرة من البيانات ويمكن أن تعرض الإجماليات، المتوسطات، العدادات، أو إحصاءات مختصرة أخرى.

1. التصفية: توفر قدرات التصفية، مما يسمح لك بعرض البيانات التي تلبي معايير معينة فقط.

<br>
تستخدم مخططات Pivot بشكل شائع في ذكاء الأعمال وتحليل البيانات لتقديم ملخص بصري واضح وملخص لمجموعات البيانات المعقدة. إنها أداة قوية لاتخاذ القرارات المستندة إلى البيانات.

## كيفية إضافة مخطط Pivot باستخدام Aspose.Cells for Node.js via C++

### **إضافة جدول محوري**

لإنشاء جدول محوري باستخدام Aspose.Cells for Node.js via C++:

1. أضف بعض البيانات إلى ورقة عمل باستخدام طريقة `putValue` لكائن الخلية. يمكنك أيضًا استخدام ملف قالب مسبق مملوء بالبيانات. ستُستخدم البيانات كمصدر بيانات لجدول المحوري.
1. أضف جدول محوري إلى ورقة العمل من خلال استدعاء طريقة `add` من مجموعة `PivotTables`.
1. الوصول إلى كائن جدول المحوري الجديد من مجموعة `PivotTables` عن طريق تمرير فهرسه. استخدم أي من كائنات جدول المحوري الموجودة لإدارة الجدول.

تم إعطاء أمثلة الكود أدناه.

```javascript
try {
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
// Obtaining the reference of the first worksheet
const sheet = workbook.getWorksheets().get(0);
// Name the sheet
sheet.setName("Data");
const cells = sheet.getCells();

// Setting the values to the cells
cells.get("A1").putValue("Employee");
cells.get("B1").putValue("Quarter");
cells.get("C1").putValue("Product");
cells.get("D1").putValue("Continent");
cells.get("E1").putValue("Country");
cells.get("F1").putValue("Sale");

const namesAndValues = [
["David", 1, "Maxilaku", "Asia", "China", 2000],
["David", 2, "Maxilaku", "Asia", "India", 500],
["David", 3, "Chai", "Asia", "Korea", 1200],
["David", 4, "Maxilaku", "Asia", "India", 1500],
["James", 1, "Chang", "Europe", "France", 500],
["James", 2, "Chang", "Europe", "France", 1500],
["James", 3, "Chang", "Europe", "Germany", 800],
["James", 4, "Chang", "Europe", "Italy", 900],
["James", 4, "Chang", "Europe", "France", 500],
["Miya", 1, "Geitost", "America", "U.S.", 1600],
["Miya", 2, "Chai", "America", "U.S.", 600],
["Miya", 3, "Geitost", "America", "Brazil", 2000],
["Miya", 2, "Geitost", "America", "U.S.", 500],
["Miya", 3, "Maxilaku", "America", "Canada", 900],
["Miya", 4, "Geitost", "America", "U.S.", 700],
["Miya", 5, "Geitost", "America", "U.S.", 1400],
["Miya", 6, "Ikuru", "Europe", "Italy", 1350],
["Miya", 7, "Ikuru", "Europe", "France", 300],
["Miya", 8, "Ikuru", "Europe", "Italy", 500],
["Miya", 9, "Ikuru", "America", "New Zealand", 1000],
["Miya", 10, "Ipoh Coffee", "Oceania", "Australia", 1500],
["Miya", 11, "Chocolade", "Oceania", "Australia", 500],
["Miya", 12, "Chocolade", "Oceania", "New Zealand", 1500],
["Miya", 13, "Chocolade", "Oceania", "S.Africa", 1600],
["Miya", 14, "Chocolade", "Africa", "Egypt", 1000],
["Miya", 15, "Chocolade", "Africa", "Egypt", 1200],
["Miya", 16, "Chocolade", "Africa", "Egypt", 1300],
];

namesAndValues.forEach((item, index) => {
const rowIndex = index + 2;
cells.get(`A${rowIndex}`).putValue(item[0]);
cells.get(`B${rowIndex}`).putValue(item[1]);
cells.get(`C${rowIndex}`).putValue(item[2]);
cells.get(`D${rowIndex}`).putValue(item[3]);
cells.get(`E${rowIndex}`).putValue(item[4]);
cells.get(`F${rowIndex}`).putValue(item[5]);
```

### **إضافة رسم بياني دوراني**

لإنشاء مخطط Pivot باستخدام Aspose.Cells for Node.js via C++:

1. أضف رسم بياني.
1. اضبط `PivotSource` المخطط للإشارة إلى جدول محوري موجود في ورقة العمل.
1. قم بتعيين سمات أخرى.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating an Workbook object
// Opening the excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "pivotTable_test.xlsx"));
// Adding a new sheet
const sheetIndex = workbook.getWorksheets().add(AsposeCells.SheetType.Chart);
const sheet3 = workbook.getWorksheets().get(sheetIndex);
sheet3.setName("PivotChart");
// Adding a column chart
const index = sheet3.getCharts().add(AsposeCells.ChartType.Column, 0, 5, 28, 16);
// Setting the pivot chart data source
sheet3.getCharts().get(index).setPivotSource("PivotTable!PivotTable1");
sheet3.getCharts().get(index).setHidePivotFieldButtons(false);
// Saving the Excel file
workbook.save(path.join(dataDir, "pivotChart_test_out.xlsx"));
```

{{< app/cells/assistant language="nodejs-cpp" >}}
