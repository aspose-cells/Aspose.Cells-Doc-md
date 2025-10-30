---
title: Upptäck filformat för krypterade Office Open XML  OOXML filer med JavaScript via C++
linktitle: Identifiera filformat för krypterade Office Open XML  OOXML filer
type: docs
weight: 340
url: /sv/javascript-cpp/detect-file-format-of-encrypted-office-open-xml-ooxml-files/
description: Lär dig hur man upptäcker filformat för krypterade OOXML filer med Aspose.Cells for JavaScript via C++
---

{{% alert color="primary" %}}  

**Office Open XML** (även känt som **OOXML** eller **Microsoft Open XML** (MOX)) är ett XML-baserat filformat utvecklat av Microsoft för att representera kontorsdokument som kalkylblad, diagram, presentationer och ordbehandlingsdokument.  

{{% /alert %}}  

Aspose.Cells ger ett sätt att upptäcka filformat för krypterade **Microsoft Open XML**-filer. För att identifiera filtypen, använd metoden [FileFormatUtil.detectFileFormat(Uint8Array)](https://reference.aspose.com/cells/javascript-cpp/fileformatutil/#detectFileFormat-uint8array-) som visas i kodexemplet nedan.  

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
