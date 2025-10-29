---
title: 使用ChartGlobalizationSettings类结合JavaScript通过C++设置图表组件的不同语言
linktitle: 使用ChartGlobalizationSettings类设置图表组件的不同语言
description: 了解如何在Aspose.Cells for Java脚本通过C++中使用ChartGlobalizationSettings类，为图表组件设置不同的语言。我们的指南将帮助你理解如何本地化图表元素、标签和图例。
keywords: Aspose.Cells for Java脚本通过C++，绘图，图表全球化，语言，本地化，ChartGlobalizationSettings，元素，标签，图例。
type: docs
weight: 2200
url: /zh/javascript-cpp/using-chartglobalizationsettings-class-to-set-different-language-for-chart-component/
---

## **可能的使用场景**  

Aspose.Cells API已公开[**ChartGlobalizationSettings**](https://reference.aspose.com/cells/javascript-cpp/chartglobalizationsettings/)类，以应对用户希望为电子表格中的图表组件设置不同语言和自定义标签（如小计标签）的场景。  

## **ChartGlobalizationSettings类介绍**  

[**ChartGlobalizationSettings**](https://reference.aspose.com/cells/javascript-cpp/chartglobalizationsettings/)类目前提供以下8个可在自定义类中重写的方法，用于翻译如AxisTitle名称、AxisUnit名称、ChartTitle名称等到不同语言。  
1. [**ChartGlobalizationSettings.axisTitleName**](https://reference.aspose.com/cells/javascript-cpp/chartglobalizationsettings/#axisTitleName--)：获取轴的标题名称。  
1. [**ChartGlobalizationSettings.axisUnitName(DisplayUnitType)**](https://reference.aspose.com/cells/javascript-cpp/chartglobalizationsettings/#axisUnitName-displayunittype-)：获取轴单位的名称。  
1. [**ChartGlobalizationSettings.chartTitleName**](https://reference.aspose.com/cells/javascript-cpp/chartglobalizationsettings/#chartTitleName--)：获取图表标题的名称。  
1. [**ChartGlobalizationSettings.legendDecreaseName**](https://reference.aspose.com/cells/javascript-cpp/chartglobalizationsettings/#legendDecreaseName--)：获取图例减少的名称。  
1. [**ChartGlobalizationSettings.legendIncreaseName**](https://reference.aspose.com/cells/javascript-cpp/chartglobalizationsettings/#legendIncreaseName--): 获取图例中的“增加”名称。  
1. [**ChartGlobalizationSettings.legendTotalName**](https://reference.aspose.com/cells/javascript-cpp/chartglobalizationsettings/#legendTotalName--)：获取图例的总名称。  
1. [**ChartGlobalizationSettings.otherName**](https://reference.aspose.com/cells/javascript-cpp/chartglobalizationsettings/#otherName--)：获取图表中“其他”标签的名称。  
1. [**ChartGlobalizationSettings.seriesName**](https://reference.aspose.com/cells/javascript-cpp/chartglobalizationsettings/#seriesName--)：获取图表中系列的名称。  

### **自定义语言翻译**  
在这里，我们将根据以下数据创建瀑布图。图表中将以英语显示图表组件的名称。我们将使用土耳其语示例来展示如何在图表中显示图表标题、图例增加/减少名称、总计名称和轴标题。  

![todo:image_alt_text](sample.png)  

## **示例代码**  
以下示例代码加载了[示例Excel文件](waterfall.xlsx)。  

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

## 示例代码生成的输出  

这是上述示例代码的控制台输出。  

{{< highlight javascript >}}  

Workbook chart title: Grafik Başlığı  

Workbook chart legend: Artış  

Workbook chart legend: Düşüş  

Workbook chart legend: Toplam  

Workbook category axis title: Eksen Başlığı  

{{< /highlight >}}
