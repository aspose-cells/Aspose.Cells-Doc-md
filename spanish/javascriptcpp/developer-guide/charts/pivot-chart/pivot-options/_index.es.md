---
title: Cómo gestionar un PivotChart con PivotOptions para JavaScript vía C++
linktitle: Opciones de Gráfico Dinámico
type: docs
weight: 10
url: /es/javascript-cpp/how-to-manage-pivotchart-with-pivotoptions/
description: Cómo gestionar un PivotChart con PivotOptions en JavaScript vía C++.
keywords: PivotChart JavaScript vía C++
---

## ¿Qué es un PivotChart?

Un PivotChart en Excel es una representación gráfica de datos creada a partir de una tabla dinámica. Permite a los usuarios visualizar y analizar datos de forma dinámica resumiendo y mostrando información en forma de gráfico. Los PivotCharts son interactivos y pueden modificarse fácilmente para mostrar diferentes perspectivas de los datos, convirtiéndolo en una poderosa herramienta para el análisis y la presentación de datos en Excel.

## Cómo gestionar el Gráfico Dinámico con Opciones de Gráfico Dinámico

Usando Aspose.Cells for JavaScript vía C++, puedes usar [**PivotOptions**](https://reference.aspose.com/cells/javascript-cpp/pivotoptions/) para gestionar PivotChart.

Archivo y código de ejemplo:
[Archivo de muestra](Sample.xlsx)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Hide PivotChart ZoneFilter Example</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet and the first chart
            const worksheet = workbook.worksheets.get(0);
            const chart = worksheet.charts.get(0);
            const opt = chart.pivotOptions;

            // Hide ZoneFilter in PivotChart
            opt.dropZoneFilter = false; // HideZoneFilter

            // Save the file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'HideZoneFilter.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">ZoneFilter hidden successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

Con el código de ejemplo anterior, puede verificar el archivo de resultado con el siguiente efecto, como se muestra en la figura:

**![Salida](Output.png)**
