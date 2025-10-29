---
title: Conversion d’un graphique en PDF avec JavaScript via C++
linktitle: Graphique en PDF
description: Apprenez à utiliser Aspose.Cells for JavaScript via C++ pour convertir un graphique en document PDF. Notre guide montre comment exporter un graphique depuis Microsoft Excel et le sauvegarder en tant que PDF pour une distribution et une archival ultérieures.
keywords: Aspose.Cells for JavaScript via C++, Graphique vers PDF, Microsoft Excel, Conversion PDF, Exportation, Distribution, Archivage.
type: docs
weight: 47
url: /fr/javascript-cpp/chart-to-pdf/
---

## **Rendu du graphique en PDF**

Afin de rendre le graphique en format PDF, les API Aspose.Cells ont exposé la méthode [**Chart.toPdf(string)**](https://reference.aspose.com/cells/javascript-cpp/chart/#toPdf-string-) avec la capacité de stocker le PDF résultant sur le chemin du disque ou en Stream.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Chart to PDF</title>
    </head>
    <body>
        <h1>Chart to PDF Example</h1>
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
            // Create a new workbook
            const workbook = new Workbook();
            // Add a new worksheet
            const sheetIndex = workbook.worksheets.add();
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding sample values to cells
            worksheet.cells.get("A1").value = 50;
            worksheet.cells.get("A2").value = 100;
            worksheet.cells.get("A3").value = 150;
            worksheet.cells.get("B1").value = 4;
            worksheet.cells.get("B2").value = 20;
            worksheet.cells.get("B3").value = 50;

            // Adding a chart to the worksheet
            const chartIndex = worksheet.charts.add(ChartType.Column, 5, 0, 15, 5);
            const chart = worksheet.charts.get(chartIndex);

            // Adding Series Collection (chart data source) to the chart ranging from "A1" cell to "B3"
            chart.nSeries.add("A1:B3", true);

            // Converting chart to PDF
            const outputData = chart.toPdf();
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'chartPDF_out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Chart PDF';

            document.getElementById('result').innerHTML = '<p style="color: green;">Chart converted to PDF successfully! Click the download link to get the PDF.</p>';
        });
    </script>
</html>
```

## **Créer un PDF de graphique avec la taille de page souhaitée**  
Vous pouvez créer un PDF de graphique avec la taille de page souhaitée en utilisant Aspose.Cells et préciser comment vous souhaitez aligner le graphique à l'intérieur de la page, par exemple en haut, en bas, au centre, à gauche, à droite, etc. De plus, le graphique de sortie peut être créé en stream ou sur le disque. Veuillez voir le code d'exemple ci-dessous qui charge le fichier Excel [exemple](64716906.xlsx), accède au premier graphique dans la feuille de calcul, puis le convertit en [PDF de sortie](64716907.pdf) avec la taille de page souhaitée. La capture d'écran suivante montre que la taille de la page dans le PDF de sortie est de 7x7 comme spécifié dans le code et que le graphique est centré horizontalement et verticalement.

![todo:image_alt_text](create-chart-pdf-with-desired-page-size_1.png)  
## **Code d'exemple**  
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Create Chart PDF With Desired Page Size</title>
    </head>
    <body>
        <h1>Create Chart PDF With Desired Page Size</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsm" />
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

            // Access first worksheet.
            const worksheet = workbook.worksheets.get(0);

            // Access first chart inside the worksheet.
            const chart = worksheet.charts.get(0);

            // Create chart pdf with desired page size.
            // Note: In browser API omit file path and receive output data (Uint8Array / ArrayBuffer)
            const outputData = chart.toPdf(7, 7, AsposeCells.PageLayoutAlignmentType.Center, AsposeCells.PageLayoutAlignmentType.Center);

            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputCreateChartPDFWithDesiredPageSize.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Chart exported to PDF successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```
