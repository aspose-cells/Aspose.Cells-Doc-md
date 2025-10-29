---
title: 用 JavaScript 通过 C++ 设置或取消共享工作簿的密码保护
linktitle: 密码保护或取消保护共享工作簿
type: docs
weight: 10
url: /zh/javascript-cpp/password-protect-or-unprotect-the-shared-workbook/
---

## **可能的使用场景**

您可以如下面截图所示，用 Microsoft Excel 保护或取消保护共享工作簿。Aspose.Cells for JavaScript 通过 C++ 也支持此功能，使用 [**Workbook.protectSharedWorkbook(string)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#protectSharedWorkbook-string-) 和 [**Workbook.unprotectSharedWorkbook(string)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#unprotectSharedWorkbook-string-) 方法。

![todo:image_alt_text](password-protect-or-unprotect-the-shared-workbook_1.png)

## **密码保护或取消保护共享工作簿**

以下示例代码创建一个工作簿并保护它，同时启用共享，然后将其另存为 [输出 Excel 文件](55541777.xlsx)。截图显示当您尝试取消保护时，Microsoft Excel 会提示您输入密码以取消保护。

![todo:image_alt_text](password-protect-or-unprotect-the-shared-workbook_2.png)

## **示例代码**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Protect Shared Workbook Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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
            // Creating an empty Workbook
            const workbook = new Workbook();

            // Protect the Shared Workbook with Password
            workbook.protectSharedWorkbook("1234");

            // Uncomment this line to Unprotect the Shared Workbook
            // workbook.unprotectSharedWorkbook("1234");

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputProtectSharedWorkbook.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook protected successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
