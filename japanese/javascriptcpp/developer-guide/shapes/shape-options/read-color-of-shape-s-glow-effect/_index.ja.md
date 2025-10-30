---
title: JavaScriptを使用してC++経由でシェイプのグロウ効果の色を読み取る
linktitle: 形状のグローエフェクトの色を読み取りたい場合は、{0}プロパティを使用してください。これにより、形状のグローエフェクトの色に関連するさまざまなプロパティがわかります。
type: docs
weight: 330
url: /ja/javascript-cpp/read-color-of-shape-s-glow-effect/
description: 8697720447Scriptを使用して、シェイプのグロウ効果の色を読み取る方法を学びます。 
---

## 可能な使用シナリオ

任意のシェイプの輝き効果の色を読みたい場合は、[**Shape.color**](https://reference.aspose.com/cells/javascript-cpp/gloweffect/#color--)プロパティを使用してください。これにより、シェイプの輝き効果に関連するさまざまなプロパティを見つけるのに役立ちます。

## シェイプのグローエフェクトの色を読む

参照のために、以下はサンプルコードとその [ソースエクセルファイル](22774108.xlsx) およびコンソール出力を示したスクリーンショットです。次のスクリーンショットは、Microsoft Excelで表示したときのソースエクセルファイル内の形状のグローエフェクトを示しています。

![todo:image_alt_text](read-color-of-shape-s-glow-effect_1.png)

## shapeのグロウ効果の色を読むJavaScriptコード

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Read Glow Effect Color Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Access the shape
            const shape = sheet.shapes.get(0);

            // Read the glow effect color and its various properties
            const effect = shape.glow;
            const color = effect.color;

            const colorValue = color.color;
            const colorIndex = color.colorIndex;
            const isShapeColor = color.isShapeColor;
            const transparency = color.transparency;
            const type = color.type;

            console.log("Color: " + colorValue);
            console.log("ColorIndex: " + colorIndex);
            console.log("IsShapeColor: " + isShapeColor);
            console.log("Transparency: " + transparency);
            console.log("Type: " + type);

            resultDiv.innerHTML = `
                <h2>Glow Effect Color Properties</h2>
                <ul>
                    <li><strong>Color:</strong> ${colorValue}</li>
                    <li><strong>ColorIndex:</strong> ${colorIndex}</li>
                    <li><strong>IsShapeColor:</strong> ${isShapeColor}</li>
                    <li><strong>Transparency:</strong> ${transparency}</li>
                    <li><strong>Type:</strong> ${type}</li>
                </ul>
            `;
        });
    </script>
</html>
```

## コンソール出力



{{< highlight javascript >}}

Color: Color [A=222, R=255, G=0, B=0]

ColorIndex: 16711672

IsShapeColor: True

Transparency: 0.13

Type: RGB

{{< /highlight >}}
