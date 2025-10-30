---
title: Especificar autor al proteger la escritura del libro de trabajo con JavaScript a través de C++
linktitle: Especificar Autor al proteger un libro de trabajo
type: docs
weight: 40
url: /es/javascript-cpp/specify-author-while-write-protecting-workbook/
description: Especificar un nombre de autor al proteger la escritura de un libro de trabajo usando Aspose.Cells for JavaScript a través de C++.
---

## **Escenarios de uso posibles**

Puede especificar un nombre de autor al proteger con escritura su libro de trabajo usando API Aspose.Cells. Por favor, use la propiedad [**Workbook.author**](https://reference.aspose.com/cells/javascript-cpp/writeprotection/#author--) para este propósito.

## **Especificar Autor al Proteger la Escritura del Libro de Trabajo**

El código de ejemplo siguiente explica el uso de la propiedad [**Workbook.author**](https://reference.aspose.com/cells/javascript-cpp/writeprotection/#author--). El código crea un libro de trabajo vacío, lo protege con una contraseña, especifica el nombre del autor y lo guarda como [archivo Excel de salida](67338582.xlsx). La siguiente captura de pantalla ilustra el efecto del código de ejemplo en el archivo Excel de salida para su referencia.

![todo:image_alt_text](specify-author-while-write-protecting-workbook_1.png)

## **Código de muestra**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Specify Author While Write Protecting Workbook</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
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
            // Create empty workbook.
            const workbook = new Workbook();

            // Write protect workbook with password.
            workbook.settings.writeProtection.password = "1234";

            // Specify author while write protecting workbook.
            workbook.settings.writeProtection.author = "SimonAspose";

            // Save the workbook in XLSX format.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSpecifyAuthorWhileWriteProtectingWorkbook.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and write-protected successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
