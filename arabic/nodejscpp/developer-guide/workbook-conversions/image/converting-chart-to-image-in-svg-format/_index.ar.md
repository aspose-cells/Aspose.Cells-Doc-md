---  
title: تحويل مخطط إلى صورة بتنسيق SVG مع Node.js عبر C++  
linktitle: تحويل الرسم البياني إلى صورة بتنسيق SVG  
type: docs  
weight: 240  
url: /ar/nodejs-cpp/converting-chart-to-image-in-svg-format/  
description: تعلم كيف تحويل مخطط إلى صورة بتنسيق SVG باستخدام Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

تعتبر الرسومات البيانية القابلة للتحجيم (SVG) تنسيق صورة ناقل معتمد على XML للرسوميات ثنائية الأبعاد والتي تدعم أيضًا التفاعل والرسوم المتحركة. مواصفات SVG هي معيار مفتوح تم تطويره من قبل W3C (المؤتمر العالمي للشبكة العنكبوتية) منذ عام 1999.  

تم تعريف صور SVG وسلوكها في ملفات نص XML. وهذا يعني أنه يمكن البحث عنها وفهرستها وتدوينها وضغطها. كملفات XML، يمكن إنشاء وتحرير صور SVG باستخدام أي محرر نص، ولكن غالبًا ما يتم إنشاؤها باستخدام برمجيات الرسم.  

يمكن لـ Aspose.Cells حفظ المخططات كصور بصيغ مختلفة مثل BMP، JPEG، PNG، GIF، SVG، وغيرها. يوضح هذا المقال كيفية حفظ مخطط بتنسيق SVG.  

{{% /alert %}}  

يشرح الرمز العينة التالي كيفية استخدام Aspose.Cells لتحويل الرسم البياني إلى صورة في تنسيق SVG. يحمل الرمز ملف Microsoft Excel المصدر ثم يحفظ الرسم البياني الأول الذي تم العثور عليه في الورقة العمل الأولى إلى SVG.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object from source file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "SampleChartBook.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first chart inside the worksheet
const chart = worksheet.getCharts().get(0);

// Set image or print options
const opts = new AsposeCells.ImageOrPrintOptions();
opts.setImageType(AsposeCells.ImageType.Svg);

// Save the chart to svg format
chart.toImage(path.join(dataDir, "Image_out.svg"), opts);
```  

