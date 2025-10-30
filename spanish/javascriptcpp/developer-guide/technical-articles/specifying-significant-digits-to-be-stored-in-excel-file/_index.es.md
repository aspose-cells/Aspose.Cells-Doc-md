---
title: Especificando Dígitos Significativos para ser Almacenados en Archivo Excel con JavaScript a través de C++
linktitle: Especificación de Dígitos Significativos a ser Almacenados en un Archivo de Excel
type: docs
weight: 30
url: /es/javascript-cpp/specifying-significant-digits-to-be-stored-in-excel-file/
description: Aprende cómo especificar dígitos significativos para ser almacenados en un archivo Excel usando Script Aspose.Cells for Java a través de C++.
---

## **Escenarios de uso posibles**  

Por defecto, Script Aspose.Cells for Java a través de C++ almacena 17 dígitos significativos de valores doble dentro del archivo Excel, a diferencia de MS-Excel que almacena solo 15 dígitos significativos. Puedes cambiar el comportamiento predeterminado de Aspose.Cells de 17 a 15 dígitos significativos usando la propiedad [**CellsHelper.significantDigits**](https://reference.aspose.com/cells/javascript-cpp/cellshelper/#significantDigits--).  

## **Especificación de Dígitos Significativos a ser almacenados en un archivo de Excel**  

El siguiente código de ejemplo fuerza a Aspose.Cells a usar 15 dígitos significativos al almacenar valores doble dentro del archivo de Excel. Por favor, revisa el [archivo Excel de salida](22774105.xlsx). Cambia su extensión a .zip y descomprímelo, verás que solo se almacenan 15 dígitos significativos en el archivo de Excel. La siguiente captura de pantalla explica el efecto de la propiedad [**CellsHelper.significantDigits**](https://reference.aspose.com/cells/javascript-cpp/cellshelper/#significantDigits--) en el archivo Excel de salida.  

![todo:image_alt_text](specifying-significant-digits-to-be-stored-in-excel-file_1.png)  

## **Código de muestra**  

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>Aspose.Cells Example - Significant Digits</title>
    </head>
    <body>
        <h1>Significant Digits Example</h1>
        <p>This example sets CellsHelper.significantDigits to 15 and writes a double to cell A1.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellsHelper } = AsposeCells;

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

            // If a file is provided, open it; otherwise create a new workbook (matches original Node behavior)
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // By default, Aspose.Cells stores 17 significant digits unlike MS-Excel which stores only 15 significant digits
            CellsHelper.significantDigits = 15;

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access cell A1
            const c = worksheet.cells.get("A1");

            // Put double value, only 15 significant digits as specified by CellsHelper.significantDigits above will be stored
            c.value = 1234567890.123451711;

            // Saving the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out_SignificantDigits.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created/modified successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
