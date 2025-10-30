---
title: Hämta Arbetsblad för Diagrammet med JavaScript via C++
linktitle: Hämta kalkylbladet för diagrammet
description: Lär dig att hämta arbetsbladet som är kopplat till ett Excel diagram med Aspose.Cells for JavaScript via C++. Anslut och manipulera diagrammets underliggande data effektivt.
keywords: Aspose.Cells for JavaScript, Excel diagram, arbetsblad, datamanipulation, underliggande data, operationer, JavaScript via C++
type: docs
weight: 1000
url: /sv/javascript-cpp/get-worksheet-of-the-chart/
---

{{% alert color="primary" %}}

Ibland vill du komma åt ett kalkylblad från ett diagrams referens. Aspose.Cells tillhandahåller egenskapen [**Chart.worksheet**](https://reference.aspose.com/cells/javascript-cpp/chart/#worksheet--) som returnerar referensen till kalkylbladet som innehåller diagrammet.

{{% /alert %}}

Följande exempel visar hur man använder [**Chart.worksheet**](https://reference.aspose.com/cells/javascript-cpp/chart/#worksheet--)-egenskapen. Koden skriver först ut namnet på arbetsbladet, sedan hämtar den det första diagrammet på arbetsbladet. Den skriver sedan ut arbetsbladets namn igen, med hjälp av [**Chart.worksheet**](https://reference.aspose.com/cells/javascript-cpp/chart/#worksheet--)-egenskapen.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Example Title</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Print worksheet name
            const sheetName = worksheet.name;
            let outputHtml = `<p>Sheet Name: ${sheetName}</p>`;

            // Access the first chart inside this worksheet
            const charts = worksheet.charts;
            if (charts.count > 0) {
                const chart = charts.get(0);

                // Access the chart's sheet and display its name again
                const chartSheetName = chart.worksheet.name;
                outputHtml += `<p>Chart's Sheet Name: ${chartSheetName}</p>`;
            } else {
                outputHtml += `<p>No charts available in the worksheet.</p>`;
            }

            document.getElementById('result').innerHTML = outputHtml;
        });
    </script>
</html>
```

Nedan är konsolresultatet som exempelkoden leder till. Som du kan se skriver den ut arbetsbladsnamnet samma namn båda gångerna.

{{< highlight javascript >}}

Sheet Name: Portfolio

Chart's Sheet Name: Portfolio

{{< /highlight >}}
