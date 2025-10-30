---
title: Hinzufügen benutzerdefinierter Beschriftungen zu Datenpunkten in der Serie des Diagramms mit JavaScript via C++
linktitle: Hinzufügen benutzerdefinierter Beschriftungen zu Datenpunkten in der Serie des Diagramms
description: Lernen Sie, wie Sie benutzerdefinierte Beschriftungen zu Datenpunkten in der Serie eines Diagramms mit Aspose.Cells for JavaScript via C++ hinzufügen. Diese Anleitung zeigt, wie Sie das Aussehen, die Position und die Formatierung der Beschriftungen anpassen und sie mit Ihrer Datenquelle verknüpfen, um eine genaue Darstellung zu gewährleisten.
keywords: Aspose.Cells for JavaScript via C++, Diagrammerstellung, benutzerdefinierte Beschriftungen, Datenpunkte, Serie, Aussehen, Position, Formatierung, Datenquelle, Darstellung.
type: docs
weight: 100
url: /de/javascript-cpp/adding-custom-labels-to-data-points-in-the-series-of-the-chart/
---

{{% alert color="primary" %}}

Sie können benutzerdefinierte Beschriftungen zu Datenpunkten in der Serie des Diagramms hinzufügen. Aspose.Cells bietet die Eigenschaft [**DataLabels.text**](https://reference.aspose.com/cells/javascript-cpp/datalabels/#text--), um diese benutzerdefinierten Beschriftungen hinzuzufügen. Dieser Artikel erklärt, wie Sie diese Eigenschaft verwenden, um benutzerdefinierte Beschriftungen zu Datenpunkten in der Serie des Diagramms hinzuzufügen.

{{% /alert %}}

Der folgende Code erstellt einen **Streudiagramm verbunden durch Linien mit Datenmarkern** und fügt dann **benutzerdefinierte Beschriftungen** zu den **Datenpunkten** in der **Serie** des **Diagramms** hinzu. Jede benutzerdefinierte Beschriftung zeigt den **Seriennamen** und den **Punktnamen** an. Sie können stattdessen jeden anderen Text verwenden.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ChartType } = AsposeCells;

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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Put data
            sheet.cells.get(0, 0).value = 1;
            sheet.cells.get(0, 1).value = 2;
            sheet.cells.get(0, 2).value = 3;

            sheet.cells.get(1, 0).value = 4;
            sheet.cells.get(1, 1).value = 5;
            sheet.cells.get(1, 2).value = 6;

            sheet.cells.get(2, 0).value = 7;
            sheet.cells.get(2, 1).value = 8;
            sheet.cells.get(2, 2).value = 9;

            // Generate the chart
            const chartIndex = sheet.charts.add(ChartType.ScatterConnectedByLinesWithDataMarker, 5, 1, 24, 10);
            const chart = sheet.charts.get(chartIndex);

            chart.title.text = "Test";
            chart.categoryAxis.title.text = "X-Axis";
            chart.valueAxis.title.text = "Y-Axis";

            chart.nSeries.categoryData = "A1:C1";

            // Insert series 1
            chart.nSeries.add("A2:C2", false);

            let series = chart.nSeries.get(0);

            let pointCount = series.points.count;
            for (let i = 0; i < pointCount; i++) {
                const pointIndex = series.points.get(i);
                pointIndex.dataLabels.text = "Series 1" + "\n" + "Point " + i;
            }

            // Insert series 2
            chart.nSeries.add("A3:C3", false);

            series = chart.nSeries.get(1);

            pointCount = series.points.count;
            for (let i = 0; i < pointCount; i++) {
                const pointIndex = series.points.get(i);
                pointIndex.dataLabels.text = "Series 2" + "\n" + "Point " + i;
            }

            // Save the modified workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
