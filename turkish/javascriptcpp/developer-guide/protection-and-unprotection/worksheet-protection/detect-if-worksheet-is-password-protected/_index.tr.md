---
title: JavaScript kullanarak C++ ile Çalışma Sayfası Parola Korumalı mı Kontrol et
linktitle: Çalışma sayfasının Parola Korumalı Olup Olmadığını Algılama
type: docs
weight: 360
url: /tr/javascript-cpp/detect-if-worksheet-is-password-protected/
description: C++ kullanarak bir çalışma sayfasının parola koruması olup olmadığını nasıl tespit edeceğinizi öğrenin. 
keywords: JavaScript ile Çalışma Sayfası Parola Korumasını Tespit et, JavaScript ile Çalışma Sayfası Parola Koruması Kontrolü, Aspose.Cells for JavaScript kullanılarak C++ ile
---

{{% alert color="primary" %}}

İş kitaplarını ve çalışma sayfalarını ayrı ayrı korumak mümkündür. Örneğin, bir çalışma sayfası parola ile korunan biri veya daha fazla çalışma sayfası içerebilir, ancak çalışma kitabı kendisi korumalı veya değil olabilir. Aspose.Cells API'leri, belirli bir çalışma sayfasının parola koruması olup olmadığını tespit etmek için araçlar sağlar. Bu makale, aynı sonucu elde etmek için C++ API üzerinden Aspose.Cells for JavaScript kullanımını göstermektedir.

{{% /alert %}}

C++ aracılığıyla Aspose.Cells for JavaScript, bir çalışma sayfasının parola korumalı olup olmadığını tespit etmek için [**Protection.isProtectedWithPassword()**](https://reference.aspose.com/cells/javascript-cpp/protection/#isProtectedWithPassword--) özelliğini ortaya çıkardı. Boolean türündeki [**Protection.isProtectedWithPassword()**](https://reference.aspose.com/cells/javascript-cpp/protection/#isProtectedWithPassword--) özelliği, eğer [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) parola ile korunuyorsa **doğru**, değilse **yanlış** döner.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Check Worksheet Password Protection</h1>
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

            // Create an instance of Workbook and load a spreadsheet
            const book = new Workbook(new Uint8Array(arrayBuffer));

            // Access the protected Worksheet
            const sheet = book.worksheets.get(0);

            // Check if Worksheet is password protected
            if (sheet.protection.isProtectedWithPassword()) {
                resultDiv.innerHTML = '<p>Worksheet is password protected</p>';
                console.log("Worksheet is password protected");
            } else {
                resultDiv.innerHTML = '<p>Worksheet is not password protected</p>';
                console.log("Worksheet is not password protected");
            }
        });
    </script>
</html>
```
