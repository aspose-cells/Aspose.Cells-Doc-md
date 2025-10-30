---
title: Smart Artをグループシェイプに変換するJavaScriptをC++で使用
linktitle: スマートアートをグループ形状に変換
type: docs
weight: 200
url: /ja/javascript-cpp/convert-the-smart-art-to-group-shape/
---

## **可能な使用シナリオ**

 [**Shape.resultOfSmartArt**](https://reference.aspose.com/cells/javascript-cpp/shape/#resultOfSmartArt--)メソッドを使用して、スマートアートシェイプをグループシェイプに変換できます。これにより、スマートアートシェイプをグループシェイプのように扱うことができ、個々の一部分やシェイプにアクセスできるようになります。

## **スマートアートをグループシェイプに変換する**

次のサンプルコードは、[サンプルExcelファイル](55541793.xlsx)を読み込み、このスクリーンショットのようにスマートアートシェイプを含みます。その後、スマートアートシェイプをグループシェイプに変換し、Shape.isGroupプロパティを出力します。以下にそのコンソール出力例を示します。

![todo:image_alt_text](convert-the-smart-art-to-group-shape_1.png)

## **サンプルコード**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Get Result Of SmartArt</title>
    </head>
    <body>
        <h1>Get Result Of SmartArt Example</h1>
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
            const resultDiv = document.getElementById('result');
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object using the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Accessing the first shape
            const shape = worksheet.shapes.get(0);

            // Determine if shape is smart art (property access, not method)
            const isSmartArt = shape.isSmartArt;

            // Determine if shape is group shape (property access)
            const isGroup = shape.isGroup;

            // Convert smart art shape into group shape result and check if group (getResultOfSmartArt -> resultOfSmartArt property)
            const resultOfSmartArtIsGroup = shape.resultOfSmartArt.isGroup;

            const html = [
                `<p>Is Smart Art Shape: ${isSmartArt}</p>`,
                `<p>Is Group Shape: ${isGroup}</p>`,
                `<p>Result of SmartArt is Group: ${resultOfSmartArtIsGroup}</p>`
            ].join('');

            resultDiv.innerHTML = html;
        });
    </script>
</html>
```

## **コンソール出力**

{{< highlight javascript >}}

Is Smart Art Shape: True

Is Group Shape: False

Is Group Shape: True

{{< /highlight >}}
