---
title: 通过JavaScript使用C++在形状的文本选项中指定东方和拉丁字体名称
linktitle: 在形状的文本选项中指定远东和拉丁文字体的名字
type: docs
weight: 1600
url: /zh/javascript-cpp/specify-the-far-east-and-latin-name-of-the-font-in-text-options-of-shape/
description: 学习如何使用Aspose.Cells for JavaScript通过C++在形状的文本选项中指定东方和拉丁字体名称。
---

## **可能的使用场景**  

有时你想用东方语言字体显示文本，例如日语、中文、泰语等。Aspose.Cells for JavaScript通过C++提供了[**TextOptions.farEastName**](https://reference.aspose.com/cells/javascript-cpp/textoptions/#farEastName--)属性，可用于指定东方语言的字体名。此外，还可以使用[**TextOptions.latinName**](https://reference.aspose.com/cells/javascript-cpp/textoptions/#latinName--)属性指定拉丁字体名。  

## **在形状的文本选项中指定远东和拉丁文字体的名字**  

以下示例代码创建了一个文本框并在其中添加一些日语文本，然后指定了文本的拉丁和远东字体名称，并将工作簿保存为[输出Excel文件](67338274.xlsx)。下方截图显示输出文本框在Microsoft Excel中的拉丁和远东字体名称。  

![todo:image_alt_text](specify-the-far-east-and-latin-name-of-the-font-in-text-options-of-shape_1.png)  

## **示例代码**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Specify Far East and Latin Name of Font in TextOptions of Shape</h1>
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
            // Create empty workbook.
            const wb = new Workbook();

            // Access first worksheet.
            const ws = wb.worksheets.get(0);

            // Add textbox inside the worksheet.
            const idx = ws.textBoxes.add(5, 5, 50, 200);
            const tb = ws.textBoxes.get(idx);

            // Set the text of the textbox.
            tb.text = "こんにちは世界";

            // Specify the Far East and Latin name of the font.
            tb.textOptions.latinName = "Comic Sans MS";
            tb.textOptions.farEastName = "KaiTi";

            // Save the output Excel file.
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSpecifyFarEastAndLatinNameOfFontInTextOptionsOfShape.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
