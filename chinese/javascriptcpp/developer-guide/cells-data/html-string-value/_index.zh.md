---
title: 在单元格内添加 HTML 富文本
linktitle: HTML 字符串值
type: docs
weight: 50
url: /zh/javascript-cpp/adding-html-rich-text-inside-the-cell/
description: 学习如何通过 Aspose.Cells for JavaScript 通过 C++ API 在单元格内添加 HTML 富文本。
keywords: 在 JavaScript 通过 C++ 使用 Aspose.Cells 库在 Excel 文件中插入超链接，而无需 MS Excel。
---

{{% alert color="primary" %}}

Aspose.Cells支持将微软Excel导向的HTML转换为XLS/XLSX格式。这意味着由微软Excel生成的HTML可以使用Aspose.Cells转换回XLS/XLSX格式。

同样，如果有一些简单的HTML，Aspose.Cells可以将其转换为HTML丰富文本。Aspose.Cells提供[**Cell.htmlString**](https://reference.aspose.com/cells/javascript-cpp/cell/#htmlString-string-)属性，可以接受这样的简单HTML并将其转换为格式化的单元格文本。

{{% /alert %}}

下面的代码示例向您展示了如何在单元格中添加HTML富文本。请查看输出Excel文件的屏幕截图。

![todo:image_alt_text](adding-html-rich-text-inside-the-cell_1)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells HTML String Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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
            let workbook;

            // If a file is provided, open it; otherwise create a new workbook
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access cell A1
            const cell = worksheet.cells.get("A1");

            // Set HTML formatted string to the cell (converted setter -> property)
            cell.htmlString = "<Font Style=\"FONT-WEIGHT: bold;FONT-STYLE: italic;TEXT-DECORATION: underline;FONT-FAMILY: Arial;FONT-SIZE: 11pt;COLOR: #ff0000;\">This is simple HTML formatted text.</Font>";

            // Save the workbook to XLSX format and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">HTML string written to A1. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


## 相关文章

- [使用HTML设置单元格值显示项目符号](/cells/zh/javascript-cpp/display-bullets-by-setting-cell-value-using/)
- [从单元格获取HTML5字符串](/cells/zh/javascript-cpp/get-html5-string-from-cell/)
