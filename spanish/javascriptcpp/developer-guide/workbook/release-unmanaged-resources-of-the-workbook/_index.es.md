---
title: Liberar recursos no gestionados del libro de trabajo con JavaScript a través de C++
linktitle: Liberar recursos no administrados del libro
type: docs
weight: 310
url: /es/javascript-cpp/release-unmanaged-resources-of-the-workbook/
description: Aprende cómo liberar recursos no gestionados del objeto Workbook utilizando Aspose.Cells for JavaScript a través de C++. 
---

{{% alert color="primary" %}}

Aspose.Cells proporciona el método [**Workbook.dispose()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#dispose--) para liberar los recursos no gestionados del objeto [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook). El patrón dispose se usa solo para objetos que acceden a recursos no gestionados, como manejadores de archivos y tuberías, manejadores del registro, manejadores de espera, o punteros a bloques de memoria no gestionada. Esto se debe a que el recolector de basura es muy eficiente en recuperar objetos gestionados no utilizados, pero no puede recuperar objetos no gestionados.

{{% /alert %}}

El objeto [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) ahora implementa la interfaz *System.IDisposable* que tiene un único método [**Workbook.dispose()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#dispose--). Puedes llamar directamente al método [**Workbook.dispose()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#dispose--) o usar la declaración *Using* para llamar a este método automáticamente.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Dispose Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Loads the workbook which contains hidden external links
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create workbook object
            const wb1 = new Workbook();

            // Call Dispose method
            wb1.dispose();

            // Call Dispose method via a scoped approach
            (async () => {
                const wb2 = new Workbook();
                // Any other code goes here
                wb2.dispose();
            })();

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully!</p>';
        });
    </script>
</html>
```
