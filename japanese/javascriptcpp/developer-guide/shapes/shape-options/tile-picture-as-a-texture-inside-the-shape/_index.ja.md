---
title: C++経由のJavaScriptを使って、シェイプ内にタイル状に画像をテクスチャとして貼り付ける方法を学びます。
linktitle: シェイプ内のテクスチャとして画像をタイル状に配置
type: docs
weight: 1700
url: /ja/javascript-cpp/tile-picture-as-a-texture-inside-the-shape/
description: シェイプ内に小さな画像をテクスチャとしてタイル貼りする方法をAspose.Cells for JavaScriptを使用して学びます。
---

## **可能な使用シナリオ**  

画像が小さく、品質を失うことなく形状の全体の表面をカバーしない場合、タイリングするオプションがあります。タイリングは、タイルであるかのように小さな画像で形状の表面を埋めるものです。  

## **画像を形状の内部にテクスチャとしてタイル状にする**  

画像をシェイプの表面に塗りつけて、[**Shape.isTiling()**](https://reference.aspose.com/cells/javascript-cpp/texturefill/#isTiling--)プロパティをtrueに設定してタイル貼りできます。以下のサンプルコードと、それに付随する[サンプルExcelファイル](46465050.xlsx)およびスクリーンショットを参照してください。  

## **スクリーンショット**  

![todo:image_alt_text](tile-picture-as-a-texture-inside-the-shape_1.png)  

## **サンプルコード**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Texture Fill IsTiling Example</title>
    </head>
    <body>
        <h1>Texture Fill IsTiling Example</h1>
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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Accessing the first shape inside the worksheet
            const shape = worksheet.shapes.get(0);

            // Tile Picture as a Texture inside the Shape
            shape.fill.textureFill.isTiling = true;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputTextureFill_IsTiling.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Texture fill set to tiling. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
