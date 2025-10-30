---
title: Implementar el Sistema de Fechas 1904 con JavaScript a través de C++
description: Aspose.Cells es una biblioteca de JavaScript para trabajar con archivos de hojas de cálculo. Admite la implementación del sistema de fechas 1904, permitiendo a los usuarios calcular y formatear basado en el sistema de fechas del 1 de enero de 1904. Este artículo describe cómo implementar el sistema de fechas 1904 usando la biblioteca Aspose.Cells.
keywords: Aspose.Cells, sistema de fechas 1904, hoja de cálculo, cálculo, formateo, JavaScript a través de C++
type: docs
weight: 7000
url: /es/javascript-cpp/implement-1904-date-system/
---

{{% alert color="primary" %}} 

Microsoft Excel soporta dos sistemas de fechas: sistema de fecha 1900 (el sistema de fechas por defecto implementado en Excel para Windows) y sistema de fecha 1904. El sistema de fechas 1904 se usa normalmente para compatibilidad con archivos de Excel para Macintosh y es el sistema predeterminado si está usando Excel para Macintosh. Puede configurar el sistema de fechas 1904 para archivos de Excel usando Aspose.Cells for JavaScript a través de C++. 

{{% /alert %}} 

Para implementar el sistema de fechas 1904 en Microsoft Excel (por ejemplo, Microsoft Excel 2003):

1. Desde el menú **Herramientas**, selecciona **Opciones**, y elige la pestaña **Cálculo**.
1. Selecciona la opción **Sistema de fecha 1904**.
1. Haz clic en **Aceptar**.

|**Seleccionar el sistema de fecha 1904 en Microsoft Excel**|
| :- |
|![todo:image_alt_text](implement-1904-date-system_1.png)|

Consulta el siguiente código de muestra sobre cómo lograr esto usando las API de Aspose.Cells.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Enable 1904 Date System</h1>
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

            // Instantiating a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Implement 1904 date system
            workbook.settings.date1904 = true;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Mybook.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">1904 date system enabled. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
