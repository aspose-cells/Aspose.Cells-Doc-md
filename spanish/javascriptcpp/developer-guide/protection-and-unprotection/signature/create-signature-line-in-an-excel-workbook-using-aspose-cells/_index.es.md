---
title: Crear línea de firma en un libro de Excel usando Aspose.Cells for JavaScript mediante C++
linktitle: Crear Línea de Firma en un Libro de Excel usando Aspose.Cells
type: docs
weight: 150
url: /es/javascript-cpp/create-signature-line-in-an-excel-workbook-using-aspose-cells/
description: Este artículo describe cómo crear una línea de firma en un libro de Excel usando código JavaScript con Aspose.Cells for JavaScript mediante C++.
keywords: Crear línea de firma en un libro de Excel JavaScript mediante C++, Cómo crear una línea de firma en un libro de Excel, Cómo agregar una línea de firma, Cómo agregar una línea de firma al archivo de Excel.
---

## **Introducción**  

Microsoft Excel proporciona una función para agregar **Línea de Firma** en libros de Excel. Puedes agregar una Línea de Firma haciendo clic en la pestaña **Insertar** y luego seleccionando **Línea de Firma** del grupo **Texto**.  

## **Cómo crear una línea de firma para Excel**  

Aspose.Cells for JavaScript mediante C++ también proporciona esta función y ha expuesto la propiedad [**Picture.signatureLine**](https://reference.aspose.com/cells/javascript-cpp/picture/#signatureLine--) para este propósito. Este artículo explicará cómo usar esta propiedad para agregar una línea de firma usando Aspose.Cells.  

El código de ejemplo siguiente agrega una línea de firma usando la propiedad [**Picture.signatureLine**](https://reference.aspose.com/cells/javascript-cpp/picture/#signatureLine--) y guarda el libro de trabajo.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Add Signature Line Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, SignatureLine, Utils } = AsposeCells;

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

            // Create or load workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Create signature line object
            const signatureLine = new SignatureLine();
            signatureLine.signer = "John Doe";
            signatureLine.title = "Development Lead";
            signatureLine.email = "john.doe@aspose.com";

            // Adds a Signature Line to the first worksheet.
            workbook.worksheets.get(0).shapes.addSignatureLine(1, 1, signatureLine);

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Signature line added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
