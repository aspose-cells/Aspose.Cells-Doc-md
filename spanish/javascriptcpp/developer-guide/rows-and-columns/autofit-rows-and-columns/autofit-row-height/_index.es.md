---
title: Ajuste automático de la altura de fila al cargar un archivo con JavaScript a través de C++
linktitle: Ajustar automáticamente la altura de la fila cuando se carga el archivo
type: docs
weight: 120
url: /es/javascript-cpp/autofit-row-height/
description: Aprende cómo ajustar filas cuya altura no está personalizada al cargar un archivo usando Aspose.Cells for JavaScript a través de C++.
keywords: Ajuste automático de la altura de fila al cargar un archivo con JavaScript a través de C++, ajuste automático de la altura de fila al abrir un archivo de Excel con JavaScript a través de C++ 
---

## **Escenarios de uso posibles**
La altura de la fila se ajusta automáticamente para coincidir con la fuente del contenido, pero cuando la altura de la fila almacenada en caché no coincide con la altura del contenido en el archivo, MS Excel ajustará automáticamente la altura de la fila al cargar el archivo, mientras que Aspose.Cells for JavaScript a través de C++ no lo ajustará automáticamente para mejorar el rendimiento. Si necesitas usar el programa Aspose.Cells para ajustar automáticamente las alturas de línea al cargar archivos, puedes lograrlo a través del parámetro [autoFitterOptions(AutoFitterOptions)](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#autoFitterOptions-autofitteroptions-) en tu código.

Por favor, consulte la siguiente imagen. Observamos que la altura de fila almacenada en caché en la línea 11 es 15, pero Excel ajustó automáticamente la altura de la fila al cargar el archivo.
<br>
<img src="1.png" width=70% />

## **Ajustar la altura de fila usando Aspose.Cells for JavaScript a través de C++**
Si carga el archivo directamente y lo guarda en PDF, los datos no se mostrarán completamente en el PDF porque su altura en caché es solo 15.
<br>
<img src="2.png" width=70% />
<br>
Si estableces el parámetro [autoFitterOptions(AutoFitterOptions)](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#autoFitterOptions-autofitteroptions-) en true al cargar el archivo, entonces Aspose.Cells ajustará automáticamente la altura de fila. La altura ajustada puede satisfacer eficazmente los requisitos de visualización del texto.
<br>
<img src="3.png" width=70% />

## **Código de ejemplo en JavaScript**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells LoadOptions & AutoFitter Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <div>
            <a id="downloadLink1" style="display: none;">Download out.pdf</a>
        </div>
        <div>
            <a id="downloadLink2" style="display: none;">Download out2.pdf</a>
        </div>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions, AutoFitterOptions } = AsposeCells;

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
            const resultDiv = document.getElementById('result');
            const downloadLink1 = document.getElementById('downloadLink1');
            const downloadLink2 = document.getElementById('downloadLink2');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            const data = new Uint8Array(arrayBuffer);

            // Load workbook and save as out.pdf
            const workbook = new Workbook(data);
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            downloadLink1.href = URL.createObjectURL(blob);
            downloadLink1.download = 'out.pdf';
            downloadLink1.style.display = 'inline';
            downloadLink1.textContent = 'Download out.pdf';

            // Prepare LoadOptions with AutoFitterOptions and onlyAuto = true
            const loadOptions = new LoadOptions();
            loadOptions.autoFitterOptions = new AutoFitterOptions();
            loadOptions.autoFitterOptions.onlyAuto = true;

            // Load workbook with loadOptions and save as out2.pdf
            const book = new Workbook(data, loadOptions);
            const outputData2 = book.save(SaveFormat.Pdf);
            const blob2 = new Blob([outputData2], { type: 'application/pdf' });
            downloadLink2.href = URL.createObjectURL(blob2);
            downloadLink2.download = 'out2.pdf';
            downloadLink2.style.display = 'inline';
            downloadLink2.textContent = 'Download out2.pdf';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download links to get the generated PDF files.</p>';
        });
    </script>
</html>
```
