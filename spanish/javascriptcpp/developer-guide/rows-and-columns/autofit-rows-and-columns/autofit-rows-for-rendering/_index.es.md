---
title: Ajuste automático de filas para renderizado con JavaScript a través de C++
linktitle: Autoajustar filas para renderizado
type: docs
weight: 130
url: /es/javascript-cpp/autofit-rows-for-rendering/
description: Aprende cómo ajustar automáticamente filas para renderizado en Excel usando Aspose.Cells for JavaScript a través de C++. Previene el recorte de texto en archivos PDF guardados.
---

En general, cuando desea mostrar todo el texto en una celda, puede ajustar automáticamente la fila en la vista normal con zoom del 100% en Microsoft Excel. Esto permite que el texto sea completamente visible en vista normal, e incluso cuando imprima o guarde el archivo como PDF, el texto se mostrará correctamente.

Sin embargo, en algunos casos, el ajuste automático de la fila funciona bien en vista normal, pero cuando cambia a vista de impresión o guarda el archivo como PDF, el texto se recorta. Por favor, verifique el archivo fuente [Book1.xlsx](Book1.xlsx) y las capturas de pantalla.

![el texto está recortado en la vista de impresión](text_clipped_in_printview.png)

Si quieres evitar que el texto se corte en el archivo PDF guardado, puedes ajustar automáticamente la fila con la opción [AutoFitterOptions.forRendering](https://reference.aspose.com/cells/javascript-cpp/autofitteroptions/#forRendering--).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Autofit Rows and Save as PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, AutoFitterOptions, SaveFormat, Utils } = AsposeCells;

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

            // Init workbook instance from uploaded file.
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Set autofit options for rendering.
            const autoFitterOptions = new AutoFitterOptions();
            autoFitterOptions.forRendering = true;

            // Autofit rows with options on first worksheet.
            const worksheet = workbook.worksheets.get(0);
            worksheet.autoFitRows(autoFitterOptions);

            // Save to pdf.
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```

Ahora, el texto no está recortado en el archivo PDF de salida.

![el texto no está recortado en el PDF guardado](text_not_clipped_in_saved_pdf.png)
