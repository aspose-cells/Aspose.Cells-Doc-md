---
title: 在导出电子表格为CSV格式时，使用JavaScript via C++修剪前导空白行和列
linktitle: 导出电子表格到CSV格式时修剪前导空白行和列
type: docs
weight: 100
url: /zh/javascript-cpp/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/
description: 学习如何在使用Aspose.Cells for JavaScript via C++导出电子表格为CSV格式时修剪前导空白行和列。
---

## **可能的使用场景**

有时，您的Excel或CSV文件具有前导空白列或行。例如，考虑这条线

{{< highlight javascript >}}

 ,,,data1,data2

{{< /highlight >}}

这里的前三个单元格或列是空白的。当您在Microsoft Excel中打开这样的CSV文件时，Microsoft Excel会丢弃这些前导空白行和列。

默认情况下，Aspose.Cells for JavaScript via C++在保存时不会丢弃前导空白列和行，但如果您想像微软Excel那样移除它们，则Aspose.Cells提供[**TxtSaveOptions.trimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/javascript-cpp/txtsaveoptions/#trimLeadingBlankRowAndColumn--)属性。请将其设置为**true**，然后所有前导空白行和列将在保存时被丢弃。

{{% alert color="primary" %}}

在发布Aspose.Cells for JavaScript via C++ 20.4之前，[**TxtSaveOptions.trimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/javascript-cpp/txtsaveoptions/#trimLeadingBlankRowAndColumn--)的默认值为**false**。自20.4版本起，[**TxtSaveOptions.trimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/javascript-cpp/txtsaveoptions/#trimLeadingBlankRowAndColumn--)的默认值为**true**。

{{% /alert %}}

## **导出电子表格到CSV格式时修剪前导空白行和列**

以下示例代码加载了具有两个前导空白列的【源 Excel 文件】（sampleTrimBlankColumns.xlsx）。它首先不做任何更改地将 Excel 文件保存为 CSV 格式，然后将 [**TxtSaveOptions.trimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/javascript-cpp/txtsaveoptions/#trimLeadingBlankRowAndColumn--) 属性设置为 **true**，再次保存。屏幕截图显示【源 Excel 文件】（sampleTrimBlankColumns.xlsx）、【不修剪空白列的输出 CSV 文件】（outputWithoutTrimBlankColumns.csv）以及【修剪空白列的输出 CSV 文件】（outputTrimBlankColumns.csv）。

![todo:image_alt_text](trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format_1.png)

## **示例代码**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Trim Blank Columns</title>
    </head>
    <body>
        <h1>Trim Blank Columns Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink1" style="display: none;">Download Result 1</a>
        <a id="downloadLink2" style="display: none; margin-left: 10px;">Download Result 2</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, TxtSaveOptions, Utils } = AsposeCells;

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
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Load source workbook
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Save in csv format (without trimming)
            const outputData1 = wb.save(SaveFormat.Csv);
            const blob1 = new Blob([outputData1]);
            const downloadLink1 = document.getElementById('downloadLink1');
            downloadLink1.href = URL.createObjectURL(blob1);
            downloadLink1.download = 'outputWithoutTrimBlankColumns.csv';
            downloadLink1.style.display = 'inline-block';
            downloadLink1.textContent = 'Download CSV Without Trimming';

            // Now save again with TrimLeadingBlankRowAndColumn as true
            const opts = new TxtSaveOptions();
            opts.trimLeadingBlankRowAndColumn = true;

            // Save in csv format (with trimming)
            const outputData2 = wb.save(opts);
            const blob2 = new Blob([outputData2]);
            const downloadLink2 = document.getElementById('downloadLink2');
            downloadLink2.href = URL.createObjectURL(blob2);
            downloadLink2.download = 'outputTrimBlankColumns.csv';
            downloadLink2.style.display = 'inline-block';
            downloadLink2.textContent = 'Download CSV With Trimmed Blank Columns';

            resultDiv.innerHTML = '<p style="color: green;">Files generated. Use the links above to download the CSVs.</p>';
        });
    </script>
</html>
```
