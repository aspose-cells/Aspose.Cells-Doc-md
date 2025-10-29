---
title: 使用JavaScript通过C++读取支持多编码的CSV文件
linktitle: 使用多种编码方式读取CSV文件
type: docs
weight: 200
url: /zh/javascript-cpp/reading-csv-file-with-multiple-encodings/
description: 学习如何使用Aspose.Cells for JavaScript通过C++读取多编码的CSV文件。
---

{{% alert color="primary" %}}

有时，你的 CSV 文件包含多种编码（Unicode、ANSI、UTF8、UTF7 等）。Aspose.Cells 允许你加载此类 CSV 文件并将其转换为其他格式，例如 PDF 或 XLSX。

{{% /alert %}}

Aspose.Cells 提供了 [**TxtLoadOptions.isMultiEncoded()**](https://reference.aspose.com/cells/javascript-cpp/txtloadoptions/#isMultiEncoded--) 属性，你需要将其设置为 **true**，以正确加载多编码的CSV文件。

以下截图显示了一个包含两行的示例CSV文件。第一行是**ANSI**编码，第二行是**Unicode**编码

|**输入文件**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_1.png)|

以下截图显示了未将 [**TxtLoadOptions.isMultiEncoded()**](https://reference.aspose.com/cells/javascript-cpp/txtloadoptions/#isMultiEncoded--) 属性设置为 **true** 的情况下，从上述CSV文件转换的XLSX文件。可以看到，Unicode文本没有正确转换。

|**输出文件1：未对多种编码进行处理**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_2.png)|

以下截图显示了在将上述 CSV 文件转换为 XLSX 文件后，将 [**TxtLoadOptions.isMultiEncoded()**](https://reference.aspose.com/cells/javascript-cpp/txtloadoptions/#isMultiEncoded--) 属性设置为 **true**。可以看到，Unicode 文本现在被正确转换。

|**输出文件2：IsMultiEncoded设置为true**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_3.png)|

以下是将上述 CSV 文件正确转换为 XLSX 格式的示例代码。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Convert Multi-Encoded CSV to XLSX</h1>
        <input type="file" id="fileInput" accept=".csv" />
        <button id="runExample">Convert to XLSX</button>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select a CSV file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Create TxtLoadOptions and set isMultiEncoded property
            const options = new TxtLoadOptions();
            options.isMultiEncoded = true;

            // Load the CSV into a Workbook using the options
            const workbook = new Workbook(new Uint8Array(arrayBuffer), options);

            // Save the workbook to XLSX format and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            const outName = file.name.replace(/(\.[^/.]+)$/, '$1.out.xlsx');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = outName;
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Converted Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">File converted successfully! Click the download link to save the XLSX file.</p>';
        });
    </script>
</html>
```

## 相关文章

- [打开 CSV 文件](/cells/zh/javascript-cpp/opening-files-with-different-formats/#opening-csv-files)
