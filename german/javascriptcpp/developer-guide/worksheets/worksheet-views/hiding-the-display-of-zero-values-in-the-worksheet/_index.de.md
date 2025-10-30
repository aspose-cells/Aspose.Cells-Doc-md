---
title: Verbergen der Anzeige von Nullwerten im Arbeitsblatt mit JavaScript über C++
linktitle: Ausblenden der Anzeige von Nullwerten im Arbeitsblatt
type: docs
weight: 50
url: /de/javascript-cpp/hiding-the-display-of-zero-values-in-the-worksheet/
description: Dieser Artikel zeigt Beispielcode, der erklärt, wie man Nullwerte in einer Excel Tabelle programmgesteuert mithilfe der JavaScript Bibliothek über C++ ausblendet.
keywords: Nullwerte im Excel Arbeitsblatt in JavaScript über C++ ausblenden
---

{{% alert color="primary" %}} 

Manchmal müssen Sie Nullwerte in einer Tabelle ausblenden. Es könnte eine persönliche Vorliebe oder ein Formatierungsstandard sein.

{{% /alert %}} 

Um Nullwerte in einem Arbeitsblatt in Microsoft Excel zu verstecken (z. B. Microsoft Excel 2003):

1. Wählen Sie im Menü **Extras** die Option **Optionen** und dann den Tab **Ansicht** aus.
1. Deaktivieren Sie die Option **Nullwerte**.
1. Klicken Sie auf **OK**.

Siehe den folgenden Beispielcode, der das Verbergen von Nullen mit Aspose.Cells for JavaScript über C++ demonstriert.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Hide Zero Values Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get First worksheet of the workbook
            const sheet = workbook.worksheets.get(0);

            // Hide the zero values in the sheet
            sheet.displayZeros = false;

            // Save the workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputfile.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
