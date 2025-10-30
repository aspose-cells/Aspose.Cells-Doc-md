---
title: Soporte para la localización alemana en fórmulas de rangos nombrados con JavaScript vía C++
linktitle: Soporte para Configuración Regional Alemana en Fórmulas de Rango Nombrado
type: docs
weight: 60
url: /es/javascript-cpp/support-for-german-locale-in-named-range-formulae/
description: Aprende cómo soportar la localidad alemana en fórmulas de rangos nombrados usando Aspose.Cells for JavaScript vía C++.
---

Las fórmulas en inglés se escriben en la región nombrada. Este archivo Excel puede abrirse en un entorno donde la configuración del sistema esté configurada en idioma alemán, sin embargo, la fórmula en inglés se traducirá al idioma alemán. El siguiente ejemplo demuestra esta característica; sin embargo, requiere que Excel esté instalado en idioma alemán y que la configuración regional del sistema también esté en alemán.  

Se puede descargar el archivo de muestra para probar esta función desde el siguiente enlace:  

[sampleNamedRangeTest.xlsm](73990165.xlsm)  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Named Range Example</title>
    </head>
    <body>
        <h1>Named Range Example</h1>
        <p>Select an existing Excel macro-enabled workbook (.xlsm) to modify, or leave empty to create a new workbook.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsm,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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
                // No file selected - a new empty workbook will be created
            }

            const file = fileInput.files.length ? fileInput.files[0] : null;
            let workbook;
            if (file) {
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Define named range name and formula
            const name = "HasFormula";
            const value = '=GET.CELL(48, INDIRECT("ZS",FALSE))';

            // Access worksheets collection
            const wsCol = workbook.worksheets;

            // Add named range and set its reference
            const nameIndex = wsCol.names.add(name);
            const namedRange = wsCol.names.get(nameIndex);
            namedRange.refersTo = value;

            // Save the modified workbook as .xlsm and provide download link
            const outputData = workbook.save(SaveFormat.Xlsm);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sampleOutputNamedRangeTest.xlsm';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Named range added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
