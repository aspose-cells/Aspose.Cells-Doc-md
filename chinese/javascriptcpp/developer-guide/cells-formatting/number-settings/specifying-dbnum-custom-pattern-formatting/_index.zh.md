---
title: 指定使用DBNum自定义模式格式
linktitle: 指定使用DBNum自定义模式格式
description: Aspose.Cells是一个支持用自定义格式模式格式化日期和数字的JavaScript/C++库。本文展示了如何使用 dbnum 自定义格式模式以更好地控制数字显示。
keywords: Aspose.Cells，JavaScript via C++，电子表格，自定义格式模式，格式化， dbnum ，控制显示
type: docs
weight: 110
url: /zh/javascript-cpp/specifying-dbnum-custom-pattern-formatting/
---

## **可能的使用场景**

Aspose.Cells for JavaScript通过C++支持*DBNum*自定义模式。例如，如果你的单元格值是123，并将其自定义格式指定为[DBNum2][$-804]常规，则显示为壹佰贰拾叁。你可以使用[**Cell.style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style--)方法和[**Style.custom(string)**](https://reference.aspose.com/cells/javascript-cpp/style/#custom-string-)方法为单元格指定自定义格式。

## **示例代码**

以下示例代码演示如何指定*DBNum*自定义格式。请查看其[输出PDF](43352081.pdf)获取更多帮助。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - DBNum Custom Formatting Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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

            // Create or load workbook
            let workbook;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access first worksheet.
            const ws = workbook.worksheets.get(0);

            // Access cell A1 and put value 123.
            const cell = ws.cells.get("A1");
            cell.value = 123;

            // Access cell style.
            const st = cell.style;

            // Specifying DBNum custom pattern formatting.
            st.custom = "[DBNum2][$-804]General";

            // Set the cell style.
            cell.style = st;

            // Set the first column width.
            ws.cells.columns.get(0).width = 30;

            // Save the workbook in output pdf format.
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: "application/pdf" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputDBNumCustomFormatting.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the PDF.</p>';
        });
    </script>
</html>
```
