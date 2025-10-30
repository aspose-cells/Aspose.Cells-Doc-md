---
title: Prevenir la exportación de contenido de hojas ocultas al guardar en HTML con JavaScript vía C++
linktitle: Evitar la exportación de contenidos ocultos de la hoja de cálculo al guardar en HTML
type: docs
weight: 210
url: /es/javascript-cpp/prevent-exporting-hidden-worksheet-contents-on-saving-to/
description: Aprende cómo prevenir la exportación de contenido de hojas ocultas al guardar archivos de Excel en HTML usando Aspose.Cells for JavaScript vía C++.
---

{{% alert color="primary" %}}

Puede guardar libros de Excel en HTML. Sin embargo, si el libro contiene hojas de cálculo ocultas, por defecto Aspose.Cells exporta los contenidos ocultos de la hoja de cálculo al directorio de salida HTML (_files) que contiene archivos como hojas de cálculo, imágenes, tabstrip.htm, stylesheet.css, etc. A veces, exportar el contenido de las hojas de cálculo ocultas de esta manera no es apropiado. Por ejemplo, si la hoja de cálculo oculta contiene imágenes que no deben ser exportadas al directorio _files.

{{% /alert %}}

Aspose.Cells for JavaScript vía C++ proporciona la propiedad [**HtmlSaveOptions.exportHiddenWorksheet**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#exportHiddenWorksheet--). Por defecto, está configurada en **true** y las hojas ocultas se exportan a HTML. Si la configuras en **false**, Aspose.Cells no exportará el contenido de las hojas ocultas.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - HTML Without Hidden Content</title>
    </head>
    <body>
        <h1>Save Workbook as HTML Without Hidden Worksheet Content</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlSaveOptions, Utils } = AsposeCells;

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

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create HtmlSaveOptions and do not export hidden worksheet contents
            const options = new HtmlSaveOptions();
            options.exportHiddenWorksheet = false;

            // Save workbook to HTML format using the options
            const outputData = workbook.save(SaveFormat.Html, options);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'HtmlWithoutHiddenContent_out.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook saved to HTML without hidden content. Click the download link to get the file.</p>';
        });
    </script>
</html>
```
