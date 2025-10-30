---
title: Configurar encabezados y pies de página diferentes para páginas distintas con JavaScript mediante C++
linktitle: Configuración de diferentes encabezados y pies de página para diferentes páginas
type: docs
weight: 35
url: /es/javascript-cpp/setting-different-headers-and-footers-for-pages-to-excel/
description: Este artículo proporciona código de ejemplo que muestra cómo establecer programáticamente encabezados y pies de página en Configuración de página de la hoja de Excel usando Aspose.Cells for JavaScript mediante C++. Configurar encabezados y pies de página para la primera, páginas impares y pares.
keywords: establecer encabezado pie de página de Excel primera página JavaScript mediante C++, establecer encabezado pie de página de páginas impares JavaScript mediante C++, establecer encabezado pie de página de páginas pares JavaScript mediante C++
---

{{% alert color="primary" %}}

 MS Excel admite la configuración de diferentes encabezados y pies de página para la primera página, páginas impares y pares desde Excel 2007.
Aspose.Cells for JavaScript mediante C++ soporta la misma característica.

{{% /alert %}}

## **Configuración de diferentes encabezados y pies de página en MS Excel**

**![Configuración de diferentes encabezados y pies de página](difpage.png)**

1. Haz clic en **diseño de página > títulos de impresión > encabezado/pie de página**.
1. Verifica **Diferentes páginas impares y pares** o **Primera página diferente**.
1. Ingrese encabezados y pies de página diferentes.

## **Establecer encabezados y pies de página diferentes con Aspose.Cells for JavaScript mediante C++**

Aspose.Cells se comporta igual que Excel.
1. Establece las banderas [PageSetup.isHFDiffOddEven()](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#isHFDiffOddEven--) y [PageSetup.isHFDiffFirst()](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#isHFDiffFirst--) 
1. Ingrese encabezados y pies de página diferentes.
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - PageSetup Headers</title>
    </head>
    <body>
        <h1>PageSetup Headers Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Gets the setting of page setup for the first worksheet.
            const pageSetup = workbook.worksheets.get(0).pageSetup;

            // Sets different odd and even pages
            pageSetup.isHFDiffOddEven = true;

            // Set center header (index 1) for odd pages
            pageSetup.header = pageSetup.header || [];
            pageSetup.header[1] = "I am the header of the Odd page.";

            // Set center header (index 1) for even pages
            pageSetup.evenHeader = pageSetup.evenHeader || [];
            pageSetup.evenHeader[1] = "I am the header of the Even page.";

            // Sets different first page
            pageSetup.isHFDiffFirst = true;

            // Set center header (index 1) for first page
            pageSetup.firstPageHeader = pageSetup.firstPageHeader || [];
            pageSetup.firstPageHeader[1] = "I am the header of the First page.";

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Page setup headers updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
