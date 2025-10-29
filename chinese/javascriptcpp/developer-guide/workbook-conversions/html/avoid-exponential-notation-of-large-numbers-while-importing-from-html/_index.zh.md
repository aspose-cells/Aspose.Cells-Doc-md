---
title: 在从HTML导入时避免大数字的指数表示
linktitle: 在从HTML导入时避免大数字的指数表示
type: docs
weight: 10
url: /zh/javascript-cpp/avoid-exponential-notation-of-large-numbers-while-importing-from/
description: 学习如何在使用Aspose.Cells for JavaScript通过C++导入HTML时防止大数字被转换为指数形式。
--- 

{{% alert color="primary" %}}  

有时你的HTML中包含如1234567890123456这样超过15位的数字，当你将HTML导入到Excel文件中时，这些数字会被转换为指数记法，比如1.23457E+15。若你希望导入的数字保持原样，不被转换为指数记法，请在加载HTML时使用[**HtmlLoadOptions.keepPrecision**](https://reference.aspose.com/cells/javascript-cpp/htmlloadoptions/#keepPrecision--)属性并设置为**true**。  

{{% /alert %}}  

以下示例代码说明了[**HtmlLoadOptions.keepPrecision**](https://reference.aspose.com/cells/javascript-cpp/htmlloadoptions/#keepPrecision--)属性的用法。API将以原始形式导入数字，不进行指数转换。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Example Title</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlLoadOptions, LoadFormat } = AsposeCells;

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
            // Sample Html containing large number with digits greater than 15
            const html = "<html><body><p>1234567890123456</p></body></html>";

            // Convert Html to byte array
            const byteArray = new TextEncoder().encode(html);

            // Set Html load options and keep precision true
            const loadOptions = new HtmlLoadOptions(LoadFormat.Html);
            loadOptions.keepPrecision = true;

            // Convert byte array into stream
            const stream = byteArray;

            // Create workbook from stream with Html load options
            const workbook = new Workbook(stream, loadOptions);

            // Access first worksheet
            const sheet = workbook.worksheets.get(0);

            // Auto fit the sheet columns
            sheet.autoFitColumns();

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputAvoidExponentialNotationWhileImportingFromHtml.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully. Click the download link to download the file.</p>';
        });
    </script>
</html>
```
