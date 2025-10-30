---
title: Cómo detectar el formato de archivo y verificar si el archivo está cifrado con JavaScript vía C++
linktitle: Cómo Detectar el Formato de un Archivo y Verificar si el Archivo está Encriptado
type: docs
weight: 2700
url: /es/javascript-cpp/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/
description: Aprende cómo detectar un formato de archivo y verificar si un archivo está cifrado usando Aspose.Cells for JavaScript vía C++.
---

{{% alert color="primary" %}}  
A veces necesitas detectar el formato de un archivo antes de abrirlo porque la extensión del archivo no garantiza que el contenido del archivo sea apropiado. El archivo podría estar cifrado (un archivo protegido con contraseña), por lo que no se puede leer directamente, o no deberíamos leerlo. Aspose.Cells for JavaScript vía C++ proporciona el método estático [**FileFormatUtil.detectFileFormat(Uint8Array)**](https://reference.aspose.com/cells/javascript-cpp/fileformatutil/#detectFileFormat-uint8array-) y algunas API relevantes que puedes usar para procesar documentos.  
{{% /alert %}}  

El siguiente código de ejemplo ilustra cómo detectar el formato de un archivo (usando la ruta del archivo) y verificar su extensión. También puedes determinar si el archivo está encriptado.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells File Format Detection Example</h1>
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

            // Detect file format
            const info = AsposeCells.FileFormatUtil.detectFileFormat(new Uint8Array(arrayBuffer));

            // Gets the detected load format (converted getter -> property)
            const extension = AsposeCells.FileFormatUtil.loadFormatToExtension(info.loadFormat);
            const encrypted = info.isEncrypted;

            console.log("The spreadsheet format is: " + extension);
            console.log("The file is encrypted: " + encrypted);

            resultDiv.innerHTML = `<p>The spreadsheet format is: <strong>${extension}</strong></p>
                                   <p>The file is encrypted: <strong>${encrypted}</strong></p>`;
        });
    </script>
</html>
```
