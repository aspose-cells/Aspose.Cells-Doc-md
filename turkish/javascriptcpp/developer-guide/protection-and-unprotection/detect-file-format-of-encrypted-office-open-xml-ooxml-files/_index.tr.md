---
title: JavaScript kullanarak Kriptolanmış Office Open XML  OOXML Dosyalarının Dosya Formatını Tespit Etme  C++ ile
linktitle: Şifrelenmiş Office Open XML  OOXML Dosyasının Dosya Biçimini Algılama
type: docs
weight: 340
url: /tr/javascript-cpp/detect-file-format-of-encrypted-office-open-xml-ooxml-files/
description: C++ ile Aspose.Cells for JavaScript kullanarak şifrelenmiş OOXML dosya formatını nasıl tespit edeceğinizi öğrenin.
---

{{% alert color="primary" %}}  

**Office Open XML** (aynı zamanda **OOXML** veya **Microsoft Open XML** (MOX) olarak da bilinir), Microsoft tarafından geliştirilmiş ve ofis belgelerini (çeşitli elektronik tablo, grafik, sunum ve word işleme belgeleri) temsil eden XML tabanlı bir dosya formatıdır.  

{{% /alert %}}  

Aspose.Cells, şifreli **Microsoft Open XML** dosyalarının dosya formatını tespit etmenin bir yolunu sunar. Dosya türünü belirlemek için, aşağıdaki kod örneğinde gösterildiği gibi [FileFormatUtil.detectFileFormat(Uint8Array)](https://reference.aspose.com/cells/javascript-cpp/fileformatutil/#detectFileFormat-uint8array-) metodunu kullanın.  

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
