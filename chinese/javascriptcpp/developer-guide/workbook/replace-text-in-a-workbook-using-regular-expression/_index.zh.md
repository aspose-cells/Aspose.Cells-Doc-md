---
title: 使用 JavaScript 通过 C++ 使用正则表达式替换工作簿中的文本
linktitle: 使用正则表达式在工作簿中替换文本
type: docs
weight: 90
url: /zh/javascript-cpp/replace-text-in-a-workbook-using-regular-expression/
description: 使用 C++ 通过 JavaScript 在工作簿中使用正则表达式替换文本
---

Aspose.Cells 提供通过正则表达式替换工作簿中内容的功能。为此，API 提供 [**ReplaceOptions.regexKey**](https://reference.aspose.com/cells/javascript-cpp/replaceoptions/#regexKey--) 属性在 [**ReplaceOptions**](https://reference.aspose.com/cells/javascript-cpp/replaceoptions) 类中。将 [**ReplaceOptions.regexKey**](https://reference.aspose.com/cells/javascript-cpp/replaceoptions/#regexKey--) 设置为 **true** 表示搜索的关键词将作为正则表达式处理。

以下代码片段演示了如何使用[**ReplaceOptions.regexKey**](https://reference.aspose.com/cells/javascript-cpp/replaceoptions/#regexKey--)属性，配合[示例Excel文件](101089318.xlsx)。生成的[输出文件](101089319.xlsx)已附带供参考。

## **示例代码**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Regex Replace Example</title>
    </head>
    <body>
        <h1>Regex Replace Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ReplaceOptions } = AsposeCells;

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

            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const replaceOptions = new ReplaceOptions();
            replaceOptions.caseSensitive = false;
            replaceOptions.matchEntireCellContents = false;
            replaceOptions.regexKey = true;

            workbook.replace("\\bKIM\\b", "^^^TIM^^^", replaceOptions);

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'RegexReplace_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Regex replace completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
