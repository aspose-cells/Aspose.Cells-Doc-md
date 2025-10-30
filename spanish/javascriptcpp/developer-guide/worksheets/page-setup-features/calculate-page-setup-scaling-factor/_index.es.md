---
title: Calcular el factor de escala de configuración de página con JavaScript vía C++
linktitle: Calcular Factor de Escala de Configuración de Página
type: docs
weight: 300
url: /es/javascript-cpp/calculate-page-setup-scaling-factor/
description: Este artículo proporciona un código de ejemplo que explica cómo usar la API de JavaScript vía C++ para calcular el factor de escala de configuración de página usando la opción Ajustar a n página(s) de ancho por m alto de la hoja de cálculo de Excel de manera programática.
keywords: Ajustar a n páginas de ancho por m alto en Excel JavaScript vía C++, calcular el factor de escala de configuración de página con JavaScript vía C++
---

{{% alert color="primary" %}}

Cuando se establece la escala de la configuración de página usando la opción **Ajustar a n páginas de ancho por m de alto**, Microsoft Excel calcula el factor de escala de la configuración de página. Puedes calcularlo usando la propiedad [**SheetRender.pageScale**](https://reference.aspose.com/cells/javascript-cpp/sheetrender/#pageScale--). Esta propiedad devuelve un valor doble que puede convertirse en porcentaje. Por ejemplo, si devuelve 0.5, significa que el factor de escala es del 50%.

{{% /alert %}}

El siguiente código de ejemplo ilustra cómo calcular el factor de escala de configuración de página utilizando la propiedad [**SheetRender.pageScale**](https://reference.aspose.com/cells/javascript-cpp/sheetrender/#pageScale--).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Page Scale</title>
    </head>
    <body>
        <h1>Page Scale Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, SheetRender, ImageOrPrintOptions, PaperSizeType, Utils } = AsposeCells;

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

            // Opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Put some data in these cells
            worksheet.cells.get("A4").putValue("Test");
            worksheet.cells.get("S4").putValue("Test");

            // Set paper size
            worksheet.pageSetup.paperSize = PaperSizeType.PaperA4;

            // Set fit to pages wide as 1
            worksheet.pageSetup.fitToPagesWide = 1;

            // Calculate page scale via sheet render
            const sr = new SheetRender(worksheet, new ImageOrPrintOptions());

            // Convert page scale double value to percentage
            const strPageScale = (sr.pageScale * 100).toFixed(0) + "%";

            // Write the page scale value
            document.getElementById('result').innerHTML = `<p>Page Scale: ${strPageScale}</p>`;
            console.log(strPageScale);
        });
    </script>
</html>
```
