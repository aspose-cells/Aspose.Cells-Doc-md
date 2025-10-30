---
title: Detectar tipo de hipervínculo
type: docs
weight: 160
url: /es/javascript-cpp/detect-hyperlink-type/
description: Aprende cómo detectar el tipo de hipervínculo mediante el Script Aspose.Cells for Java con API C++.
keywords: Detectar el tipo de hipervínculo con JavaScript mediante C++, Detectar el tipo de hipervínculo con JavaScript mediante C++, Obtener el tipo de hipervínculo con JavaScript mediante C++
---

## **Detectar tipo de hipervínculo**

Un archivo de Excel puede tener diferentes tipos de hipervínculos como externos, referencia a celda, ruta de archivo, etc. Script Aspose.Cells for Java con C++ soporta la detección del tipo de hipervínculo. Los tipos de hipervínculos están representados por la enumeración [**TargetModeType**](https://reference.aspose.com/cells/javascript-cpp/targetmodetype). La enumeración [**TargetModeType**](https://reference.aspose.com/cells/javascript-cpp/targetmodetype) tiene los siguientes miembros.

- Externo: Enlace externo
- RutaArchivo: Ruta local y completa a archivos/carpetas.
- Email: Correo electrónico
- ReferenciaCelda: Enlace a celda o rango con nombre.

Para verificar el tipo de hipervínculo, la clase [**Hyperlink**](https://reference.aspose.com/cells/javascript-cpp/hyperlink) proporciona una propiedad [**linkType**](https://reference.aspose.com/cells/javascript-cpp/hyperlink/#linkType--) con un tipo de retorno [**TargetModeType**](https://reference.aspose.com/cells/javascript-cpp/targetmodetype). El siguiente fragmento de código demuestra el uso de la propiedad [**linkType**](https://reference.aspose.com/cells/javascript-cpp/hyperlink/#linkType--) usando este [archivo Excel fuente](94896195.xlsx).

### Código Fuente

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Link Types Example</title>
    </head>
    <body>
        <h1>Link Types Example</h1>
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

            document.getElementById('runExample').addEventListener('click', async () => {
                const fileInput = document.getElementById('fileInput');
                const resultDiv = document.getElementById('result');

                if (!fileInput.files.length) {
                    resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                    return;
                }

                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();

                // Instantiating a Workbook object from the uploaded file
                const workbook = new Workbook(new Uint8Array(arrayBuffer));

                // Get the first (default) worksheet
                const worksheet = workbook.worksheets.get(0);

                // Create a range A1:A7 (original code created A1:B7 but used A1 to A7 in parameters)
                const range = worksheet.cells.createRange("A1", "A7");

                // Get Hyperlinks in range
                const hyperlinks = range.hyperlinks;

                let outputHtml = '<p>Hyperlinks found:</p><ul>';
                if (typeof hyperlinks.forEach === 'function') {
                    hyperlinks.forEach(link => {
                        outputHtml += `<li>${link.textToDisplay}: ${link.linkType}</li>`;
                    });
                } else {
                    for (let i = 0; i < hyperlinks.count; i++) {
                        const link = hyperlinks.get(i);
                        outputHtml += `<li>${link.textToDisplay}: ${link.linkType}</li>`;
                    }
                }
                outputHtml += '</ul>';

                resultDiv.innerHTML = outputHtml;
            });
        });
    </script>
</html>
```


El siguiente es el resultado generado por el fragmento de código dado anteriormente.

### Salida en Consola
