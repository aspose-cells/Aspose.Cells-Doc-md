---
title: Json con JavaScript vía C++
linktitle: Json
type: docs
weight: 300
url: /es/javascript-cpp/convert-workbook-to-json/
description: Aprende cómo convertir un libro de Excel a JSON usando Aspose.Cells for JavaScript vía C++.
---

{{% alert color="primary" %}}
Aspose.Cells soporta la conversión de un libro a JSON (JavaScript Object Notation).
{{% /alert %}}

## **Convertir Libro de Excel a JSON**

La API de Aspose.Cells ofrece soporte para convertir hojas de cálculo a formato JSON. Para exportar el libro a JSON, pasa [**SaveFormat.Json**](https://reference.aspose.com/cells/javascript-cpp/saveformat) como el segundo parámetro del método [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-string-saveformat-). También puedes usar la clase [**JsonSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/jsonsaveoptions) para especificar configuraciones adicionales para exportar la hoja de cálculo a JSON.

El siguiente ejemplo de código demuestra cómo exportar la hoja activa a JSON usando el miembro de enumeración [**SaveFormat.Json**](https://reference.aspose.com/cells/javascript-cpp/saveformat/#json). Por favor, vea el código para convertir el [archivo fuente](book1.xlsx) al [archivo JSON de salida](book1.Json) generado por el código como referencia.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Convert Workbook to JSON</title>
    </head>
    <body>
        <h1>Convert Workbook to JSON Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to JSON</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save workbook as JSON
            const outputData = workbook.save(SaveFormat.Json);
            const blob = new Blob([outputData], { type: 'application/json' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.json';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download JSON File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook converted to JSON successfully! Click the download link to get the JSON file.</p>';
        });
    </script>
</html>
```

## **Temas avanzados**
- [Convertir CSV a JSON](/cells/es/javascript-cpp/convert-csv-to-json/)
- [Convertir-Excel-a-JSON](/cells/es/javascript-cpp/convert-excel-to-json/)
- [Convertir JSON a CSV](/cells/es/javascript-cpp/convert-json-to-csv/)
- [Convertir-JSON-a-Excel](/cells/es/javascript-cpp/convert-json-to-excel/)
