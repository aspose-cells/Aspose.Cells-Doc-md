---
title: Convertir revisión de XLSB a XLSM con JavaScript a través de C++
linktitle: Convertir revisión de XLSB a XLSM
type: docs
weight: 290
url: /es/javascript-cpp/convert-revision-of-xlsb-to-xlsm/
description: Aprende cómo convertir completamente revisiones de archivos XLSB en formato XLSM usando Aspose.Cells for JavaScript a través de C++.
---

{{% alert color="primary" %}}

Aspose.Cells ahora admite la conversión completa de revisiones de archivos XLSB a archivos XLSM. Las revisiones se encuentran dentro de la ruta \xl\revisions. Puedes verlas cambiando la extensión de tu archivo XLSB a ZIP. La ruta \xl\revisions contiene archivos que terminan con extensión .bin.

Cuando conviertes tu archivo XLSB a un archivo XLSM usando Aspose.Cells, estos archivos .bin se convierten exitosamente en archivos .xml como se muestra en estas dos capturas de pantalla.

{{% /alert %}}

 El siguiente ejemplo de código te muestra cómo convertir el archivo XLSB en formato XLSM usando Aspose.Cells for JavaScript a través de C++.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert XLSB to XLSM Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsb,.csv" />
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file (.xlsb, .xls, .xlsx).</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Open workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save Workbook to XLSM format
            const outputData = workbook.save(SaveFormat.Xlsm);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsm';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Converted XLSM File';

            resultDiv.innerHTML = '<p style="color: green;">Workbook converted to XLSM successfully. Click the download link to save the file.</p>';
        });
    </script>
</html>
```
