---
title: JavaScriptを使用してC++経由の形状のテキストに事前設定されたWordArtスタイルを設定します
linktitle: シェイプのグローエフェクトの色を読み取る
type: docs
weight: 280
url: /ja/javascript-cpp/set-preset-wordart-style-to-the-text-of-the-shape/
description: C++経由のAspose.Cells for JavaScriptを使って、形のテキストに事前設定されたWordArtスタイルを設定する方法を学びます。
---

## **可能な使用シナリオ**
 C++経由のAspose.Cells for JavaScriptを使用して、形状のテキストに事前設定されたWordArtスタイルを設定できます。 [FontSetting.wordArtStyle(PresetWordArtStyle)]](https://reference.aspose.com/cells/javascript-cpp/fontsetting/#wordArtStyle-presetwordartstyle-)または [FontSettingCollection.wordArtStyle(PresetWordArtStyle)]](https://reference.aspose.com/cells/javascript-cpp/fontsettingcollection/#wordArtStyle-presetwordartstyle-)メソッドを使用してください。

## **テキストのシェイプに組み込みのWordArtスタイルを設定する**
 以下のサンプルコードは、テキストボックスを作成し、そのテキストの事前設定されたWordArtスタイルを[FontSetting.wordArtStyle(PresetWordArtStyle)]](https://reference.aspose.com/cells/javascript-cpp/fontsetting/#wordArtStyle-presetwordartstyle-)メソッドを使用して設定します。この方法で、 [出力Excelファイル](5115445.xlsx) はMicrosoft Excelで次のように見えます。

![todo:image_alt_text](set-preset-wordart-style-to-the-text-of-the-shape_1.png)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Set Preset WordArt Style</title>
    </head>
    <body>
        <h1>Set Preset WordArt Style Example</h1>
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
            const resultDiv = document.getElementById('result');

            // Create a new workbook (original JavaScript code created a new Workbook without reading a file)
            const workbook = new Workbook();

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Create a textbox with some text
            const textbox = worksheet.shapes.addTextBox(0, 0, 0, 0, 100, 700);
            textbox.text = "Aspose File Format APIs";
            textbox.font.size = 44;

            // Sets preset WordArt style to the text of the shape.
            const fntSetting = textbox.richFormattings[0];
            fntSetting.wordArtStyle = AsposeCells.PresetWordArtStyle.WordArtStyle3;

            // Save the workbook in xlsx format and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSetPresetWordArtStyle.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File with WordArt';

            resultDiv.innerHTML = '<p style="color: green;">Workbook created and ready for download.</p>';
        });
    </script>
</html>
```
