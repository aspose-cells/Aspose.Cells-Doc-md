---
title: 使用 C++ 通过 JavaScript 保护和解除保护工作表
linktitle: 保护和取消保护工作表
type: docs
weight: 40
url: /zh/javascript-cpp/protect-and-unprotect-worksheets/
description: 使用 C++ 通过 Aspose.Cells for JavaScript 保护和解除保护Excel文件的工作表。
---

{{% alert color="primary" %}}  
为防止其他用户意外或故意更改、移动或删除工作表中的数据，您可以锁定 Excel 工作表上的单元格，然后使用密码保护工作表。  
{{% /alert %}}  

## **在 MS Excel 中保护和取消保护工作表**  

**![保护和取消保护工作表](protect-and-unprotect-worksheet.png)**  

1. 点击 **审阅 > 保护工作表**。  
1. 在 **密码框** 中输入密码。  
1. 选择 **允许** 选项。  
1. 选择 **确定**，重新输入密码以确认，然后再次选择 **确定**。  

## ** 使用 C++ 通过 Aspose.Cells for JavaScript 保护工作表**  
只需要以下简单代码行来实现保护 Excel 文件的工作簿结构。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Protect Worksheet Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ProtectionType } = AsposeCells;

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
            // Create a new file (workbook)
            const workbook = new Workbook();

            // Gets the first worksheet.
            const sheet = workbook.worksheets.get(0);

            // Protect contents of the worksheet.
            sheet.protect(ProtectionType.Contents);

            // Protect worksheet with password.
            sheet.protection.password = "test";

            // Save as Excel file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Book1.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet protected and file is ready. Click the download link to get the file.</p>';
        });
    </script>
</html>
```  

## ** 使用 C++ 通过 Aspose.Cells for JavaScript 解除保护工作表**  
使用Aspose.Cells API轻松取消保护工作表。如果工作表被密码保护，则需要提供正确的密码。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Unprotect Worksheet Example</title>
    </head>
    <body>
        <h1>Unprotect Worksheet Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Unprotect Worksheet</button>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Unprotect contents of the worksheet using password
            sheet.unprotect("password");

            // Save the modified workbook to XLSX format and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Book1.unprotected.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Unprotected Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet unprotected successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

## **高级主题**  
- [自 Excel XP 以来的高级保护设置](/cells/zh/javascript-cpp/advanced-protection-settings-since-excel-xp/)  
- [检测工作表是否受密码保护](/cells/zh/javascript-cpp/detect-if-worksheet-is-password-protected/)  
- [保护工作表](/cells/zh/javascript-cpp/protecting-worksheets/)  
- [取消保护工作表](/cells/zh/javascript-cpp/unprotect-a-worksheet/)  
- [验证用于保护工作表的密码](/cells/zh/javascript-cpp/verify-password-used-to-protect-the-worksheet/)
