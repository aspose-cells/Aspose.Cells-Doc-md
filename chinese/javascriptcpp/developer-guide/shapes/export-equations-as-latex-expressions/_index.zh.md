---
title: 如何将 Excel 方程导出为其他类型的表达式
linktitle: 导出公式
type: docs
weight: 100
url: /zh/javascript-cpp/export-equation/
---

有时，您可能需要在代码中将 Excel 公式导出为其他格式以满足工作需要，Aspose.Cells 库可以满足您的需求。以下内容介绍一些将 Excel 公式导出到其他格式的方法，希望对您有所帮助。

这里提供了示例代码，帮助您使用Aspose.Cells实现目标，同时也提供了必要的示例文件。

示例文件：[Sample.xlsx](Sample.xlsx)

## 将公式导出为LaTeX表达式

如果您想将 Excel 中的方程导出为 LaTeX 表达式，可以使用 [EquationNode.toLaTeX()](https://reference.aspose.com/cells/javascript-cpp/equationnode/#toLaTeX--) 方法。 

以下示例代码演示如何使用 [EquationNode.toLaTeX()](https://reference.aspose.com/cells/javascript-cpp/equationnode/#toLaTeX--) 方法，并将生成的结果插入到 HTML 中：

### JavaScript 转 LaTeX

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="UTF-8" />
        <script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML"></script>
        <script type="text/x-mathjax-config">
            MathJax.Hub.Config({
                tex2jax: {
                    inlineMath: [['$','$'], ['\\(','\\)']],
                    processEscapes: true
                }
            });
        </script>
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            table { border-collapse: collapse; margin-bottom: 20px; }
            td, th { border: 1px solid #ccc; padding: 4px 8px; }
            .sheet-title { margin-top: 16px; font-weight: bold; }
            #downloadLink { display: none; margin-left: 8px; }
            #result p.error { color: red; }
            #result p.success { color: green; }
        </style>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink">Download Result</a>
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
            const resultDiv = document.getElementById('result');
            const downloadLink = document.getElementById('downloadLink');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p class="error">Please select an Excel file.</p>';
                downloadLink.style.display = 'none';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Build HTML output to display sheet names and cell values (MathJax-enabled)
            let outHtml = '';
            outHtml += '<div>';
            outHtml += '<p class="success">Workbook loaded successfully. Rendering sheet data below. Math expressions (if any) will be processed by MathJax.</p>';

            const sheetCount = workbook.worksheets.count;
            outHtml += `<p>Total sheets: ${sheetCount}</p>`;

            for (let si = 0; si < sheetCount; si++) {
                const sheet = workbook.worksheets.get(si);
                outHtml += `<div class="sheet-section">`;
                outHtml += `<div class="sheet-title">Sheet ${si + 1}: ${sheet.name}</div>`;

                // Get rows/columns counts (limited to a reasonable max to avoid huge output)
                const rows = sheet.cells.rows;
                const cols = sheet.cells.columns;
                let rowCount = rows.count || 0;
                let colCount = cols.count || 0;

                // If counts are zero, still attempt a small scan window (first 50x20)
                const MAX_ROWS = 100;
                const MAX_COLS = 50;

                if (rowCount <= 0) rowCount = Math.min(MAX_ROWS, 50);
                else rowCount = Math.min(rowCount, MAX_ROWS);

                if (colCount <= 0) colCount = Math.min(MAX_COLS, 20);
                else colCount = Math.min(colCount, MAX_COLS);

                outHtml += '<table><thead><tr><th></th>';
                for (let c = 0; c < colCount; c++) {
                    outHtml += `<th>C${c}</th>`;
                }
                outHtml += '</tr></thead><tbody>';

                for (let r = 0; r < rowCount; r++) {
                    let rowHasData = false;
                    let rowHtml = `<tr><th>R${r}</th>`;
                    for (let c = 0; c < colCount; c++) {
                        const cell = sheet.cells.get(r, c);
                        let cellText = '';
                        if (cell) {
                            // Prefer cell.value; fall back to empty string
                            const v = cell.value;
                            if (v !== undefined && v !== null) {
                                cellText = String(v);
                                rowHasData = rowHasData || (cellText.trim() !== '');
                            }
                        }
                        // Escape HTML special chars
                        cellText = cellText
                            .replace(/&/g, '&amp;')
                            .replace(/</g, '&lt;')
                            .replace(/>/g, '&gt;');

                        // Keep inline math delimiters if present so MathJax can render
                        rowHtml += `<td>${cellText}</td>`;
                    }
                    rowHtml += '</tr>';
                    // Only append rows that have any data to avoid huge empty tables
                    if (rowHasData) {
                        outHtml += rowHtml;
                    }
                }

                outHtml += '</tbody></table>';
                outHtml += `</div>`;
            }

            outHtml += '</div>';

            resultDiv.innerHTML = outHtml;

            // Trigger MathJax typeset for dynamically added content (MathJax v2 API)
            if (window.MathJax && MathJax.Hub && typeof MathJax.Hub.Queue === 'function') {
                MathJax.Hub.Queue(["Typeset", MathJax.Hub, resultDiv]);
            }

            // Prepare download of the (unmodified) workbook as an XLSX file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" });
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'inline-block';
            downloadLink.textContent = 'Download Excel File';
        });
    </script>
</html>
```

## 将公式导出为MathML表达式

如果你想将 Excel 中的方程导出为 MathML 表达式，可以使用 [EquationNode.toMathML()](https://reference.aspose.com/cells/javascript-cpp/equationnode/#toMathML--) 方法。 

以下示例代码演示如何使用 [EquationNode.toMathML()](https://reference.aspose.com/cells/javascript-cpp/equationnode/#toMathML--) 方法，并将生成的结果插入到 HTML 中：

### JavaScript 转 MathML

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Extract MathML from TextBox Equation</title>
    </head>
    <body>
        <h1>Extract MathML from TextBox Equation</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;"></a>
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

            // Access shapes from the first worksheet
            const shapes = workbook.worksheets.get(0).shapes;
            const textBox = shapes.get(0);

            if (textBox instanceof AsposeCells.TextBox) {
                const mathNode = textBox.equationParagraph.child(0);
                const mathML = mathNode.toMathML();

                const htmlContent = '<!DOCTYPE html>\r\n<html lang="en">\r\n<head>\r\n    <meta charset="UTF-8">\r\n    <title>Title</title>\r\n    <script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML"></script>\r\n</head>\r\n<body>' + mathML + '\r\n</body>\r\n</html>';

                document.getElementById('result').innerHTML = '<p style="color: green;">MathML extracted. Click the download link to save the result.html file.</p>';

                const blob = new Blob([htmlContent], { type: 'text/html' });
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = 'result.html';
                downloadLink.style.display = 'block';
                downloadLink.textContent = 'Download result.html';
            } else {
                document.getElementById('result').innerHTML = '<p style="color: red;">No TextBox with an equation was found in the first worksheet.</p>';
            }
        });
    </script>
</html>
```
