---
title: 使用JavaScript通过C++添加带有内置样式的字图文字
linktitle: 添加具有内置样式的艺术字文本
type: docs
weight: 270
url: /zh/javascript-cpp/add-word-art-text-with-built-in-styles/
description: 学习如何使用Aspose.Cells for JavaScript通过C++添加带有内置样式的字图文字，在Excel中创建具有视觉吸引力的文本
---

## **可能的使用场景**
您可以使用Aspose.Cells for JavaScript通过C++添加带有内置样式的字图文字。请使用 [ShapeCollection.addWordArt()](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addWordArt-presetwordartstyle-string-number-number-number-number-number-number-) 方法。

## **添加具有内置样式的艺术字文本**
以下示例代码使用不同的内置样式添加Word Art文本。请使用[code]output excel file[/code]检查使用此代码生成的[输出excel文件](5115470.xlsx)。这是[输出excel文件](5115470.xlsx)在Microsoft Excel中的外观。

![todo:image_alt_text](add-word-art-text-with-built-in-styles_1.png)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Add WordArt Example</title>
    </head>
    <body>
        <h1>Add WordArt Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PresetWordArtStyle } = AsposeCells;

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
            if (fileInput.files.length === 0) {
                // If no file selected, create a new workbook
                var workbook = new Workbook();
            } else {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                var workbook = new Workbook(new Uint8Array(arrayBuffer));
            }

            // Ensure at least one worksheet exists
            if (workbook.worksheets.count === 0) {
                workbook.worksheets.add();
            }

            // Access first worksheet
            const ws = workbook.worksheets.get(0);

            // Add Word Art Text with Built-in Styles
            ws.shapes.addWordArt(PresetWordArtStyle.WordArtStyle1, "Aspose File Format APIs", 0, 0, 0, 0, 100, 800);
            ws.shapes.addWordArt(PresetWordArtStyle.WordArtStyle2, "Aspose File Format APIs", 10, 0, 0, 0, 100, 800);
            ws.shapes.addWordArt(PresetWordArtStyle.WordArtStyle3, "Aspose File Format APIs", 20, 0, 0, 0, 100, 800);
            ws.shapes.addWordArt(PresetWordArtStyle.WordArtStyle4, "Aspose File Format APIs", 30, 0, 0, 0, 100, 800);
            ws.shapes.addWordArt(PresetWordArtStyle.WordArtStyle5, "Aspose File Format APIs", 40, 0, 0, 0, 100, 800);

            // Save the workbook in xlsx format
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">WordArt added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
