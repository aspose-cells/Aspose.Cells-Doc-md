---
title: Hämta ekvationen Text av diagramtrendlinje med JavaScript via C++
description: Lär dig hur du använder Aspose.Cells for JavaScript via C++ för att hämta ekvationstexten av en trendlinje i ett diagram skapat i Microsoft Excel. Vår guide visar hur man får åtkomst till och extraherar ekvationen för en trendlinje för vidare analys eller visning.
keywords: Aspose.Cells for JavaScript via C++, Diagramtrendlinje, Ekvationstext, Microsoft Excel, Dataanalys, Visning.
linktitle: Trendlinjer
type: docs
weight: 110
url: /sv/javascript-cpp/get-equation-text-of-chart-trendline/
---

{{% alert color="primary" %}}

Du kan hämta ekvationstexten av diagramtrendlinje med Aspose.Cells for JavaScript via C++. Aspose.Cells erbjuder [**DataLabels.text**](https://reference.aspose.com/cells/javascript-cpp/datalabels/#text--) egenskapen som returnerar ekvationstexten av diagramtrendlinjen. För att använda denna egenskap måste du först anropa [**Chart.calculate()**](https://reference.aspose.com/cells/javascript-cpp/chart/#calculate--) metod.

{{% /alert %}}

Följande skärm visar diagrammet med en trendlinje och dess ekvationstext visas i röd färg. Vi kommer att hämta denna text med hjälp av [**DataLabels.text**](https://reference.aspose.com/cells/javascript-cpp/datalabels/#text--) egenskapen i följande kodexempel.

![todo:image_alt_text](get-equation-text-of-chart-trendline_1.png)

## JavaScript kod för att få ekvationstexten av diagramtrendlinje

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

## Utdata genererad av provkoden

Detta är konsoloutputen för ovanstående exempelkod.

{{< highlight javascript >}}

Equation Text: y = 8.1333x + 5

{{< /highlight >}}
