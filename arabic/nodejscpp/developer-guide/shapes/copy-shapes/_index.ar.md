---
title: نسخ الأشكال بين أوراق العمل باستخدام Node.js عبر C++
linktitle: نسخ الأشكال
type: docs
weight: 200
url: /ar/nodejs-cpp/copy-shapes-between-worksheets/
description: تعلم كيفية نسخ الأشكال مثل الصور والمخططات بين أوراق العمل باستخدام Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}}

أحيانًا، تحتاج إلى نسخ عناصر على ورقة عمل، مثل الصور والمخططات والكائنات الرسومية الأخرى، بين أوراق العمل. يدعم Aspose.Cells for Node.js via C++ هذه الميزة. يمكن نسخ المخططات والصور والأشياء الأخرى بأعلى درجات الدقة.

يوفر هذا المقال فهمًا مفصلًا لكيفية نسخ الأشكال بين صفحات العمل.

{{% /alert %}}

## **نسخ صورة من ورقة عمل إلى أخرى**

لنسخ صورة من ورقة عمل إلى أخرى، استخدم الطريقة التالية كما هو موضح في الكود العيني أدناه.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample_picture.xlsx");

// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Get the Picture from the "Picture" worksheet.
const picturesource = workbook.getWorksheets().get("Picture").getPictures().get(0);

// Save Picture to Memory Stream
const ms = picturesource.getData();

// Copy the picture to the Result Worksheet
workbook.getWorksheets().get("Result").getPictures().add(picturesource.getUpperLeftRow(), picturesource.getUpperLeftColumn(), ms, picturesource.getWidthScale(), picturesource.getHeightScale());

// Save the Worksheet
workbook.save(path.join(dataDir, "PictureCopied_out.xlsx"));
```

## **نسخ رسم بياني من ورقة عمل إلى أخرى**

يوضح الكود التالي استخدام الطريقة لنسخ رسم بياني من ورقة عمل إلى أخرى.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample_chart.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Get the Chart from the "Chart" worksheet.
const chartsource = workbook.getWorksheets().get("Chart").getCharts().get(0);
const cshape = chartsource.getChartObject();

// Copy the Chart to the Result Worksheet
workbook.getWorksheets().get("Result").getShapes().addCopy(cshape, 20, 0, 2, 0);

// Save the Worksheet
workbook.save(path.join(dataDir, "ChartCopied_out.xlsx"));
```

## **نسخ عناصر التحكم والرسومات الأخرى من ورقة عمل إلى أخرى**

لنسخ عناصر التحكم والكائنات الرسم الأخرى، استخدم طريقة [**ShapeCollection.addCopy(Shape, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addCopy-shape-number-number-number-number-) كما هو موضح في المثال أدناه.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample_control.xlsx");
// Open the template file
const workbook = new AsposeCells.Workbook(filePath);

// Get the Shapes from the "Control" worksheet.
const shape = workbook.getWorksheets().get("Control").getShapes();

// Copy the Textbox to the Result Worksheet
workbook.getWorksheets().get("Result").getShapes().addCopy(shape.get(0), 5, 0, 2, 0);

// Copy the Oval Shape to the Result Worksheet
workbook.getWorksheets().get("Result").getShapes().addCopy(shape.get(1), 10, 0, 2, 0);

// Save the Worksheet
workbook.save(path.join(dataDir, "ControlsCopied_out.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
