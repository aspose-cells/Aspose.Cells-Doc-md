---
title: Wie man mit JavaScript via C++ ein Sunburst Diagramm erstellt
linktitle: Wie erstelle ich ein Sonnenstrahlendiagramm
description: Erfahren Sie, wie man ein Sunburst Diagramm in Aspose.Cells for JavaScript via C++ erstellt, ein Diagramm, das Daten in einem Kreis darstellt. Unser Leitfaden hilft Ihnen, verschiedene Eigenschaften und Formatierungen Ihres Diagramms einzurichten, einschließlich Datenbeschriftungen, Legenden, Farben und mehr.
keywords: Aspose.Cells for JavaScript via C++, Sunburst Diagramm, erstellen, Eigenschaften setzen, Datenbeschriftungen, Legende, Formatierung, Farbe, Kreis, Daten rendering.
type: docs
weight: 162
url: /de/javascript-cpp/creating-sunburst-chart/
---

## **Mögliche Verwendungsszenarien**
Reingrafik-Diagramme sind gut geeignet, um Anteile innerhalb der Hierarchie zu vergleichen; jedoch sind Reingrafik-Diagramme nicht optimal, um hierarchische Ebenen zwischen den größten Kategorien und jedem Datenpunkt darzustellen. Ein Sonnenstrahldiagramm ist dafür viel besser geeignet. Das Sonnenstrahldiagramm ist ideal zur Anzeige hierarchischer Daten. Jede Ebene der Hierarchie wird durch einen Ring oder Kreis dargestellt, wobei der innerste Kreis die Spitze der Hierarchie ist. Ein Sonnenstrahldiagramm ohne hierarchische Daten (eine Kategorieebene) sieht ähnlich wie ein Donut-Diagramm aus. Ein Sonnenstrahldiagramm mit mehreren Kategorienebenen zeigt, wie die äußeren Ringe zu den inneren Ringen in Beziehung stehen. Das Sonnenstrahldiagramm ist am besten geeignet, um zu zeigen, wie ein Ring in seine beitragenden Teile zerlegt ist, während eine andere Art hierarchischer Diagramme, das Reingrafik-Diagramm, ideal zum Vergleich relativer Größen ist.

![todo:image_alt_text](sample.png)
## **Sonnenstrahlendiagramm**
Nach Ausführen des unten stehenden Codes wird das Sonnenstrahlendiagramm wie unten gezeigt angezeigt.

![todo:image_alt_text](result.png)
## **Beispielcode**
Der folgende Beispielcode lädt die [Beispieldatei Excel](sunburst.xlsx) und erstellt die [Ausgabedatei Excel](out.xlsx).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Sunburst Chart Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Sunburst Chart Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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

            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            const worksheet = workbook.worksheets.get(0);

            const pieIdx = worksheet.charts.add(AsposeCells.ChartType.Sunburst, 5, 6, 25, 12);
            const chart = worksheet.charts.get(pieIdx);

            chart.showLegend = true;
            chart.title.text = "Sunburst Chart";
            chart.nSeries.add("D2:D16", true);
            chart.nSeries.categoryData = "A2:C16";
            chart.nSeries.get(0).dataLabels.showCategoryName = true;
            chart.plotArea.area.fillFormat.fillType = AsposeCells.FillType.None;

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Sunburst chart created successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
