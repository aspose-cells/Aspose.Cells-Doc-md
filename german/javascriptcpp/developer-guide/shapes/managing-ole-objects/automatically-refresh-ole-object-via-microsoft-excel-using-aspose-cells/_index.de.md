---
title: OLE Objekt automatisch mit Microsoft Excel mit Aspose.Cells for JavaScript über C++ aktualisieren
linktitle: OLE Objekt automatisch über Microsoft Excel mit Aspose.Cells aktualisieren
type: docs
weight: 270
url: /de/javascript-cpp/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/
description: Erfahren Sie, wie Sie OLE Objekte in Excel mithilfe von Aspose.Cells for JavaScript via C++ automatisch aktualisieren.
---

{{% alert color="primary" %}}  
Aspose.Cells bietet die Eigenschaft [**OleObject.autoLoad**](https://reference.aspose.com/cells/javascript-cpp/oleobject/#autoLoad--), um das OLE-Objekt zu aktualisieren, wenn die Excel-Datei in Microsoft Excel geöffnet wird. Aufgrund dieser Eigenschaft wird das OLE-Objekt das korrekte OLE-Bild anzeigen, das von Microsoft Excel generiert wurde.  
{{% /alert %}}  

Der folgende Beispielcode lädt die [Beispieldatei Excel](5115231.xlsx), die ein nicht-reales OLE-Bild enthält. Das OLE-Objekt ist tatsächlich ein Microsoft-Word-Dokument, aber die Beispieldatei Excel zeigt stattdessen das Tierbild an. Wenn Sie jedoch die [Ausgabedatei Excel](5115225.xlsx) öffnen, sehen Sie, dass Microsoft Excel das korrekte OLE-Bild anzeigt.  

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
