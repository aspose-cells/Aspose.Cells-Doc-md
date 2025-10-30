---
title: Obtener validación de celda en archivos ODS
type: docs
weight: 180
url: /es/javascript-cpp/get-cell-validation-in-ods-files/
description: Aprenda cómo obtener la validación de celdas en archivos ODS mediante el script Aspose.Cells for Java a través de la API C++. 
keywords: Obtener Validación de Celdas mediante JavaScript vía C++, Obtener Validación de Celdas mediante C++
---

## **Obtener validación de celda en archivos ODS**  

Con Aspose.Cells for JavaScript vía C++, puedes obtener la validación aplicada a una celda en archivos ODS. Para esto, la API proporciona la propiedad [**Cell.validation**](https://reference.aspose.com/cells/javascript-cpp/cell/#validation--) de la clase [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell/).  

El siguiente ejemplo de código demuestra el uso de la propiedad [**Cell.validation**](https://reference.aspose.com/cells/javascript-cpp/cell/#validation--) cargando el archivo [source ODS](101089354.ods) y leyendo la validación de la celda A9.  

### **Código de muestra**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Validation Check Example</h1>
        <input type="file" id="fileInput" accept=".ods,.xls,.xlsx,.csv" />
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
            const resultEl = document.getElementById('result');

            if (!fileInput.files.length) {
                resultEl.innerHTML = '<p style="color: red;">Please select an Excel or ODS file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Opening the Excel/ODS file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the file
            const worksheet = workbook.worksheets.get(0);

            // Access cell A9
            const cell = worksheet.cells.get("A9");

            if (cell.validation !== null) {
                resultEl.innerHTML = `<p>Validation type: ${cell.validation.type}</p>`;
            } else {
                resultEl.innerHTML = '<p>No validation on A9.</p>';
            }
        });
    </script>
</html>
```
