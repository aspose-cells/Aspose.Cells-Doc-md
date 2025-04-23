---  
title: إضافة علامة مائية WordArt إلى الرسم البياني باستخدام Node.js عبر C++  
linktitle: إضافة علامة مائية WordArt إلى الرسم البياني  
description: تعلم كيفية استخدام Aspose.Cells for Node.js via C++ لإضافة علامة مائية WordArt إلى رسم بياني في Microsoft Excel. سيُظهر دليلنا كيفية إنشاء وتحديد موقع علامة مائية WordArt لتعزيز الجاذبية البصرية والتفرد لرسمك البياني.  
keywords: Aspose.Cells لـ Node.js، علامة مائية WordArt، علامة مائية للرسم البياني، Microsoft Excel، جاذبية بصرية، تفرد الرسم البياني.  
type: docs  
weight: 50  
url: /ar/nodejs-cpp/add-wordart-watermark-to-chart/  
---  

{{% alert color="primary" %}}  

يمكنك استخدام WordArt لإضافة تأثيرات نص خاصة إلى جداول البيانات. على سبيل المثال، تمدد عنوان، وزين النص، واجعل النص يناسب الشكل المحدد مسبقًا، أو قم بتطبيق النص المتأثر على منطقة الرسم البياني كعلامة مائية. يصبح WordArt كائن يمكنك نقله أو وضعه في جداول البيانات الخاصة بك لإضافة الديكور.  

المثال التالي يوضح كيفية إضافة شكل WordArt كعلامة مائية لمنطقة رسم البياني.  

{{% /alert %}}  

المثال التالي يوضح كيفية إضافة شكل WordArt كعلامة مائية لمنطقة رسم البياني الحالية.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Open the existing excel file.
const workbook = new AsposeCells.Workbook(filePath);

// Get the chart in the first worksheet.
const chart = workbook.getWorksheets().get(0).getCharts().get(0);

// Add a WordArt watermark (shape) to the chart's plot area.
const wordart = chart.getShapes().addTextEffectInChart(AsposeCells.MsoPresetTextEffect.TextEffect2,
"CONFIDENTIAL", "Arial Black", 66, false, false, 1200, 500, 2000, 3000);

// Get the shape's fill format.
const wordArtFormat = wordart.getFill();

// Set the transparency.
wordArtFormat.setTransparency(0.9);

// Get the line format.
const lineFormat = wordart.getLine();

// Set Line format to invisible.
lineFormat.setWeight(0.0);

// Save the excel file.
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

