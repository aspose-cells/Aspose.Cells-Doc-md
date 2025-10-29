---
title: 在使用C++中的JavaScript进行Excel转HTML时，排除未使用的样式
linktitle: 在Excel转换为HTML时排除未使用的样式
type: docs
weight: 30
url: /zh/javascript-cpp/exclude-unused-styles-during-excel-to-html-conversion/
description: 学习如何在使用Aspose.Cells for JavaScript via C++将Excel转换为HTML时排除未使用的样式。
---

## **可能的使用场景**  

 Microsoft Excel文件可能包含许多未使用的样式。当将Excel文件导出为HTML格式时，这些未使用的样式也会被导出。这可能会增加HTML的大小。您可以在将Excel文件转换为HTML的过程中排除未使用的样式，方法是设置[**HtmlSaveOptions.excludeUnusedStyles**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#excludeUnusedStyles--)属性。当将其设置为**true**时，所有未使用的样式将从输出的HTML中排除。以下截图显示了输出HTML中的一个未使用样式的示例。  

![todo:image_alt_text](exclude-unused-styles-during-excel-to-html-conversion_1.png)  

## **在将 Excel 转换为 HTML 时排除未使用的样式**  

 以下示例代码创建了一个工作簿，并且还创建了一个未使用的命名样式。由于将[**HtmlSaveOptions.excludeUnusedStyles**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#excludeUnusedStyles--)设置为**true**，此未使用的命名样式不会导出到[输出HTML](61767778.zip)。但如果将其设置为**false**，则此未使用的样式将存在于输出的HTML中，你可以在HTML标记中看到，如上方截图所示。  

## **示例代码**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Exclude Unused Styles</title>
    </head>
    <body>
        <h1>Exclude Unused Styles from Excel to HTML</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;"></a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlSaveOptions } = AsposeCells;

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

            if (fileInput.files.length > 0 && fileInput.files[0].size === 0) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select a valid Excel file.</p>';
                return;
            }

            // Instantiate workbook from selected file or create a new one
            let wb;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                wb = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                wb = new Workbook();
            }

            // Create an unused named style
            const style = wb.createStyle();
            style.name = "UnusedStyle_XXXXXXXXXXXXXX";

            // Access first worksheet
            const ws = wb.worksheets.get(0);

            // Put some value in cell C7
            const cell = ws.cells.get("C7");
            cell.value = "This is sample text.";

            // Specify html save options, we want to exclude unused styles
            const opts = new HtmlSaveOptions();
            // Comment this line to include unused styles
            opts.excludeUnusedStyles = true;

            // Save the workbook in html format
            const outputData = wb.save(SaveFormat.Html, opts);
            const blob = new Blob([outputData], { type: "text/html" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputExcludeUnusedStylesInExcelToHTML.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">HTML generated successfully. Click the download link to get the result.</p>';
        });
    </script>
</html>
```
