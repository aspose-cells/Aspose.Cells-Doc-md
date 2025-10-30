---
title: Desactivar comentarios revelados a nivel inferior al guardar en HTML con JavaScript vía C++
linktitle: Desactivar los Comentarios Revelados de Niveles Inferiores al guardar en HTML
type: docs
weight: 20
url: /es/javascript-cpp/disable-downlevel-revealed-comments-while-saving-to/
description: Aprende cómo desactivar los comentarios revelados a nivel inferior al guardar un archivo de Excel en HTML usando Aspose.Cells for JavaScript vía C++.
---

## **Escenarios de uso posibles**

Al guardar tu archivo Excel en HTML, Aspose.Cells revela los Comentarios Condicionales en nivel inferior. Estos comentarios condicionales son relevantes principalmente para versiones antiguas de Internet Explorer y no para navegadores modernos. Puedes leer más detalles en el siguiente enlace.

- [Comentario condicional - comentario condicional revelado de niveles inferiores](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

Aspose.Cells for JavaScript vía C++ permite eliminar estos Comentarios Revelados a nivel inferior configurando la propiedad [**HtmlSaveOptions.disableDownlevelRevealedComments**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#disableDownlevelRevealedComments--) a **true**.

## **Desactivar Comentarios Revelados de Niveles Inferiores al guardar en HTML**

El siguiente ejemplo muestra cómo usar la propiedad [**HtmlSaveOptions.disableDownlevelRevealedComments**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#disableDownlevelRevealedComments--). La captura de pantalla muestra el efecto de esta propiedad cuando no está configurada en true. Descarga el [archivo de ejemplo Excel](50528257.xlsx) usado en este código y el [HTML de salida](50528258.zip) generado por él para referencia.

![todo:image_alt_text](disable-downlevel-revealed-comments-while-saving-to-html_1.png)

## **Código de muestra**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Disable Downlevel Revealed Comments Example</h1>
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

            // Load sample workbook
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Disable DisableDownlevelRevealedComments
            const opts = new HtmlSaveOptions();
            opts.disableDownlevelRevealedComments = true;

            // Save the workbook in html
            const outputData = workbook.save(SaveFormat.Html, opts);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputDisableDownlevelRevealedComments_true.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook saved as HTML with DisableDownlevelRevealedComments = true. Click the download link to get the result.</p>';
        });
    </script>
</html>
```
