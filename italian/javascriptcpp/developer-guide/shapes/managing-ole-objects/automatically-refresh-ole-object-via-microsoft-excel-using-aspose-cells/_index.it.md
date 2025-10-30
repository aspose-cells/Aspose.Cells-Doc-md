---
title: Aggiorna automaticamente l oggetto OLE tramite Microsoft Excel usando Aspose.Cells for JavaScript tramite C++
linktitle: Aggiorna automaticamente l oggetto OLE tramite Microsoft Excel utilizzando Aspose.Cells
type: docs
weight: 270
url: /it/javascript-cpp/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/
description: Impara come aggiornare automaticamente gli oggetti OLE in Excel usando Aspose.Cells for JavaScript tramite C++.
---

{{% alert color="primary" %}}  
Aspose.Cells fornisce la proprietà [**OleObject.autoLoad**](https://reference.aspose.com/cells/javascript-cpp/oleobject/#autoLoad--) per aggiornare l'oggetto OLE quando il file Excel viene aperto in Microsoft Excel. Grazie a questa proprietà, l'oggetto OLE visualizzerà l'immagine OLE corretta generata da Microsoft Excel.  
{{% /alert %}}  

Il seguente codice di esempio carica il [file Excel di esempio](5115231.xlsx) che contiene un'immagine OLE non reale. L'oggetto OLE è effettivamente un documento di Microsoft Word ma il file Excel di esempio mostra l'immagine dell'animale invece dell'immagine di Microsoft Word. Ma se si apre il [file Excel di output](5115225.xlsx), si vedrà che Microsoft Excel mostra l'immagine OLE corretta.  

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
