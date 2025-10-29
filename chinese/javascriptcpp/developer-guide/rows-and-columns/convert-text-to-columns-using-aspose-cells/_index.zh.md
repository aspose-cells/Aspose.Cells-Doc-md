---
title: 使用Aspose.Cells for JavaScript通过C++将文本转换为列。
linktitle: 将文本转换为列
type: docs
weight: 30
url: /zh/javascript-cpp/convert-text-to-columns-using-aspose-cells/
description: 学习如何使用Aspose.Cells for JavaScript通过C++在Excel中将文本转换为列。
---

## **可能的使用场景**  

可以使用Microsoft Excel将文本转换为列。此功能在*数据工具*下的*数据*标签中提供。为了将一列内容拆分为多列，数据中应包含特定分隔符（如逗号或其他字符），Microsoft Excel会根据此分隔符将单元格内容拆分成多个单元格。Aspose.Cells for JavaScript通过C++也提供了此功能。  

## **使用Aspose.Cells for JavaScript通过C++将文本转换为列。**  

以下示例代码说明了 [**Cells.textToColumns(number, number, number, TxtLoadOptions)**](https://reference.aspose.com/cells/javascript-cpp/cells/#textToColumns-number-number-number-txtloadoptions-) 方法的用法。代码首先在第一个工作表的 A 列添加一些人名。名和姓用空格字符分隔。然后对 A 列应用 [**Cells.textToColumns(number, number, number, TxtLoadOptions)**](https://reference.aspose.com/cells/javascript-cpp/cells/#textToColumns-number-number-number-txtloadoptions-) 方法，并将结果保存为输出的 Excel 文件。如果你打开 [输出 Excel 文件](25395213.xlsx)，会看到名字在 A 列，姓在 B 列，如截图所示。  

![todo:image_alt_text](convert-text-to-columns-using-aspose-cells_1.png)  

## **示例代码**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Text to Columns Example</h1>
        <p>Select an optional Excel file to start from, or leave empty to create a new workbook.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, TxtLoadOptions, Utils } = AsposeCells;

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

            // Basic validation only: file is optional
            let workbook;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                // Create a new workbook if no file is provided
                workbook = new Workbook();
            }

            // Access first worksheet.
            const ws = workbook.worksheets.get(0);

            // Add people name in column A. First name and last name are separated by space.
            ws.cells.get("A1").value = "John Teal";
            ws.cells.get("A2").value = "Peter Graham";
            ws.cells.get("A3").value = "Brady Cortez";
            ws.cells.get("A4").value = "Mack Nick";
            ws.cells.get("A5").value = "Hsu Lee";

            // Create text load options with space as separator.
            const opts = new TxtLoadOptions();
            opts.separator = ' ';

            // Split the column A into two columns using TextToColumns() method.
            // Now column A will have first name and column B will have second name.
            ws.cells.textToColumns(0, 0, 5, opts);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputTextToColumns.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
