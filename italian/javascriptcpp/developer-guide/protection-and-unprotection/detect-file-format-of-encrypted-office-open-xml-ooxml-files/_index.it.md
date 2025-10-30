---
title: Rileva il formato del file di Office Open XML crittografato  File OOXML con JavaScript via C++
linktitle: Rileva il Formato File dei File Office Open XML Crittografati  File OOXML
type: docs
weight: 340
url: /it/javascript-cpp/detect-file-format-of-encrypted-office-open-xml-ooxml-files/
description: Impara come rilevare il formato del file di file OOXML crittografati usando Aspose.Cells for JavaScript via C++.
---

{{% alert color="primary" %}}  

**Office Open XML** (noto anche come **OOXML** o **Microsoft Open XML** (MOX)) è un formato di file basato su XML sviluppato da Microsoft per rappresentare documenti di ufficio come fogli di calcolo, grafici, presentazioni e documenti di word processing.  

{{% /alert %}}  

Aspose.Cells fornisce un modo per rilevare il formato del file di file Microsoft Open XML crittografati. Per identificare il tipo di file, utilizza il metodo [FileFormatUtil.detectFileFormat(Uint8Array)](https://reference.aspose.com/cells/javascript-cpp/fileformatutil/#detectFileFormat-uint8array-) come mostrato nell'esempio di codice.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells FileFormat Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, FileFormatUtil, Utils } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");

            document.getElementById('runExample').addEventListener('click', async () => {
                // Create a small byte stream equivalent to the original JavaScript Buffer
                const stream = new Uint8Array([0x50, 0x4B, 0x03, 0x04]);

                // Verify password (will propagate errors if any)
                FileFormatUtil.verifyPassword(stream, "1234");

                // Detect file format
                const fileFormatInfo = FileFormatUtil.detectFileFormat(stream);

                // Use property access per universal getter/setter conversion
                document.getElementById('result').innerHTML = '<p>File Format: ' + fileFormatInfo.fileFormatType + '</p>';
                console.log("File Format: " + fileFormatInfo.fileFormatType);
            });
        });
    </script>
</html>
```
