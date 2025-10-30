---
title: Verificar formato de número personalizado al establecer la propiedad Style.Custom
linktitle: Verificar formato de número personalizado al establecer la propiedad Style.Custom
description: Aspose.Cells es una biblioteca de JavaScript para trabajar con archivos de hojas de cálculo, que soporta verificar formatos personalizados de números al aplicar estilos. Este artículo te mostrará cómo usar la biblioteca Aspose.Cells para verificar formatos personalizados de números y asegurar que el estilo sea correcto.
keywords: Aspose.Cells, bibliotecas de JavaScript, hojas de cálculo, estilos, formatos personalizados de números, verificación, validación
type: docs
weight: 170
url: /es/javascript-cpp/check-custom-number-format-when-setting-style-custom-property/
---

## **Escenarios de uso posibles**

Si asignas un formato personalizado de número inválido a la propiedad [**Style.custom**](https://reference.aspose.com/cells/javascript-cpp/style/#custom-string-), entonces Aspose.Cells for JavaEl Script vía C++ no lanzará ninguna excepción. Pero si quieres que Aspose.Cells verifique si el formato personalizado asignado es válido o no, por favor configura la propiedad [**Workbook.settings.checkCustomNumberFormat**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#checkCustomNumberFormat-boolean-) en **true**.

## **Verificar formato personalizado de número al establecer la propiedad Style.custom**

El siguiente código de ejemplo asigna un formato personalizado de número inválido a la propiedad [**Style.custom**](https://reference.aspose.com/cells/javascript-cpp/style/#custom-string-). Dado que ya configuramos la propiedad [**Workbook.settings.checkCustomNumberFormat**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#checkCustomNumberFormat-boolean-) en **true**, lanzará una excepción, por ejemplo, Formato de número inválido. Lee los comentarios en el código para más ayuda.

## **Código de muestra**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Check Custom Number Format</h1>
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
            let workbook;

            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                // Create a new empty workbook if no file is provided
                workbook = new Workbook();
            }

            // Setting this property to true will make Aspose.Cells throw an exception
            // when invalid custom number format is assigned to Style.custom property
            workbook.settings.checkCustomNumberFormat = true;

            // Access first worksheet
            const sheet = workbook.worksheets.get(0);

            // Access cell A1 and put some number to it
            const cell = sheet.cells.get("A1");
            cell.value = 2347;

            // Access cell's style and set its Style.custom property
            const style = cell.style;

            // This line will throw exception if workbook.settings.checkCustomNumberFormat is set to true
            style.custom = "ggg @ fff"; // Invalid custom number format

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed. Click the download link to get the file.</p>';
        });
    </script>
</html>
```
