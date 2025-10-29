---
title: 每个 Excel 工作表渲染一个 PDF 页面  使用 C++ 通过 JavaScript 转换 Excel 为 PDF
linktitle: 将Excel工作表渲染为一份PDF页面  Excel转PDF转换
type: docs
weight: 100
url: /zh/javascript-cpp/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/
---

{{% alert color="primary" %}}

当处理大型 Microsoft Excel 文件（例如，包含许多工作表，每个有50列和300行以上数据的工作簿）时，你可能希望每个工作表显示一页 PDF，无论工作表的大小。这意味着每页的尺寸可能会有很大差异。这可以通过 C++ Aspose.Cells for JavaScript 实现。

{{% /alert %}}

请查看以下示例代码，将多个工作表的Excel文件转换为PDF。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Excel to PDF</title>
    </head>
    <body>
        <h1>Convert Excel to PDF (One Page Per Worksheet)</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Convert to PDF</button>
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

            // Initialize a new Workbook by opening the selected Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Implement one page per worksheet option
            const pdfSaveOptions = new PdfSaveOptions();
            pdfSaveOptions.onePagePerSheet = true;

            // Save the PDF file (returns binary data)
            const outputData = workbook.save(SaveFormat.Pdf, pdfSaveOptions);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'OutputFile.out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

如果设置了 [PdfSaveOptions.onePagePerSheet](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#onePagePerSheet--) 选项为**true**，所有工作表内容将渲染到一页 PDF 中。

{{% /alert %}} {{% alert color="primary" %}}

如果你的电子表格包含公式，最好在渲染为 PDF 之前调用 [Workbook.calculateFormula()](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--)。这确保依赖公式的值被重新计算，PDF 中显示正确的值。

{{% /alert %}}
