---
title: Använda ChartGlobalizationSettings klass för att ställa in olika språk för diagramkomponenten med JavaScript via C++
linktitle: Utvecklare kan inte bara kontrollera synligheten av stora rutnätlinjer utan också andra egenskaper inklusive dess färg osv.
description: Lär dig hur du använder ChartGlobalizationSettings klass i Aspose.Cells for JavaScript via C++ för att ställa in olika språk för diagramkomponenter. Vår guide hjälper dig att förstå hur du lokaliserar diagram element, etiketter och legend.
keywords: Aspose.Cells for JavaScript via C++, diagram, globalisering av diagram, språk, lokalisering, ChartGlobalizationSettings, element, etiketter, legender.
type: docs
weight: 2200
url: /sv/javascript-cpp/using-chartglobalizationsettings-class-to-set-different-language-for-chart-component/
---

## **Möjliga användningsscenario**  

Aspose.Cells API:er har exponerat [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/javascript-cpp/chartglobalizationsettings/)-klassen för att hantera scenarier där användaren vill ställa in diagramkomponenter till olika språk och anpassade etiketter för deltotaler i ett kalkylblad.  

## **Introduktion till ChartGlobalizationSettings-klassen**  

Klass [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/javascript-cpp/chartglobalizationsettings/) erbjuder för närvarande följande 8 metoder som kan åsidosättas i en anpassad klass för att översätta till exempel AxisTitle-namn, AxisUnit-namn, ChartTitle-namn och så vidare till olika språk.  
1. [**ChartGlobalizationSettings.axisTitleName**](https://reference.aspose.com/cells/javascript-cpp/chartglobalizationsettings/#axisTitleName--): Hämtar namnet på titeln för axeln.  
1. [**ChartGlobalizationSettings.axisUnitName(DisplayUnitType)**](https://reference.aspose.com/cells/javascript-cpp/chartglobalizationsettings/#axisUnitName-displayunittype-): Hämtar namnet på axelenhet.  
1. [**ChartGlobalizationSettings.chartTitleName**](https://reference.aspose.com/cells/javascript-cpp/chartglobalizationsettings/#chartTitleName--): Hämtar namnet på diagramtiteln.  
1. [**ChartGlobalizationSettings.legendDecreaseName**](https://reference.aspose.com/cells/javascript-cpp/chartglobalizationsettings/#legendDecreaseName--): Hämtar namnet på minskningen för förklaringen.  
1. [**ChartGlobalizationSettings.legendIncreaseName**](https://reference.aspose.com/cells/javascript-cpp/chartglobalizationsettings/#legendIncreaseName--): Hämtar namnet på Increase för Legend.  
1. [**ChartGlobalizationSettings.legendTotalName**](https://reference.aspose.com/cells/javascript-cpp/chartglobalizationsettings/#legendTotalName--): Hämtar namnet på totalen för förklaringen.  
1. [**ChartGlobalizationSettings.otherName**](https://reference.aspose.com/cells/javascript-cpp/chartglobalizationsettings/#otherName--): Hämtar namnet på "Annan" etiketter för diagrammet.  
1. [**ChartGlobalizationSettings.seriesName**](https://reference.aspose.com/cells/javascript-cpp/chartglobalizationsettings/#seriesName--): Hämtar namnet på serier i diagrammet.  

### **Anpassad språköversättning**  
Här kommer vi att skapa en stapeldiagram baserat på följande data. Namnen på diagramkomponenterna kommer att visas på engelska i diagrammet. Vi kommer att använda ett turkiskt språkexempel för att visa hur man visar diagramtitel, förklarings-ökning/minskning, totalt namn och axelns titel på turkiska.  

![todo:image_alt_text](sample.png)  

## **Exempelkod**  
Följande exempelkod laddar [prov Excel-filen](vattenfall.xlsx).  

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

## Utdata genererad av provkoden  

Detta är konsoloutputen för ovanstående exempelkod.  

{{< highlight javascript >}}  

Workbook chart title: Grafik Başlığı  

Workbook chart legend: Artış  

Workbook chart legend: Düşüş  

Workbook chart legend: Toplam  

Workbook category axis title: Eksen Başlığı  

{{< /highlight >}}
