---
title: C++ kullanarak JavaScript ile Dosya Formatını Tespit Etme ve Dosyanın Şifreli olup olmadığını Kontrol Etme
linktitle: Bir Dosya Biçimini Algılamak ve Dosyanın Şifreli Olup Olmadığını Kontrol Etme
type: docs
weight: 2700
url: /tr/javascript-cpp/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/
description: C++ kullanarak Aspose.Cells for JavaScript ile dosya formatını tespit etmeyi ve dosyanın şifreli olup olmadığını kontrol etmeyi öğrenin.
---

{{% alert color="primary" %}}  
Bazen, dosya uzantısı dosya içeriğinin uygun olduğunu garanti etmediği için, dosyayı açmadan önce formatını tespit etmeniz gerekir. Dosya şifreli olabilir (parola korumalı dosya) ve doğrudan okunamayabilir veya okumamamız gerekebilir. C++ kullanarak Aspose.Cells for JavaScript [**FileFormatUtil.detectFileFormat(Uint8Array)**](https://reference.aspose.com/cells/javascript-cpp/fileformatutil/#detectFileFormat-uint8array-) statik metodunu ve ilgili API'leri kullanarak belgeleri işleyebilirsiniz.  
{{% /alert %}}  

Aşağıdaki örnek kod, dosya biçimini (dosya yolu kullanarak) algılamanın ve uzantısını kontrol etmenin nasıl yapıldığını göstermektedir. Ayrıca dosyanın şifreli olup olmadığını belirleyebilirsiniz.  

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
