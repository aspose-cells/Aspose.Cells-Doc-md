---
title: Anpassen von Diagrammen mit JavaScript via C++
linktitle: Diagramme anpassen
description: Erfahren Sie, wie Sie Diagramme in Aspose.Cells for JavaScript via C++ anpassen. Unser Leitfaden zeigt, wie Sie Diagrammlayouts ändern, Datenreihen hinzufügen und formatieren, Achsen anpassen und verschiedene Formatierungsoptionen anwenden, um das Aussehen und die Benutzerfreundlichkeit Ihrer Diagramme zu verbessern.
keywords: Aspose.Cells for JavaScript via C++, Diagrammanpassung, Layouts, Datenreihen, Achsen, Formatierung, Erscheinungsbild, Benutzerfreundlichkeit.
type: docs
weight: 40
url: /de/javascript-cpp/customizing-charts/
---

## **Erstellen von benutzerdefinierten Diagrammen**  

Bisher haben wir beim Diskutieren von Diagrammen die Standarddiagramme mit ihren Standard-Formatierungseinstellungen betrachtet. Wir definieren nur die Datenquelle, setzen einige Eigenschaften, und das Diagramm wird mit den Standard-Formatierungen erstellt. Aber Aspose.Cells APIs unterstützen auch die Erstellung benutzerdefinierter Diagramme, mit denen Entwickler eigene Formatierungen vornehmen können.  

Entwickler können benutzerdefinierte Diagramme zur Laufzeit mithilfe von Aspose.Cells erstellen.  

Ein Diagramm besteht aus einer Datensammlung. Jede Datenreihe in Aspose.Cells wird durch ein [**Series**](https://reference.aspose.com/cells/javascript-cpp/series) Objekt dargestellt, während [**SeriesCollection**](https://reference.aspose.com/cells/javascript-cpp/seriescollection) Objekt als Sammlung von [**Series**](https://reference.aspose.com/cells/javascript-cpp/series) Objekten dient. Bei der Erstellung eines benutzerdefinierten Diagramms haben Entwickler die Freiheit, verschiedene Diagrammtypen für verschiedene Datenreihen (gesammelt im [**SeriesCollection**](https://reference.aspose.com/cells/javascript-cpp/seriescollection) Objekt) zu verwenden.  

Der nachstehende Beispielcode zeigt, wie benutzerdefinierte Diagramme erstellt werden können. In diesem Beispiel verwenden wir ein Säulendiagramm für die erste Datenreihe und ein Liniendiagramm für die zweite Reihe. Das Ergebnis ist, dass wir ein Säulendiagramm, kombiniert mit einem Liniendiagramm, dem Arbeitsblatt hinzufügen.  

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

        const readyPromise = AsposeCells.onReady({
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
            // Ensure Aspose.Cells is initialized
            await readyPromise;

            // Instantiate a new Workbook
            const workbook = new Workbook();

            // Adding a new worksheet to the Workbook object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding sample values to cells
            worksheet.cells.get("A1").value = 50;
            worksheet.cells.get("A2").value = 100;
            worksheet.cells.get("A3").value = 150;
            worksheet.cells.get("A4").value = 110;
            worksheet.cells.get("B1").value = 260;
            worksheet.cells.get("B2").value = 12;
            worksheet.cells.get("B3").value = 50;
            worksheet.cells.get("B4").value = 100;

            // Adding a chart to the worksheet
            const chartIndex = worksheet.charts.add(ChartType.Column, 5, 0, 15, 5);

            // Accessing the instance of the newly added chart
            const chart = worksheet.charts.get(chartIndex);

            // Adding NSeries (chart data source) to the chart ranging from "A1" cell to "B4"
            chart.nSeries.add("A1:B4", true);

            // Setting the chart type of 2nd NSeries to display as line chart
            chart.nSeries.get(1).type = ChartType.Line;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```  

{{% alert color="primary" %}}  

Derzeit unterstützt Aspose.Cells nur benutzerdefinierte Diagramme, die Kreis-, Linien-, Säulen- und Säulenstapel-Diagramme kombinieren, aber in zukünftigen Versionen werden weitere Diagrammtypen unterstützt.  

{{% /alert %}}
