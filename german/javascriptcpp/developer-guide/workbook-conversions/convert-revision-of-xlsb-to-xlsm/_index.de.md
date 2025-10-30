---
title: Revision von XLSB in XLSM mit JavaScript über C++ konvertieren
linktitle: Revision von XLSB zu XLSM konvertieren
type: docs
weight: 290
url: /de/javascript-cpp/convert-revision-of-xlsb-to-xlsm/
description: Lernen Sie, wie Sie Revisionen von XLSB Dateien vollständig in das XLSM Format mit Aspose.Cells for JavaScript über C++ umwandeln.
---

{{% alert color="primary" %}}

Aspose.Cells unterstützt jetzt die vollständige Konvertierung von Revisionen von XLSB-Dateien in XLSM-Dateien. Revisionen befinden sich im Pfad \xl\revisions. Sie können sie anzeigen, indem Sie die Erweiterung Ihrer XLSB-Datei in ZIP ändern. Der Pfad \xl\revisions enthält Dateien, die mit .bin enden.

Wenn Sie Ihre XLSB-Datei mit Aspose.Cells in eine XLSM-Datei umwandeln, werden diese .bin-Dateien erfolgreich in .xml-Dateien umgewandelt, wie in diesen beiden Screenshots gezeigt.

{{% /alert %}}

Der folgende Beispielcode zeigt, wie Sie die XLSB-Datei mit Aspose.Cells for JavaScript über C++ in das XLSM-Format konvertieren.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert XLSB to XLSM Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsb,.csv" />
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file (.xlsb, .xls, .xlsx).</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Open workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save Workbook to XLSM format
            const outputData = workbook.save(SaveFormat.Xlsm);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsm';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Converted XLSM File';

            resultDiv.innerHTML = '<p style="color: green;">Workbook converted to XLSM successfully. Click the download link to save the file.</p>';
        });
    </script>
</html>
```
