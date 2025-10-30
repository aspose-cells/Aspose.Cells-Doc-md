---
title: Rotar texto con forma dentro de la hoja de trabajo usando JavaScript a través de C++
linktitle: Rotar Texto con Forma dentro de la Hoja de Cálculo
type: docs
weight: 1300
url: /es/javascript-cpp/rotate-text-with-shape-inside-the-worksheet/
description: Aprenda cómo rotar el texto con la forma dentro de una hoja de Excel usando Aspose.Cells for JavaScript a través de C++.
---

## **Escenarios de uso posibles**

Puede agregar texto dentro de cualquier forma usando Microsoft Excel. Si agrega una forma usando Microsoft Excel 2003 muy antiguo, entonces el texto no rotará con la forma. Pero si agrega una forma usando versiones más recientes de Microsoft Excel, por ejemplo, 2007, 2010, 2013 o 2016, etc., entonces el texto rotará con la forma. Puede controlar si el texto debe rotar con la forma o no usando la propiedad [**ShapeTextAlignment.rotateTextWithShape**](https://reference.aspose.com/cells/javascript-cpp/shapetextalignment/#rotateTextWithShape--). Su valor predeterminado es **true**, lo que significa que el texto rotará con la forma, pero si lo establece en **false**, entonces el texto no rotará con la forma.

## **Rotar texto con forma dentro de la hoja de cálculo**

El siguiente código de ejemplo carga el [archivo de Excel de muestra](64716896.xlsx) que tiene una forma de triángulo y su texto rota con la forma. Si abres el archivo de Excel de muestra en Microsoft Excel y giras la forma del triángulo, el texto también rotará con ella. Luego, el código establece la propiedad [**ShapeTextAlignment.rotateTextWithShape**](https://reference.aspose.com/cells/javascript-cpp/shapetextalignment/#rotateTextWithShape--) como **false** y lo guarda como [archivo de Excel de salida](64716897.xlsx). Si ahora abres el archivo de Excel de salida en Microsoft Excel y giras la forma del triángulo, el texto no rotará con ella. Por favor, mira la siguiente captura de pantalla que muestra el efecto del código en el archivo de Excel de muestra para referencia.

![todo:image_alt_text](rotate-text-with-shape-inside-the-worksheet_1.png)

## **Código de muestra**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Rotate Text With Shape</title>
    </head>
    <body>
        <h1>Rotate Text With Shape Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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

            // Instantiating a Workbook object by loading the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet.
            const worksheet = workbook.worksheets.get(0);

            // Access cell B4 and add message inside it.
            const cellB4 = worksheet.cells.get("B4");
            cellB4.value = "Text is not rotating with shape because RotateTextWithShape is false.";

            // Access first shape.
            const shape = worksheet.shapes.get(0);

            // Access shape text alignment.
            const shapeTextAlignment = shape.textBody.textAlignment;

            // Do not rotate text with shape by setting RotateTextWithShape as false.
            shapeTextAlignment.rotateTextWithShape = false;

            // Saving the modified Excel file and providing download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputRotateTextWithShapeInsideWorksheet.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
