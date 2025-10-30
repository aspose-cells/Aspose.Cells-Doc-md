---
title: Coloca una imagen como textura dentro de la forma con JavaScript a través de C++
linktitle: Colocar imagen como textura dentro de la forma
type: docs
weight: 1700
url: /es/javascript-cpp/tile-picture-as-a-texture-inside-the-shape/
description: Aprende cómo tiled una pequeña imagen como textura dentro de una forma usando Aspose.Cells for JavaScript a través de C++.
---

## **Escenarios de uso posibles**  

Cuando la imagen es pequeña y no cubre toda la superficie de la forma sin perder su calidad, entonces tiene la opción de colocarla como textura. Colocar como textura llena la superficie de la forma con una imagen pequeña repitiéndola como si fueran azulejos.  

## **Colocar imagen como textura dentro de la forma**  

Puedes llenar la superficie de la forma con alguna imagen y tiled usando la propiedad [**Shape.isTiling()**](https://reference.aspose.com/cells/javascript-cpp/texturefill/#isTiling--) y configurándola en **true**. Por favor, consulta el siguiente código de ejemplo, su [archivo Excel de ejemplo](46465050.xlsx) así como la captura de pantalla para referencia.  

## **Captura de pantalla**  

![todo:image_alt_text](tile-picture-as-a-texture-inside-the-shape_1.png)  

## **Código de muestra**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Texture Fill IsTiling Example</title>
    </head>
    <body>
        <h1>Texture Fill IsTiling Example</h1>
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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Accessing the first shape inside the worksheet
            const shape = worksheet.shapes.get(0);

            // Tile Picture as a Texture inside the Shape
            shape.fill.textureFill.isTiling = true;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputTextureFill_IsTiling.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Texture fill set to tiling. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
