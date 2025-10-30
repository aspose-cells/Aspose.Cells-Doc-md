---
title: Mostrar Rango de Celdas como las Etiquetas de Datos con JavaScript vía C++
linktitle: Mostrar rango de celdas como las etiquetas de datos
description: Aprende cómo mostrar un rango de celdas como etiquetas de datos en gráficos usando Aspose.Cells for JavaScript vía C++. Nuestra guía demostrará cómo vincular las etiquetas a tu fuente de datos y formatearlas para proporcionar información precisa y significativa en tus gráficos.
keywords: Aspose.Cells for JavaScript vía C++, gráficos, etiquetas de datos, rango de celdas, fuente de datos, formato, precisión, información significativa.
type: docs
weight: 130
url: /es/javascript-cpp/showing-cell-range-as-the-data-labels/
---

{{% alert color="primary" %}}
En Microsoft Excel 2013, puedes mostrar un rango de celdas para las etiquetas de datos. Aspose.Cells for JavaScript vía C++ soporta esta función.
{{% /alert %}}

## **Casilla de verificación para Mostrar rango de celdas como etiquetas de datos**

Para mostrar el rango de celdas como etiquetas de datos en Microsoft Excel:

1. Selecciona las etiquetas de datos de la serie y haz clic derecho para abrir el menú contextual.  
1. Selecciona **Formato de etiquetas de datos**. Se muestran las opciones de etiquetas.  
1. Selecciona o deselecciona la opción **La etiqueta contiene - Valor de las celdas**.  

El código de ejemplo a continuación accede a las etiquetas de datos de una serie de gráficos y establece la propiedad [**DataLabels.showCellRange**](https://reference.aspose.com/cells/javascript-cpp/datalabels/#showCellRange--) en **true** para seleccionar la opción **Etiqueta Contiene - Valor de Celdas**.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Show Range in Data Labels</title>
    </head>
    <body>
        <h1>Show Range in Data Labels Example</h1>
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

            // Create workbook from the source Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access the chart inside the worksheet
            const chart = worksheet.charts.get(0);

            // Check the "Label Contains - Value From Cells"
            const dataLabels = chart.nSeries.get(0).dataLabels;
            dataLabels.showCellRange = true;

            // Save the workbook
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
