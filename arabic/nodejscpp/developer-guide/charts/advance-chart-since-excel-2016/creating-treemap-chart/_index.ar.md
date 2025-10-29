---  
title: كيفية إنشاء مخطط TreeMap مع Node.js عبر C++  
linktitle: كيفية إنشاء رسم بياني لخريطة الشجرة  
description: تعلم كيفية إنشاء مخطط Treemap في Aspose.Cells for Node.js via C++. سيساعدك دليلنا على فهم الخصائص المختلفة وخيارات التنسيق المتاحة لمخططات Treemap، بما في ذلك الألوان، التسميات، وتمثيل البيانات.  
keywords: Aspose.Cells لـ Node.js، مخطط Treemap، إنشاء، خصائص، تنسيق، ألوان، تسميات، تمثيل البيانات، مخطط دائري، تخطيط هرمى.  
type: docs  
weight: 161  
url: /ar/nodejs-cpp/creating-treemap-chart/  
---  

## **سيناريوهات الاستخدام المحتملة**  
رسم بياني لخريطة الشجرة يوفر رؤية تسلسلية لبياناتك ويجعل من السهل رؤية الأنماط، مثل أي العناصر هي أفضل المبيعات في المحل. تمثل الفروع الشجرية بواسطة المستطيلات، ويتم عرض كل فرع فرعي كمستطيل أصغر. يعرض رسم بياني الخريطة الشجرية الفئات بواسطة اللون والقرب، ويمكن عرض الكثير من البيانات بسهولة مما قد يكون صعبًا مع أنواع الرسوم البيانية الأخرى.  

![todo:image_alt_text](sample.png)  
## **رسم بياني لخريطة الشجرة**  
بعد تشغيل الكود أدناه، سترون رسم بياني لخريطة الشجرة كما هو موضح أدناه.  

![todo:image_alt_text](result.png)  
## **الكود المثالي**  
الكود العيني التالي يقوم بتحميل [ملف Excel العيني](treemap.xlsx) ويولد [ملف Excel الناتج](out.xlsx).  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "treemap.xlsx");
// Create an instance of Workbook
const workbook = new AsposeCells.Workbook(filePath);
// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);
// Add a Treemap chart
const pieIdx = worksheet.getCharts().add(AsposeCells.ChartType.Treemap, 5, 6, 20, 12);
// Retrieve the Chart object
const chart = worksheet.getCharts().get(pieIdx);
// Set the legend can be showed
chart.setShowLegend(true);
// Set the chart title name 
chart.getTitle().setText("TreeMap Chart");
// Add series data range(D2:D13,actually)
chart.getNSeries().add("D2:F13", true);
// Set category data(A2:A13 is incorrect )
chart.getNSeries().setCategoryData("A2:C13");
// Show the DataLabels with category names
chart.getNSeries().get(0).getDataLabels().setShowCategoryName(true);
// Fill the PlotArea area with nothing 
chart.getPlotArea().getArea().getFillFormat().setFillType(AsposeCells.FillType.None);
// Save the Excel file
workbook.save("out.xlsx");
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
