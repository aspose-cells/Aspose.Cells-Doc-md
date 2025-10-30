---
title: Excel belgesini oluşturan uygulamanın sürüm numarasını JavaScript ve C++ kullanarak alın.
linktitle: Excel Belgesini Oluşturan Uygulamanın Sürüm Numarasını Almak
type: docs
weight: 210
url: /tr/javascript-cpp/get-the-version-number-of-the-application-that-created-the-excel-document/
---

{{% alert color="primary" %}}

Microsoft Excel belgesi oluşturan uygulamanın sürüm numarasını genellikle bilmeniz gerekir. Aspose.Cells for JavaScript ve C++ bu amaçla [**Workbook.builtInDocumentProperties**](https://reference.aspose.com/cells/javascript-cpp/workbook/#builtInDocumentProperties--) özelliğini sağlar.

{{% /alert %}}

Aşağıdaki örnek kod, [**Workbook.builtInDocumentProperties**](https://reference.aspose.com/cells/javascript-cpp/workbook/#builtInDocumentProperties--) özelliğinin kullanımını gösterir. Microsoft Excel 2003, 2007, 2010 ve 2013 ile oluşturulan Excel dosyalarını yükler ve bu belgeleri oluşturan uygulamanın sürüm numarasını yazdırır.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Print Excel Version</title>
    </head>
    <body>
        <h1>Print Excel Version Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" multiple />
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
                resultDiv.innerHTML = '<p style="color: red;">Please select one or more Excel files.</p>';
                return;
            }

            let outputHtml = '<h2>File Versions</h2><ul>';
            for (const file of fileInput.files) {
                const arrayBuffer = await file.arrayBuffer();
                // Instantiating a Workbook object from the uploaded file
                const workbook = new Workbook(new Uint8Array(arrayBuffer));
                // Access built-in document properties and read version
                const version = workbook.builtInDocumentProperties.version;
                console.log(file.name + " Version: " + version);
                outputHtml += `<li><strong>${file.name}</strong>: ${version}</li>`;
            }
            outputHtml += '</ul>';
            resultDiv.innerHTML = outputHtml;
        });
    </script>
</html>
```
