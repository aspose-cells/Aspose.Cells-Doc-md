---
title: كيفية إنشاء مخطط شمسية مع Node.js عبر C++
linktitle: كيفية إنشاء رسم بياني للتفجير الشمسي
description: تعلم كيفية إنشاء مخطط شمسية في Aspose.Cells for Node.js via C++، وهو مخطط يعرض البيانات بشكل دائرة. الدليل الخاص بنا سيساعدك في إعداد خصائص وتنسيقات مختلفة لمخططك، بما في ذلك تسميات البيانات، الأساطير، الألوان، والمزيد.
keywords: Aspose.Cells for Node.js via C++، مخطط الشمسية، إنشاء، ضبط الخصائص، تسميات البيانات، الأسطورة، التنسيف، اللون، الدائرة، عرض البيانات.
type: docs
weight: 162
url: /ar/nodejs-cpp/creating-sunburst-chart/
---

## **سيناريوهات الاستخدام المحتملة**
جداول الأشجار جيدة للمقارنة بين النسب داخل الهيكل؛ ومع ذلك، فإن جداول الأشجار ليست رائعة في عرض المستويات الهرمية بين أكبر الفئات وكل نقطة بيانات. مخطط الشمسية هو أكثر وضوحًا لهذا الغرض. يُعد مخطط الشمسية مثاليًا لعرض البيانات الهرمية. يُمثل كل مستوى من الهيكل بواسطة خاتم واحد أو دائرة، مع أصغر دائرة تمثل أعلى مستوى من الهرمية. يبدو مخطط الشمسية بدون بيانات هرمية (مستوى واحد من الفئات) مشابهًا لمخطط الدونات. ومع ذلك، فإن مخطط الشمسية متعدد المستويات يُظهر كيف ترتبط الحلقات الخارجية بالحلقات الداخلية. يتمتع مخطط الشمسية بأقصى فاعليته في إظهار كيف يتم تقسيم حلقة واحدة إلى أجزائها المساهمة، بينما نوع آخر من المخططات الهرمية، مخطط الشجرة، مثالي للمقارنة بين الأحجام النسبية.

![todo:image_alt_text](sample.png)
## **رسم بياني للتفجير الشمسي**
بعد تشغيل الكود أدناه، سترون رسم بياني للتفجير الشمسي كما هو موضح أدناه.

![todo:image_alt_text](result.png)
## **الكود المثالي**
الكود المثالي التالي يحمل [ملف Excel العيني](sunburst.xlsx) ويُولّد [ملف Excel الإخراج](out.xlsx).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sunburst.xlsx");
// Create an instance of Workbook
const workbook = new AsposeCells.Workbook(filePath);
// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);
// Add a Treemap chart
const pieIdx = worksheet.getCharts().add(AsposeCells.ChartType.Sunburst, 5, 6, 25, 12);
// Retrieve the Chart object
const chart = worksheet.getCharts().get(pieIdx);
// Set the legend can be showed
chart.setShowLegend(true);
// Set the chart title name 
chart.getTitle().setText("Sunburst Chart");
// Add series data range
chart.getNSeries().add("D2:D16", true);
// Set category data (A2:A16 is incorrect, as hierarchical category)
chart.getNSeries().setCategoryData("A2:C16");
// Show the DataLabels with category names
chart.getNSeries().get(0).getDataLabels().setShowCategoryName(true);
// Fill the PlotArea area with nothing 
chart.getPlotArea().getArea().getFillFormat().setFillType(AsposeCells.FillType.None);
// Save the Excel file
workbook.save("out.xlsx");
```
