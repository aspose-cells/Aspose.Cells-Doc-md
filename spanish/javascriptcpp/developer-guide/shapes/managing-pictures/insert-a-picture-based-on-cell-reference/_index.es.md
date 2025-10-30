---
title: Insertar una imagen basada en la referencia de celda con JavaScript a través de C++
linktitle: Insertar una imagen basada en una referencia de celda
type: docs
weight: 150
url: /es/javascript-cpp/insert-a-picture-based-on-cell-reference/
description: Aprende cómo insertar una imagen en una hoja de cálculo basada en una referencia de celda usando Aspose.Cells for JavaScript a través de C++. Mostrar los datos de la celda en una imagen.
---

{{% alert color="primary" %}}
A veces tienes una imagen vacía y necesitas mostrar datos o contenidos en la imagen configurando una referencia de celda en la Barra de Fórmulas. Aspose.Cells soporta esta característica (Microsoft Excel 2010).
{{% /alert %}}

## Insertar una imagen basada en una referencia de celda

Aspose.Cells for JavaScript a través de C++ admite mostrar el contenido de una celda de hoja de cálculo en una forma de imagen. Puedes enlazar la imagen a la celda que contiene los datos que deseas mostrar. Como la celda o rango de celdas está enlazada al objeto gráfico, los cambios que hagas en los datos en esa celda o rango de celdas aparecen automáticamente en el objeto gráfico. Agrega una imagen a la hoja llamando al método [**ShapeCollection.addPicture(number, number, number, number, Uint8Array)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addPicture-number-number-number-number-uint8array-) de la colección [**ShapeCollection**](https://reference.aspose.com/cells/javascript-cpp/shapecollection) (encapsulado en el objeto [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)). Especifica el rango de celdas usando el atributo [**Picture.formula**](https://reference.aspose.com/cells/javascript-cpp/picture/#formula--) del objeto [**Picture**](https://reference.aspose.com/cells/javascript-cpp/picture).

### Ejemplo de código

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Referenced Picture Example</h1>
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
            // Instantiate a new Workbook
            const workbook = new Workbook();
            // Get the first worksheet's cells collection
            const cells = workbook.worksheets.get(0).cells;

            // Add string values to the cells
            cells.get("A1").value = "A1";
            cells.get("C10").value = "C10";

            // Get the conditional icon's image data
            const imagedata = AsposeCells.ConditionalFormattingIcon.iconImageData(AsposeCells.IconSetType.TrafficLights31, 0);
            // Create a stream based on the image data
            const stream = Uint8Array.from(imagedata);

            // Add a blank picture to the D1 cell
            const pic = workbook.worksheets.get(0).shapes.addPicture(0, 3, stream, 10, 10);
            // Specify the formula that refers to the source range of cells
            pic.formula = "A1:C10";
            // Update the shapes selected value in the worksheet
            workbook.worksheets.get(0).shapes.updateSelectedValue();

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'referencedpicture.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
