---
title: Wie man ein Dateiformat erkennt und prüft, ob die Datei verschlüsselt ist, mit JavaScript via C++
linktitle: Wie man ein Dateiformat erkennt und überprüft, ob die Datei verschlüsselt ist
type: docs
weight: 2700
url: /de/javascript-cpp/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/
description: Lernen Sie, wie man ein Dateiformat erkennt und prüft, ob eine Datei mit Aspose.Cells for JavaScript via C++ verschlüsselt ist.
---

{{% alert color="primary" %}}  
Manchmal müssen Sie das Format einer Datei erkennen, bevor Sie sie öffnen, weil die Dateierweiterung nicht garantiert, dass der Inhalt der Datei geeignet ist. Die Datei könnte verschlüsselt sein (passwortgeschützt), sodass sie nicht direkt gelesen werden kann, oder wir sollten sie nicht lesen. Aspose.Cells for JavaScript via C++ bietet die statische Methode [**FileFormatUtil.detectFileFormat(Uint8Array)**](https://reference.aspose.com/cells/javascript-cpp/fileformatutil/#detectFileFormat-uint8array-) und einige relevante APIs, die Sie zum Verarbeiten von Dokumenten verwenden können.  
{{% /alert %}}  

Der folgende Beispielcode veranschaulicht, wie man ein Dateiformat (unter Verwendung des Dateipfads) erkennt und ihre Erweiterung überprüft. Sie können auch feststellen, ob die Datei verschlüsselt ist.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells File Format Detection Example</h1>
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Detect file format
            const info = AsposeCells.FileFormatUtil.detectFileFormat(new Uint8Array(arrayBuffer));

            // Gets the detected load format (converted getter -> property)
            const extension = AsposeCells.FileFormatUtil.loadFormatToExtension(info.loadFormat);
            const encrypted = info.isEncrypted;

            console.log("The spreadsheet format is: " + extension);
            console.log("The file is encrypted: " + encrypted);

            resultDiv.innerHTML = `<p>The spreadsheet format is: <strong>${extension}</strong></p>
                                   <p>The file is encrypted: <strong>${encrypted}</strong></p>`;
        });
    </script>
</html>
```
