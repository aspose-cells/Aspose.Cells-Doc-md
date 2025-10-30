---
title: Cargar una imagen web desde una URL en una hoja de cálculo de Excel con JavaScript a través de C++
linktitle: Cargar una Imagen Web desde una URL en una Hoja de Excel
type: docs
weight: 30
url: /es/javascript-cpp/load-a-web-image-from-a-url-into-an-excel-worksheet/
description: Cómo convertir una imagen desde URL en una imagen de Excel real usando Aspose.Cells for JavaScript a través de C++.
keywords: Excel muestra imágenes desde URL, Excel URL a imagen, mostrar imagen en Excel desde URL, Excel insertar imagen desde URL, convertir URL a imagen en Excel, imagen desde URL en Excel, cargar imagen desde URL en Excel, JavaScript, Excel
---

## Cargar una imagen desde una URL en una hoja de Excel

Aspose.Cells for JavaScript a través de C++ proporciona una manera sencilla y fácil de cargar imágenes desde URLs en hojas de cálculo de Excel. Este artículo explica cómo descargar los datos de la imagen en un flujo y luego insertarlos en la hoja usando la API Aspose.Cells. Usando este método, las imágenes se convierten en parte del archivo de Excel y no se descargan cada vez que se abre la hoja de cálculo.

## Código de Muestra

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Insert Web Image</title>
    </head>
    <body>
        <h1>Insert Web Image into Excel</h1>
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
            if (!fileInput.files.length) {
                // If no file provided, create a new workbook
                document.getElementById('result').innerHTML = '<p style="color: orange;">No input workbook selected. A new workbook will be created.</p>';
            }

            // Create or load workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Ensure at least one worksheet exists
            if (workbook.worksheets.count === 0) {
                workbook.worksheets.add("Sheet1");
            }
            const worksheet = workbook.worksheets.get(0);

            // Download the image from the web
            const url = "https://www.aspose.com/Images/aspose-logo.jpg";
            const response = await fetch(url);
            if (!response.ok) {
                document.getElementById('result').innerHTML = `<p style="color: red;">Failed to download image: ${response.status} ${response.statusText}</p>`;
                return;
            }
            const imgArrayBuffer = await response.arrayBuffer();
            const imgBytes = new Uint8Array(imgArrayBuffer);

            // Insert the image into the worksheet at row 0, column 0
            worksheet.pictures.add(0, 0, imgBytes);

            // Save the modified workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'webimagebook.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Image inserted successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}
Podría haber casos donde siempre quieras la imagen actualizada desde una URL. Para lograr esto, puedes seguir las instrucciones dadas en el artículo [Insertar una imagen enlazada desde una dirección web](/cells/es/javascript-cpp/insert-a-linked-picture-from-web-address/). Siguiendo este método, la imagen se carga desde la URL cada vez que se abre la hoja de cálculo.
{{% /alert %}}
