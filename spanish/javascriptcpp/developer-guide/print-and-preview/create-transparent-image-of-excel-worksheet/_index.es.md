---
title: Crear una imagen transparente de una hoja de cálculo de Excel con JavaScript a través de C++
linktitle: Create Transparent Image of Excel Worksheet
type: docs
weight: 170
url: /es/javascript-cpp/create-transparent-image-of-excel-worksheet/
description: Aprende cómo generar una imagen transparente de una hoja de cálculo de Excel usando Aspose.Cells for JavaScript a través de C++.
---

{{% alert color="primary" %}}

A veces, es necesario generar la imagen de la hoja de cálculo como una imagen transparente. Desea aplicar transparencia a todas las celdas que no tienen colores de relleno. Aspose.Cells proporciona la propiedad [**ImageOrPrintOptions.transparent**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#transparent--) para aplicar transparencia a la imagen de la hoja de cálculo. Cuando esta propiedad es **false**, entonces las celdas sin colores de relleno se dibujan con color blanco, y cuando es **true**, las celdas sin colores de relleno se dibujan transparentes.

{{% /alert %}}

En la siguiente imagen de la hoja de cálculo, no se ha aplicado transparencia. Las celdas sin colores de relleno se dibujan de color blanco.

|**Resultado sin transparencia: el fondo de la celda es blanco**|
| :- |
|![todo:image_alt_text](create-transparent-image-of-excel-worksheet_1.png)|

Mientras que, en la siguiente imagen de la hoja de cálculo, se ha aplicado transparencia. Las celdas sin colores de relleno son transparentes.

|**Resultado con transparencia habilitada**|
| :- |
|![todo:image_alt_text](create-transparent-image-of-excel-worksheet_2.png)|

El siguiente código de ejemplo genera una imagen transparente a partir de una hoja de cálculo de Excel.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Create Transparent Image Example</title>
    </head>
    <body>
        <h1>Create Transparent Image Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsm,.csv" />
        <button id="runExample">Create Transparent PNG</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, ImageOrPrintOptions, SheetRender, ImageType } = AsposeCells;

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

            // Create workbook object from uploaded file
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const sheet = wb.worksheets.get(0);

            // Apply different image or print options
            const imgOption = new ImageOrPrintOptions();
            imgOption.imageType = ImageType.Png;
            imgOption.horizontalResolution = 200;
            imgOption.verticalResolution = 200;
            imgOption.onePagePerSheet = true;

            // Apply transparency to the output image
            imgOption.transparent = true;

            // Create image after applying image or print options
            const sr = new SheetRender(sheet, imgOption);
            const outputData = await sr.toImage(0);

            const blob = new Blob([outputData], { type: 'image/png' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputCreateTransparentImage.png';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PNG Image';

            document.getElementById('result').innerHTML = '<p style="color: green;">Image created successfully! Click the download link to get the PNG file.</p>';
        });
    </script>
</html>
```
