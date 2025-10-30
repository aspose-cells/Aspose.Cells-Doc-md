---
title: Implementar tamaño de papel personalizado de la hoja para renderizado con JavaScript vía C++
linktitle: Implementar tamaño de papel personalizado de la hoja de cálculo para la representación
type: docs
weight: 70
url: /es/javascript-cpp/implement-custom-paper-size-of-worksheet-for-rendering/
description: Este artículo explica cómo usar la API de JavaScript vía C++ para establecer un tamaño de papel personalizado en las hojas deseadas al renderizar un archivo de Excel a formato PDF de manera programática.
keywords: Establecer tamaño de papel personalizado al convertir Excel a PDF JavaScript mediante C++
---

## **Escenarios de uso posibles**  

No hay opción disponible directamente para crear tamaños de papel personalizados en MS Excel, sin embargo, puedes establecer un tamaño de papel personalizado en las hojas de trabajo deseadas al renderizar un archivo de Excel en formato PDF. Este documento explica cómo configurar un tamaño de papel personalizado en una hoja de trabajo usando las API de Aspose.Cells.  

## **Implementar Tamaño de Papel Personalizado de la Hoja de Cálculo para el Renderizado**  

 Aspose.Cells te permite implementar el tamaño de papel deseado de la hoja de trabajo. Puedes usar el método [**PageSetup.customPaperSize(number, number)**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#customPaperSize-number-number-) de la clase [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/) para especificar un tamaño de página personalizado. El siguiente código de ejemplo ilustra cómo especificar un tamaño de papel personalizado para la primera hoja del libro. También mira el [PDF de salida](45056028.pdf) generado con el siguiente código como referencia.  

## **Captura de pantalla**  

![todo:image_alt_text](implement-custom-paper-size-of-worksheet-for-rendering_1.png)  

## **Código de muestra**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Custom PDF Paper Size Example</h1>
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
                // If no file provided, create a new workbook as in the original JavaScript example
                const wb = new Workbook();

                // Access first worksheet
                const ws = wb.worksheets.get(0);

                // Set custom paper size in unit of inches
                ws.pageSetup.customPaperSize(6, 4);

                // Access cell B4
                const b4 = ws.cells.get("B4");

                // Add the message in cell B4
                b4.value = "Pdf Page Dimensions: 6.00 x 4.00 in";

                // Save the workbook in pdf format
                const outputData = wb.save(SaveFormat.Pdf);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = 'outputCustomPaperSize.pdf';
                downloadLink.style.display = 'block';
                downloadLink.textContent = 'Download PDF File';

                document.getElementById('result').innerHTML = '<p style="color: green;">PDF created successfully! Click the download link to get the file.</p>';
                return;
            }

            // If a file is provided, open it and apply the same operations
            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate workbook from uploaded file
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const ws = wb.worksheets.get(0);

            // Set custom paper size in unit of inches
            ws.pageSetup.customPaperSize(6, 4);

            // Access cell B4
            const b4 = ws.cells.get("B4");

            // Add the message in cell B4
            b4.value = "Pdf Page Dimensions: 6.00 x 4.00 in";

            // Save the workbook in pdf format
            const outputData = wb.save(SaveFormat.Pdf);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputCustomPaperSize.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
