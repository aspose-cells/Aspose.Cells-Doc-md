---
title: Desactivar CSS al guardar en HTML con JavaScript vía C++
linktitle: Desactivar CSS al guardar en HTML
type: docs
weight: 320
url: /es/javascript-cpp/disable-css-while-saving-to-html/
description: Aprende cómo desactivar CSS al guardar archivos de Excel en HTML usando Aspose.Cells for JavaScript vía C++. 
---

## **Escenarios de uso posibles**

Al guardar tu archivo Excel en HTML de una sola página, normalmente los elementos CSS se incrustan dentro del archivo HTML y estarán en la sección HEAD. Si adjuntas este archivo como contenido/cuerpo de un correo, la mayoría de los clientes de correo eliminarán los estilos CSS, resultando en una visualización incorrecta. La versión 24.12 de Aspose.Cells introduce una opción que permite desactivar opcionalmente el CSS, permitiendo que los estilos se apliquen directamente en los elementos HTML. Si quieres configurar el HTML como contenido/cuerpo del correo, usa la propiedad [**HtmlSaveOptions.disableCss**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#disableCss--) y configúrala en **true**.

## **Desactivar CSS al guardar en HTML**

El siguiente código de ejemplo muestra el uso de la propiedad [**HtmlSaveOptions.disableCss**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#disableCss--). 

## **Código de muestra**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Disable CSS Example</title>
    </head>
    <body>
        <h1>Disable CSS Save Example</h1>
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
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const opts = new HtmlSaveOptions();
            opts.disableCss = true;

            const outputData = workbook.save(SaveFormat.Html, opts);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputDisable.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">HTML file generated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
