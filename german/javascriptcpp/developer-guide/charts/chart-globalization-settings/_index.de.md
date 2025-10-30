---
title: Verwendung der ChartGlobalizationSettings Klasse, um mit JavaScript via C++ unterschiedliche Sprachen für Diagrammelemente einzustellen
linktitle: Verwendung der ChartGlobalizationSettings Klasse zum Einstellen einer anderen Sprache für das Diagrammkomponente
description: Erfahren Sie, wie Sie die ChartGlobalizationSettings Klasse in Aspose.Cells for JavaScript via C++ verwenden, um verschiedene Sprachen für Diagrammelemente festzulegen. Unser Leitfaden hilft Ihnen, Diagrammelemente, Beschriftungen und Legenden zu lokalisieren.
keywords: Aspose.Cells for JavaSkript via C++, Diagramme, Diagrammlokalisierung, Sprachen, Lokalisierung, ChartGlobalizationSettings, Elemente, Beschriftungen, Legenden.
type: docs
weight: 2200
url: /de/javascript-cpp/using-chartglobalizationsettings-class-to-set-different-language-for-chart-component/
---

## **Mögliche Verwendungsszenarien**  

Die Aspose.Cells APIs haben die [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/javascript-cpp/chartglobalizationsettings/) Klasse bereitgestellt, um Szenarien zu behandeln, in denen der Benutzer Diagrammelemente auf verschiedene Sprachen einstellen und benutzerdefinierte Beschriftungen für Zwischensummen in einer Tabelle erstellen möchte.  

## **Einführung in die ChartGlobalizationSettings-Klasse**  

Die [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/javascript-cpp/chartglobalizationsettings/) Klasse bietet derzeit die folgenden 8 Methoden, die in einer benutzerdefinierten Klasse überschrieben werden können, um z. B. den AxisTitle Namen, AxisUnit Namen, ChartTitle Namen usw. in verschiedene Sprachen zu übersetzen.  
1. [**ChartGlobalizationSettings.axisTitleName**](https://reference.aspose.com/cells/javascript-cpp/chartglobalizationsettings/#axisTitleName--): Gibt den Titel für die Achse zurück.  
1. [**ChartGlobalizationSettings.axisUnitName(DisplayUnitType)**](https://reference.aspose.com/cells/javascript-cpp/chartglobalizationsettings/#axisUnitName-displayunittype-): Gibt den Namen der Achseneinheit zurück.  
1. [**ChartGlobalizationSettings.chartTitleName**](https://reference.aspose.com/cells/javascript-cpp/chartglobalizationsettings/#chartTitleName--): Gibt den Titel des Diagramms zurück.  
1. [**ChartGlobalizationSettings.legendDecreaseName**](https://reference.aspose.com/cells/javascript-cpp/chartglobalizationsettings/#legendDecreaseName--): Gibt den Namen der Abnahme für die Legende zurück.  
1. [**ChartGlobalizationSettings.legendIncreaseName**](https://reference.aspose.com/cells/javascript-cpp/chartglobalizationsettings/#legendIncreaseName--): Holt den Namen von Increase für Legenden.  
1. [**ChartGlobalizationSettings.legendTotalName**](https://reference.aspose.com/cells/javascript-cpp/chartglobalizationsettings/#legendTotalName--): Gibt den Namen des Gesamtwerts für die Legende zurück.  
1. [**ChartGlobalizationSettings.otherName**](https://reference.aspose.com/cells/javascript-cpp/chartglobalizationsettings/#otherName--): Gibt den Namen der "Andere"-Beschriftungen für das Diagramm zurück.  
1. [**ChartGlobalizationSettings.seriesName**](https://reference.aspose.com/cells/javascript-cpp/chartglobalizationsettings/#seriesName--): Gibt den Namen der Serie im Diagramm zurück.  

### **Benutzerdefinierte Sprachübersetzung**  
Hier erstellen wir ein Wasserfalldiagramm basierend auf den folgenden Daten. Die Namen der Diagrammkomponenten werden im Diagramm auf Englisch angezeigt. Wir verwenden ein Beispiel für die türkische Sprache, um zu zeigen, wie der Diagrammtitel, die Legenden-Abnahme/Zunahme-Namen, der Gesamtwert und der Achsentitel auf Türkisch angezeigt werden.  

![todo:image_alt_text](sample.png)  

## **Beispielcode**  
Der folgende Beispielcode lädt die [Beispieldatei Excel](waterfall.xlsx).  

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

## Ausgabe, die vom Beispielcode generiert wurde  

Dies ist die Konsolenausgabe des obigen Beispiels.  

{{< highlight javascript >}}  

Workbook chart title: Grafik Başlığı  

Workbook chart legend: Artış  

Workbook chart legend: Düşüş  

Workbook chart legend: Toplam  

Workbook category axis title: Eksen Başlığı  

{{< /highlight >}}
