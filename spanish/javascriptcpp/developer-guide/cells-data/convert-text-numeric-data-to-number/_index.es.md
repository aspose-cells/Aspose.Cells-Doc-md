---
title: Convertir Datos Numéricos de Texto a Número
type: docs
weight: 900
url: /es/javascript-cpp/convert-text-numeric-data-to-number/
description: Aprende cómo convertir números almacenados como texto en Excel a números usando la API Aspose.Cells for JavaScript vía C++.
keywords: convertir texto a número en Excel, código JavaScript para convertir texto a número en Excel, convertir datos numéricos en texto a número en Excel, convertir datos numéricos en texto a número en código JavaScript, convertir texto numérico a número en Excel, código JavaScript para convertir texto numérico a número en Excel, convertir texto numérico a número con JavaScript en Excel, convertir texto numérico a número en Excel con código JavaScript, convertir cadena numérica a número en Excel con código JavaScript, convertir datos numéricos en texto a número en Excel JavaScript, convertir cadena numérica a número en JavaScript en Excel
---

## **Escenarios de uso posibles**
A veces, quieres convertir datos numéricos ingresados como texto en números. Puedes ingresar números como texto en Microsoft Excel poniendo un apóstrofe antes del número, por ejemplo **'12345**. Excel entonces trata el número como una cadena de texto. Aspose.Cells for JavaScript vía C++ te permite convertir cadenas a números.


## Cómo convertir números almacenados como texto a números en Excel
Puede convertir números almacenados como texto a números siguiendo unos pocos pasos simples.
1. Seleccione cualquier celda individual o rango de celdas que tenga un indicador de error en la esquina superior izquierda.
1. Junto a la celda o rango de celdas seleccionado, haga clic en el botón de error que aparece. En el menú, haga clic en Convertir a Número. 
<br>
<img src="4.png" width=70% />
1. Si el botón de alerta no está disponible, seleccione una columna con este problema. Si no desea convertir toda la columna, puede seleccionar una o más celdas en su lugar. Asegúrese de que las celdas que seleccione estén en la misma columna, de lo contrario este proceso no funcionará. El botón Texto en Columnas se usa típicamente para dividir una columna, pero también se puede usar para convertir una sola columna de texto a números. En la pestaña Datos, haga clic en Texto en Columnas.
<br>
<img src="1.png" width=70% />
1. Haga clic en el botón Finalizar en el cuadro emergente.
<br>
<img src="2.png" width=70% />
1. Los números almacenados como texto se transforman en números.
<br>
<img src="3.png" width=70% />

## Cómo convertir números almacenados como texto en números usando Aspose.Cells for JavaScript vía C++
Aspose.Cells for JavaScript vía C++ proporciona el método [**Cells.convertStringToNumericValue()**](https://reference.aspose.com/cells/javascript-cpp/cells/#convertStringToNumericValue--) que puede usarse para convertir todos los datos numéricos en cadenas o texto en números.

La siguiente captura de pantalla muestra números de cadena en las celdas **A1:A17**. Los números de cadena están alineados a la izquierda.
<br>
<img src="5.png" width=70% />

Estos números de cadena se han convertido en números utilizando [**Cells.convertStringToNumericValue()**](https://reference.aspose.com/cells/javascript-cpp/cells/#convertStringToNumericValue--) en la siguiente captura de pantalla. Como se puede ver, ahora están alineados a la derecha.
<br>
<img src="6.png" width=70% />

## Código JavaScript para convertir datos numéricos en cadena a números reales

El siguiente código de muestra ilustra cómo convertir todos los datos numéricos de cadena en números reales en todas las hojas de cálculo.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Strings to Numeric Values in All Sheets</h1>
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

            // Instantiate workbook object with the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access worksheets collection
            const sheets = workbook.worksheets;
            const sheetcount = sheets.count;

            // Iterate through all worksheets and convert strings to numeric values
            for (let i = 0; i < sheetcount; i++) {
                const sheet = sheets.get(i);
                sheet.cells.convertStringToNumericValue();
            }

            // Save the modified workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
