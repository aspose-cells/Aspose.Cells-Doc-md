---
title: JavaScript ile C++ kullanarak Çalışma Kitabının Yönetilmeyen Kaynaklarını Serbest Bırakın
linktitle: Çalışma Kitabının Yönetilmeyen Kaynaklarını Serbest Bırak
type: docs
weight: 310
url: /tr/javascript-cpp/release-unmanaged-resources-of-the-workbook/
description: C++ kullanarak Aspose.Cells for JavaScript ile Çalışma Kitabı nesnesinin yönetilmeyen kaynaklarını serbest bırakmayı öğrenin. 
---

{{% alert color="primary" %}}

Aspose.Cells, [**Workbook.dispose()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#dispose--) metodunu sağlayarak [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) nesnesinin yönetilmeyen kaynaklarını serbest bırakmanızı sağlar. Dispose deseni, yalnızca dosya ve boru tutamağı, kayıt defteri tutamağı, bekleme tutamağı veya yönetilmeyen bellek bloklarına işaret eden iş nesneleriyle erişen nesneler için kullanılır. Bu, çöp toplayıcının kullanılmayan yönetilen nesneleri geri kazanmakta çok verimli olması, ancak yönetilmeyen nesneleri geri kazanamaması nedeniyle yapılır.

{{% /alert %}}

[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) nesnesi artık *System.IDisposable* arayüzünü uygular ve tek bir yöntem olan [**Workbook.dispose()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#dispose--) içerir. Ya doğrudan [**Workbook.dispose()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#dispose--) metodunu çağırabilir veya *Using* ifadesiyle bu yöntemi otomatik olarak çağırabilirsiniz.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Dispose Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Loads the workbook which contains hidden external links
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create workbook object
            const wb1 = new Workbook();

            // Call Dispose method
            wb1.dispose();

            // Call Dispose method via a scoped approach
            (async () => {
                const wb2 = new Workbook();
                // Any other code goes here
                wb2.dispose();
            })();

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully!</p>';
        });
    </script>
</html>
```
