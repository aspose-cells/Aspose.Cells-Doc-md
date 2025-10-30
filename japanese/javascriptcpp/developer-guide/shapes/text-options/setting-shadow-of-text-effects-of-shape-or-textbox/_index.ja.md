---
title: C++経由でJavaScriptを使用してShapeやTextBoxの文字効果の影を設定します。
linktitle: シェイプまたはテキストボックスのテキスト効果の影の設定
type: docs
weight: 250
url: /ja/javascript-cpp/setting-shadow-of-text-effects-of-shape-or-textbox/
description: 任意のShapeやTextBoxの文字効果の影を設定する方法を、C++経由のAspose.Cells for JavaScriptを使用して学びます。
---

{{% alert color="primary" %}}  

どのシェイプまたはテキストボックスの「テキスト効果」のシャドウを設定できます。[**Shape.textBody**](https://reference.aspose.com/cells/javascript-cpp/shape/#textBody--)プロパティを使用してください。これはシェイプのテキスト設定を示し、[**FontSetting**](https://reference.aspose.com/cells/javascript-cpp/fontsetting)オブジェクトを返します。それにアクセスした後、[**FontSetting.presetType**](https://reference.aspose.com/cells/javascript-cpp/shadoweffect/#presetType--) プロパティを通じて**Shadow**を設定してください。このプロパティは [**PresetShadowType**](https://reference.aspose.com/cells/javascript-cpp/presetshadowtype) 型で、いくつかの値を持ちます。  

- DiagonalBottomRightのOffset  
- ボトムのオフセット  
- DiagonalTopRightのOffset  
- 左内部  
- 中央内部  
- PerspectiveDiagonalUpperLeft  
- PerspectiveDiagonalLowerRight  

{{% /alert %}}  

以下のコードスニペットは、[**FontSetting.presetType**](https://reference.aspose.com/cells/javascript-cpp/shadoweffect/#presetType--) プロパティを使用してShapeまたはTextBoxのテキスト効果のシャドウを設定する例です。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells: Set Text Effects Shadow of Shape or Textbox</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PresetShadowType, Color } = AsposeCells;

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
            // Create workbook object
            const wb = new Workbook();

            // Access first worksheet
            const ws = wb.worksheets.get(0);

            // Add text box with these dimensions
            const tb = ws.shapes.addTextBox(2, 0, 2, 0, 100, 400);

            // Set the text of the textbox
            tb.text = "This text has the following settings.\n\nText Effects > Shadow > Offset Bottom";

            // Set all the text runs shadow to preset offset bottom
            const textBody = tb.textBody;
            for (let i = 0; i < textBody.count; i++) {
                const textRun = textBody.get(i);
                textRun.textOptions.shadow.presetType = PresetShadowType.OffsetBottom;
            }

            // Set the font color and size of the textbox
            tb.font.color = Color.Red;
            tb.font.size = 16;

            // Save the output file
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSettingTextEffectsShadowOfShapeOrTextbox.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created. Click the download link to get the file.</p>';
        });
    </script>
</html>
```
