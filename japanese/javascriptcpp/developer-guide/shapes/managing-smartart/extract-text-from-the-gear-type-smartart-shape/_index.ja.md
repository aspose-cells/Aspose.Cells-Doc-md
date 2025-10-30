---
title: JavaScriptを使用してC++経由でGear Type SmartArt Shapeからテキストを抽出する
linktitle: ギア型スマートアート形状からテキストを抽出
type: docs
weight: 500
url: /ja/javascript-cpp/extract-text-from-the-gear-type-smartart-shape/
description: Aspose.Cells for JavaScriptを使用してC++経由でGear Type SmartArt Shapeからテキストを抽出する方法を学ぶ。
---

## **可能な使用シナリオ**

Aspose.CellsはGear Type Smart Art Shapeからテキストを抽出できます。そのためには、最初にSmart Art Shapeを[**Shape.resultOfSmartArt**](https://reference.aspose.com/cells/javascript-cpp/shape/#resultOfSmartArt--)プロパティを使用してGroup Shapeに変換する必要があります。その後、[**GroupShape.groupedShapes**](https://reference.aspose.com/cells/javascript-cpp/groupshape/#groupedShapes--)プロパティを使ってGroup Shapeを構成する個々のShapeの配列を取得します。最後に、ループを使ってすべての個々のShapeを逐次処理し、それらのテキストを[**Shape.text**](https://reference.aspose.com/cells/javascript-cpp/shape/#text--)プロパティで抽出できます。

## **ギアタイプのスマートアートシェイプからテキストを抽出する**

以下のサンプルコードは、上記で説明したように、Gear Type Smart Art Shapeを含む[sample Excel file](67338483.xlsx)をロードし、その個々の形状からテキストを抽出します。以下は、サンプルコードのコンソール出力です。

## **サンプルコード**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Extract Gear SmartArt Text Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet.
            const worksheet = workbook.worksheets.get(0);

            // Access first shape.
            const shape = worksheet.shapes.get(0);

            // Get the result of gear type smart art shape in the form of group shape.
            const groupShape = shape.resultOfSmartArt;

            // Get the list of individual shapes consisting of group shape.
            const shapes = groupShape.groupedShapes;

            // Extract the text of gear type shapes and display them.
            const results = [];
            for (let i = 0; i < shapes.count; i++) {
                const s = shapes.get(i);

                if (s.type === AsposeCells.AutoShapeType.Gear9 || s.type === AsposeCells.AutoShapeType.Gear6) {
                    const text = s.text;
                    results.push(text);
                    console.log("Gear Type Shape Text: " + text);
                }
            }

            if (results.length) {
                document.getElementById('result').innerHTML = '<p style="color: green;">Found gear shape texts:</p><ul>' + results.map(t => '<li>' + t + '</li>').join('') + '</ul>';
            } else {
                document.getElementById('result').innerHTML = '<p style="color: orange;">No gear type SmartArt shapes found in the first shape.</p>';
            }
        });
    </script>
</html>
```

## **コンソール出力**

{{< highlight javascript >}}

Gear Type Shape Text: Nice

Gear Type Shape Text: Good

Gear Type Shape Text: Excellent

{{< /highlight >}}
