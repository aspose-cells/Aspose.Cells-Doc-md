---
title: Establecer color de pestaña de hoja de cálculo con JavaScript a través de C++
linktitle: Establecer el color de la pestaña de la hoja de cálculo
type: docs
weight: 120
url: /es/javascript-cpp/set-worksheet-tab-color/
description: Este artículo muestra un ejemplo de código que establece el color de la pestaña de la hoja de cálculo de Excel programáticamente utilizando JavaScript a través de C++.
keywords: establecer color de pestaña de Excel JavaScript a través de C++, código para establecer color de pestaña de Excel JavaScript a través de C++
---

{{% alert color="primary" %}}

Aspose.Cells te permite cambiar el color de las pestañas individuales de las hojas de cálculo para hacerlas más destacadas. Por ejemplo, puedes hacer que Gastos sean rojos, Ventas verdes, Activos azules, etc.

{{% /alert %}}
## **Establecer el color de la pestaña de la hoja de cálculo con Microsoft Excel**
1. Haz clic derecho en una pestaña en la hoja de pestañas en la parte inferior de la hoja de cálculo actual.
1. Seleccione **Color de pestaña**.
1. Selecciona un color de la paleta.
1. Haz clic en **Aceptar**.
## **Configurar el color de la pestaña de la hoja de cálculo con Aspose.Cells**
El código de ejemplo a continuación muestra cómo configurar el color de la pestaña con Aspose.Cells.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Set Worksheet Tab Color Example</title>
    </head>
    <body>
        <h1>Set Worksheet Tab Color Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
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
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            const worksheet = workbook.worksheets.get(0);
            worksheet.tabColor = AsposeCells.Color.Red;
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'worksheettabcolor.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';
            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet tab color set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
