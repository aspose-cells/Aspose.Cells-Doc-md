---
title: 在保存为 PDF 时使用 C++ 通过 JavaScript 打印批注
linktitle: 保存为PDF时打印注释
type: docs
weight: 10
url: /zh/javascript-cpp/print-comments-while-saving-to-pdf/
description: 学习如何在使用 C++ 通过 JavaScript 将 Excel 文档保存为 PDF 时打印批注。
---

{{% alert color="primary" %}}  

Microsoft Excel允许您在打印或保存为PDF格式时打印注释，具有以下选项  

- 无  
- 工作表末尾  
- 如在工作表上显示的那样  

Aspose.Cells 提供 [**PrintCommentsType**](https://reference.aspose.com/cells/javascript-cpp/printcommentstype) 枚举以支持相同功能。[**PrintCommentsType**](https://reference.aspose.com/cells/javascript-cpp/printcommentstype) 枚举包含以下成员  

- PrintNoComments  
- PrintInPlace  
- PrintSheetEnd  

{{% /alert %}}  

## **保存为PDF时打印注释**  

以下示例代码说明了如何使用[**PrintCommentsType**](https://reference.aspose.com/cells/javascript-cpp/printcommentstype)在保存为PDF时打印批注。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Print Comments to PDF</title>
    </head>
    <body>
        <h1>Print Comments While Saving to PDF Example</h1>
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
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const worksheet = workbook.worksheets.get(0);

            worksheet.pageSetup.printComments = AsposeCells.PrintCommentsType.PrintSheetEnd;

            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'PrintCommentWhileSavingToPdf_out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook saved to PDF with comments printed at sheet end. Click the download link to get the file.</p>';
        });
    </script>
</html>
```
