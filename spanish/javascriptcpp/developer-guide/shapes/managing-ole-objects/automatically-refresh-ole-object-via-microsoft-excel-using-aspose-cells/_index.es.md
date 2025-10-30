---
title: Actualiza automáticamente el objeto OLE en Microsoft Excel usando Aspose.Cells for JavaScript a través de C++
linktitle: Actualizar automáticamente el objeto OLE a través de Microsoft Excel usando Aspose.Cells
type: docs
weight: 270
url: /es/javascript-cpp/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/
description: Aprende cómo actualizar automáticamente los objetos OLE en Excel usando Aspose.Cells for JavaScript a través de C++.
---

{{% alert color="primary" %}}  
Aspose.Cells proporciona la propiedad [**OleObject.autoLoad**](https://reference.aspose.com/cells/javascript-cpp/oleobject/#autoLoad--) para actualizar el objeto OLE cuando se abre el archivo de Excel en Microsoft Excel. Gracias a esta propiedad, el objeto OLE mostrará la imagen OLE correcta generada por Microsoft Excel.  
{{% /alert %}}  

El siguiente código de ejemplo carga el [archivo de Excel de muestra](5115231.xlsx) que tiene una imagen OLE no real. El objeto OLE es en realidad un documento de Microsoft Word pero el archivo de Excel de muestra muestra la imagen de un animal en lugar de la imagen de Microsoft Word. Pero si abre el [archivo de Excel de salida](5115225.xlsx), verá que Microsoft Excel muestra la imagen OLE correcta.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Refresh OLE Objects Example</title>
    </head>
    <body>
        <h1>Refresh OLE Objects Example</h1>
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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const sheet = workbook.worksheets.get(0);

            // Set auto load property of first ole object to true
            sheet.oleObjects.get(0).autoLoad = true;

            // Save the workbook in xlsx format and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'RefreshOLEObjects_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">OLE object autoLoad set to true. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
