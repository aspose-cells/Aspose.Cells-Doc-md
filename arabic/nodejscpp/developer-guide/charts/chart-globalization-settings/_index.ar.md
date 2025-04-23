---  
title: استخدام فئة ChartGlobalizationSettings لضبط لغة مختلفة لمكون المخطط باستخدام Node.js عبر C++  
linktitle: استخدام فئة ChartGlobalizationSettings لتعيين لغة مختلفة لعنصر رسم بياني  
description: تعلم كيفية استخدام فئة ChartGlobalizationSettings في Aspose.Cells for Node.js via C++ لضبط لغات مختلفة لمكونات المخطط. سيساعدك دليلنا على فهم كيفية تخصيص عناصر المخطط، التسميات، والأساطير لعرضها بلغات مختلفة.  
keywords: Aspose.Cells for Node.js via C++، المخططات، تعريب المخطط، اللغات، التوطين، ChartGlobalizationSettings، العناصر، التسميات، الأساطير.  
type: docs  
weight: 2200  
url: /ar/nodejs-cpp/using-chartglobalizationsettings-class-to-set-different-language-for-chart-component/  
---  

## **سيناريوهات الاستخدام المحتملة**  

قامت APIs الخاصة بـ Aspose.Cells بالكشف عن فئة [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/) للتعامل مع السيناريوهات التي يرغب فيها المستخدم في تعيين مكونات المخطط إلى لغات مختلفة وتسميات مخصصة للمجاميع الفرعية في جدول البيانات.  

## **مقدمة في فئة ChartGlobalizationSettings**  

تقدم فئة [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/) حالياً الطرق الثمانية التالية والتي يمكن تجاوزها في فئة مخصصة لترجمة مثل اسم عنوان المحور، اسم وحدة المحور، اسم عنوان المخطط، وغيرها إلى لغات مختلفة.  
1. [**ChartGlobalizationSettings.getAxisTitleName()**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getAxisTitleName--): يحصل على اسم العنوان للمحور.  
1. [**ChartGlobalizationSettings.getAxisUnitName(DisplayUnitType)**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getAxisUnitName-displayunittype-): يحصل على اسم وحدة المحور.  
1. [**ChartGlobalizationSettings.getChartTitleName()**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getChartTitleName--): يحصل على اسم عنوان الرسم البياني.  
1. [**ChartGlobalizationSettings.getLegendDecreaseName()**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getLegendDecreaseName--): يحصل على اسم الانخفاض لوحة التفسير.  
1. [**ChartGlobalizationSettings.getLegendIncreaseName()**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getLegendIncreaseName--): يحصل على اسم زيادة للوسيلة التوضيحية.  
1. [**ChartGlobalizationSettings.getLegendTotalName()**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getLegendTotalName--): يحصل على اسم الإجمالي لوحة التفسير.  
1. [**ChartGlobalizationSettings.getOtherName()**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getOtherName--): يحصل على اسم تسميات "أخرى" للرسم البياني.  
1. [**ChartGlobalizationSettings.getSeriesName()**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getSeriesName--): يحصل على اسم السلاسل في الرسم البياني.  

### **ترجمة لغة مخصصة**  
هنا، سنقوم بإنشاء رسم بياني شلالي استنادًا إلى البيانات التالية. سيتم عرض أسماء مكونات الرسم البياني باللغة الإنجليزية في الرسم البياني. سنستخدم مثال باللغة التركية لنريك كيفية عرض عنوان الرسم البياني وأسماء زيادة/انخفاض لوحة التفسير واسم الإجمالي وعنوان المحور باللغة التركية.  

![todo:image_alt_text](sample.png)  

## **الكود المثالي**  
يقوم الكود العيني التالي بتحميل [ملف Excel العيني](waterfall.xlsx).  

```javascript
try {
const path = require("path");
const AsposeCells = require("aspose.cells.node");

class TurkeyChartGlobalizationSettings extends AsposeCells.ChartGlobalizationSettings {
getChartTitleName() {
return "Grafik Başlığı"; // Chart Title
}
getLegendIncreaseName() {
return "Artış"; // Increase
}
getLegendDecreaseName() {
return "Düşüş"; // Decrease
}
getLegendTotalName() {
return "Toplam"; // Total
}
getAxisTitleName() {
return "Eksen Başlığı"; // Axis Title
}
}

async function chartGlobalizationSettingsTest() {
// Create an instance of existing Workbook
const dataDir = path.join(__dirname, "data");
const pathName = path.join(dataDir, "input.xlsx");
const workbook = new AsposeCells.Workbook(pathName);

// Set custom chartGlobalizationSettings, here is TurkeyChartGlobalizationSettings
workbook.getSettings().getGlobalizationSettings().setChartSettings(new TurkeyChartGlobalizationSettings());

// Get the worksheet 
const worksheet = workbook.getWorksheets().get(0);
const chartCollection = worksheet.getCharts();

// Load the chart from source worksheet
const chart = chartCollection.get(0);

// Chart Calculate
chart.calculate();

// Get the chart title
const title = chart.getTitle();
console.log("\nWorkbook chart title: " + title.getText());

const legendEntriesLabels = chart.getLegend().getLegendLabels();

// Output the name of the Legend 
legendEntriesLabels.forEach(label => {
console.log("\nWorkbook chart legend: " + label);
```  

## الإخراج الذي تم توليده بواسطة رمز العينة  

هذا هو إنتاج الكونسول للكود العيني أعلاه.  

{{< highlight javascript >}}  

Workbook chart title: Grafik Başlığı  

Workbook chart legend: Artış  

Workbook chart legend: Düşüş  

Workbook chart legend: Toplam  

Workbook category axis title: Eksen Başlığı  

{{< /highlight >}}  

