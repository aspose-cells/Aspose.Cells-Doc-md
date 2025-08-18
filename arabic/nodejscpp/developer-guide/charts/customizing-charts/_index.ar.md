---  
title: تخصيص المخططات باستخدام Node.js عبر C++  
linktitle: تخصيص المخططات  
description: تعلم كيفية تخصيص المخططات في Aspose.Cells for Node.js via C++. سيرشدك دليلنا إلى تعديل تخطيطات المخطط، وإضافة وتنسيق سلسلة البيانات، وضبط المحاور، وتطبيق خيارات تنسيق مختلفة لتعزيز مظهر واستخدام مخططاتك.  
keywords: Aspose.Cells for Node.js via C++، المخططات، التخصيص، التخطيطات، سلسلة البيانات، المحاور، التنسيق، المظهر، الاستخدام.  
type: docs  
weight: 40  
url: /ar/nodejs-cpp/customizing-charts/  
---  


## **إنشاء مخططات مخصصة**  

حتى الآن، عند مناقشة المخططات، نظرنا إلى المخططات القياسية التي تحتوي على إعدادات تنسيقها القياسية. نحن فقط نحدد مصدر البيانات، ونضبط بعض الخصائص، ويتم إنشاء المخطط بالتنسيق الافتراضي الخاص به. لكن APIs الخاصة بـ Aspose.Cells تدعم أيضًا إنشاء مخططات مخصصة تتيح للمطورين إنشاء مخططات مع إعداداتهم الخاصة.  

يمكن للمطورين إنشاء مخططات مخصصة أثناء التشغيل باستخدام Aspose.Cells.  

المخطط يتكون من سلسلة بيانات. كل سلسلة بيانات في Aspose.Cells يتم تمثيلها بواسطة كائن [**Series**](https://reference.aspose.com/cells/nodejs-cpp/series)، في حين أن كائن [**SeriesCollection**](https://reference.aspose.com/cells/nodejs-cpp/seriescollection) يعمل كمجموعة من كائنات [**Series**](https://reference.aspose.com/cells/nodejs-cpp/series). عند إنشاء مخطط مخصص، يتمتع المطورون بحرية استخدام أنواع مختلفة من المخططات لسلاسل البيانات المختلفة (المجمعة في كائن [**SeriesCollection**](https://reference.aspose.com/cells/nodejs-cpp/seriescollection)).  

الكود المثال أدناه يوضح كيفية إنشاء مخططات مخصصة. في هذا المثال، سنستخدم مخطط عمودي لأول سلسلة بيانات ومخطط خطي للسلسلة الثانية. النتيجة هي أننا نضيف مخطط عمودي، مع مخطط خطي، إلى ورقة العمل.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Workbook object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding sample values to cells
worksheet.getCells().get("A1").putValue(50);
worksheet.getCells().get("A2").putValue(100);
worksheet.getCells().get("A3").putValue(150);
worksheet.getCells().get("A4").putValue(110);
worksheet.getCells().get("B1").putValue(260);
worksheet.getCells().get("B2").putValue(12);
worksheet.getCells().get("B3").putValue(50);
worksheet.getCells().get("B4").putValue(100);

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 5, 0, 15, 5);

// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);

// Adding NSeries (chart data source) to the chart ranging from "A1" cell to "B4"
chart.getNSeries().add("A1:B4", true);

// Setting the chart type of 2nd NSeries to display as line chart
chart.getNSeries().get(1).setType(AsposeCells.ChartType.Line);

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```  

{{% alert color="primary" %}}  

حالياً، يدعم Aspose.Cells فقط المخططات المخصصة التي تجمع بين مخططات الفطيرة، والخط، والعمود، والتكديس العمودي، ولكن سيتم دعم المزيد من المخططات في الإصدارات المستقبلية.  

{{% /alert %}}  

