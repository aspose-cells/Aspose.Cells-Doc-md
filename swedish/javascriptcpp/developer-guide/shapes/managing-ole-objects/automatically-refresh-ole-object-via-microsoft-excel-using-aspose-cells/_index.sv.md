---
title: Automatiskt uppdatera OLE objekt via Microsoft Excel med Aspose.Cells for JavaScript via C++
linktitle: Automatisk uppdatering av OLE objekt via Microsoft Excel med Aspose.Cells
type: docs
weight: 270
url: /sv/javascript-cpp/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/
description: Lära dig hur man automatiskt uppdaterar OLE objekt i Excel med Aspose.Cells for JavaScript via C++.
---

{{% alert color="primary" %}}  
Aspose.Cells tillhandahåller [**OleObject.autoLoad**](https://reference.aspose.com/cells/javascript-cpp/oleobject/#autoLoad--)-egenskapen för att uppdatera OLE-objektet när Excel-filen öppnas i Microsoft Excel. På grund av denna egenskap kommer OLE-objektet att visa korrekt OLE-bild som genererats av Microsoft Excel.  
{{% /alert %}}  

Följande provkod laddar [provexempel Excel-filen](5115231.xlsx) som har en icke verklig OLE-bild. OLE-objektet är faktiskt ett Microsoft Word-dokument men provexempelfilen visar djurbilden istället för Microsoft Word-bilden. Men om du öppnar [utmatningsexelfilen](5115225.xlsx) kommer du att se att Microsoft Excel visar den korrekta OLE-bilden.  

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
