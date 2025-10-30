---
title: Aplicar subtotal y cambiar dirección de resumen de contorno de filas debajo del detalle
type: docs
weight: 100
url: /es/javascript-cpp/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/
description: Aprende cómo aplicar subtotal y cambiar la dirección de las filas de resumen del esquema debajo de los Detalles usando el script Aspose.Cells for Java a través de la API C++.
keywords: Aplicar subtotal, agregar subtotal, cambiar dirección del resumen de contorno de filas debajo del detalle, cambiar dirección del resumen de contorno de columnas a la derecha del detalle, crear subtotal y cambiar dirección de resumen de contorno de filas debajo del detalle
---

{{% alert color="primary" %}}

Este artículo explicará cómo aplicar un subtotal a los datos y cambiar la dirección de las filas de resumen de contorno debajo del detalle.

Puede aplicar un subtotal a los datos usando el método [**Worksheet.cells.subtotal()**](https://reference.aspose.com/cells/javascript-cpp/cells/#subtotal-cellarea-number-consolidationfunction-numberarray-boolean-boolean-boolean-). Toma los siguientes parámetros.

- **ÁreaCelda** - El rango en el que aplicar el subtotal
- **AgruparPor** - El campo por el que agrupar, como un desplazamiento entero basado en cero
- **Función** - La función de subtotal
- **ListaTotal** - Una matriz de desplazamientos de campo basados en cero, que indica los campos a los que se añaden los subtotales.
- **Reemplazar** - Indica si reemplazar los subtotales actuales
- **SaltosDePágina** - Indica si agregar salto de página entre grupos
- **ResumenDebajoDeDatos** - Indica si agregar resumen debajo de los datos.

Además, puede controlar la dirección de las **filas de resumen de contorno debajo del detalle** como se muestra en la siguiente captura de pantalla utilizando la propiedad Worksheet.Outline.SummaryRowBelow. Puede abrir esta configuración en Microsoft Excel usando **Datos > Contorno > Configuración**

![todo:image_alt_text](1.png)

{{% /alert %}}

## Imágenes de los archivos de origen y salida

La siguiente captura de pantalla muestra el archivo de Excel de origen utilizado en el código de ejemplo a continuación, que contiene algunos datos en las columnas A y B.

![todo:image_alt_text](2.png)

La siguiente captura de pantalla muestra el archivo de Excel de salida generado por el código de ejemplo. Como se puede ver, se ha aplicado un subtotal al rango A2:B11 y la dirección del contorno es resumen de filas debajo del detalle.

![todo:image_alt_text](3.png)

## JavaScript para aplicar subtotal y cambiar la dirección de las filas de resumen del esquema



```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Subtotal Example</title>
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
        const { Workbook, SaveFormat, CellArea, ConsolidationFunction, Utils } = AsposeCells;

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

            // Create workbook from uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Get the Cells collection in the first worksheet
            const cells = worksheet.cells;

            // Create a cellarea i.e., A2:B11
            const ca = CellArea.createCellArea("A2", "B11");

            // Apply subtotal, the consolidation function is Sum and it will applied to Second column (B) in the list
            cells.subtotal(ca, 0, ConsolidationFunction.Sum, [1], true, false, true);

            // Set the direction of outline summary
            worksheet.outline.summaryRowBelow = true;

            // Save the excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Subtotal applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
