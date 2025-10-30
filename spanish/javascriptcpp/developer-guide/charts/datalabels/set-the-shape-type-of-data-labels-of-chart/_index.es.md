---
title: Establecer el Tipo de Forma de las Etiquetas de Datos del Gráfico con JavaScript vía C++
linktitle: Establecer el tipo de forma de las etiquetas de datos del gráfico
description: Aprende cómo establecer el tipo de forma de las etiquetas de datos en gráficos usando Aspose.Cells for JavaScript vía C++. Nuestra guía explicará los diferentes tipos de formas disponibles y te mostrará cómo seleccionar la forma apropiada para tus etiquetas de datos para mejorar la presentación y usabilidad.
keywords: Aspose.Cells for JavaScript vía C++, gráficos, etiquetas de datos, tipos de formas, presentación, usabilidad.
type: docs
weight: 110
url: /es/javascript-cpp/set-the-shape-type-of-data-labels-of-chart/
---

## **Escenarios de uso posibles**
Puedes cambiar el tipo de forma de las etiquetas de datos del gráfico usando la propiedad `DataLabels.shapeType`. Toma el valor del enumerado `DataLabelShapeType` y cambia el tipo de forma de las etiquetas de datos en consecuencia. Algunos de sus valores son

{{< highlight javascript >}}
 DataLabelShapeType.BentLineCallout
DataLabelShapeType.DownArrowCallout
DataLabelShapeType.Ellipse
DataLabelShapeType.LineCallout
DataLabelShapeType.Rect
etc.
{{< /highlight >}}

## **Establecer el tipo de forma de las etiquetas de datos del gráfico**
El siguiente ejemplo cambia el tipo de forma de las etiquetas de datos del gráfico a `DataLabelShapeType.WedgeEllipseCallout`. Por favor, revisa el archivo de Excel de ejemplo ([60489778.xlsx](60489778.xlsx)) usado en este código y el archivo de Excel de salida ([60489779.xlsx](60489779.xlsx)) generado por él. La captura de pantalla muestra el efecto del código en el archivo de ejemplo.

![todo:image_alt_text](set-the-shape-type-of-data-labels-of-chart_1.png)
## **Código de muestra**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Set Shape Type of Data Labels of Chart Example</title>
    </head>
    <body>
        <h1>Set Shape Type of Data Labels of Chart Example</h1>
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
            const downloadLink = document.getElementById('downloadLink');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Accessing the first chart
            const chart = worksheet.charts.get(0);

            // Accessing the first series
            const series = chart.nSeries.get(0);

            // Set the shape type of data labels i.e. Speech Bubble Oval
            series.dataLabels.shapeType = AsposeCells.DataLabelShapeType.WedgeEllipseCallout;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSetShapeTypeOfDataLabelsOfChart.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Shape type set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
