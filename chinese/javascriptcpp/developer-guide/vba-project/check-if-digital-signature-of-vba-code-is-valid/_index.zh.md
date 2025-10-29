---
title: 使用JavaScript通过C++检查VBA代码的数字签名是否有效
linktitle: 检查VBA代码的数字签名是否有效
type: docs
weight: 120
url: /zh/javascript-cpp/check-if-digital-signature-of-vba-code-is-valid/
description: 学习如何使用Aspose.Cells for JavaScript通过C++检查VBA代码数字签名的有效性。
--- 

{{% alert color="primary" %}}

Aspose.Cells允许您使用[**Workbook.isValidSigned()**](https://reference.aspose.com/cells/javascript-cpp/vbaproject/#isValidSigned--)属性检查VBA代码的数字签名是否有效。如果签名有效，则返回**true**，否则返回**false**。当您更改VBA代码时，VBA代码的数字签名将变为无效。

{{% /alert %}}

## **用JavaScript检查VBA代码的数字签名是否有效**

以下代码演示了使用该属性的用法，使用[示例Excel文件](5115030.xlsm)进行测试。相同的Excel文件具有有效的签名，但当我们修改其VBA代码并保存工作簿后重新检查时，我们发现其签名已变为无效。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells VBA Signature Example</title>
    </head>
    <body>
        <h1>VBA Signature Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsm,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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
            const resultEl = document.getElementById('result');
            if (!fileInput.files.length) {
                resultEl.innerHTML = '<p style="color: red;">Please select an Excel file (preferably .xlsm).</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Loads the workbook which contains the VBA project
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Signature status before modification
            const isSignedBefore = workbook.vbaProject.isValidSigned();
            console.log("Is VBA Code Project Valid Signed: " + isSignedBefore);

            // Modify the VBA Code, save the workbook then reload
            // VBA Code Signature will now be invalid
            let code = workbook.vbaProject.modules.get(1).codes;
            code = code.replace("Welcome to Aspose", "Welcome to Aspose.Cells");
            workbook.vbaProject.modules.get(1).codes = code;

            // Save the modified workbook to a downloadable blob
            const outputData = workbook.save(SaveFormat.Xlsm);
            const blob = new Blob([outputData], { type: 'application/vnd.ms-excel.sheet.macroEnabled.12' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsm';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            // Reload from the saved output data to verify signature status
            const reloadedWorkbook = new Workbook(new Uint8Array(outputData));
            const isSignedAfter = reloadedWorkbook.vbaProject.isValidSigned();
            console.log("Is VBA Code Project Valid Signed: " + isSignedAfter);

            // Update result UI
            resultEl.innerHTML = `
                <p style="color: green;">Operation completed successfully!</p>
                <p>Signature valid before modification: <strong>${isSignedBefore}</strong></p>
                <p>Signature valid after modification: <strong>${isSignedAfter}</strong></p>
                <p>Click the download link to get the modified file.</p>
            `;
        });
    </script>
</html>
```
