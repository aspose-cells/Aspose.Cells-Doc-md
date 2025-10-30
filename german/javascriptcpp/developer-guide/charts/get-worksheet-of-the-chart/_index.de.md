---
title: Erhalten Sie das Arbeitsblatt des Diagramms mit JavaScript via C++
linktitle: Arbeitsblatt des Diagramms abrufen
description: Erfahren Sie, wie Sie das mit einem Excel Diagramm verbundene Arbeitsblatt mit Aspose.Cells for JavaScript via C++ abrufen. Zugriff auf die zugrunde liegenden Daten des Diagramms und Manipulation dieser Daten effizient durchführen.
keywords: Aspose.Cells for JavaScript, Excel Diagramme, Arbeitsblätter, Datenmanipulation, zugrunde liegende Daten, Operationen, JavaScript via C++
type: docs
weight: 1000
url: /de/javascript-cpp/get-worksheet-of-the-chart/
---

{{% alert color="primary" %}}

Manchmal möchten Sie auf ein Arbeitsblatt über einen Diagrammverweis zugreifen. Aspose.Cells bietet die [**Chart.worksheet**](https://reference.aspose.com/cells/javascript-cpp/chart/#worksheet--)-Eigenschaft, die den Verweis auf das Arbeitsblatt zurückgibt, das das Diagramm enthält.

{{% /alert %}}

Das folgende Beispiel zeigt, wie die [**Chart.worksheet**](https://reference.aspose.com/cells/javascript-cpp/chart/#worksheet--)-Eigenschaft verwendet wird. Der Code gibt zuerst den Namen des Arbeitsblatts aus, greift dann auf das erste Diagramm im Arbeitsblatt zu und gibt den Namen des Arbeitsblatts erneut aus, diesmal mit der [**Chart.worksheet**](https://reference.aspose.com/cells/javascript-cpp/chart/#worksheet--)-Eigenschaft.

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

Unten ist die Konsolenausgabe, die das Beispiel des Codes ergibt. Wie Sie sehen können, druckt es den Arbeitsblattnamen beide Male gleich aus.

{{< highlight javascript >}}

Sheet Name: Portfolio

Chart's Sheet Name: Portfolio

{{< /highlight >}}
