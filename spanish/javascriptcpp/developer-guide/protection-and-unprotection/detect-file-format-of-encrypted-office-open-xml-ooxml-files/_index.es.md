---
title: Detectar formato de archivo de archivos encriptados de Office Open XML  OOXML con JavaScript vía C++
linktitle: Detectar formato de archivo de XML abierto de oficina encriptado archivos OOXML
type: docs
weight: 340
url: /es/javascript-cpp/detect-file-format-of-encrypted-office-open-xml-ooxml-files/
description: Aprende cómo detectar el formato de archivo de archivos OOXML cifrados usando Aspose.Cells for JavaScript vía C++.
---

{{% alert color="primary" %}}  

**Office Open XML** (también conocido como **OOXML** o **Microsoft Open XML** (MOX)) es un formato de archivo basado en XML desarrollado por Microsoft para representar documentos de oficina como hojas de cálculo, gráficos, presentaciones y documentos de procesamiento de textos.  

{{% /alert %}}  

Aspose.Cells proporciona una manera de detectar el formato de archivo de archivos encriptados **Microsoft Open XML**. Para identificar el tipo de archivo, usa el método [FileFormatUtil.detectFileFormat(Uint8Array)](https://reference.aspose.com/cells/javascript-cpp/fileformatutil/#detectFileFormat-uint8array-) como se muestra en el ejemplo de código a continuación.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells FileFormat Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, FileFormatUtil, Utils } = AsposeCells;

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
                // Create a small byte stream equivalent to the original JavaScript Buffer
                const stream = new Uint8Array([0x50, 0x4B, 0x03, 0x04]);

                // Verify password (will propagate errors if any)
                FileFormatUtil.verifyPassword(stream, "1234");

                // Detect file format
                const fileFormatInfo = FileFormatUtil.detectFileFormat(stream);

                // Use property access per universal getter/setter conversion
                document.getElementById('result').innerHTML = '<p>File Format: ' + fileFormatInfo.fileFormatType + '</p>';
                console.log("File Format: " + fileFormatInfo.fileFormatType);
            });
        });
    </script>
</html>
```
