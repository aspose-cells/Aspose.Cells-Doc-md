---
title: Excel 2016 Diagramme mit JavaScript via C++ lesen und bearbeiten
linktitle: Excel 2016 Diagramme lesen und bearbeiten
description: Erfahren Sie, wie Sie Excel 2016 Diagramme mit Aspose.Cells for JavaScript via C++ lesen und manipulieren. Dieser Leitfaden zeigt, wie Sie verschiedene Diagrammeigenschaften aufrufen und ändern.
keywords: Aspose.Cells for JavaScript via C++, Excel 2016 Diagramme, lesen, manipulieren, Datenbeschriftungen, Serienfarben, Layout, hierarchisches Diagramm, Kreisdiagramm.
type: docs
weight: 48
url: /de/javascript-cpp/read-and-manipulate-excel-2016-charts/
---

## **Mögliche Verwendungsszenarien**  
Aspose.Cells unterstützt jetzt das Lesen und die Manipulation von Microsoft Excel 2016-Diagrammen, die in Microsoft Excel 2013 oder früheren Versionen nicht vorhanden sind.  
## **Excel 2016 Diagramme lesen und bearbeiten**  
Der folgende Beispielcode lädt die [Quelldatei](22774101.xlsx), die Excel 2016-Diagramme im ersten Arbeitsblatt enthält. Es liest alle Diagramme nacheinander aus und ändert den Titel entsprechend ihrem Diagrammtyp. Das folgende Bildschirmfoto zeigt die Quelldatei vor der Ausführung des Codes. Wie Sie sehen können, ist der Diagrammtitel bei allen Diagrammen gleich.

![todo:image_alt_text](read-and-manipulate-excel-2016-charts_1.png)

Der folgende Screenshot zeigt die [Ausgabedatei Excel](22774104.xlsx) nach der Ausführung des Codes. Wie Sie sehen können, wurde der Diagrammtitel entsprechend seinem Diagrammtyp geändert.

![todo:image_alt_text](read-and-manipulate-excel-2016-charts_2.png)  
## **Beispielcode**  
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Read and Update Chart Titles</h1>
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

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            // Read selected file
            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet which contains the charts
            const sheet = workbook.worksheets.get(0);

            // Access all charts one by one and read their types
            const chartsCount = sheet.charts.count;
            let logHtml = '<ul>';
            for (let i = 0; i < chartsCount; i++) {
                // Access the chart
                const ch = sheet.charts.get(i);

                // Read chart type
                const typeStr = ch.type.toString();
                console.log(typeStr);

                // Change the title of the chart
                ch.title.text = "Chart Type is " + typeStr;

                logHtml += `<li>Chart ${i}: ${typeStr}</li>`;
            }
            logHtml += '</ul>';

            // Save the workbook to a downloadable file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out_excel2016Charts.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Charts updated successfully! Click the download link to get the modified file.</p>' + logHtml;
        });
    </script>
</html>
```  
## **Konsolenausgabe**  


{{< highlight javascript >}}  

 Waterfall  

Treemap  

Sunburst  

Histogram  

BoxWhisker  

{{< /highlight >}}  

## **Erweiterte Themen**  
- [Erstellung eines Wasserfalldiagramms](/cells/de/javascript-cpp/creating-waterfall-chart/)  
- [Erstellung eines TreeMap-Diagramms](/cells/de/javascript-cpp/creating-treemap-chart/)  
- [Erstellung eines Sunburst-Diagramms](/cells/de/javascript-cpp/creating-sunburst-chart/)
