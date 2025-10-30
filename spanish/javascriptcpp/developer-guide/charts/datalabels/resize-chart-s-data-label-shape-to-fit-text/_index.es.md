---
title: Redimensionar la forma de la etiqueta de datos del gráfico para que se ajuste al texto con JavaScript vía C++
linktitle: Redimensionar la forma de la etiqueta de datos del gráfico para ajustar el texto
description: Aprende cómo redimensionar la forma de la etiqueta de datos en un gráfico para que se ajuste al texto en Aspose.Cells for JavaScript vía C++. Nuestra guía te mostrará cómo ajustar el tamaño y la forma del contenedor de la etiqueta para garantizar que el texto se muestre correctamente sin truncamientos ni superposiciones.
keywords: Aspose.Cells for JavaScript vía C++, gráficos, etiquetas de datos, redimensionamiento de forma, ajuste de texto, truncamiento, superposición.
type: docs
weight: 220
url: /es/javascript-cpp/resize-chart-s-data-label-shape-to-fit-text/
---

{{% alert color="primary" %}}  
La aplicación de Excel proporciona la opción **Redimensionar la forma para que se ajuste al texto** para las Etiquetas de Datos en el Gráfico con el fin de aumentar el tamaño de la forma para que el texto quepa en ella.  
{{% /alert %}}  

## **Cómo Cambiar el Tamaño de la Forma de la Etiqueta de Datos en un Gráfico en Microsoft Excel**  

Esta opción puede accederse en la interfaz de Excel seleccionando alguna de las etiquetas de datos en el gráfico. Haz clic derecho y selecciona el menú **Formato de etiquetas de datos**. En la pestaña **Tamaño y propiedades**, expande **Alineación** para revelar las propiedades relacionadas, incluyendo la opción **Redimensionar forma para ajustar el texto**.  

## **Cómo redimensionar la forma de la etiqueta de datos del gráfico para que se ajuste al texto usando Aspose.Cells for JavaScript vía C++**  

Para imitar la función de Excel de redimensionar las formas de etiquetas de datos para que se ajusten al texto, las API de Aspose.Cells han expuesto la propiedad booleana [**DataLabels.isResizeShapeToFitText()**](https://reference.aspose.com/cells/javascript-cpp/charttextframe/#isResizeShapeToFitText--). El siguiente código muestra un escenario de uso simple de la propiedad [**DataLabels.isResizeShapeToFitText()**](https://reference.aspose.com/cells/javascript-cpp/charttextframe/#isResizeShapeToFitText--).  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Chart Data Labels Resize Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet that contains the Chart
            const sheet = workbook.worksheets.get(0);

            for (let c = 0; c < sheet.charts.count; c++) {
                // Access the Chart
                const chart = sheet.charts.get(c);

                for (let index = 0; index < chart.nSeries.count; index++) {
                    // Access the DataLabels of indexed NSeries
                    const labels = chart.nSeries.get(index).dataLabels;

                    // Set ResizeShapeToFitText property to true
                    labels.isResizeShapeToFitText = true;
                }

                // Calculate Chart
                chart.calculate();
            }

            // Save the result
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
