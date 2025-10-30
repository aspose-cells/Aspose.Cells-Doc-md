---
title: Cambiar la fuente de datos del gráfico a la hoja de destino mientras se copian filas o rango con JavaScript vía C++
linktitle: Cambiar la fuente de datos del gráfico a la hoja de trabajo de destino al copiar filas o rango
description: Aprende cómo cambiar la fuente de datos de un gráfico a una hoja de destino mientras copias filas o un rango en Aspose.Cells for JavaScript vía C++. Esta guía demuestra cómo actualizar el rango de datos del gráfico y enlazarlo a la hoja de destino.
keywords: Aspose.Cells for JavaScript vía C++, gráficos, fuente de datos, hoja de destino, filas, rango, copiar, actualizar, rango de datos, enlace.
type: docs
weight: 440
url: /es/javascript-cpp/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/
---

## **Escenarios de uso posibles**

Cuando copias filas o rangos que contienen gráficos a una nueva hoja, la fuente de datos del gráfico no cambia. Por ejemplo, si la fuente de datos del gráfico es `=Sheet1!$A$1:$B$4`, después de copiar filas o rango a una nueva hoja, la fuente de datos seguirá siendo la misma, es decir, `=Sheet1!$A$1:$B$4`. Aún hace referencia a la hoja antigua, es decir, Sheet1. Este también es el comportamiento en Microsoft Excel. Pero si quieres que apunte a la nueva hoja de destino, usa la propiedad [**CopyOptions.referToDestinationSheet**](https://reference.aspose.com/cells/javascript-cpp/copyoptions/#referToDestinationSheet--) y establecela en **true** al llamar al método [**Cells.copyRows(Cells, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#copyRows-cells-number-number-number-). Ahora, si tu hoja de destino es DestSheet, la fuente de datos de tu gráfico cambiará de `=Sheet1!$A$1:$B$4` a `=DestSheet!$A$1:$B$4`.

## **Cambiar la fuente de datos del gráfico a la hoja de trabajo de destino al copiar filas o rango**

El siguiente código de ejemplo explica cómo usar la propiedad [**CopyOptions.referToDestinationSheet**](https://reference.aspose.com/cells/javascript-cpp/copyoptions/#referToDestinationSheet--) al copiar filas o rangos que contienen gráficos a una nueva hoja. El código usa el [archivo de ejemplo en Excel](5113699.xlsx) y genera el [archivo de salida en Excel](5113697.xlsx).

![todo:image_alt_text](change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range_1.png)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Copy Worksheet with Charts</title>
    </head>
    <body>
        <h1>Copy Worksheet with Charts Example</h1>
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate Workbook from the uploaded file
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first sheet which contains chart
            const source = wb.worksheets.get(0);

            // Add another sheet named DestSheet
            const destination = wb.worksheets.add("DestSheet");

            // Set CopyOptions.referToDestinationSheet to true
            const options = new AsposeCells.CopyOptions();
            options.referToDestinationSheet = true;

            // Copy all the rows of source worksheet to destination worksheet which includes chart as well
            // The chart data source will now refer to DestSheet
            destination.cells.copyRows(source.cells, 0, 0, source.cells.maxDisplayRange.rowCount, options);

            // Save workbook in xlsx format and provide download link
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Worksheet copied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
