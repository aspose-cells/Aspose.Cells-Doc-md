---
title: Detect File Format of Encrypted Office Open XML - OOXML Files with JavaScript via C++
linktitle: Detect File Format of Encrypted Office Open XML - OOXML Files
type: docs
weight: 340
url: /javascript-cpp/detect-file-format-of-encrypted-office-open-xml-ooxml-files/
description: Learn how to detect the file format of encrypted OOXML files using Aspose.Cells for JavaScript via C++.
---

{{% alert color="primary" %}}  

**Office Open XML** (also known as **OOXML** or **Microsoft Open XML** (MOX)) is an XML-based file format developed by Microsoft for representing office documents like spreadsheets, charts, presentations, and word processing documents.  

{{% /alert %}}  

Aspose.Cells provides a way to detect the file format of encrypted **Microsoft Open XML** files. To identify the file type, use the [FileFormatUtil.detectFileFormat(Uint8Array)](https://reference.aspose.com/cells/javascript-cpp/fileformatutil/#detectFileFormat-uint8array-) method as shown below in the code example.  

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