---
title: Erkennung des Dateiformats verschlüsselter Office Open XML  OOXML Dateien mit JavaScript via C++
linktitle: Dateiformat von verschlüsselten Office Open XML  OOXML Dateien erkennen
type: docs
weight: 340
url: /de/javascript-cpp/detect-file-format-of-encrypted-office-open-xml-ooxml-files/
description: Lernen Sie, wie man das Dateiformat verschlüsselter OOXML Dateien mit Aspose.Cells for JavaScript via C++ erkennt.
---

{{% alert color="primary" %}}  

**Office Open XML** (auch bekannt als **OOXML** oder **Microsoft Open XML** (MOX)) ist ein XML-basiertes Dateiformat, das von Microsoft entwickelt wurde, um Office-Dokumente wie Tabellen, Diagramme, Präsentationen und Textverarbeitungsdokumente darzustellen.  

{{% /alert %}}  

Aspose.Cells bietet eine Möglichkeit, das Dateiformat verschlüsselter **Microsoft Open XML**-Dateien zu erkennen. Um den Dateityp zu identifizieren, verwenden Sie die Methode [FileFormatUtil.detectFileFormat(Uint8Array)](https://reference.aspose.com/cells/javascript-cpp/fileformatutil/#detectFileFormat-uint8array-) wie im folgenden Codebeispiel gezeigt.  

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
