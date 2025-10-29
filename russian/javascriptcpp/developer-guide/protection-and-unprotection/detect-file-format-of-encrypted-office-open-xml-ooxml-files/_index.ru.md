---
title: Обнаружение формата файла зашифрованных Office Open XML  OOXML файлов с помощью JavaScript через C++
linktitle: Определить формат файла зашифрованного Office Open XML  OOXML
type: docs
weight: 340
url: /ru/javascript-cpp/detect-file-format-of-encrypted-office-open-xml-ooxml-files/
description: Узнайте, как определить формат файла зашифрованных OOXML файлов с помощью Aspose.Cells for JavaScript через C++.
---

{{% alert color="primary" %}}  

**Office Open XML** (также известный как **OOXML** или **Microsoft Open XML** (MOX)) — это основанный на XML формат файла, разработанный Microsoft для представления офисных документов, таких как таблицы, диаграммы, презентации и текстовые документы.  

{{% /alert %}}  

Aspose.Cells предоставляет способ определения формата файла зашифрованных **Microsoft Open XML** файлов. Чтобы определить тип файла, используйте метод [FileFormatUtil.detectFileFormat(Uint8Array)](https://reference.aspose.com/cells/javascript-cpp/fileformatutil/#detectFileFormat-uint8array-) как показано в примере кода ниже.  

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
