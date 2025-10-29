---
title: 使用Aspose.Cells for JavaScript通过C++读取苹果公司开发的Numbers电子表格
linktitle: 读取由Apple Inc.开发的Numbers电子表格
type: docs
weight: 140
url: /zh/javascript-cpp/read-numbers-spreadsheet-developed-by-apple-inc-using-aspose-cells/
description: 学习如何用Aspose.Cells for JavaScript通过C++读取苹果公司开发的Numbers电子表格。 
---

## **可能的使用场景**

Numbers 是由 Apple Inc. 开发的一款电子表格应用程序。Aspose.Cells 可以读取 Numbers 电子表格，但不支持写入。它可以读取 Numbers 电子表格中的数据、样式和公式。

## **用Aspose.Cells for JavaScript通过C++读取苹果公司开发的Numbers电子表格**

以下示例代码加载【示例数字电子表格】（sampleNumbersByAppleInc.numbers），并将其转换为【输出 PDF 格式】（outputNumbersByAppleInc.pdf）。您需要在构造函数中使用 [**LoadOptions**](https://reference.aspose.com/cells/javascript-cpp/loadoptions) 类并指定 [**LoadFormat.Numbers**](https://reference.aspose.com/cells/javascript-cpp/loadformat) 作为参数来成功加载。请从提供的链接下载它们。您可以用任何数字电子表格尝试代码。也请阅读代码注释以获取更多帮助。

## **示例代码**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Numbers to PDF Example</title>
    </head>
    <body>
        <h1>Convert Apple Numbers to PDF</h1>
        <input type="file" id="fileInput" accept=".numbers" />
        <button id="runExample">Convert to PDF</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions, LoadFormat } = AsposeCells;

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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select a .numbers file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Specify load options to load Numbers spreadsheet
            const opts = new LoadOptions(LoadFormat.Numbers);

            // Load the Numbers spreadsheet in workbook with above load options
            const wb = new Workbook(new Uint8Array(arrayBuffer), opts);

            // Save the workbook to PDF format
            const outputData = wb.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputNumbersByAppleInc.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the PDF.</p>';
        });
    </script>
</html>
```
