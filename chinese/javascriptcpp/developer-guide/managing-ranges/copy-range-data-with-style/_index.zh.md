---
title: 使用 JavaScript 复制带样式的范围数据，通过 C++
linktitle: 仅复制范围数据和样式
type: docs
weight: 610
url: /zh/javascript-cpp/copy-range-data-with-style/
description: 学习如何使用 C++ 中的脚本复制带格式的单元格范围。
---

{{% alert color="primary" %}}

[仅复制范围数据](/cells/zh/javascript-cpp/copy-range-data-only/) 说明了如何将一个范围的单元格数据复制到另一个范围。具体来说，它为复制的单元格应用一套新的样式。Aspose.Cells 也可以复制完整带格式的范围。本文将进行说明。

{{% /alert %}}

Aspose.Cells 提供了一套用于操作范围的类和方法，例如 [**createRange(string, string)**](https://reference.aspose.com/cells/javascript-cpp/cells/#createRange-string-string-), [**StyleFlag**](https://reference.aspose.com/cells/javascript-cpp/styleflag/) 和 [**applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/javascript-cpp/cells/#applyStyle-style-styleflag-)。

此示例：

1. 创建一个工作簿。  
2. 在第一个工作表中填充多个单元格数据。  
3. 创建一个 [**Range**](https://reference.aspose.com/cells/javascript-cpp/range/)。  
4. 使用指定的格式属性创建一个 [**Style**](https://reference.aspose.com/cells/javascript-cpp/style/) 对象。  
5. 将样式应用到数据范围。  
6. 创建第二个单元格范围。  
7. 将第一个范围的带格式数据复制到第二个范围。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Copy Range Example</h1>
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
            if (fileInput.files.length && fileInput.files[0]) {
                // If a file is provided, open it and modify
            } else {
                // No file provided, will create a new workbook
            }

            // Instantiate or load workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Get the first Worksheet Cells.
            const cells = workbook.worksheets.get(0).cells;

            // Fill some sample data into the cells.
            for (let i = 0; i < 50; i++) {
                for (let j = 0; j < 10; j++) {
                    cells.get(i, j).value = `${i},${j}`;
                }
            }

            // Create a range (A1:D3).
            const range = cells.createRange("A1", "D3");

            // Create a style object.
            let style = workbook.createStyle();
            // Specify the font attribute.
            style.font.name = "Calibri";
            // Specify the shading color.
            style.foregroundColor = AsposeCells.Color.Yellow;
            style.pattern = AsposeCells.BackgroundType.Solid;
            // Specify the border attributes.
            style.borders.get(AsposeCells.BorderType.TopBorder).lineStyle = AsposeCells.CellBorderType.Thin;
            style.borders.get(AsposeCells.BorderType.TopBorder).color = AsposeCells.Color.Blue;
            style.borders.get(AsposeCells.BorderType.BottomBorder).lineStyle = AsposeCells.CellBorderType.Thin;
            style.borders.get(AsposeCells.BorderType.BottomBorder).color = AsposeCells.Color.Blue;
            style.borders.get(AsposeCells.BorderType.LeftBorder).lineStyle = AsposeCells.CellBorderType.Thin;
            style.borders.get(AsposeCells.BorderType.LeftBorder).color = AsposeCells.Color.Blue;
            style.borders.get(AsposeCells.BorderType.RightBorder).lineStyle = AsposeCells.CellBorderType.Thin;
            style.borders.get(AsposeCells.BorderType.RightBorder).color = AsposeCells.Color.Blue;

            // Create the styleflag object.
            const flag1 = new AsposeCells.StyleFlag();
            // Implement font attribute
            flag1.fontName = true;
            // Implement the shading / fill color.
            flag1.cellShading = true;
            // Implement border attributes.
            flag1.borders = true;
            // Set the Range style.
            range.applyStyle(style, flag1);

            // Create a second range (C10:F12).
            const range2 = cells.createRange("C10", "F12");

            // Copy the range data with formatting.
            range2.copy(range);

            // Save the excel file.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'CopyRange.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
