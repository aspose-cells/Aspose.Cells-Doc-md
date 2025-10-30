---
title: Bestimmen Sie den Typ der X und Y Werte von Punkten in Diagrammserien mit JavaScript via C++
linktitle: Suchen Sie nach dem Typ von X und Y Werten der Punkte in der Diagrammserie
description: Lernen Sie, wie Sie den Typ der X und Y Werte in Diagrammserienpunkten mit Aspose.Cells for JavaScript via C++ feststellen. Diese Anleitung erklärt die Datenarten und wie Sie sie in Ihren Diagrammen abrufen und bearbeiten.
keywords: Aspose.Cells for JavaScript via C++, Diagrammerstellung, X Werte, Y Werte, Datentypen, Zugriff, Bearbeitung, Diagrammserien.
type: docs
weight: 150
url: /de/javascript-cpp/find-type-of-x-and-y-values-of-points-in-chart-series/
---

## **Mögliche Verwendungsszenarien**  
 Manchmal möchten Sie den Typ der X- und Y-Werte von Punkten in einer Serie kennen. Aspose.Cells for JavaScript via C++ bietet die Eigenschaften `ChartPoint.XValueType` und `ChartPoint.YValueType` dafür an. Bitte beachten Sie, dass Sie die Methode `Chart.calculate()` aufrufen müssen, bevor Sie diese Eigenschaften effektiv nutzen können.  

## **Typen von X- und Y-Werten von Punkten in Diagrammserien herausfinden**  
Der folgende Beispielcode lädt die [Beispieldatei Excel](64716905.xlsx) und greift auf das erste Diagramm im ersten Arbeitsblatt zu. Anschließend ruft er die Methode `Chart.calculate()` auf und ermittelt den Typ der X- und Y-Werte des ersten Diagrammpunkts, den er in der Konsole ausgibt. Bitte sehen Sie sich die unten angezeigte Konsolenausgabe zur Referenz an.  

## **Beispielcode**  
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Find Type Of X and Y Values Of Points In Chart Series</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object using the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet.
            const worksheet = workbook.worksheets.get(0);

            // Access first chart.
            const chart = worksheet.charts.get(0);

            // Calculate chart data.
            chart.calculate();

            // Access first chart point in the first series.
            const point = chart.nSeries.get(0).points.get(0);

            // Get the types of X and Y values of chart point.
            const xValueType = point.xValueType;
            const yValueType = point.yValueType;

            // Display results
            document.getElementById('result').innerHTML = `
                <p style="color: green;">Operation completed successfully!</p>
                <p>X Value Type: ${xValueType}</p>
                <p>Y Value Type: ${yValueType}</p>
            `;
        });
    </script>
</html>
```  

## **Konsolenausgabe**  

{{< highlight java >}}  
 X Value Type: IsString  

Y Value Type: IsNumeric  
{{< /highlight >}}
