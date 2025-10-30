---
title: Exportar estilos de borde similares cuando el estilo de borde no es soportado por los navegadores web con JavaScript vía C++  
linktitle: Exportar un Estilo de Borde Similar cuando el Estilo de Borde no es compatible con los Navegadores Web  
type: docs  
weight: 70  
url: /es/javascript-cpp/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/  
description: Aprende cómo exportar bordes que no son soportados por navegadores web al convertir archivos de Excel a HTML usando Aspose.Cells for JavaScript vía C++.  
---  

## **Escenarios de uso posibles**  

Microsoft Excel soporta algunos tipos de bordes discontinuos que no son compatibles con los navegadores web. Cuando conviertes dicho archivo de Excel a HTML usando Aspose.Cells for JavaScript vía C++, dichos bordes son eliminados. Sin embargo, Aspose.Cells también puede soportar la visualización de tales bordes con la propiedad [**HtmlSaveOptions.exportSimilarBorderStyle**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#exportSimilarBorderStyle--). Por favor, configura su valor en **true** y los bordes no soportados también se exportarán al archivo HTML.  

## **Exportar un estilo de borde similar cuando el estilo de borde no es soportado por los navegadores web**  

El siguiente código de ejemplo carga el [archivo de Excel de ejemplo](64716806.xlsx) que contiene algunos bordes no soportados como se muestra en la siguiente captura de pantalla. La captura ilustra además el efecto de la propiedad [**HtmlSaveOptions.exportSimilarBorderStyle**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#exportSimilarBorderStyle--) dentro del [HTML de salida](64716804.zip).  

![todo:image_alt_text](export-similar-border-style-when-border-style-is-not-supported-by-web-browsers_1.png)  

## **Código de muestra**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Export Similar Border Style Example</title>
    </head>
    <body>
        <h1>Export Similar Border Style Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlSaveOptions } = AsposeCells;

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

            // Specify Html Save Options - Export Similar Border Style
            const opts = new HtmlSaveOptions();
            opts.exportSimilarBorderStyle = true;

            // Save the workbook in Html format with specified Html Save Options
            const outputData = workbook.save(SaveFormat.Html, opts);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputExportSimilarBorderStyle.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Export completed successfully! Click the download link to get the HTML file.</p>';
        });
    </script>
</html>
```
