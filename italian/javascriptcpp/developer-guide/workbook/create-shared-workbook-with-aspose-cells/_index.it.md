---
title: Crea un libro di lavoro condiviso con Aspose.Cells for JavaScript tramite C++
linktitle: Creare un libro di lavoro condiviso con Aspose.Cells
type: docs
weight: 40
url: /it/javascript-cpp/create-shared-workbook-with-aspose-cells/
description: Scopri come creare un libro di lavoro condiviso usando Aspose.Cells for JavaScript tramite C++.
---

## **Possibili Scenari di Utilizzo**  

Microsoft Excel ti consente di condividere il libro di lavoro come mostrato nella schermata seguente. Quando condividi il libro, più utenti possono modificarlo in rete. Aspose.Cells for JavaScript tramite C++ ti permette di creare un libro di lavoro condiviso con la proprietà [**WorkbookSettings.shared**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#shared--).  

![todo:image_alt_text](create-shared-workbook-with-aspose-cells_1.png)  

## **Creare un libro di lavoro condiviso con Aspose.Cells**  

Il seguente esempio di codice crea un workbook condiviso impostando la proprietà [**WorkbookSettings.shared**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#shared--) come **true**. Quando apri il [file Excel di output](55541786.xlsx) in Microsoft Excel, vedrai la dicitura **Shared** insieme al nome del workbook come mostrato in questa schermata.  

![todo:image_alt_text](create-shared-workbook-with-aspose-cells_2.png)  

## **Codice di Esempio**  

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
