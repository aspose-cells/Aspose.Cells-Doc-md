---
title: Bestimmen, welche Achse im Diagramm existiert mit JavaScript via C++
linktitle: Bestimmen Sie, welche Achse im Diagramm vorhanden ist
description: Lernen Sie, wie man bestimmt, welche Achse in einem mit Aspose.Cells for JavaScript und C++ erstellten Diagramm existiert. Unser Leitfaden hilft Ihnen, die verschiedenen Achsen in einem Diagramm zu identifizieren und zuzugreifen, einschließlich Kategorie , Wert und Sekundärachsen.
keywords: Aspose.Cells for JavaScript mit C++, Diagramm, Achse, Existenz, Kategorie, Wert, sekundär.
type: docs
weight: 140
url: /de/javascript-cpp/determine-which-axis-exists-in-the-chart/
---

{{% alert color="primary" %}}  
Manchmal muss der Nutzer wissen, ob eine bestimmte Achse im Diagramm vorhanden ist. Zum Beispiel, ob eine Sekundär-Wertachse im Diagramm vorhanden ist oder nicht. Einige Diagramme wie Kreis, Explodierter Kreis, Pfeil-Kreis, Kreisbalken, 3D-Kreis, 3D-Explodierter Kreis, Donut, Explodierter Donut usw. haben keine Achse.  

Aspose.Cells stellt die Methode [**Chart.hasAxis(axisType, isPrimary)**](https://reference.aspose.com/cells/javascript-cpp/chart/#hasAxis-AxisType-boolean-) bereit, um festzustellen, ob das Diagramm eine bestimmte Achse hat oder nicht.  
{{% /alert %}}  

Das folgende Beispiel zeigt, wie [**Chart.hasAxis(axisType, isPrimary)**](https://reference.aspose.com/cells/javascript-cpp/chart/#hasAxis-AxisType-boolean-) verwendet wird, um zu bestimmen, ob das Beispiel-Diagramm primäre und sekundäre Kategorie- und Wertachsen hat.  

## JavaScript-Code, um zu bestimmen, welche Achse im Diagramm existiert

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Check Chart Axes Example</h1>
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
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Create workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Check if there are any charts before accessing
            const charts = worksheet.charts;
            if (charts.count === 0) {
                resultDiv.innerHTML = '<p>No charts found in the worksheet.</p>';
                return;
            }

            // Access the chart
            const chart = charts.get(0);

            // Determine which axis exists in chart
            let outputs = [];
            let ret = chart.hasAxis(AsposeCells.AxisType.Category, true);
            outputs.push("Has Primary Category Axis: " + ret);

            ret = chart.hasAxis(AsposeCells.AxisType.Category, false);
            outputs.push("Has Secondary Category Axis: " + ret);

            ret = chart.hasAxis(AsposeCells.AxisType.Value, true);
            outputs.push("Has Primary Value Axis: " + ret);

            ret = chart.hasAxis(AsposeCells.AxisType.Value, false);
            outputs.push("Has Secondary Value Axis: " + ret);

            resultDiv.innerHTML = '<p>' + outputs.join('</p><p>') + '</p>';
        });
    </script>
</html>
```

## Von dem Beispielcode generierte Konsolenausgabe

Der Konsolenausdruck des Codes ist unten dargestellt und zeigt `true` für die Primäre Kategorie- und Wertachse sowie `false` für die Sekundäre Kategorie- und Wertachse.  

{{< highlight java >}}  
Has Primary Category Axis: True  
Has Secondary Category Axis: False  
Has Primary Value Axis: True  
Has Secondary Value Axis: False  
{{< /highlight >}}
