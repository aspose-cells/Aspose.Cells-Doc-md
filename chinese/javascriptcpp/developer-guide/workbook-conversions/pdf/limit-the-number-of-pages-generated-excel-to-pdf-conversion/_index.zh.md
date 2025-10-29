---
title: 限制生成页数  使用 C++ 通过 JavaScript 转换 Excel 为 PDF
linktitle: 限制生成的页面数量  将Excel转换为PDF
type: docs
weight: 180
url: /zh/javascript-cpp/limit-the-number-of-pages-generated-excel-to-pdf-conversion/
description: 学习如何在使用 C++ 通过 JavaScript 将 Excel 工作表转换为 PDF 时限制生成的页数。 
---

{{% alert color="primary" %}}

有时，你希望将特定范围的页面输出到 PDF 文件中。使用 C++ 通过 JavaScript 转换时，Aspose.Cells for JavaScript 可以设置限制，控制生成的页面数量。

{{% /alert %}}

## **限制生成的页面数量**

以下示例显示了如何将Microsoft Excel文件的页面范围（第3页和第4页）呈现为PDF。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells PDF Export Example</title>
    </head>
    <body>
        <h1>Export Specific Pages to PDF</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions } = AsposeCells;

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

            // Open an Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Instantiate the PdfSaveOption
            const options = new PdfSaveOptions();

            // Print only Page 3 and Page 4 in the output PDF
            // Starting page index (0-based index)
            options.pageIndex = 3;
            // Number of pages to be printed
            options.pageCount = 2;

            // Save the PDF file
            const outputData = workbook.save(SaveFormat.Pdf, options);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outPDF1.out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

如果电子表格包含公式，建议在渲染为PDF之前调用[**Workbook.calculateFormula()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--)。这样可以确保依赖公式的值被重新计算，并在输出文件中显示正确的值。

{{% /alert %}}
