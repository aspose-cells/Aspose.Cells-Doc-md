---
title: استخدام خطوط الفاصل وتنسيقات الإعدادات بطريقة ثلاثية الأبعاد مع Node.js عبر C++
linktitle: استخدام الشرائط وإعدادات تنسيق ثلاثي الأبعاد
type: docs
weight: 40
url: /ar/nodejs-cpp/using-sparklines-and-settings-3d-format/
description: تعلم كيفية استخدام خطوط الفاصل وتطبيق التنسيق الثلاثي الأبعاد في ملفات إكسل باستخدام Aspose.Cells for Node.js via C++. 
---

## **استخدام الشرائط**
يمكن لبرنامج Microsoft Excel 2010 تحليل المعلومات بطرق أكثر من أي وقت مضى. يسمح للمستخدمين بتتبع وتسليط الضوء على اتجاهات البيانات المهمة باستخدام أدوات تحليل البيانات والرؤية الجديدة. الشرائط هي رسومات مصغرة يمكنك وضعها داخل الخلايا بحيث يمكنك عرض البيانات والرسم البياني على الجدول نفسه. عند استخدام الشرائط بشكل صحيح، يكون تحليل البيانات أسرع وأكثر دقة. كما أنها توفر رؤية بسيطة للمعلومات، مما يجنب ورقات العمل المزدحمة بالرسوم البيانية الكثيرة.

يوفر Aspose.Cells for Node.js via C++ API للتلاعب بخطوط الفاصل في جداول البيانات.
### **الشرائط في Microsoft Excel**
لإدراج الشرائط في Microsoft Excel 2010:

1. حدد الخلايا التي ترغب في ظهور الشرائط فيها. لجعلها سهلة الرؤية، حدد الخلايا على جانب البيانات.
1. انقر على **Insert** في الشريط واختر **column** في **Sparklines**.
1. حدد أو أدخل نطاق الخلايا في ورقة العمل التي تحتوي على البيانات. ستظهر الرسوم البيانية.

تساعد الشرائط في رؤية الاتجاهات، على سبيل المثال، سجل الفوز أو الخسارة لدوري الكرة اللينة. يمكن للشرائط حتى الإشارة إلى مجموع الموسم بأكمله لكل فريق في الدوري.
### **شفرات خطوط الفاصل باستخدام Aspose.Cells for Node.js via C++**
يمكن للمطورين إنشاء أو حذف أو قراءة خطوط الفاصل (في ملف القالب) باستخدام API المقدم من Aspose.Cells for Node.js via C++. تحتوي الفئات التي تدير خطوط الفاصل على وحدة [SparklineGroupCollection](https://reference.aspose.com/cells/nodejs-cpp/sparklinegroupcollection/)، لذلك تحتاج إلى استيراد هذه الوحدة قبل استخدام هذه الميزات.

من خلال إضافة رسومات مخصصة لنطاق البيانات المعطى، يحصل المطورون على حرية إضافة أنواع مختلفة من الرسوم الصغيرة إلى مناطق الخلايا المحددة.

يوضح المثال أدناه ميزة شرائط البيانات. يوضح المثال كيفية:

1. فتح ملف قالب بسيط.
1. قراءة معلومات شرائط البيانات لورقة عمل.
1. إضافة شرائط بيانات جديدة لنطاق بيانات معطى إلى منطقة خلية.
1. حفظ ملف Excel على القرص.


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a Workbook
// Open a template file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "Book1.xlsx"));
// Get the first worksheet
const sheet = workbook.getWorksheets().get(0);

// Use the following lines if you need to read the Sparklines
// Read the Sparklines from the template file (if it has)
const sparklinesCount = sheet.getSparklineGroups().getCount();

for (let i = 0; i < sparklinesCount; i++)
{
const group = sheet.getSparklineGroups().get(i);
// Display the Sparklines group information e.g type, number of sparklines items
console.log(`sparkline group: type:${group.getType()}, sparkline items count:${group.getSparklines().getCount()}`);
const sparklineCount = sparklineGroup.getSparklines().getCount();
for (let j = 0; j < sparklineCount; j++) 
{
const sparkline = sparklineGroup.getSparklines().get(j);
// Display the individual Sparkines and the data ranges
console.log(`sparkline: row:${sparkline.getRow()}, col:${sparkline.getColumn()}, dataRange:${sparkline.getDataRange()}`);
}
}


// Add Sparklines
// Define the CellArea D2:D10
const ca = AsposeCells.CellArea.createCellArea(1, 4, 7, 4);
// Add new Sparklines for a data range to a cell area
const idx = sheet.getSparklineGroups().add(AsposeCells.SparklineType.Column, "Sheet1!B2:D8", false, ca);
const group = sheet.getSparklineGroups().get(idx);
// Create CellsColor
const clr = workbook.createCellsColor();
clr.setColor(AsposeCells.Color.Orange);
group.setSeriesColor(clr);

// Save the excel file
workbook.save(path.join(dataDir, "Book1.out.xlsx"));
```
## **ضبط تنسيق ثلاثي الأبعاد**
قد تحتاج إلى أنماط مخططات ثلاثية الأبعاد بحيث يمكنك الحصول فقط على النتائج لنطاق السيناريو الخاص بك. يوفر Aspose.Cells for Node.js via C++ API ذات الصلة لتطبيق تنسيق ثلاثي الأبعاد في Microsoft Excel 2007.

يتم تقديم مثال كامل أدناه لتوضيح كيفية إنشاء رسم بياني وتطبيق تنسيق Microsoft Excel 2007 ثلاثي الأبعاد. بعد تنفيذ كود المثال، سيتم إضافة رسم بياني للأعمدة (مع تأثيرات ثلاثية الأبعاد) إلى ورقة العمل.


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "3d_format.out.xlsx");

// Instantiate a new Workbook
const book = new AsposeCells.Workbook();

// Add a Data Worksheet
const dataSheet = book.getWorksheets().add("DataSheet");

// Add Chart Worksheet
const sheet = book.getWorksheets().add("MyChart");

// Put some values into the cells in the data worksheet
dataSheet.getCells().get("B1").putValue(1);
dataSheet.getCells().get("B2").putValue(2);
dataSheet.getCells().get("B3").putValue(3);
dataSheet.getCells().get("A1").putValue("A");
dataSheet.getCells().get("A2").putValue("B");
dataSheet.getCells().get("A3").putValue("C");

// Define the Chart Collection
const charts = sheet.getCharts();
// Add a Column chart to the Chart Worksheet
const chartSheetIdx = charts.add(AsposeCells.ChartType.Column, 5, 0, 25, 15);

// Get the newly added Chart
const chart = book.getWorksheets().get(2).getCharts().get(0);

// Set the background/foreground color for PlotArea/ChartArea
chart.getPlotArea().getArea().setBackgroundColor(AsposeCells.Color.White);
chart.getChartArea().getArea().setBackgroundColor(AsposeCells.Color.White);
chart.getPlotArea().getArea().setForegroundColor(AsposeCells.Color.White);
chart.getChartArea().getArea().setForegroundColor(AsposeCells.Color.White);

// Hide the Legend
chart.setShowLegend(false);

// Add Data Series for the Chart
chart.getNSeries().add("DataSheet!B1:B3", true);
// Specify the Category Data
chart.getNSeries().setCategoryData("DataSheet!A1:A3");

// Get the Data Series
const ser = chart.getNSeries().get(0);

// Apply the 3-D formatting
const spPr = ser.getShapeProperties();
const fmt3d = spPr.getFormat3D();

// Specify Bevel with its height/width
const bevel = fmt3d.getTopBevel();
bevel.setType(AsposeCells.BevelPresetType.Circle);
bevel.setHeight(2);
bevel.setWidth(5);

// Specify Surface material type
fmt3d.setSurfaceMaterialType(AsposeCells.PresetMaterialType.WarmMatte);

// Specify surface lighting type
fmt3d.setSurfaceLightingType(AsposeCells.LightRigType.ThreePoint);

// Specify lighting angle
fmt3d.setLightingAngle(20);

// Specify Series background/foreground and line color
ser.getArea().setBackgroundColor(AsposeCells.Color.Maroon);
ser.getArea().setForegroundColor(AsposeCells.Color.Maroon);
ser.getBorder().setColor(AsposeCells.Color.Maroon);

// Save the Excel file
book.save(filePath);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
