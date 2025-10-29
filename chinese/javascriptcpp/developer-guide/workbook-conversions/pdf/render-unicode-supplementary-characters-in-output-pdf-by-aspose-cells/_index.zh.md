---
title: 在输出 PDF 时渲染 Unicode 扩展字符 Aspose.Cells for JavaScript 通过 C++
linktitle: 通过Aspose.Cells在输出PDF中呈现Unicode补充字符
type: docs
weight: 350
url: /zh/javascript-cpp/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/
description: 学习如何使用 Aspose.Cells for JavaScript 通过 C++ 在输出 PDF 中渲染 Unicode 扩展字符。 
---

{{% alert color="primary" %}}

普通的Unicode字符长为2个字节，而Unicode补充字符长为4个字节。Aspose.Cells现在支持呈现这些4字节Unicode字符。

在Unicode字符标准中，补充字符是指分配的代码点范围从U+10000到U+10FFFF。换句话说，这些是大于U+FFFF的Unicode字符。

- 在UTF-8中，这些字符每个都是4个字节长。
- 在UTF-16中，这些字符需要2个代理对（16位单位）。

{{% /alert %}}

## 通过 C++ Aspose.Cells for JavaScript 在输出 PDF 时渲染 Unicode 扩展字符

以下截图展示了 Aspose.Cells 如何将 [源 Excel 文件](5115563.xlsx) 转换为 [输出 PDF](5115564.pdf)。可以看到所有三个 Unicode 补充字符都被准确渲染，与 Microsoft Excel 完全一致。

![todo:image_alt_text](output.png)

## 示例代码

您可以使用此示例代码将[源Excel文件](5115563.xlsx)转换为[输出PDF](5115564.pdf)。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Render Unicode Supplementary Characters to PDF</title>
    </head>
    <body>
        <h1>Render Unicode Supplementary Characters to PDF</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save the workbook as PDF
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'RenderUnicodeInOutput_out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```
