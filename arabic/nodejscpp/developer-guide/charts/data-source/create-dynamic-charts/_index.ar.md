---  
title: إنشاء مخططات ديناميكية باستخدام Node.js عبر C++  
linktitle: إنشاء رسوم بيانية ديناميكية  
description: تعلم كيفية إنشاء مخططات ديناميكية في Aspose.Cells for Node.js via C++. سيرينا دليلك كيفية تحديث بيانات المخطط، السلاسل، والتنسيق بشكل ديناميكي استنادًا إلى متطلباتك، مما يتيح لك عرض البيانات المتغيرة بصريًا في أوراق العمل الخاصة بك.  
keywords: Aspose.Cells لـ Node.js، المخططات، المخططات الديناميكية، البيانات، السلاسل، التنسيق، أوراق العمل، التحديث.  
type: docs  
weight: 240  
url: /ar/nodejs-cpp/create-dynamic-charts/  
---  

{{% alert color="primary" %}}  
الرسوم البيانية الديناميكية (أو التفاعلية) لها القدرة على التغيير عند تغيير نطاق البيانات. وبعبارة أخرى، يمكن للرسوم البيانية الديناميكية أن تعكس تلقائيًا التغييرات عند تغيير مصدر البيانات. من أجل تحفيز تغيير مصدر البيانات، يمكن استخدام خيارات التصفية لجداول البيانات في Excel أو استخدام عنصر تحكم مثل مربع القائمة المنسدلة أو قائمة البحث.

يوضح هذا المقال استخدام APIs الخاصة بـ Aspose.Cells for Node.js via C++ لإنشاء مخططات ديناميكية باستخدام كلا النهجين المذكورين أعلاه.  
{{% /alert %}}  

## **استخدام جداول Excel**  

{{% alert color="primary" %}}  
تشير جداول إكسل المُشار إليها على أنها ListObjects من منظور Aspose.Cells، لذا سنستخدم مصطلح "ListObject" بدلاً من "جدول" لزيادة الوضوح. يرجى القراءة بالتفصيل حول كيفية [إنشاء ListObjects](/cells/ar/nodejs-cpp/create-and-format-table/) باستخدام Aspose.Cells for Node.js via C++.  
{{% /alert %}}  

تحتوي ListObjects على وظيفة مدمجة لفرز وتصفية البيانات عند تفاعل المستخدم. يتم توفير خيارات الفرز والتصفية من خلال القوائم المنسدلة التي تُضاف تلقائيًا إلى صف الرأس في [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject). نظرًا لهذه الميزات (الفرز والتصفية)، يبدو أن [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject) هو المرشح المثالي ليكون مصدر بيانات لمخطط ديناميكي لأنه عند تغيير الفرز أو التصفية، ستتغير صورة البيانات في المخطط لتعكس الحالة الحالية لـ [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject).

لتسهيل الفهم، سوف ننشئ [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) من الصفر ونتقدم خطوة بخطوة كما هو موضح أدناه.

1. إنشاء [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) فارغة.
1. الوصول إلى [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) لأول [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) في [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook).
3. إدراج بعض البيانات في الخلايا.
1. إنشاء [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject) بناءً على البيانات المدخلة.
1. إنشاء [**Chart**](https://reference.aspose.com/cells/nodejs-cpp/chart) بناءً على نطاق البيانات لـ [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject).
احفظ النتيجة على القرص الصلب.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create an instance of Workbook
const book = new AsposeCells.Workbook();
// Access first worksheet from the collection
const sheet = book.getWorksheets().get(0);
// Access cells collection of the first worksheet
const cells = sheet.getCells();

// Insert data column-wise
cells.get("A1").putValue("Category");
cells.get("A2").putValue("Fruit");
cells.get("A3").putValue("Fruit");
cells.get("A4").putValue("Fruit");
cells.get("A5").putValue("Fruit");
cells.get("A6").putValue("Vegetables");
cells.get("A7").putValue("Vegetables");
cells.get("A8").putValue("Vegetables");
cells.get("A9").putValue("Vegetables");
cells.get("A10").putValue("Beverages");
cells.get("A11").putValue("Beverages");
cells.get("A12").putValue("Beverages");

cells.get("B1").putValue("Food");
cells.get("B2").putValue("Apple");
cells.get("B3").putValue("Banana");
cells.get("B4").putValue("Apricot");
cells.get("B5").putValue("Grapes");
cells.get("B6").putValue("Carrot");
cells.get("B7").putValue("Onion");
cells.get("B8").putValue("Cabbage");
cells.get("B9").putValue("Potato");
cells.get("B10").putValue("Coke");
cells.get("B11").putValue("Coladas");
cells.get("B12").putValue("Fizz");

cells.get("C1").putValue("Cost");
cells.get("C2").putValue(2.2);
cells.get("C3").putValue(3.1);
cells.get("C4").putValue(4.1);
cells.get("C5").putValue(5.1);
cells.get("C6").putValue(4.4);
cells.get("C7").putValue(5.4);
cells.get("C8").putValue(6.5);
cells.get("C9").putValue(5.3);
cells.get("C10").putValue(3.2);
cells.get("C11").putValue(3.6);
cells.get("C12").putValue(5.2);

cells.get("D1").putValue("Profit");
cells.get("D2").putValue(0.1);
cells.get("D3").putValue(0.4);
cells.get("D4").putValue(0.5);
cells.get("D5").putValue(0.6);
cells.get("D6").putValue(0.7);
cells.get("D7").putValue(1.3);
cells.get("D8").putValue(0.8);
cells.get("D9").putValue(1.3);
cells.get("D10").putValue(2.2);
cells.get("D11").putValue(2.4);
cells.get("D12").putValue(3.3);

// Create ListObject, Get the List objects collection in the first worksheet
const listObjects = sheet.getListObjects();

// Add a List based on the data source range with headers on
let index = listObjects.add(0, 0, 11, 3, true);

sheet.autoFitColumns();

// Create chart based on ListObject
index = sheet.getCharts().add(AsposeCells.ChartType.Column, 21, 1, 35, 18);
const chart = sheet.getCharts().get(index);
chart.setChartDataRange("A1:D12", true);
chart.getNSeries().setCategoryData("A2:B12");

// Save spreadsheet
book.save(path.join(dataDir, "output_out.xlsx"));
```  

## **استخدام الصيغ الديناميكية**  

في حال رغبتك بعدم استخدام [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject) كمصدر بيانات للمخطط الديناميكي، فإن الخيار الآخر هو استخدام وظائف إكسل (أو الصيغ) لإنشاء مجال بيانات ديناميكي، وعنصر تحكم (مثل مربع مركب) لتفعيل التغيير في البيانات. في هذا السيناريو، سنستخدم وظيفة VLOOKUP لاسترجاع القيم الملائمة استنادًا إلى اختيار مربع مركب. عند تغيير الاختيار، ستقوم وظيفة VLOOKUP بتحديث قيمة الخلية. إذا كان مدى الخلايا يستخدم وظيفة VLOOKUP، فيمكن تحديث النطاق بأكمله عند تفاعل المستخدم، وبالتالي يمكن استخدامه كمصدر لمخطط ديناميكي.

من أجل إبقاء العرض التوضيحي بسيطًا للفهم، سنقوم بإنشاء دفتر العمل من البداية والمضي قدمًا خطوة بخطوة كما هو موضح أدناه.

1. إنشاء [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) فارغة.
1. الوصول إلى [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) لأول [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) في [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook).
1. إدراج بعض البيانات في الخلايا عن طريق إنشاء نطاق مسمى. ستكون هذه البيانات مصدرًا للمخطط الديناميكي.
1. إنشاء [**ComboBox**](https://reference.aspose.com/cells/nodejs-cpp/combobox) استنادًا إلى النطاق المسمي الذي تم إنشاؤه في الخطوة السابقة.
1. إدراج بعض البيانات الإضافية في الخلايا التي ستعتبر مصدرًا لوظيفة VLOOKUP.
1. إدراج وظيفة VLOOKUP (مع المعلمات المناسبة) لنطاق من الخلايا. سيعمل هذا النطاق كمصدر للمخطط الديناميكي.
1. إنشاء [**Chart**](https://reference.aspose.com/cells/nodejs-cpp/chart) استنادًا إلى النطاق الذي تم إنشاؤه في الخطوة السابقة.
احفظ النتيجة على القرص الصلب.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Create a workbook object
const workbook = new AsposeCells.Workbook(filePath);

// Get the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Create a range in the second worksheet
const range = worksheet.getCells().createRange("C21", "C24");

// Name the range
range.setName("MyRange");

// Fill different cells with data in the range
range.get(0, 0).putValue("North");
range.get(1, 0).putValue("South");
range.get(2, 0).putValue("East");
range.get(3, 0).putValue("West");

const comboBox = worksheet.getShapes().addComboBox(15, 0, 2, 0, 17, 64);
comboBox.setInputRange("=MyRange");
comboBox.setLinkedCell("=B16");
comboBox.setSelectedIndex(0);
const cell = worksheet.getCells().get("B16");
const style = cell.getStyle();
style.getFont().setColor(AsposeCells.Color.White);
cell.setStyle(style);

worksheet.getCells().get("C16").setFormula("=INDEX(Sheet1!$C$21:$C$24,$B$16,1)");

// Put some data for chart source
// Data Headers
worksheet.getCells().get("D15").putValue("Jan");
worksheet.getCells().get("D20").putValue("Jan");

worksheet.getCells().get("E15").putValue("Feb");
worksheet.getCells().get("E20").putValue("Feb");

worksheet.getCells().get("F15").putValue("Mar");
worksheet.getCells().get("F20").putValue("Mar");

worksheet.getCells().get("G15").putValue("Apr");
worksheet.getCells().get("G20").putValue("Apr");

worksheet.getCells().get("H15").putValue("May");
worksheet.getCells().get("H20").putValue("May");

worksheet.getCells().get("I15").putValue("Jun");
worksheet.getCells().get("I20").putValue("Jun");

// Data
worksheet.getCells().get("D21").putValue(304);
worksheet.getCells().get("D22").putValue(402);
worksheet.getCells().get("D23").putValue(321);
worksheet.getCells().get("D24").putValue(123);

worksheet.getCells().get("E21").putValue(300);
worksheet.getCells().get("E22").putValue(500);
worksheet.getCells().get("E23").putValue(219);
worksheet.getCells().get("E24").putValue(422);

worksheet.getCells().get("F21").putValue(222);
worksheet.getCells().get("F22").putValue(331);
worksheet.getCells().get("F23").putValue(112);
worksheet.getCells().get("F24").putValue(350);

worksheet.getCells().get("G21").putValue(100);
worksheet.getCells().get("G22").putValue(200);
worksheet.getCells().get("G23").putValue(300);
worksheet.getCells().get("G24").putValue(400);

worksheet.getCells().get("H21").putValue(200);
worksheet.getCells().get("H22").putValue(300);
worksheet.getCells().get("H23").putValue(400);
worksheet.getCells().get("H24").putValue(500);

worksheet.getCells().get("I21").putValue(400);
worksheet.getCells().get("I22").putValue(200);
worksheet.getCells().get("I23").putValue(200);
worksheet.getCells().get("I24").putValue(100);

// Dynamically load data on selection of Dropdown value
worksheet.getCells().get("D16").setFormula("=IFERROR(VLOOKUP($C$16,$C$21:$I$24,2,FALSE),0)");
worksheet.getCells().get("E16").setFormula("=IFERROR(VLOOKUP($C$16,$C$21:$I$24,3,FALSE),0)");
worksheet.getCells().get("F16").setFormula("=IFERROR(VLOOKUP($C$16,$C$21:$I$24,4,FALSE),0)");
worksheet.getCells().get("G16").setFormula("=IFERROR(VLOOKUP($C$16,$C$21:$I$24,5,FALSE),0)");
worksheet.getCells().get("H16").setFormula("=IFERROR(VLOOKUP($C$16,$C$21:$I$24,6,FALSE),0)");
worksheet.getCells().get("I16").setFormula("=IFERROR(VLOOKUP($C$16,$C$21:$I$24,7,FALSE),0)");

// Create Chart
const index = worksheet.getCharts().add(AsposeCells.ChartType.Column, 0, 3, 12, 9);
const chart = worksheet.getCharts().get(index);
chart.getNSeries().add("='Sheet1'!$D$16:$I$16", false);
chart.getNSeries().get(0).setName("=C16");
chart.getNSeries().setCategoryData("=$D$15:$I$15");

// Save result on disc
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
