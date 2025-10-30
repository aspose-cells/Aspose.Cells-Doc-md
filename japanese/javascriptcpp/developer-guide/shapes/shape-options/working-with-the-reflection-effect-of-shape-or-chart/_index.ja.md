---
title: ShapeまたはChartのリフレクション効果で操作
linktitle: 図形またはグラフの反射効果の操作
type: docs
weight: 210
url: /ja/javascript-cpp/working-with-the-reflection-effect-of-shape-or-chart/
description: シェイプやチャートの反射効果をC++経由のAspose.Cells for JavaScriptを使って操作する方法を学びます。望ましい結果を得るためにさまざまな反射プロパティを設定します。
---

## **可能な使用シナリオ**
Aspose.Cells for JavaScriptは、C++を介して[Shape.reflection](https://reference.aspose.com/cells/javascript-cpp/shape/#reflection--)プロパティと[ReflectionEffect](https://reference.aspose.com/cells/javascript-cpp/reflectioneffect)クラスを提供し、シェイプやチャートの反射効果を操作します。[ReflectionEffect](https://reference.aspose.com/cells/javascript-cpp/reflectioneffect)クラスには、アプリケーションの要件に応じて異なる結果を得るために設定できる次のプロパティが含まれています。

- [ReflectionEffect.blur](https://reference.aspose.com/cells/javascript-cpp/reflectioneffect/#blur--)
- [ReflectionEffect.direction](https://reference.aspose.com/cells/javascript-cpp/reflectioneffect/#direction--)
- [ReflectionEffect.distance](https://reference.aspose.com/cells/javascript-cpp/reflectioneffect/#distance--)
- [ReflectionEffect.fadeDirection](https://reference.aspose.com/cells/javascript-cpp/reflectioneffect/#fadeDirection--)
- [ReflectionEffect.rotWithShape](https://reference.aspose.com/cells/javascript-cpp/reflectioneffect/#rotWithShape--)
- [ReflectionEffect.size](https://reference.aspose.com/cells/javascript-cpp/reflectioneffect/#size--)
- [ReflectionEffect.transparency](https://reference.aspose.com/cells/javascript-cpp/reflectioneffect/#transparency--)
- [ReflectionEffect.type](https://reference.aspose.com/cells/javascript-cpp/reflectioneffect/#type--)

## **図形またはグラフの反射効果の操作**
次のサンプルコードは[ソースExcelファイル](5115424.xlsx)を読み込み、デフォルトシートの最初のシェイプにアクセスします。[Shape.reflection](https://reference.aspose.com/cells/javascript-cpp/shape/#reflection--)のさまざまなプロパティを設定し、その後ワークブックを[出力Excelファイル](5115423.xlsx)に保存します。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Set Shape Reflection Effect Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;"></a>
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

            // Instantiating a Workbook object by loading the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access first shape
            const shape = worksheet.shapes.get(0);

            // Set the reflection effect of the shape, set its Blur, Size, Transparency and Distance properties
            const reflectionEffect = shape.reflection;
            reflectionEffect.blur = 30;
            reflectionEffect.size = 90;
            reflectionEffect.transparency = 0;
            reflectionEffect.distance = 80;

            // Save the workbook in xlsx format
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Reflection effect updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
