---
title: Renderizar Complementos de Office al convertir Excel a PDF con JavaScript vía C++
linktitle: Renderizar complementos de Office al convertir Excel a PDF
type: docs
weight: 100
url: /es/javascript-cpp/render-office-add-ins-while-converting-excel-to-pdf/
---

## **Escenarios de uso posibles**

Anteriormente, Aspose.Cells no podía renderizar complementos de Office cuando se guardaba un archivo Excel en formato PDF. Ahora Aspose.Cells los renderiza correctamente. No es necesario usar ningún método o propiedad especial para renderizar complementos de Office en el PDF de salida. Solo guarde su archivo Excel en formato PDF y se renderizarán los complementos de Office.

## **Renderizar complementos de Office al convertir Excel a PDF**

El siguiente código de ejemplo guarda el [archivo de Excel de muestra](60489769.xlsx), que contiene los complementos de Office. Por favor, mira el [PDF de salida generado con la versión anterior, es decir, 17.11](60489770.pdf) y el [PDF de salida generado con la versión más reciente, es decir, 17.12 y posteriores](60489771.pdf). La salida de la versión anterior es en blanco, pero la versión más reciente muestra los complementos de Office.

## **Código de muestra**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Render Office Add-Ins to PDF Example</title>
    </head>
    <body>
        <h1>Render Office Add-Ins to PDF Example</h1>
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
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get Aspose.Cells version (converted from getVersion())
            const version = AsposeCells.CellsHelper.version;

            // Save workbook to PDF format
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = `output-${version}.pdf`;
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Saved to PDF successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
