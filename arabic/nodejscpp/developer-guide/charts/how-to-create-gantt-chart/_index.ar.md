---
title: كيفية إنشاء مخطط جانت باستخدام Node.js عبر C++
linktitle: كيفية إنشاء مخطط جانت
type: docs
weight: 72
url: /ar/nodejs-cpp/how-to-create-gantt-chart/
description: تعلم كيفية إنشاء مخطط جانت باستخدام API Aspose.Cells for Node.js via C++.
keywords: Node.js إنشاء مخطط جانت، إضافة مخطط جانت، إدراج مخطط جانت
---

## **ما هو مخطط جانت**

مخطط جانت هو نوع من مخططات الأعمدة يوضح جدول مشروع. يُظهر تواريخ بدء وانتهاء عناصر المشروع المختلفة. يمثل كل مهمة أو نشاط بواسطة عمود، وطوله يتوافق مع مدته. تشير مخططات جانت أيضًا إلى الاعتماديات بين المهام، مما يسمح لمديري المشاريع برؤية التسلسل الذي يجب إكمال المهام فيه. تستخدم على نطاق واسع في إدارة المشاريع لتخطيط، جدولة، وتتبع المشاريع بشكل فعال.

## **كيفية إنشاء مخطط جانت في إكسل**

يمكنك إنشاء مخطط جانت في إكسل باتباع هذه الخطوات:
1. إضافة بعض البيانات لمخطط جانت. 
<br>
<img src="00.png" width=50% />
1. اختر البيانات واذهب إلى إدراج --> مخططات --> إدراج مخطط عمود أو مخطط أعمدة --> مخطط الأعمدة المجمعة. في مثالنا، هو B1:B7، ثم إدراج مخطط **مخطط أعمدة مجمعة**.
<br>
<img src="1.png" width=50% />

1. اختر المخطط، **اختيار البيانات** -> **إضافة**، حدد **اسم السلسلة** و**قيم السلسلة** كما هو موضح أدناه.
<br>
<img src="2.png" width=50% />

1. اختر المخطط، عدل **محور البيانات الأفقي (الفئة)**.
<br>
<img src="3.png" width=50% />

1. **تنسيق المحور** للمحور الصادي، حدد **الفئات بترتيب عكسي**.
1. اختر **السلسلة الزرقاء** وضع **ملء -> لا ملء**.
1. **تنسيق محور** للمحور الأفقي، حدد **الحد الأدنى والأقصى** (1/5/2019:43470، 1/30/2019:43494).
<br>
<img src="4.png" width=50% />

1. **إضافة تسميات البيانات** للمخطط، الآن ستحصل على مخطط جانت.
<br>
<img src="0.png" width=50% />


## **كيفية إضافة مخطط جانت في Aspose.Cells**
يرجى مراجعة رمز العينة التالي. يقوم بتحميل ملف إكسل عينة ([sample.xlsx](sample.xlsx)) الذي يحتوي على بعض البيانات النموذجية. ثم ينشئ مخطط الأعمدة المجمعة استنادًا إلى البيانات الأولية ويحدد الخصائص ذات الصلة. في النهاية، يحفظ ملف العمل بصيغة XLSX الناتجة ([result.xlsx](result.xlsx)). تُظهر لقطة الشاشة التالية مخطط جانت الذي أنشأته Aspose.Cells في ملف الإكسل الناتج.
<br>
<img src="5.png" width=60% />

### **الكود المثالي**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);
// Create BarStacked Chart
const i = worksheet.getCharts().add(AsposeCells.ChartType.BarStacked, 5, 6, 20, 15);
// Retrieve the Chart object
const chart = worksheet.getCharts().get(i);
// Set the chart title name 
chart.getTitle().setText("Gantt Chart");
// Set the chart title is Visible
chart.getTitle().setIsVisible(true);
// Set data range
chart.setChartDataRange("B1:B6", true);
// Add series data range
chart.getNSeries().add("C2:C6", true);
// No fill for one serie
chart.getNSeries().get(0).getArea().getFillFormat().setFillType(AsposeCells.FillType.None);
// Set the Horizontal(Category) Axis
chart.getNSeries().setCategoryData("A2:A6");
// Reverse the Horizontal(Category) Axis
chart.getCategoryAxis().setIsPlotOrderReversed(true);
// Set the value axis's MinValue and MaxValue
const minValue = parseFloat(worksheet.getCells().get("B2").getValue());
const maxValue = parseFloat(worksheet.getCells().get("D6").getValue());
chart.getValueAxis().setMinValue(isNaN(minValue) ? 0 : minValue);
chart.getValueAxis().setMaxValue(isNaN(maxValue) ? 0 : maxValue);
chart.getPlotArea().getArea().getFillFormat().setFillType(AsposeCells.FillType.None);
// Show the DataLabels
chart.getNSeries().get(1).getDataLabels().setShowValue(true);
// Disable the Legend
chart.setShowLegend(false);
// Save the result
workbook.save("result.xlsx");
```

{{< app/cells/assistant language="nodejs-cpp" >}}
