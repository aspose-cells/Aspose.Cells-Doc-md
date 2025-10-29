---
title: 获取创建 Excel 文档的应用程序的版本号，使用 C++ 通过 JavaScript
linktitle: 获取创建Excel文档的应用程序的版本号
type: docs
weight: 210
url: /zh/javascript-cpp/get-the-version-number-of-the-application-that-created-the-excel-document/
---

{{% alert color="primary" %}}

经常需要知道创建 Microsoft Excel 文档的应用程序的版本号。 Aspose.Cells for JavaScript 通过 C++ 提供了 [**Workbook.builtInDocumentProperties**](https://reference.aspose.com/cells/javascript-cpp/workbook/#builtInDocumentProperties--) 属性来实现此目的。

{{% /alert %}}

以下示例代码演示了如何使用[**Workbook.builtInDocumentProperties**](https://reference.aspose.com/cells/javascript-cpp/workbook/#builtInDocumentProperties--)属性。它加载由Microsoft Excel 2003、2007、2010和2013创建的Excel文件，并输出创建这些Excel文件的应用程序的版本号。

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
