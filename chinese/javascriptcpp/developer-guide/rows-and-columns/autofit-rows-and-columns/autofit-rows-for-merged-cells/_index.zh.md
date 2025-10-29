---
title: 通过 C++ 使用 JavaScript 自动调整合并单元格行高
linktitle: 自动调整合并单元格的行高
type: docs
weight: 120
url: /zh/javascript-cpp/autofit-rows-for-merged-cells/
description: 了解如何使用 Aspose.Cells for JavaScript 通过 C++ 为合并单元格自动调整行高。在电子表格中实现自动调整合并单元格的功能。
---

{{% alert color="primary" %}}

Microsoft Excel提供了一个功能，可以根据内容自动调整单元格的高度。该功能称为自动调整行高。Microsoft Excel不会本机设置合并单元格的自动调整操作。有时，这项功能对于真正需要在合并单元格上实现自动调整行高的用户来说是至关重要的。

{{% /alert %}}

## **如何使用AutoFitMergedCellsType自动调整行高**
Aspose.Cells for JavaScript 通过 C++ 支持此功能，借助 [**AutoFitterOptions.autoFitMergedCellsType**](https://reference.aspose.com/cells/javascript-cpp/autofitmergedcellstype/) API。使用此 API，可以在包括合并单元格的工作表中自动调整行高。以下列出了所有可能类型的合并单元格自动调整方式：

- 无
- 首行
- 末行
- 每行

## **自动调整合并单元格的行高**

 见以下代码，它创建了一个工作簿对象并添加了多个工作表。对每个工作表使用不同的方法进行自动调整。截屏显示了运行样例代码后的结果。

<br>
<img src="result.png" width=80% />

## **JavaScript 示例代码**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Autofit Merged Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, AutoFitterOptions, AutoFitMergedCellsType, Utils } = AsposeCells;

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
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Obtaining the reference of the first worksheet
            const sheet1 = workbook.worksheets.get(0);

            // Create a range A1:B2
            const range = sheet1.cells.createRange(0, 0, 2, 2);

            // Merge the cells
            range.merge();

            // Insert value to the merged cell A1
            const cell1 = sheet1.cells.get(0, 0);
            cell1.value = "A quick brown fox jumps over the lazy dog. A quick brown fox jumps over the lazy dog....end";

            // Create a style object
            const style = cell1.style;

            // Set wrapping text on
            style.isTextWrapped = true;

            // Apply the style to the cell
            cell1.style = style;

            // Create an object for AutoFitterOptions
            const options = new AutoFitterOptions();

            // Only expands the height of the first row.
            options.autoFitMergedCellsType = AutoFitMergedCellsType.FirstLine;

            // Autofit rows in the sheet (including the merged cells)
            sheet1.autoFitRows(options);

            let index = workbook.worksheets.add();
            const sheet2 = workbook.worksheets.get(index);
            sheet2.name = "Sheet2";
            // Create a range A1:B2
            const range2 = sheet2.cells.createRange(0, 0, 2, 2);

            // Merge the cells
            range2.merge();

            // Insert value to the merged cell A1
            const cell2 = sheet2.cells.get(0, 0);
            cell2.value = "A quick brown fox jumps over the lazy dog. A quick brown fox jumps over the lazy dog....end";

            // Create a style object
            const style2 = cell2.style;

            // Set wrapping text on
            style2.isTextWrapped = true;

            // Apply the style to the cell
            cell2.style = style2;

            // Create an object for AutoFitterOptions
            const options2 = new AutoFitterOptions();

            // Only expands the height of the last row.
            options2.autoFitMergedCellsType = AutoFitMergedCellsType.LastLine;

            // Autofit rows in the sheet (including the merged cells)
            sheet2.autoFitRows(options2);

            index = workbook.worksheets.add();
            const sheet3 = workbook.worksheets.get(index);
            sheet3.name = "Sheet3";
            // Create a range A1:B2
            const range3 = sheet3.cells.createRange(0, 0, 2, 2);

            // Merge the cells
            range3.merge();

            // Insert value to the merged cell A1
            const cell3 = sheet3.cells.get(0, 0);
            cell3.value = "A quick brown fox jumps over the lazy dog. A quick brown fox jumps over the lazy dog....end";

            // Create a style object
            const style3 = cell3.style;

            // Set wrapping text on
            style3.isTextWrapped = true;

            // Apply the style to the cell
            cell3.style = style3;

            // Create an object for AutoFitterOptions
            const options3 = new AutoFitterOptions();

            // Only expands the height of each row.
            options3.autoFitMergedCellsType = AutoFitMergedCellsType.EachLine;

            // Autofit rows in the sheet (including the merged cells)
            sheet3.autoFitRows(options3);

            index = workbook.worksheets.add();
            const sheet4 = workbook.worksheets.get(index);
            sheet4.name = "Sheet4";
            // Create a range A1:B2
            const range4 = sheet4.cells.createRange(0, 0, 2, 2);

            // Merge the cells
            range4.merge();

            // Insert value to the merged cell A1
            const cell4 = sheet4.cells.get(0, 0);
            cell4.value = "A quick brown fox jumps over the lazy dog. A quick brown fox jumps over the lazy dog....end";

            // Create a style object
            const style4 = cell4.style;

            // Set wrapping text on
            style4.isTextWrapped = true;

            // Apply the style to the cell
            cell4.style = style4;

            // Create an object for AutoFitterOptions
            const options4 = new AutoFitterOptions();

            // Ignore merged cells.
            options4.autoFitMergedCellsType = AutoFitMergedCellsType.None;

            // Autofit rows in the sheet (not including the merged cells)
            sheet4.autoFitRows(options4);

            // Saving the modified Excel file and creating a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
