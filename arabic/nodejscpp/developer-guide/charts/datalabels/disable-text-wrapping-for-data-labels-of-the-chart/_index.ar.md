---
title: تعطيل التغليف النصي لتسميات البيانات في المخطط باستخدام Node.js عبر C++
description: تعلم كيفية تعطيل التغليف النصي لتسميات البيانات في المخططات باستخدام Aspose.Cells for Node.js via C++. سيرينا دليلنا كيف تمنع تداخل التسميات الطويلة وتوفر عرضًا أكثر وضوحًا وقراءة للمخططات.
keywords: Aspose.Cells for Node.js via C++، رسم بياني، تسميات البيانات، التغليف النصي، التداخل، قراءة، العروض.
type: docs
weight: 70
url: /ar/nodejs-cpp/disable-text-wrapping-for-data-labels-of-the-chart/
---

{{% alert color="primary" %}}

يسمح Microsoft Excel 2013 للمستخدمين بتضمين أو عدم تضمين النص داخل تسميات البيانات في الرسم البياني. بشكل افتراضي، يكون النص داخل تسميات البيانات في الرسم البياني في حالة التضمين.

توفر Aspose.Cells خاصية [**DataLabels.isTextWrapped()**](https://reference.aspose.com/cells/nodejs-cpp/datalabels/#isTextWrapped--) التي يمكنك تعيينها true أو false لتمكين أو تعطيل تغليف نص تسميات البيانات على التوالي.

{{% /alert %}}

يظهر النموذج العيني التالي كيفية تعطيل تضمين النص لتسميات البيانات في الرسم البياني.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample_wrap_label.xlsx");
// Load the sample Excel file inside the workbook object
const workbook = new AsposeCells.Workbook(filePath);

// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access the first chart inside the worksheet
const chart = worksheet.getCharts().get(0);

// Disable the Text Wrapping of Data Labels in all Series
chart.getNSeries().get(0).getDataLabels().setIsTextWrapped(false);
chart.getNSeries().get(1).getDataLabels().setIsTextWrapped(false);
chart.getNSeries().get(2).getDataLabels().setIsTextWrapped(false);

// Save the workbook
workbook.save(path.join(dataDir, "Output_out.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
