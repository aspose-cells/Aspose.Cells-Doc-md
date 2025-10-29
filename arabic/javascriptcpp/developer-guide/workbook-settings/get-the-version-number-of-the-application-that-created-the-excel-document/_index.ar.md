---
title: الحصول على رقم إصدار التطبيق الذي أنشأ مستند إكسل باستخدام جافا سكريبت عبر C++
linktitle: الحصول على رقم الإصدار للتطبيق الذي أنشأ مستند Excel
type: docs
weight: 210
url: /ar/javascript-cpp/get-the-version-number-of-the-application-that-created-the-excel-document/
---

{{% alert color="primary" %}}

 غالبًا ما تحتاج إلى معرفة رقم إصدار التطبيق الذي أنشأ مستند ميكروسوفت إكسل. يوفر Aspose.Cells for JavaScript عبر C++ الخاصية [**Workbook.builtInDocumentProperties**](https://reference.aspose.com/cells/javascript-cpp/workbook/#builtInDocumentProperties--) لهذا الغرض.

{{% /alert %}}

يوضح كود المثال التالي استخدام خاصية [**Workbook.builtInDocumentProperties**](https://reference.aspose.com/cells/javascript-cpp/workbook/#builtInDocumentProperties--)، حيث يحمل ملفات Excel التي أنشأتها Microsoft Excel 2003، 2007، 2010 و2013 ويطبع رقم إصدار التطبيق الذي أنشأ هذه الوثائق.

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
