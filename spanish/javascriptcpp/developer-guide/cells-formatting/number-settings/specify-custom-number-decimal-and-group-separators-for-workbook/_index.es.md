---
title: Especificar Separadores de Números Decimales y de Grupo Personalizados para Libro de Trabajo
linktitle: Especificar Separadores de Números Decimales y de Grupo Personalizados para Libro de Trabajo
type: docs
weight: 110
url: /es/javascript-cpp/specify-custom-number-decimal-and-group-separators-for-workbook/
description: Cambiar separadores decimales y de agrupación en números en Excel usando Aspose.Cells for JavaScript vía C++.
keywords: especificar separador decimal personalizado en Excel JavaScript vía C++, especificar separador de grupo personalizado en Excel JavaScript vía C++, cambiar separador decimal y de grupo en Excel JavaScript vía C++
---

{{% alert color="primary" %}}

En Microsoft Excel, puedes especificar los Separadores de Decimales y Miles Personalizados en lugar de usar Separadores de Sistema de las **Opciones Avanzadas de Excel** como se muestra en la captura de pantalla a continuación.

Aspose.Cells proporciona los métodos [**WorkbookSettings.numberDecimalSeparator**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#numberDecimalSeparator-string-) y [**WorkbookSettings.numberGroupSeparator**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#numberGroupSeparator-string-) para establecer los separadores personalizados para formatear/parsing de números.

{{% /alert %}}

## **Especificar Separadores Personalizados usando Microsoft Excel**

La siguiente captura de pantalla muestra las **Opciones Avanzadas de Excel** y destaca la sección para especificar los **Separadores Personalizados**.

![todo:image_alt_text](specify-custom-number-decimal-and-group-separators-for-workbook_1.png)

## **Especificación de separadores personalizados usando Aspose.Cells for JavaScript vía C++**

El siguiente código de ejemplo ilustra cómo especificar los separadores personalizados utilizando la API de Aspose.Cells. Especifica los Separadores de Decimal y Grupo Personalizados como punto y espacio, respectivamente.

### Código JavaScript para especificar separadores personalizados de Número Decimal y de Grupo

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Custom Number Separator Example</h1>
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

            // Load workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Specify custom separators
            workbook.settings.numberDecimalSeparator = '.';
            workbook.settings.numberGroupSeparator = ' ';

            const worksheet = workbook.worksheets.get(0);

            // Set cell value
            const cell = worksheet.cells.get("A1");
            cell.value = 123456.789;

            // Set custom cell style
            const style = cell.style;
            style.custom = "#,##0.000;[Red]#,##0.000";
            cell.style = style;

            worksheet.autoFitColumns();

            // Save workbook as pdf
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'CustomSeparator_out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the PDF.</p>';
        });
    </script>
</html>
```
