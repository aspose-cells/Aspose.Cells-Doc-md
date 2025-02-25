---  
title: Using ChartGlobalizationSettings Class to Set Different Language for Chart Component with Node.js via C++  
linktitle: Using ChartGlobalizationSettings Class to Set Different Language for Chart Component  
description: Learn how to use the ChartGlobalizationSettings class in Aspose.Cells for Node.js via C++ to set different languages for chart components. Our guide will help you understand how to localize chart elements, labels, and legends.  
keywords: Aspose.Cells for Node.js via C++, charting, chart globalization, languages, localization, ChartGlobalizationSettings, elements, labels, legends.  
type: docs  
weight: 2200  
url: /nodejs-cpp/using-chartglobalizationsettings-class-to-set-different-language-for-chart-component/  
---  

## **Possible Usage Scenarios**  

Aspose.Cells APIs have exposed the [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/) class in order to deal with the scenarios where the user wishes to set chart component to different languages and custom labels for Subtotals in a spreadsheet.  

## **Introduction to ChartGlobalizationSettings Class**  

The [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/) class currently offers the following 8 methods which can be overridden in a custom class to translate such as AxisTitle name, AxisUnit name, ChartTitle name, and so on to different languages.  
1. [**getAxisTitleName**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getAxisTitleName): Gets the name of Title for Axis.  
1. [**getAxisUnitName**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getAxisUnitName): Gets the Name of Axis Unit.  
1. [**getChartTitleName**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getChartTitleName): Gets the name of Chart Title.  
1. [**getLegendDecreaseName**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getLegendDecreaseName): Gets the name of Decrease for Legend.  
1. [**getLegendIncreaseName**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getLegendIncreaseName): Gets the name of Increase for Legend.  
1. [**getLegendTotalName**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getLegendTotalName): Gets the name of Total for Legend.  
1. [**getOtherName**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getOtherName): Gets the name of "Other" labels for Chart.  
1. [**getSeriesName**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getSeriesName): Gets the name of Series in the Chart.  

### **Custom language translation**  
Here, we will create a waterfall chart based on the following data. The names of chart components will be displayed in English in the chart. We will use a Turkish language example to show how to display the Chart Title, Legend Increase/Decrease names, Total name, and Axis Title in Turkish.  

![todo:image_alt_text](sample.png)  

## **Sample Code**  
The following sample code loads the [sample Excel file](waterfall.xlsx).  

```javascript
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
    });

    // Output the name of the Axis title 
    const categoryAxisTitle = chart.getCategoryAxis().getTitle();
    console.log("\nWorkbook category axis title: " + categoryAxisTitle.getText());
}

chartGlobalizationSettingsTest();
```  

## Output generated by the sample code  

This is the console output of the above sample code.  

{{< highlight javascript >}}  

Workbook chart title: Grafik Başlığı  

Workbook chart legend: Artış  

Workbook chart legend: Düşüş  

Workbook chart legend: Toplam  

Workbook category axis title: Eksen Başlığı  

{{< /highlight >}}  
  