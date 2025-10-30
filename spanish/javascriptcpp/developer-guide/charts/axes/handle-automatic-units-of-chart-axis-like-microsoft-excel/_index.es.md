---
title: Manejar unidades automáticas del eje del gráfico como Microsoft Excel con JavaScript vía C++
linktitle: Manejar las unidades automáticas del eje del gráfico como en Microsoft Excel
description: Aprende cómo manejar unidades automáticas en los ejes del gráfico en Aspose.Cells for JavaScript mediante C++. Nuestra guía te mostrará cómo configurar y personalizar las unidades automáticas en un eje de gráfico, incluyendo la visualización en notación científica y ajustar la escala.
keywords: Aspose.Cells for JavaScript mediante C++, ejes del gráfico, unidades automáticas, Microsoft Excel, configuración, personalización, notación científica, escalado.
type: docs
weight: 120
url: /es/javascript-cpp/handle-automatic-units-of-chart-axis-like-microsoft-excel/
---

## **Escenarios de uso posibles**  
Las versiones tempranas de Aspose.Cells for JavaScript mediante C++ no podían manejar correctamente las unidades automáticas del eje del gráfico cuando el gráfico se renderizaba en imagen o PDF. Ahora, Aspose.Cells for JavaScript mediante C++ soporta el manejo de unidades automáticas del eje del gráfico. No hay cambios en el código. Solo convierte tu gráfico en una imagen o PDF y renderizará el eje del gráfico igual que lo hace Microsoft Excel.  

## **Manejar Unidades Automáticas del Eje del Gráfico como Microsoft Excel**  
El siguiente código de ejemplo carga el [archivo de Excel de muestra](61767755.xlsx) y genera el [gráfico PDF de salida](61767752.pdf). La captura de pantalla muestra las unidades automáticas del eje del gráfico en rectángulos rojos y también compara el gráfico del archivo de Excel de muestra con el gráfico PDF de salida. Ambos son exactamente iguales.  

![todo:image_alt_text](handle-automatic-units-of-chart-axis-like-microsoft-excel_1.png)  

## **Código de muestra**  
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Handle Automatic Units Of Chart Axis Like Microsoft Excel</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            await readyPromise;

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object using the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access first chart
            const chart = worksheet.charts.get(0);

            // Render chart to pdf
            const outputData = await chart.toPdf();

            // Create download link for the generated PDF
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputHandleAutomaticUnitsOfChartAxisLikeMicrosoftExcel.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Chart rendered to PDF successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```
