---
title: Etiqueta de Datos Personalizados de Texto Enriquecido de Punto de Gráfico con JavaScript vía C++
description: Aprende cómo agregar etiquetas de datos personalizadas de texto enriquecido a puntos de gráficos en Aspose.Cells for JavaScript vía C++. Nuestra guía te mostrará cómo formatear las etiquetas con diferentes fuentes, colores y opciones de alineación para mejorar la apariencia y legibilidad de tus gráficos.
keywords: Aspose.Cells for JavaScript vía C++, gráficos, texto enriquecido, etiquetas de datos personalizadas, fuentes, colores, alineación, apariencia, legibilidad.
type: docs
weight: 10
url: /es/javascript-cpp/rich-text-custom-data-label-of-chart-point/
---

{{% alert color="primary" %}}

Puedes usar Aspose.Cells para crear etiquetas de datos personalizadas con texto enriquecido para puntos del gráfico. Aspose.Cells proporciona el método [**ChartTextFrame.characters(number, number)**](https://reference.aspose.com/cells/javascript-cpp/charttextframe/#characters-number-number-) para devolver el objeto [**FontSetting**](https://reference.aspose.com/cells/javascript-cpp/fontsetting) que puede usarse para establecer las propiedades de fuente del texto, como el color, negrita, etc.

{{% /alert %}}

## Etiqueta de Datos Personalizada con Texto Enriquecido del Punto del Gráfico

El siguiente código accede al primer punto de la primera serie, establece su texto y luego configura la fuente de los primeros 10 caracteres estableciendo su color a rojo y su negrita en **true**.

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
            const resultDiv = document.getElementById('result');
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Creating a Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access the first chart inside the sheet
            const chart = worksheet.charts.get(0);

            // Access the data label of first series first point
            const dlbls = chart.nSeries.get(0).points.get(0).dataLabels;

            // Set data label text
            dlbls.text = "Rich Text Label";

            // Set the font setting of the first 10 characters
            const fntSetting = dlbls.characters(0, 10);
            const font = fntSetting.font;
            font.color = AsposeCells.Color.Red;
            font.isBold = true;

            // Save the workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Data label updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
