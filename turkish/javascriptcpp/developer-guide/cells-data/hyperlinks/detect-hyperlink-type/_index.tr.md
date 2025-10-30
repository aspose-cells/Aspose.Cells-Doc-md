---
title: Bağlantı Türünü Algıla
type: docs
weight: 160
url: /tr/javascript-cpp/detect-hyperlink-type/
description: 12345678Script aracılığıyla C++ API kullanarak köprü türünü nasıl tespit edeceğinizi öğrenin.
keywords: JavaScript ile köprü türünü tespit edin, C++ ile köprü türünü tespit edin, JavaScript ile köprü türünü alın.
---

## **Bağlantı Türünü Algılamak**

Bir Excel dosyası, dış, hücre referansı, dosya yolu vb. gibi farklı türlerde köprülere sahip olabilir. 12345678Script C++ ile köprü türünü tespit etme özelliğini destekler. Köprü türleri [**TargetModeType**](https://reference.aspose.com/cells/javascript-cpp/targetmodetype) Enum'u ile temsil edilir. [**TargetModeType**](https://reference.aspose.com/cells/javascript-cpp/targetmodetype) Enum'unun aşağıdaki üyeleri vardır.

- Dış: Dış bağlantı
- DosyaYolu: Dosyaların/klasörlerin yerel ve tam yolu.
- E-posta: E-posta
- HücreReferansı: Hücre veya adlandırılmış alan bağlantısı.

Köprü türünü kontrol etmek için, [**Hyperlink**](https://reference.aspose.com/cells/javascript-cpp/hyperlink) sınıfı, [**linkType**](https://reference.aspose.com/cells/javascript-cpp/hyperlink/#linkType--) özelliğiyle ve [**TargetModeType**](https://reference.aspose.com/cells/javascript-cpp/targetmodetype) dönüş tipiyle bir özellik sağlar. Aşağıdaki kod parçası, bu [kaynak excel dosyasını](94896195.xlsx) kullanarak [**linkType**](https://reference.aspose.com/cells/javascript-cpp/hyperlink/#linkType--) özelliğinin kullanımını gösterir.

### Kaynak Kodu

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Link Types Example</title>
    </head>
    <body>
        <h1>Link Types Example</h1>
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

            document.getElementById('runExample').addEventListener('click', async () => {
                const fileInput = document.getElementById('fileInput');
                const resultDiv = document.getElementById('result');

                if (!fileInput.files.length) {
                    resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                    return;
                }

                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();

                // Instantiating a Workbook object from the uploaded file
                const workbook = new Workbook(new Uint8Array(arrayBuffer));

                // Get the first (default) worksheet
                const worksheet = workbook.worksheets.get(0);

                // Create a range A1:A7 (original code created A1:B7 but used A1 to A7 in parameters)
                const range = worksheet.cells.createRange("A1", "A7");

                // Get Hyperlinks in range
                const hyperlinks = range.hyperlinks;

                let outputHtml = '<p>Hyperlinks found:</p><ul>';
                if (typeof hyperlinks.forEach === 'function') {
                    hyperlinks.forEach(link => {
                        outputHtml += `<li>${link.textToDisplay}: ${link.linkType}</li>`;
                    });
                } else {
                    for (let i = 0; i < hyperlinks.count; i++) {
                        const link = hyperlinks.get(i);
                        outputHtml += `<li>${link.textToDisplay}: ${link.linkType}</li>`;
                    }
                }
                outputHtml += '</ul>';

                resultDiv.innerHTML = outputHtml;
            });
        });
    </script>
</html>
```


Yukarıda verilen kod parçası tarafından üretilen çıktı aşağıdaki gibidir.

### Konsol Çıktısı
