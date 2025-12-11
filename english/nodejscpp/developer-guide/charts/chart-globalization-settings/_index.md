---  
title: Using ChartGlobalizationSettings Class to Set Different Language for Chart Component with Node.js via C++  
linktitle: Using ChartGlobalizationSettings Class to Set Different Language for Chart Component  
description: Learn how to use the ChartGlobalizationSettings class in Aspose.Cells for Node.js via C++ to set different languages for chart components. Our guide will help you understand how to localize chart elements, labels, and legends.  
keywords: Aspose.Cells for Node.js via C++, charting, chart globalization, languages, localization, ChartGlobalizationSettings, elements, labels, legends.  
type: docs  
weight: 2200  
url: /nodejs-cpp/using-chartglobalizationsettings-class-to-set-different-language-for-chart-component/  
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

## **Possible Usage Scenarios**  

Aspose.Cells APIs have exposed the [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/) class in order to deal with scenarios where the user wishes to set chart components to different languages and custom labels for subtotals in a spreadsheet.  

## **Introduction to ChartGlobalizationSettings Class**  

The [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/) class currently offers the following eight methods, which can be overridden in a custom class to translate items such as AxisTitle name, AxisUnit name, ChartTitle name, and so on, to different languages.  
1. [**ChartGlobalizationSettings.getAxisTitleName()**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getAxisTitleName--): Gets the name of the title for an axis.  
1. [**ChartGlobalizationSettings.getAxisUnitName(DisplayUnitType)**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getAxisUnitName-displayunittype-): Gets the name of the axis unit.  
1. [**ChartGlobalizationSettings.getChartTitleName()**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getChartTitleName--): Gets the name of the chart title.  
1. [**ChartGlobalizationSettings.getLegendDecreaseName()**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getLegendDecreaseName--): Gets the name of “Decrease” for the legend.  
1. [**ChartGlobalizationSettings.getLegendIncreaseName()**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getLegendIncreaseName--): Gets the name of “Increase” for the legend.  
1. [**ChartGlobalizationSettings.getLegendTotalName()**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getLegendTotalName--): Gets the name of “Total” for the legend.  
1. [**ChartGlobalizationSettings.getOtherName()**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getOtherName--): Gets the name of “Other” labels for the chart.  
1. [**ChartGlobalizationSettings.getSeriesName()**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getSeriesName--): Gets the name of a series in the chart.  

### **Custom language translation**  
Here, we will create a waterfall chart based on the following data. The names of chart components will be displayed in English in the chart. We will use a Turkish language example to show how to display the chart title, legend increase/decrease names, total name, and axis title in Turkish.  

![todo:image_alt_text](sample.png)  

## **Sample Code**  
The following sample code loads the [sample Excel file](waterfall.xlsx).  

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
        // Create an instance of an existing workbook
        const dataDir = path.join(__dirname, "data");
        const pathName = path.join(dataDir, "input.xlsx");
        const workbook = new AsposeCells.Workbook(pathName);

        // Set custom chart globalization settings; here we use TurkeyChartGlobalizationSettings
        workbook.getSettings().getGlobalizationSettings().setChartSettings(new TurkeyChartGlobalizationSettings());

        // Get the worksheet 
        const worksheet = workbook.getWorksheets().get(0);
        const chartCollection = worksheet.getCharts();

        // Load the chart from the source worksheet
        const chart = chartCollection.get(0);

        // Calculate the chart
        chart.calculate();

        // Get the chart title
        const title = chart.getTitle();
        console.log("\nWorkbook chart title: " + title.getText());

        const legendEntriesLabels = chart.getLegend().getLegendLabels();

        // Output the names of the legend entries
        legendEntriesLabels.forEach(label => {
            console.log("\nWorkbook chart legend: " + label);
        });
    }
} catch (e) {
    console.error(e);
}
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
  
{{< app/cells/assistant language="nodejs-cpp" >}}
