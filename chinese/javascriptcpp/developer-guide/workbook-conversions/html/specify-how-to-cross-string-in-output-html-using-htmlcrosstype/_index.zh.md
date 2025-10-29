---
title: 指定如何在输出 HTML 中交叉字符串，使用 HtmlCrossType 结合 JavaScript 通过 C++
linktitle: 使用HtmlCrossType指定输出HTML中如何交叉字符串
type: docs
weight: 140
url: /zh/javascript-cpp/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/
description: 学习如何通过 Aspose.Cells for JavaScript 使用 C++ 通过指定 HtmlCrossType 控制 HTML 输出中的字符串溢出。
---

## **可能的使用场景**

当单元格含文本或字符串，但其长度超过单元格宽度时，如果下一列的单元格为空，字符串会溢出。保存Excel为HTML时，可以通过指定交叉类型（[**HtmlCrossType**](https://reference.aspose.com/cells/javascript-cpp/htmlcrosstype)枚举）控制此溢出。其值包括：

- **HtmlCrossType.Default**：显示方式类似MS Excel；依赖下一单元格。如果下一单元格为空，字符串将会超出或被截断。

- **HtmlCrossType.MSExport**: 以MS Excel导出HTML的方式显示字符串.

- **HtmlCrossType.Cross**：显示 HTML 交叉字符串；创建大型 HTML 文件的性能比设置为 Default 或 FitToCell 快十倍以上。

- **HtmlCrossType.FitToCell**：仅在单元格宽度内显示字符串。

## **使用HtmlCrossType指定输出HTML中如何交叉字符串**

以下示例代码加载[示例Excel文件](51740732.xlsx)，并通过指定不同的[**HtmlCrossType**](https://reference.aspose.com/cells/javascript-cpp/htmlcrosstype)将其保存为HTML格式。请下载由此代码生成的[输出HTML](51740734.zip)。示例Excel文件包含一个以红色边框标记的图片，如此截图所示，展示了[**HtmlCrossType**](https://reference.aspose.com/cells/javascript-cpp/htmlcrosstype)值对输出HTML的影响。

![todo:image_alt_text](specify-how-to-cross-string-in-output-html-using-htmlcrosstype_1.png)

## **示例代码**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Export HTML Cross String Type Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlSaveOptions, HtmlCrossType, Utils } = AsposeCells;

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

            // Specify HTML Cross Type via HtmlSaveOptions
            const opts = new HtmlSaveOptions();
            // Applying the sequence of assignments as in the original JavaScript code
            opts.htmlCrossStringType = HtmlCrossType.Default;
            opts.htmlCrossStringType = HtmlCrossType.MSExport;
            opts.htmlCrossStringType = HtmlCrossType.Cross;
            opts.htmlCrossStringType = HtmlCrossType.FitToCell;

            // Save workbook to HTML using the specified options
            const outputData = workbook.save(SaveFormat.Html, opts);
            const blob = new Blob([outputData], { type: "text/html" });
            const downloadLink = document.getElementById('downloadLink');
            const fileName = 'out' + opts.htmlCrossStringType + '.htm';
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = fileName;
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">HTML exported successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
