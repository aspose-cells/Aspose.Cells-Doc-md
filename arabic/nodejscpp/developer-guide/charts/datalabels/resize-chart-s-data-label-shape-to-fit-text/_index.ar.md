---  
title: تغيير حجم شكل تسمية البيانات للمخطط ليتناسب مع النص باستخدام Node.js عبر C++  
linktitle: تغيير شكل تسمية بيانات الرسم البياني لتناسب النص  
description: تعلم كيفية تعديل حجم شكل تسمية البيانات في المخطط ليتناسب مع النص في Aspose.Cells for Node.js via C++. سيرينا دليلنا كيفية تعديل حجم وشكل حاوية التسمية لضمان عرض النص بشكل صحيح دون اقتطاع أو تداخل.  
keywords: Aspose.Cells for Node.js via C++، رسم بياني، تسميات البيانات، تغيير الحجم، ملاءمة النص، الاقتطاع، التداخل.  
type: docs  
weight: 220  
url: /ar/nodejs-cpp/resize-chart-s-data-label-shape-to-fit-text/  
---  

{{% alert color="primary" %}}  
توفر تطبيق Excel الخيار **تغيير شكل لملاءمة النص** لتسميات بيانات الرسم البياني من أجل زيادة حجم الشكل بحيث يتناسب النص بداخله.  
{{% /alert %}}  

## **كيفية تغيير شكل تسمية بيانات الرسم البياني لملاءمة النص في Microsoft Excel**  

يمكن الوصول إلى هذا الخيار على واجهة إكسل عن طريق تحديد أي من تسميات البيانات على المخطط. انقر بزر الماوس الأيمن واختر قائمة **تكوين تسميات البيانات**. في علامة التبويب **الحجم والخصائص**، قم بتوسيع **المحاذاة** للكشف عن الخصائص ذات الصلة بما في ذلك خيار **تغيير حجم الشكل لملاءمة النص**.  

## **كيفية تغيير حجم شكل تسمية البيانات ليناسب النص باستخدام Aspose.Cells for Node.js via C++**  

لمحاكاة ميزة إكسل في تغيير حجم أشكال تسمية البيانات لتناسب النص، قدمت واجهات برمجة التطبيقات Aspose.Cells الخاصية [**DataLabels.isResizeShapeToFitText()**](https://reference.aspose.com/cells/nodejs-cpp/charttextframe/#isResizeShapeToFitText--) من نوع Boolean. يُظهر الكود التالي سيناريو الاستخدام البسيط الخاص بـ [**DataLabels.isResizeShapeToFitText()**](https://reference.aspose.com/cells/nodejs-cpp/charttextframe/#isResizeShapeToFitText--) الخاصية.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "source.xlsx");

// Create an instance of Workbook containing the Chart
const workbook = new AsposeCells.Workbook(filePath);

// Access the Worksheet that contains the Chart
const sheet = workbook.getWorksheets().get(0);

for (let c = 0; c < sheet.getCharts().getCount(); c++) 
{
// Access the Chart
const chart = sheet.getCharts().get(c);

for (let index = 0; index < chart.getNSeries().getCount(); index++) {
// Access the DataLabels of indexed NSeries
const labels = chart.getNSeries().get(index).getDataLabels();

// Set ResizeShapeToFitText property to true
labels.setIsResizeShapeToFitText(true);
}

// Calculate Chart
chart.calculate();
}

// Save the result
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
