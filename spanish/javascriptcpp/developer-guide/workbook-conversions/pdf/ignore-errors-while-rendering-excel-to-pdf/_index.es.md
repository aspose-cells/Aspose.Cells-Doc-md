---
title: Ignorar errores al renderizar Excel a PDF con JavaScript vía C++
linktitle: Ignorar Errores al Renderizar Excel a PDF
type: docs
weight: 80
url: /es/javascript-cpp/ignore-errors-while-rendering-excel-to-pdf/
description: Aprende cómo ignorar errores durante la conversión de archivos Excel a PDF usando Aspose.Cells for JavaScript vía C++.
---

## **Escenarios de uso posibles**  

A veces, al convertir su archivo Excel a PDF, ocurren errores o excepciones y el proceso de conversión termina. Puede ignorar todos esos errores durante la conversión usando la propiedad [**PdfSaveOptions.ignoreError**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#ignoreError--). De esta manera, el proceso de conversión se completará sin lanzar ningún error o excepción, pero puede ocurrir pérdida de datos. Por lo tanto, utilice esta propiedad solo si la pérdida de datos no es crítica para usted.  

## **Ignorar errores al renderizar Excel a PDF**  

El siguiente código carga el [archivo Excel de ejemplo](55541778.xlsx), pero el archivo de ejemplo tiene errores y lanza un error durante la [conversión a PDF](55541779.pdf) en 17.11, pero como estamos usando la propiedad [**PdfSaveOptions.ignoreError**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#ignoreError--), no lanza error. Sin embargo, una *forma en forma de flecha roja redonda* como se muestra en esta captura de pantalla se pierde.  

![todo:image_alt_text](ignore-errors-while-rendering-excel-to-pdf_1.png)  

## **Código de muestra**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Excel to PDF (Ignore Errors) Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to PDF (Ignore Errors)</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions, Utils } = AsposeCells;

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

            // Specify Pdf Save Options - Ignore Error
            const opts = new PdfSaveOptions();
            opts.ignoreError = true;

            // Save the Workbook in Pdf with Pdf Save Options
            const outputData = workbook.save(SaveFormat.Pdf, opts);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputErrorExcel2Pdf.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
