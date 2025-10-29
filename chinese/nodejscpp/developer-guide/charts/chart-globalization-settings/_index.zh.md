---  
title: 使用ChartGlobalizationSettings类通过Node.js与C++设置图表组件的多语言  
linktitle: 使用ChartGlobalizationSettings类设置图表组件的不同语言  
description: 了解如何在Aspose.Cells for Node.js via C++中使用ChartGlobalizationSettings类为图表组件设置不同语言。我们的指南将帮助您理解如何本地化图表元素、标签和图例。  
keywords: Aspose.Cells for Node.js via C++，图表，图表全球化，语言，本地化，ChartGlobalizationSettings，元素，标签，图例。  
type: docs  
weight: 2200  
url: /zh/nodejs-cpp/using-chartglobalizationsettings-class-to-set-different-language-for-chart-component/  
---  

## **可能的使用场景**  

Aspose.Cells API已公开[**ChartGlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/)类，以应对用户希望为电子表格中的图表组件设置不同语言和自定义标签（如小计标签）的场景。  

## **ChartGlobalizationSettings类介绍**  

[**ChartGlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/)类目前提供以下8个可在自定义类中重写的方法，用于翻译如AxisTitle名称、AxisUnit名称、ChartTitle名称等到不同语言。  
1. [**ChartGlobalizationSettings.getAxisTitleName()**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getAxisTitleName--)：获取轴的标题名称。  
1. [**ChartGlobalizationSettings.getAxisUnitName(DisplayUnitType)**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getAxisUnitName-displayunittype-)：获取轴单位的名称。  
1. [**ChartGlobalizationSettings.getChartTitleName()**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getChartTitleName--)：获取图表标题的名称。  
1. [**ChartGlobalizationSettings.getLegendDecreaseName()**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getLegendDecreaseName--)：获取图例减少的名称。  
1. [**ChartGlobalizationSettings.getLegendIncreaseName()**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getLegendIncreaseName--): 获取图例中的“增加”名称。  
1. [**ChartGlobalizationSettings.getLegendTotalName()**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getLegendTotalName--)：获取图例的总名称。  
1. [**ChartGlobalizationSettings.getOtherName()**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getOtherName--)：获取图表中“其他”标签的名称。  
1. [**ChartGlobalizationSettings.getSeriesName()**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getSeriesName--)：获取图表中系列的名称。  

### **自定义语言翻译**  
在这里，我们将根据以下数据创建瀑布图。图表中将以英语显示图表组件的名称。我们将使用土耳其语示例来展示如何在图表中显示图表标题、图例增加/减少名称、总计名称和轴标题。  

![todo:image_alt_text](sample.png)  

## **示例代码**  
以下示例代码加载了[示例Excel文件](waterfall.xlsx)。  

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

## 示例代码生成的输出  

这是上述示例代码的控制台输出。  

{{< highlight javascript >}}  

Workbook chart title: Grafik Başlığı  

Workbook chart legend: Artış  

Workbook chart legend: Düşüş  

Workbook chart legend: Toplam  

Workbook category axis title: Eksen Başlığı  

{{< /highlight >}}  

{{< app/cells/assistant language="nodejs-cpp" >}}
