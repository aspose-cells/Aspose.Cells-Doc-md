---
title: Using ChartGlobalizationSettings Class to Set Different Languages for Chart Components with JavaScript via C++
linktitle: Using ChartGlobalizationSettings Class to Set Different Languages for Chart Components
description: Learn how to use the ChartGlobalizationSettings class in Aspose.Cells for JavaScript via C++ to set different languages for chart components. Our guide will help you understand how to localize chart elements, labels, and legends.
keywords: Aspose.Cells for JavaScript via C++, charting, chart globalization, languages, localization, ChartGlobalizationSettings, elements, labels, legends.
type: docs
weight: 2200
url: /javascript-cpp/using-chartglobalizationsettings-class-to-set-different-language-for-chart-component/
---

## **Possible Usage Scenarios**  

Aspose.Cells APIs have exposed the [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/javascript-cpp/chartglobalizationsettings/) class to address scenarios where the user wishes to set chart components to different languages and provide custom labels for subtotals in a spreadsheet.  

## **Introduction to ChartGlobalizationSettings Class**  

The [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/javascript-cpp/chartglobalizationsettings/) class currently offers the following eight methods, which can be overridden in a custom class to translate items such as the AxisTitle name, AxisUnit name, ChartTitle name, and so on into different languages.  

1. **ChartGlobalizationSettings.axisTitleName**: Gets the title name for an axis.  
2. **ChartGlobalizationSettings.axisUnitName(DisplayUnitType)**: Gets the name of an axis unit.  
3. **ChartGlobalizationSettings.chartTitleName**: Gets the chart title name.  
4. **ChartGlobalizationSettings.legendDecreaseName**: Gets the name for the decrease label in the legend.  
5. **ChartGlobalizationSettings.legendIncreaseName**: Gets the name for the increase label in the legend.  
6. **ChartGlobalizationSettings.legendTotalName**: Gets the name for the total label in the legend.  
7. **ChartGlobalizationSettings.otherName**: Gets the name of the “Other” label for the chart.  
8. **ChartGlobalizationSettings.seriesName**: Gets the series name in the chart.  

### **Custom language translation**  
Here, we will create a waterfall chart based on the following data. The names of chart components will be displayed in English by default. We will use a Turkish-language example to show how to display the chart title, legend increase/decrease names, total name, and axis title in Turkish.  

![todo:image_alt_text](sample.png)  

## **Sample Code**  
The following sample code loads the [sample Excel file](waterfall.xlsx).  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Chart Globalization Settings Example</title>
    </head>
    <body>
        <h1>Chart Globalization Settings Example (Turkey)</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;
        
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        // Define TurkeyChartGlobalizationSettings by converting getXxx methods to properties
        class TurkeyChartGlobalizationSettings extends AsposeCells.ChartGlobalizationSettings {
            constructor() {
                super();
                this.chartTitleName = "Grafik Başlığı"; // Chart Title
                this.legendIncreaseName = "Artış"; // Increase
                this.legendDecreaseName = "Düşüş"; // Decrease
                this.legendTotalName = "Toplam"; // Total
                this.axisTitleName = "Eksen Başlığı"; // Axis Title
            }
        }

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '';

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            // No try-catch: let errors propagate
            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Set custom chartGlobalizationSettings (Turkey)
            workbook.settings.globalizationSettings.chartSettings = new TurkeyChartGlobalizationSettings();

            // Access the first worksheet and its charts
            const worksheet = workbook.worksheets.get(0);
            const chartCollection = worksheet.charts;
            const chart = chartCollection.get(0);

            // Calculate the chart
            chart.calculate();

            // Get the chart title text
            const title = chart.title;
            const titleText = title ? title.text : "(No Title)";
            
            // Prepare output messages
            const messages = [];
            messages.push('<p style="color: green;">Operation completed successfully!</p>');
            messages.push(`<p>Workbook chart title: ${titleText}</p>`);

            // Get legend labels and output them
            const legendEntriesLabels = chart.legend.legendLabels;
            if (legendEntriesLabels && legendEntriesLabels.forEach) {
                const legendItems = [];
                legendEntriesLabels.forEach(label => {
                    legendItems.push(`<li>${label}</li>`);
                });
                if (legendItems.length) {
                    messages.push('<p>Workbook chart legend:</p>');
                    messages.push(`<ul>${legendItems.join('')}</ul>`);
                } else {
                    messages.push('<p>(No legend labels found)</p>');
                }
            } else {
                messages.push('<p>(No legend or legend labels available)</p>');
            }

            // Save modified workbook to allow download (optional)
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = messages.join('');
        });
    </script>
</html>
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