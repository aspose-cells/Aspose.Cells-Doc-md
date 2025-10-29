---
title: تغيير اتجاه تسمية العلامات باستخدام Node.js عبر C++
linktitle: تغيير اتجاه التسمية التلقائية
description: تعلم كيفية تغيير اتجاه تسمية العلامات في Aspose.Cells لـ Node.js. سيساعدك دليلنا على فهم كيفية ضبط اتجاه التسمية على المحاور، بما في ذلك الاتجاه الأفقي، الرأسي، والزوايا.
keywords: Aspose.Cells لـ Node.js، تسميات العلامات، الاتجاه، الاتجاهية، المحاور، أفقي، رأسي، بزوايا.
type: docs
weight: 170
url: /ar/nodejs-cpp/change-tick-label-direction/
---

## **تغيير اتجاه التسمية التلقائية**

توفر Aspose.Cells إمكانية تغيير اتجاه تسميات العلامات على الرسم البياني باستخدام خاصية [**TickLabels.getDirectionType()**](https://reference.aspose.com/cells/nodejs-cpp/ticklabels/#getDirectionType--). تقبل الخاصية [**TickLabels.getDirectionType()**](https://reference.aspose.com/cells/nodejs-cpp/ticklabels/#getDirectionType--) قيمة تعداد [**ChartTextDirectionType**](https://reference.aspose.com/cells/nodejs-cpp/charttextdirectiontype). يوفر تعداد [**ChartTextDirectionType**](https://reference.aspose.com/cells/nodejs-cpp/charttextdirectiontype) الأعضاء التالية:

- أفقي
- رأسي
- دوران 90
- دوران 270
- مكدس

صورة تقارن بين الملف الأصلي وملف الإخراج

### **صورة الملف الأصلي**

![todo:image_alt_text](change-tick-label-direction_1.jpg)

### **صورة الملف الإخراج**

![todo:image_alt_text](change-tick-label-direction_2.jpg)

مقتطف الكود التالي يغير اتجاه تسمية العلامة المحورية من دوران 90 إلى أفقي.

## **الكود المثالي**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");
const filePath = path.join(sourceDir, "SampleChangeTickLabelDirection.xlsx");

// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

const worksheet = workbook.getWorksheets().get(0);

// Load the chart from source worksheet
const chart = worksheet.getCharts().get(0);

chart.getCategoryAxis().getTickLabels().setDirectionType(AsposeCells.ChartTextDirectionType.Horizontal);

// Output the file
workbook.save(path.join(outputDir, "outputChangeChartDataLableDirection.xlsx"));
```

يمكن تحميل ملفات المصدر والإخراج من الروابط التالية.

[ملف المصدر](105480221.xlsx)

[ملف الإخراج](105480223.xlsx)
{{< app/cells/assistant language="nodejs-cpp" >}}
