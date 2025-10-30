---
title: Establecer ancho de columna en unidades escalables como em o porcentaje con JavaScript vía C++
linktitle: Establecer ancho de columna a unidad escalable como em o porcentaje
type: docs
weight: 130
url: /es/javascript-cpp/set-column-width-to-scalable-unit-like-em-or-percent/
description: Aprende cómo establecer el ancho de columna en unidades escalables como em o porcentaje en Aspose.Cells for JavaScript vía C++. Mejora la presentación de las tablas HTML generadas.
---

Generar un archivo HTML a partir de una hoja de cálculo es muy común. El tamaño de las columnas se define en "pt," lo cual funciona en muchos casos. Sin embargo, puede haber situaciones donde este tamaño fijo no sea necesario. Por ejemplo, si el ancho de un panel contenedor es de 600px, donde se está visualizando esta página HTML, puede aparecer una barra de desplazamiento horizontal si el ancho de la tabla generada es mayor. Se requiere que este tamaño fijo se cambie a una unidad escalable como em o porcentaje para mejorar la presentación. El siguiente código de ejemplo se puede usar donde [**HtmlSaveOptions.widthScalable**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#widthScalable--) se establece en **true** para crear un ancho escalable.

Se pueden descargar archivos fuente de muestra y archivos de salida desde los siguientes enlaces:

[sampleForScalableColumns.xlsx](73990150.xlsx)

[outsampleForScalableColumns.zip](73990151.zip)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Scalable Columns to HTML</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, HtmlSaveOptions, SaveFormat } = AsposeCells;

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

            // Specify Html Save Options
            const options = new HtmlSaveOptions();

            // Set the property for scalable width (converted from setWidthScalable)
            options.widthScalable = true;

            // Specify image save format (converted from setExportImagesAsBase64)
            options.exportImagesAsBase64 = true;

            // Save the workbook in Html format with specified Html Save Options
            const outputData = workbook.save(SaveFormat.Html, options);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outsampleForScalableColumns.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">File converted to HTML successfully! Click the download link to get the result.</p>';
        });
    </script>
</html>
```
