---
title: 通过 C++ 使用 JavaScript 自动调整行高以进行渲染
linktitle: 在渲染时自动调整列的行高
type: docs
weight: 130
url: /zh/javascript-cpp/autofit-rows-for-rendering/
description: 了解如何使用 Aspose.Cells for JavaScript 通过 C++ 在 Excel 中自动调整行高以进行渲染，防止文本被截断到已保存的 PDF 文件中。
---

通常情况下，为了在单元格中显示全部文本，可以在Microsoft Excel中以普通视图（100%的缩放）自动调整行高。这允许在普通视图中完全显示文本，即使打印或保存为PDF，文本也会正确显示。

然而，在某些情况下，自动调整行高在普通视图中效果良好，但切换到打印视图或保存为PDF时，文本会被剪裁。请检查源文件【Book1.xlsx】及截图。

![打印视图中文本被截断](text_clipped_in_printview.png)

如果你想防止在已保存的 PDF 文件中被裁剪的文本，可以使用 [AutoFitterOptions.forRendering](https://reference.aspose.com/cells/javascript-cpp/autofitteroptions/#forRendering--) 选项自动调整行高。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Autofit Rows and Save as PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, AutoFitterOptions, SaveFormat, Utils } = AsposeCells;

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

            // Init workbook instance from uploaded file.
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Set autofit options for rendering.
            const autoFitterOptions = new AutoFitterOptions();
            autoFitterOptions.forRendering = true;

            // Autofit rows with options on first worksheet.
            const worksheet = workbook.worksheets.get(0);
            worksheet.autoFitRows(autoFitterOptions);

            // Save to pdf.
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```

现在，在输出的 PDF 文件中文本不再被截断。

![保存的 PDF 文件中文本未被截断](text_not_clipped_in_saved_pdf.png)
