---
title: Crear libro de trabajo compartido con Aspose.Cells for JavaScript vía C++
linktitle: Crear libro compartido con Aspose.Cells
type: docs
weight: 40
url: /es/javascript-cpp/create-shared-workbook-with-aspose-cells/
description: Aprende cómo crear un libro de trabajo compartido usando Aspose.Cells for JavaScript vía C++.
---

## **Escenarios de uso posibles**  

Microsoft Excel te permite compartir el libro de trabajo como se muestra en la siguiente captura de pantalla. Cuando compartes el libro, más de un usuario puede editarlo en la red. Aspose.Cells for JavaScript vía C++ te permite crear un libro compartido con la propiedad [**WorkbookSettings.shared**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#shared--).  

![todo:image_alt_text](create-shared-workbook-with-aspose-cells_1.png)  

## **Crear libro compartido con Aspose.Cells**  

El siguiente código de ejemplo crea un libro compartido estableciendo la propiedad [**WorkbookSettings.shared**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#shared--) como **true**. Cuando abras el [archivo de Excel de salida](55541786.xlsx) en Microsoft Excel, verás **Compartido** junto al nombre del libro de salida como se muestra en esta captura de pantalla.  

![todo:image_alt_text](create-shared-workbook-with-aspose-cells_2.png)  

## **Código de muestra**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Create Shared Workbook Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="createShared" disabled>Create Shared Workbook</button>
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
            document.getElementById('createShared').disabled = false;
        });

        document.getElementById('createShared').addEventListener('click', async () => {
            const wb = new Workbook();

            // Share the Workbook (converted getter/setter to property)
            wb.settings.shared = true;

            // Save the Shared Workbook
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSharedWorkbook.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Shared Workbook';

            document.getElementById('result').innerHTML = '<p style="color: green;">Shared workbook created successfully! Click the download link to save the file.</p>';
        });
    </script>
</html>
```
