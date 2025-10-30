---
title: Detectar si una hoja está protegida con contraseña mediante JavaScript usando C++
linktitle: Detectar si la hoja de cálculo está protegida con contraseña
type: docs
weight: 360
url: /es/javascript-cpp/detect-if-worksheet-is-password-protected/
description: Aprende cómo detectar si una hoja está protegida con contraseña usando Aspose.Cells for JavaScript mediante C++. 
keywords: Detectar protección con contraseña en hoja de cálculo JavaScript mediante C++, Verificar si una hoja está protegida con contraseña JavaScript mediante C++, Aspose.Cells for JavaScript mediante C++
---

{{% alert color="primary" %}}

Es posible proteger los libros de trabajo y las hojas de trabajo por separado. Por ejemplo, una hoja de cálculo puede contener una o más hojas de trabajo con contraseña, sin embargo, la hoja de cálculo en sí puede estar protegida o no. Las APIs de Aspose.Cells proporcionan los medios para detectar si una hoja de trabajo determinada está protegida con contraseña o no. Este artículo demuestra el uso de Aspose.Cells for JavaScript a través de la API de C++ para lograr lo mismo.

{{% /alert %}}

Aspose.Cells for JavaScript a través de C++ ha expuesto la propiedad [**Protection.isProtectedWithPassword()**](https://reference.aspose.com/cells/javascript-cpp/protection/#isProtectedWithPassword--) para detectar si una hoja de trabajo está protegida con contraseña o no. La propiedad de tipo booleano [**Protection.isProtectedWithPassword()**](https://reference.aspose.com/cells/javascript-cpp/protection/#isProtectedWithPassword--) devuelve **true** si [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) está protegida con contraseña y **false** si no.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Check Worksheet Password Protection</h1>
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

            // Create an instance of Workbook and load a spreadsheet
            const book = new Workbook(new Uint8Array(arrayBuffer));

            // Access the protected Worksheet
            const sheet = book.worksheets.get(0);

            // Check if Worksheet is password protected
            if (sheet.protection.isProtectedWithPassword()) {
                resultDiv.innerHTML = '<p>Worksheet is password protected</p>';
                console.log("Worksheet is password protected");
            } else {
                resultDiv.innerHTML = '<p>Worksheet is not password protected</p>';
                console.log("Worksheet is not password protected");
            }
        });
    </script>
</html>
```
