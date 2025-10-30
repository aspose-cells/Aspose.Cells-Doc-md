---
title: Cómo hacer que la serie sea invisible con JavaScript a través de C++
linktitle: Cómo establecer la serie como invisible
description: Aprende a hacer que una serie sea invisible en un gráfico de Excel usando Aspose.Cells for JavaScript a través de C++. 
keywords: Gráfico de Excel, Serie, Invisible, IsFiltered JavaScript vía C++.
type: docs
weight: 74
url: /es/javascript-cpp/how-to-set-series-invisible/
---

## Cómo hacer que una serie sea invisible en un gráfico de Excel

En un gráfico de Excel, puedes hacer clic derecho en el gráfico, seleccionar "Seleccionar datos", y en la ventana emergente, puedes definir si una serie está visible marcándola o desmarcándola. Puedes descargar el siguiente [archivo de ejemplo](SeriesFiltered.xlsx) y operarlo en Excel como se muestra en la figura para lograr esta función. A continuación, te explicaremos cómo lograrlo usando la biblioteca Aspose.Cells.

![todo:image_alt_text](series-invisible.png)

## Cómo hacer que una serie sea invisible usando Aspose.Cells 

Usamos el siguiente código para hacer que una serie sea invisible usando Aspose.Cells:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Modify Chart Series Color Variation</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet and its charts
            const charts = workbook.worksheets.get(0).charts;
            const chart = charts.get("Chart 1");

            // Access filtered NSeries and NSeries collections (properties instead of getters)
            const nSeriesFiltered = chart.filteredNSeries;
            const nSeries = chart.nSeries;

            // Set IsColorVaried on series (converted from setIsColorVaried to property assignment)
            nSeries.get(1).isColorVaried = true;
            nSeries.get(0).isColorVaried = true;

            // Save the modified workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

Puedes obtener el [archivo de entrada](SeriesFiltered.xlsx) y el [archivo de salida](output.xlsx).

Como se muestra en la figura a continuación, las dos primeras series que originalmente estaban visibles, se han vuelto invisibles en el archivo de salida.
![todo:image_alt_text](output.png)
