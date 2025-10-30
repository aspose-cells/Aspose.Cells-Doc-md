---
title: Cálculo de las funciones MINIFS y MAXIFS en Excel 2016 con JavaScript vía C++
description: Este artículo explica cómo usar la biblioteca Aspose.Cells para calcular las funciones MINIFS y MAXIFS en Microsoft Excel 2016 usando JavaScript vía C++. Carga un archivo de Excel existente o crea uno nuevo, y usa los métodos de Aspose.Cells para calcular estas funciones y guardar los resultados en disco.
keywords: Aspose.Cells, Excel, 2016, función MINIFS, función MAXIFS, cálculo JavaScript vía C++
type: docs
weight: 300
url: /es/javascript-cpp/calculation-of-excel-2016-minifs-and-maxifs-functions/
---

## **Escenarios de uso posibles**
Microsoft Excel 2016 soporta las funciones MINIFS y MAXIFS. Estas funciones no son compatibles en Excel 2013 o versiones anteriores. Aspose.Cells for JavaScript vía C++ también soporta el cálculo de estas funciones. La siguiente captura ilustra el uso de estas funciones. Por favor, lee los comentarios en rojo dentro de la captura para saber cómo funcionan estas funciones.

![todo:image_alt_text](calculation-of-excel-2016-minifs-and-maxifs-functions_1.png)

## **Cálculo de las funciones MINIFS y MAXIFS de Excel 2016**
El siguiente código de ejemplo carga el [archivo de Excel de ejemplo](5115149.xlsx) y llama al método [Workbook.calculateFormula()](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--) para realizar el cálculo de fórmulas a través de Aspose.Cells for JavaScript en C++, y luego guarda los resultados en el [PDF de salida](5115154.pdf).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>MINIFS and MAXIFS Calculation to PDF</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions } = AsposeCells;

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

            // Load your source workbook containing MINIFS and MAXIFS functions
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Perform Aspose.Cells formula calculation
            workbook.calculateFormula();

            // Save the calculations result in pdf format
            const options = new PdfSaveOptions();
            options.onePagePerSheet = true;

            const outputData = workbook.save(SaveFormat.Pdf, options);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputMINIFSAndMAXIFS.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF Result';

            document.getElementById('result').innerHTML = '<p style="color: green;">Calculation and conversion completed successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```
