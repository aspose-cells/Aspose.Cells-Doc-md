---
title: Erhalten Sie den Gleichungstext der Trendlinie im Diagramm mit JavaScript via C++
description: Erfahren Sie, wie Sie das Aspose.Cells for JavaSkript via C++ verwenden, um den Gleichungstext einer Trendlinie in einem in Microsoft Excel erstellten Diagramm abzurufen. Unser Leitfaden zeigt, wie man die Gleichung einer Trendlinie für weitere Analysen oder die Anzeige zugänglich macht.
keywords: Aspose.Cells for JavaSkript via C++, Diagramm Trendlinie, Gleichungstext, Microsoft Excel, Datenanalyse, Anzeige.
linktitle: Trendlinien
type: docs
weight: 110
url: /de/javascript-cpp/get-equation-text-of-chart-trendline/
---

{{% alert color="primary" %}}

Sie können den Gleichungstext der Diagramm-Trendlinie mit Aspose.Cells for JavaSkript via C++ abrufen. Aspose.Cells bietet die [**DataLabels.text**](https://reference.aspose.com/cells/javascript-cpp/datalabels/#text--)-Eigenschaft, die den Gleichungstext der Diagramm-Trendlinie zurückgibt. Um diese Eigenschaft zu verwenden, müssen Sie zuerst die [**Chart.calculate()**](https://reference.aspose.com/cells/javascript-cpp/chart/#calculate--)-Methode aufrufen.

{{% /alert %}}

Das folgende Bildschirmfoto zeigt das Diagramm mit einer Trendlinie, deren Gleichungstext in roter Farbe angezeigt wird. Wir werden diesen Text mit der [**DataLabels.text**](https://reference.aspose.com/cells/javascript-cpp/datalabels/#text--)-Eigenschaft im folgenden Beispielcode abrufen.

![todo:image_alt_text](get-equation-text-of-chart-trendline_1.png)

## JavaScript-Code, um den Gleichungstext der Diagramm-Trendlinie zu erhalten

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Read Trendline Equation Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access the first chart inside the worksheet
            const chart = worksheet.charts.get(0);

            // Calculate the Chart to get the Equation Text of Trendline
            chart.calculate();

            // Access the Trendline
            const trendLine = chart.nSeries.get(0).trendLines.get(0);

            // Read the Equation Text of Trendline
            const equationText = trendLine.dataLabels.text;

            document.getElementById('result').innerHTML = `<p>Equation Text: ${equationText}</p>`;
        });
    </script>
</html>
```

## Ausgabe, die vom Beispielcode generiert wurde

Dies ist die Konsolenausgabe des obigen Beispiels.

{{< highlight javascript >}}

Equation Text: y = 8.1333x + 5

{{< /highlight >}}
