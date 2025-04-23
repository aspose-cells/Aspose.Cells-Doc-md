---
title: كيفية إخفاء سلسلة باستخدام Node.js عبر C++
linktitle: كيفية إخفاء سلسلة
description: تعلم كيفية إخفاء السلسلة في مخطط إكسل باستخدام Aspose.Cells for Node.js via C++. 
keywords: مخطط إكسل، سلسلة، مخفية، IsFiltered Node.js عبر C++.
type: docs
weight: 74
url: /ar/nodejs-cpp/how-to-set-series-invisible/
---

## كيفية إخفاء سلسلة في مخطط إكسل

في مخطط إكسل، يمكنك النقر بزر الماوس الأيمن على مخطط، ثم اختيار "تحديد البيانات"، وفي النافذة المنبثقة، يمكنك تحديد ما إذا كانت السلسلة مرئية عبر الاختيار أو إلغاء الاختيار. يمكنك تحميل [ملف النموذج](SeriesFiltered.xlsx) التالي واستخدامه في إكسل لتحقيق هذه الوظيفة، وسنشرح لاحقًا كيفية تحقيق ذلك باستخدام مكتبة Aspose.Cells.

![todo:image_alt_text](series-invisible.png)

## كيفية إخفاء سلسلة باستخدام Aspose.Cells 

نستخدم الكود التالي لإخفاء سلسلة باستخدام Aspose.Cells:

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "SeriesFiltered.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

const charts = workbook.getWorksheets().get(0).getCharts();
const chart = charts.get("Chart 1");
const nSeriesFiltered = chart.getFilteredNSeries();
const nSeries = chart.getNSeries();
nSeries.get(1).setIsColorVaried(true);
nSeries.get(0).setIsColorVaried(true);
workbook.save(path.join(dataDir, "output.xlsx"));
```

يمكنك الحصول على الملف المدخل التالي [Input file](SeriesFiltered.xlsx) وملف الإخراج [output file](output.xlsx).

كما هو موضح في الشكل أدناه، السلسلتان الأوليان اللتان كانتا مرئيتين أصلاً، أصبحتا غير مرئيتين في ملف الإخراج.
![todo:image_alt_text](output.png)
