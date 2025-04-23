---  
title: عرض نطاق الخلايا كتسميات البيانات باستخدام Node.js عبر C++  
linktitle: عرض نطاق الخلية كعلامات البيانات  
description: تعلم كيفية عرض مدى من الخلايا كتسميات بيانات في المخططات باستخدام Aspose.Cells for Node.js via C++. ستوضح لك دليلاتنا كيفية ربط التسميات بمصدر البيانات الخاص بك وتنسيقها لتوفير معلومات دقيقة وذات مغزى في مخططاتك.  
keywords: Aspose.Cells for Node.js via C++، رسم بياني، تسميات البيانات، نطاق الخلايا، مصدر البيانات، التنسيق، الدقة، المعلومات ذات المعنى.  
type: docs  
weight: 130  
url: /ar/nodejs-cpp/showing-cell-range-as-the-data-labels/  
---  

{{% alert color="primary" %}}  
في Microsoft Excel 2013، يمكنك عرض نطاق خلايا لعلامات البيانات. يدعم Aspose.Cells لـ Node.js هذه الميزة.  
{{% /alert %}}  

## **علامة اختيار لعرض نطاق الخلايا كتسميات بيانات**  

لعرض نطاق الخلايا كتسميات بيانات في Microsoft Excel:  

1. حدد تسميات بيانات السلسلة وانقر بزر الماوس الأيمن لفتح القائمة المنسدلة.  
1. حدد **تنسيق تسميات البيانات**. تعرض خيارات التسميات.  
1. حدد أو قم بمسح الخيار **تحتوي التسمية على - قيمة من الخلايا**.  

الكود النموذجي أدناه يصل إلى علامات بيانات سلسلة الرسم البياني ويضبط الخاصية [**DataLabels.getShowCellRange()**](https://reference.aspose.com/cells/nodejs-cpp/datalabels/#getShowCellRange--) على **صحيح** لاختيار خيار **العلامة تتضمن - القيمة من الخلايا**.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "source_show_range.xlsx");

// Create workbook from the source Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access the chart inside the worksheet
const chart = worksheet.getCharts().get(0);

// Check the "Label Contains - Value From Cells"
const dataLabels = chart.getNSeries().get(0).getDataLabels();
dataLabels.setShowCellRange(true);

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

