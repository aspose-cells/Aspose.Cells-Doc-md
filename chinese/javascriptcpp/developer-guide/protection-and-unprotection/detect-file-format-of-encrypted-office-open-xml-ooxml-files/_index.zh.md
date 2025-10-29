---
title: 用C++的JavaScript检测加密的Office Open XML（OOXML）文件的文件格式
linktitle: 检测加密的Office Open XML  OOXML文件的文件格式
type: docs
weight: 340
url: /zh/javascript-cpp/detect-file-format-of-encrypted-office-open-xml-ooxml-files/
description: 学习如何使用 Aspose.Cells for JavaScript 通过 C++ 检测加密的 OOXML 文件的文件格式。
---

{{% alert color="primary" %}}  

**Office Open XML**（也称为**OOXML**或**微软开放XML**（MOX））是一种由微软开发的基于XML的文件格式，用于表示办公文档，如电子表格、图表、演示文稿和文字处理文件。  

{{% /alert %}}  

Aspose.Cells 提供了一种检测加密的 **Microsoft Open XML** 文件的文件格式的方法。要识别文件类型，请使用 [FileFormatUtil.detectFileFormat(Uint8Array)](https://reference.aspose.com/cells/javascript-cpp/fileformatutil/#detectFileFormat-uint8array-) 方法，如下代码示例所示。  

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
