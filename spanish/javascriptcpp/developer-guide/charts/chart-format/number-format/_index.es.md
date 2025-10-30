---
title: Establecer el Código de Formato de Valores de Series de Gráficos con JavaScript vía C++
description: Aprende cómo configurar el código de formato de valores de series de gráficos en Aspose.Cells for JavaScript vía C++. Esta guía te ayudará a entender cómo formatear los datos de tus series de gráficos utilizando el código de formato adecuado, permitiéndote presentar tus datos de manera precisa y profesional.
keywords: Aspose.Cells for JavaScript vía C++, series de gráficos, código de formato de valores, formateo, presentación de datos, precisión, profesionalismo.
linktitle: Formato de número
type: docs
weight: 100
url: /es/javascript-cpp/set-the-values-format-code-of-chart-series/
---

## **Escenarios de uso posibles**
Puedes establecer el código de formato de valores de series de gráficos usando la propiedad [Series.valuesFormatCode](https://reference.aspose.com/cells/javascript-cpp/series/#valuesFormatCode--). Esta propiedad no solo es útil para las series basadas en el rango dentro de la hoja de cálculo, sino que también funciona bien para las series creadas con una matriz de valores.

## **Establecer el código de formato de valores de la serie del gráfico**
 El siguiente código de ejemplo añade una serie en un gráfico vacío que no tenía series previamente. Añade la serie usando la matriz de valores. Una vez que añade la serie, la formatea con el código $#,##0 usando la propiedad [Series.valuesFormatCode](https://reference.aspose.com/cells/javascript-cpp/series/#valuesFormatCode--) y el número 10000 se transforma en $10,000. La captura de pantalla muestra el efecto del código en el [archivo de Excel de ejemplo](51740712.xlsx) y en el [archivo de Excel de salida](51740713.xlsx) tras la ejecución.

![todo:image_alt_text](set-the-values-format-code-of-chart-series_1.png)

## **Código de muestra**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Chart Series Example</h1>
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

                // Access first worksheet
                const worksheet = workbook.worksheets.get(0);

                // Access first chart
                const chart = worksheet.charts.get(0);

                // Add series using an array of values
                chart.nSeries.add("{10000, 20000, 30000, 40000}", true);

                // Access the series and set its values format code
                const series = chart.nSeries.get(0);
                series.valuesFormatCode = "$#,##0";

                // Saving the modified Excel file
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = '51740713.xlsx';
                downloadLink.style.display = 'block';
                downloadLink.textContent = 'Download Modified Excel File';

                document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
            });
        });
    </script>
</html>
```
