---
title: Leer hojas de cálculo de Numbers desarrolladas por Apple Inc. usando Aspose.Cells for JavaScript a través de C++
linktitle: Leer Hojas de cálculo Numbers desarrolladas por Apple Inc. usando Aspose.Cells
type: docs
weight: 140
url: /es/javascript-cpp/read-numbers-spreadsheet-developed-by-apple-inc-using-aspose-cells/
description: Aprende cómo leer hojas de cálculo Numbers desarrolladas por Apple Inc. usando Aspose.Cells for JavaScript a través de C++. 
---

## **Escenarios de uso posibles**

Numbers es una aplicación de hoja de cálculo desarrollada por Apple Inc. Aspose.Cells puede leer hojas de cálculo de Numbers, pero no soporta escribir en ellas. Puede leer datos, estilos y fórmulas de hojas de cálculo de Numbers.

## **Leer hojas de cálculo Numbers desarrolladas por Apple Inc. usando Aspose.Cells for JavaScript a través de C++**

El siguiente código de ejemplo carga la [Hoja de cálculo de Números de muestra](sampleNumbersByAppleInc.numbers) y la convierte en [Formato PDF de salida](outputNumbersByAppleInc.pdf). Tendrás que usar la clase [**LoadOptions**](https://reference.aspose.com/cells/javascript-cpp/loadoptions) y especificar [**LoadFormat.Numbers**](https://reference.aspose.com/cells/javascript-cpp/loadformat) como parámetro en su constructor para cargarla correctamente. Por favor, descarga ambos desde los enlaces proporcionados. Puedes probar el código con cualquier hoja de cálculo de Numbers. También lee los comentarios del código para más ayuda.

## **Código de muestra**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Numbers to PDF Example</title>
    </head>
    <body>
        <h1>Convert Apple Numbers to PDF</h1>
        <input type="file" id="fileInput" accept=".numbers" />
        <button id="runExample">Convert to PDF</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions, LoadFormat } = AsposeCells;

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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select a .numbers file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Specify load options to load Numbers spreadsheet
            const opts = new LoadOptions(LoadFormat.Numbers);

            // Load the Numbers spreadsheet in workbook with above load options
            const wb = new Workbook(new Uint8Array(arrayBuffer), opts);

            // Save the workbook to PDF format
            const outputData = wb.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputNumbersByAppleInc.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the PDF.</p>';
        });
    </script>
</html>
```
