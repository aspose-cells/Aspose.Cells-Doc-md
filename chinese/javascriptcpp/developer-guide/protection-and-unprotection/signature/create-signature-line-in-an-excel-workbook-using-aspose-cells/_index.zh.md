---
title: 使用 Aspose.Cells for JavaScript 通过 C++ 在 Excel 工作簿中创建签名行
linktitle: 使用Aspose.Cells在Excel工作簿中创建签名行
type: docs
weight: 150
url: /zh/javascript-cpp/create-signature-line-in-an-excel-workbook-using-aspose-cells/
description: 本文介绍如何用 JavaScript 及 Aspose.Cells for JavaScript 通过 C++ 在 Excel 工作簿中创建签名行
keywords: 通过 C++ 和 JavaScript 在 Excel 工作簿中创建签名行，如何创建签名行，如何添加签名行，如何将签名行添加到 Excel 文件中
---

## **介绍**  

Microsoft Excel提供了在Excel工作簿中添加 **签名行** 的功能。您可以通过单击 **插入** 选项卡，然后从 **文本** 组中选择 **签名行** 来添加签名行。  

## **如何为Excel创建签名行**  

 Aspose.Cells for JavaScript 通过 C++ 还支持此功能，并公开了 [**Picture.signatureLine**](https://reference.aspose.com/cells/javascript-cpp/picture/#signatureLine--) 属性用于此目的。本文将说明如何使用此属性通过 Aspose.Cells 添加签名行  

 以下示例代码使用[**Picture.signatureLine**](https://reference.aspose.com/cells/javascript-cpp/picture/#signatureLine--)属性添加签名线，并保存工作簿。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Add Signature Line Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, SignatureLine, Utils } = AsposeCells;

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

            // Create or load workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Create signature line object
            const signatureLine = new SignatureLine();
            signatureLine.signer = "John Doe";
            signatureLine.title = "Development Lead";
            signatureLine.email = "john.doe@aspose.com";

            // Adds a Signature Line to the first worksheet.
            workbook.worksheets.get(0).shapes.addSignatureLine(1, 1, signatureLine);

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Signature line added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
