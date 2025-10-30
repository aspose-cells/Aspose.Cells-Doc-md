---
title: Creando Subtotales
type: docs
weight: 800
url: /es/javascript-cpp/creating-subtotals/
description: Aprende cómo crear subtotales para valores repetidos en una hoja de cálculo usando la API Aspose.Cells for JavaScript vía C++.
keywords: Aplicar subtotales, Establecer subtotales, Agregar subtotales, Crear subtotales, Cómo agregar subtotales a una hoja de cálculo 
---

{{% alert color="primary" %}}

Puedes crear automáticamente subtotales para valores repetidos en una hoja de cálculo. Aspose.Cells for JavaScript vía C++ ofrece funciones API que te ayudan a agregar subtotales a las hojas de cálculo programáticamente.

{{% /alert %}}

## **Usar Microsoft Excel**

Para agregar subtotales en Microsoft Excel:

1. Cree una lista de datos simple en la primera hoja de cálculo del libro (como se muestra en la figura siguiente) y guarde el archivo como Libro1.xls.
1. Seleccione cualquier celda dentro de su lista.
1. Desde el menú **Datos**, seleccione **Subtotales**. Se mostrará el cuadro de diálogo Subtotales. Defina qué función usar y dónde colocar los subtotales.

## **Usando la API Aspose.Cells for JavaScript vía C++**

Aspose.Cells for JavaScript vía C++ proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) contiene una colección [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) que permite acceder a cada hoja de cálculo en el archivo de Excel.

Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). La clase proporciona un amplio rango de propiedades y métodos para gestionar hojas y otros objetos. Cada hoja de cálculo consiste en una colección [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells). Para agregar subtotales a una hoja, usa el método [**subtotal**](https://reference.aspose.com/cells/javascript-cpp/cells/#subtotal-cellarea-number-consolidationfunction-numberarray-) de la clase [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells). Proporciona valores de parámetros para indicar cómo se debe calcular y colocar el subtotal.

En los ejemplos a continuación, hemos agregado subtotales a la primera hoja del [archivo plantilla](book1.xlsx) usando la API Aspose.Cells for JavaScript vía C++. Cuando se ejecuta el código, se crea una hoja con subtotales.

Los fragmentos de código que siguen muestran cómo agregar subtotales a una hoja de cálculo con Aspose.Cells for JavaScript vía C++.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Apply Subtotal Example</h1>
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

            // Instantiate a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the Cells collection in the first worksheet
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;

            // Create a cellarea i.e., B3:C19
            const ca = new AsposeCells.CellArea();
            ca.startRow = 2;
            ca.startColumn = 1;
            ca.endRow = 18;
            ca.endColumn = 2;

            // Apply subtotal, the consolidation function is Sum and it will be applied to
            // Second column (C) in the list
            cells.subtotal(ca, 0, AsposeCells.ConsolidationFunction.Sum, [1]);

            // Save the excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Subtotal applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
