---
title: Insertar imagen de fondo en Excel con JavaScript mediante C++
linktitle: Insertar imagen de fondo en Excel
type: docs
weight: 90
url: /es/javascript-cpp/insert-background-image-to-excel/
description: "Cómo insertar imagen de fondo en Excel usando Aspose.Cells for JavaScript mediante C++."
---

{{% alert color="primary" %}} 

Puede hacer que una hoja de cálculo sea más atractiva agregando una imagen como fondo de la hoja. Esta función puede ser muy efectiva si tiene un gráfico corporativo especial que agrega un toque del fondo sin ocultar los datos en la hoja. Puede establecer una imagen de fondo para una hoja utilizando la API de Aspose.Cells.

{{% /alert %}} 

## **Establecer fondo de hoja en Microsoft Excel**

Para establecer una imagen de fondo de hoja en Microsoft Excel (por ejemplo, Microsoft Excel 2019):

1. Desde el menú **Diseño de página**, encontrar la opción **Configurar página**, y luego hacer clic en la opción **Fondo**.
1. Seleccionar una imagen para establecer la imagen de fondo de la hoja.

   **Establecer un fondo de hoja**

![todo:image_alt_text](insert-background-to-excel.jpg)

## **Configurar fondo de hoja con Aspose.Cells for JavaScript mediante C++**

El código a continuación establece una imagen de fondo utilizando una imagen de un flujo.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Set Worksheet Background Image</title>
    </head>
    <body>
        <h1>Set Worksheet Background Image Example</h1>
        <p>
            Select a background image to apply to a new workbook's first worksheet,
            then click "Apply Background & Save" to generate XLSX and HTML files.
        </p>
        <input type="file" id="bgInput" accept="image/*" />
        <button id="runExample">Apply Background & Save</button>
        <a id="downloadXlsx" style="display: none; margin-left: 10px;"></a>
        <a id="downloadHtml" style="display: none; margin-left: 10px;"></a>
        <div id="result" style="margin-top: 1em;"></div>
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
            const bgInput = document.getElementById('bgInput');
            const resultDiv = document.getElementById('result');

            if (!bgInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select a background image file.</p>';
                return;
            }

            const bgFile = bgInput.files[0];
            const arrayBuffer = await bgFile.arrayBuffer();
            const imgBytes = new Uint8Array(arrayBuffer);

            // Create a new Workbook.
            const workbook = new Workbook();

            // Get the first worksheet.
            const sheet = workbook.worksheets.get(0);

            // Set the background image for the worksheet.
            sheet.backgroundImage = imgBytes;

            // Save the Excel file (XLSX)
            const xlsxData = workbook.save(SaveFormat.Xlsx);
            const blobXlsx = new Blob([xlsxData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
            const downloadXlsx = document.getElementById('downloadXlsx');
            downloadXlsx.href = URL.createObjectURL(blobXlsx);
            downloadXlsx.download = 'outputBackImageSheet.xlsx';
            downloadXlsx.style.display = 'inline';
            downloadXlsx.textContent = 'Download Excel File';

            // Save the HTML file
            const htmlData = workbook.save(SaveFormat.Html);
            const blobHtml = new Blob([htmlData], { type: 'text/html' });
            const downloadHtml = document.getElementById('downloadHtml');
            downloadHtml.href = URL.createObjectURL(blobHtml);
            downloadHtml.download = 'outputBackImageSheet.html';
            downloadHtml.style.display = 'inline';
            downloadHtml.textContent = 'Download HTML File';

            resultDiv.innerHTML = '<p style="color: green;">Background image applied. Download links are ready.</p>';
        });
    </script>
</html>
```

## Artículos relacionados

- [Trabajar con fondo en archivos ODS](/cells/es/javascript-cpp/working-with-background-in-ods-files/)
