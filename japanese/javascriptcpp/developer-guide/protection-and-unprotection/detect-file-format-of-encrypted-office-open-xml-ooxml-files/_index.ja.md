---
title: JavaScriptを使用した暗号化されたOffice Open XML  OOXMLファイルのファイル形式の検出（C++経由）
linktitle: 暗号化されたOffice Open XMLファイルのファイル形式を検出する
type: docs
weight: 340
url: /ja/javascript-cpp/detect-file-format-of-encrypted-office-open-xml-ooxml-files/
description: C++を使用したAspose.Cells for JavaScriptで暗号化されたOOXMLファイルのファイル形式を検出する方法を学びます。
---

{{% alert color="primary" %}}  

**Office Open XML**（または**OOXML**、**Microsoft Open XML**（MOX）とも呼ばれる）は、Microsoftが開発したXMLベースのファイル形式であり、スプレッドシート、チャート、プレゼンテーション、ワードプロセッシングドキュメントの表現に使用されます。  

{{% /alert %}}  

Aspose.Cellsは、暗号化された**Microsoft Open XML**ファイルのファイル形式を検出する方法を提供します。ファイルタイプを識別するには、以下のコード例のように[FileFormatUtil.detectFileFormat(Uint8Array)](https://reference.aspose.com/cells/javascript-cpp/fileformatutil/#detectFileFormat-uint8array-)メソッドを使用します。  

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
