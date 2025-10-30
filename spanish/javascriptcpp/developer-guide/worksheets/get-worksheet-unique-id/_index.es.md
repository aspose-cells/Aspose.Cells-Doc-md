---
title: Obtener ID único de la hoja de trabajo con JavaScript vía C++
linktitle: Obtener el identificador único de la hoja de trabajo
type: docs
weight: 190
url: /es/javascript-cpp/get-worksheet-unique-id/
description: Este artículo muestra cómo obtener el ID único de la hoja de Excel usando la biblioteca JavaScript y la API de C++ de manera programática.
keywords: ID único de la hoja de Excel JavaScript vía C++, ID único de la hoja JavaScript vía C++
---

## **Obtener el ID único de la hoja de trabajo**

Aspose.Cells for JavaScript vía C++ ofrece la capacidad de obtener el ID único de una hoja de trabajo utilizando la propiedad [**Worksheet.uniqueId**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#uniqueId--). El siguiente fragmento de código demuestra el uso de la propiedad [**Worksheet.uniqueId**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#uniqueId--) para imprimir el ID único de una hoja. El siguiente fragmento de código usa este [archivo de ejemplo de Excel](105480213.xlsx).

### Código Fuente

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Get Worksheet Unique Id Example</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Get Unique Id
            const uniqueId = worksheet.uniqueId;
            console.log("Unique Id: " + uniqueId);

            document.getElementById('result').innerHTML = '<p style="color: green;">Unique Id: ' + uniqueId + '</p>';
        });
    </script>
</html>
```
