---
title: ShapeがSmart ArtシェイプかどうかをJavaScriptをC++で使用して判定する
linktitle: 形状がスマートアート形状かどうかの判定
type: docs
weight: 400
url: /ja/javascript-cpp/determine-if-shape-is-smart-art-shape/
description: Aspose.Cells for JavaScriptをC++経由で使用して、Excel内のシェイプがSmart Artシェイプかどうかを判定する方法を学びます。
---

## **可能な使用シナリオ**  

スマートアートシェイプは、Microsoft Excelの特殊なシェイプで、自動的に複雑な図を作成できます。Shapeがスマートアートか通常のシェイプかどうかは[**Shape.isSmartArt()**](https://reference.aspose.com/cells/javascript-cpp/shape/#isSmartArt--)プロパティを使って調査できます。  

## **シェイプがスマートアートシェイプかどうかを判定する**  

次のサンプルコードは、[サンプルExcelファイル](55541792.xlsx)を読み込み、このスクリーンショットのようにスマートアートシェイプを含みます。その後、最初のシェイプの[**Shape.isSmartArt()**](https://reference.aspose.com/cells/javascript-cpp/shape/#isSmartArt--)プロパティの値を出力します。以下にそのコンソール出力例を示します。  

![todo:image_alt_text](determine-if-shape-is-smart-art-shape_1.png)  

## **サンプルコード**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Example Title</h1>
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
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Accessing the first shape
            const shape = worksheet.shapes.get(0);

            // Determine if shape is smart art (converted to property access)
            const isSmartArt = shape.isSmartArt;

            document.getElementById('result').innerHTML = `<p>Is Smart Art Shape: ${isSmartArt}</p>`;
        });
    </script>
</html>
```  

## **コンソール出力**  

{{< highlight java >}}  

Is Smart Art Shape: True  

{{< /highlight >}}
