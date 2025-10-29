---  
title: قراءة تسميات المحور بعد حساب المخطط باستخدام Node.js عبر C++  
linktitle: قراءة تسميات المحور بعد حساب الرسم البياني  
description: تعلم كيفية قراءة تسميات المحور في Aspose.Cells for Node.js via C++ بعد حساب المخطط. دليلنا سيعرض لك كيفية الوصول إلى تسميات المحور واسترجاعها، بما في ذلك تنسيقها وموقعها.  
keywords: Aspose.Cells لـ Node.js، مخطط، تسميات المحور، الحساب، القراءة، الوصول، الاسترجاع، التنسيق، التموضع، Node.js عبر C++  
type: docs  
weight: 90  
url: /ar/nodejs-cpp/read-axis-labels-after-calculating-the-chart/  
---  

## **سيناريوهات الاستخدام المحتملة**

يمكنك قراءة تسميات المحور بعد حساب قيمه باستخدام طريقة [**Chart.calculate()**](https://reference.aspose.com/cells/nodejs-cpp/chart/#calculate--). يرجى استخدام طريقة [**Axis.getAxisTexts()**](https://reference.aspose.com/cells/nodejs-cpp/axis/#getAxisTexts--) لهذا الغرض التي ستعيد قائمة تسميات المحور.

## **قراءة تسميات المحور بعد حساب الرسم البياني**

يرجى الاطلاع على رمز العينة التالي الذي يحمل [ملف Excel عيني](ReadAxisLabels.xlsx) ويقرأ تسميات المحور الفئوي للرسم البياني في الورقة العمل الأولى. ثم يقوم بطباعة قيم تسميات المحور على وحدة التحكم. يرجى الاطلاع على الإخراج على وحدة التحكم من رمز العينة الذي يلي للرجوع إليه.

## **الكود المثالي**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "ReadAxisLabels_new.xlsx");

// Load the Excel file containing chart
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access the chart
const chart = worksheet.getCharts().get(0);

// Calculate the chart
chart.calculate();

// Read axis labels of category axis
const lstLabels = chart.getCategoryAxis().getAxisTexts();

// Print axis labels on console
console.log("Category Axis Labels: ");
console.log("---------------------");

// Iterate axis labels and print them one by one
for (let i = 0; i < lstLabels.length; i++) {
console.log(lstLabels[i]);
}
```

## **مخرجات الوحدة**

{{< highlight javascript >}}  
 Category Axis Labels:  

\---------------------  

Iran  

China  

USA  

Brazil  

England  
{{< /highlight >}}  

{{< app/cells/assistant language="nodejs-cpp" >}}
