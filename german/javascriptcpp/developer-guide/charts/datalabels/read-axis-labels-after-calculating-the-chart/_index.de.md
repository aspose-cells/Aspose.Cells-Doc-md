---
title: Achsenbeschriftungen nach der Diagrammberechnung mit JavaScript via C++ lesen
linktitle: Achsenbeschriftungen nach Berechnen des Diagramms lesen
description: Erfahren Sie, wie Sie Achsenbeschriftungen in Aspose.Cells for JavaScript via C++ nach der Diagrammberechnung lesen. Unser Leitfaden zeigt, wie Sie auf Achsenbeschriftungen zugreifen und diese abrufen, einschließlich ihrer Formatierung und Positionierung.
keywords: Aspose.Cells for JavaScript, Diagramm, Achsenbeschriftungen, Berechnung, Lesen, Zugriff, Abrufen, Formatierung, Positionierung, JavaScript via C++
type: docs
weight: 90
url: /de/javascript-cpp/read-axis-labels-after-calculating-the-chart/
---

## **Mögliche Verwendungsszenarien**

Sie können die Achsenbeschriftungen Ihres Diagramms nach der Berechnung der Werte mit der [**Chart.calculate()**](https://reference.aspose.com/cells/javascript-cpp/chart/#calculate--)-Methode lesen. Bitte verwenden Sie die [**Axis.axisTexts**](https://reference.aspose.com/cells/javascript-cpp/axis/#axisTexts--)-Eigenschaft dafür, die die Liste der Achsenbeschriftungen zurückgibt.

## **Lesen Sie die Achsenbeschriftungen nach der Berechnung des Diagramms**

Siehe bitte den folgenden Beispielcode, der die [Beispieldatei für Excel](ReadAxisLabels.xlsx) lädt und die Kategorienachsenbeschriftungen des Diagramms im ersten Arbeitsblatt liest. Anschließend werden die Werte der Achsenbeschriftungen in der Konsole ausgegeben. Bitte sehen Sie sich die Konsolenausgabe des untenstehenden Beispielcodes als Referenz an.

## **Beispielcode**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Read Axis Labels</title>
    </head>
    <body>
        <h1>Read Chart Category Axis Labels</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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
            resultDiv.innerHTML = '';

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access the chart
            const chart = worksheet.charts.get(0);

            // Calculate the chart
            chart.calculate();

            // Read axis labels of category axis
            const lstLabels = chart.categoryAxis.axisTexts;

            // Display axis labels
            let html = '<h2>Category Axis Labels:</h2>';
            html += '<hr/>';
            if (!lstLabels || !lstLabels.length) {
                html += '<p>No axis labels found.</p>';
            } else {
                html += '<ul>';
                for (let i = 0; i < lstLabels.length; i++) {
                    console.log(lstLabels[i]);
                    html += `<li>${lstLabels[i]}</li>`;
                }
                html += '</ul>';
            }
            resultDiv.innerHTML = html;
        });
    </script>
</html>
```

## **Konsolenausgabe**

{{< highlight javascript >}}  
 Category Axis Labels:  

\---------------------  

Iran  

China  

USA  

Brazil  

England  
{{< /highlight >}}
