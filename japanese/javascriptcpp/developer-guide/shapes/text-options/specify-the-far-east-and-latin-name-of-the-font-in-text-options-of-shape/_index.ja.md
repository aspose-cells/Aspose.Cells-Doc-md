---
title: ShapeのテキストオプションでFar EastとLatinのフォント名を指定する方法（JavaScript/C++）
linktitle: テキストオプションのフォントの遠隔地およびラテン名を指定する
type: docs
weight: 1600
url: /ja/javascript-cpp/specify-the-far-east-and-latin-name-of-the-font-in-text-options-of-shape/
description: ShapeのテキストオプションでFar EastとLatinのフォント名を指定する方法（C++/Aspose.Cells for JavaScriptを使用）を学びます。
---

## **可能な使用シナリオ**  

時には、日本語、中国語、タイ語などのFar East言語フォントでテキストを表示したい場合があります。C++経由のAspose.Cells for JavaScriptは、Far East言語のフォント名を指定できる[**TextOptions.farEastName**](https://reference.aspose.com/cells/javascript-cpp/textoptions/#farEastName--)プロパティを提供しています。さらに、[**TextOptions.latinName**](https://reference.aspose.com/cells/javascript-cpp/textoptions/#latinName--)プロパティを使用してLatinフォント名も指定できます。  

## **テキストオプションのフォントの遠隔地およびラテン名を指定する**  

次のサンプルコードは、テキストボックスを作成し、その中に日本語のテキストを追加します。次に、テキストのラテンフォント名と東アジアフォント名を指定し、ワークブックを[出力Excelファイル](67338274.xlsx)として保存します。以下のスクリーンショットは、Microsoft Excelで出力されたテキストボックスのラテンと東アジアフォント名を示しています。  

![todo:image_alt_text](specify-the-far-east-and-latin-name-of-the-font-in-text-options-of-shape_1.png)  

## **サンプルコード**  

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
