---
title: كيفية إدارة PivotChart مع PivotOptions باستخدام Node.js عبر C++
linktitle: Pivot Options
type: docs
weight: 10
url: /ar/nodejs-cpp/how-to-manage-pivotchart-with-pivotoptions/
description: كيفية إدارة PivotChart مع PivotOptions في Node.js عبر C++.
keywords: PivotChart Node.js عبر C++
---
## ما هو PivotChart

PivotChart في Excel هو تمثيل رسومي للبيانات تم إنشاؤه من PivotTable. يتيح للمستخدمين تصور البيانات وتحليلها ديناميكيًا من خلال تلخيص وعرض المعلومات في شكل رسوم بيانية. تكون PivotCharts تفاعلية ويمكن تعديلها بسهولة لعرض وجهات نظر مختلفة للبيانات، مما يجعلها أداة قوية لتحليل البيانات والعرض في Excel.

## كيفية إدارة PivotChart مع PivotOptions

باستخدام Aspose.Cells for Node.js via C++، يمكنك استخدام [**PivotOptions**](https://reference.aspose.com/cells/nodejs-cpp/pivotoptions/) لإدارة PivotChart.

ملف وكود مثالي:
[ملف المثال](Sample.xlsx)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
const chart = workbook.getWorksheets().get(0).getCharts().get(0);
const opt = chart.getPivotOptions();

// Hide ZoneFilter in PivotChart
opt.setDropZoneFilter(false); // HideZoneFilter

// You can set more properties, try them!
// opt.setDropZoneCategories(false); // HideZoneCategories
// opt.setDropZoneData(false); // HideZoneData
// opt.setDropZoneSeries(false); // HideZoneSeries
// opt.setDropZonesVisible(false); // Hide All

// Save the file and see the effect.
workbook.save(path.join(dataDir, "HideZoneFilter.xlsx"));
```

مع الكود المثالي أعلاه، يمكنك التحقق من ملف النتيجة بالتأثير التالي، كما هو موضح في الشكل:

**![النتيجة](الناتج.png)**
{{< app/cells/assistant language="nodejs-cpp" >}}
