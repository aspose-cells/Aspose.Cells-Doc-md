---
title: Как определить формат файла и проверить, зашифрован ли файл с помощью JavaScript через C++
linktitle: Как определить формат файла и проверить, зашифрован ли файл
type: docs
weight: 2700
url: /ru/javascript-cpp/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/
description: Узнайте, как определить формат файла и проверить, зашифрован ли файл, с помощью Aspose.Cells for JavaScript через C++.
---

{{% alert color="primary" %}}  
Иногда нужно определить формат файла перед его открытием, потому что расширение файла не гарантирует, что содержимое файла подходит. Файл может быть зашифрован (защищен паролем), поэтому его нельзя читать напрямую, или нам не нужно его читать. Aspose.Cells for JavaScript через C++ предоставляет статический метод [**FileFormatUtil.detectFileFormat(Uint8Array)**](https://reference.aspose.com/cells/javascript-cpp/fileformatutil/#detectFileFormat-uint8array-) и некоторые соответствующие API, которые можно использовать для обработки документов.  
{{% /alert %}}  

В следующем образце кода показано, как определить формат файла (с использованием пути к файлу) и проверить его расширение. Вы также можете определить, зашифрован ли файл.  

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
