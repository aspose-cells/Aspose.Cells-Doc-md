---
title: JavaScriptを使用してC++経由でシート内のShapeのテキストを回転させる方法
linktitle: ワークシート内の図形と一緒にテキストを回転する
type: docs
weight: 1300
url: /ja/javascript-cpp/rotate-text-with-shape-inside-the-worksheet/
description: C++経由のAspose.Cells for JavaScriptを使用して、Excelのシート内でShapeのテキストを回転させる方法を学びます。
---

## **可能な使用シナリオ**

Microsoft Excelを使用して任意の形状内にテキストを追加できます。非常に古いMicrosoft Excel 2003を使用して形状を追加した場合、テキストは回転しません。ただし、新しいバージョンのMicrosoft Excel（例：2007、2010、2013、2016など）を使用して形状を追加すれば、テキストも形状とともに回転します。[**ShapeTextAlignment.rotateTextWithShape**](https://reference.aspose.com/cells/javascript-cpp/shapetextalignment/#rotateTextWithShape--)プロパティを使用して、テキストが形状とともに回転するかどうかを制御できます。デフォルト値は**true**で、これはテキストが形状とともに回転することを意味しますが、**false**に設定すれば、テキストは回転しません。

## **ワークシート内の図形と一緒にテキストを回転する**

次のサンプルコードは、三角形のシェイプとそのテキストがシェイプとともに回転するサンプルExcelファイル([sample Excel file](64716896.xlsx))をロードします。Microsoft ExcelでサンプルExcelファイルを開き、三角形のシェイプを回転させると、テキストもそれに伴い回転します。次に、[**ShapeTextAlignment.rotateTextWithShape**](https://reference.aspose.com/cells/javascript-cpp/shapetextalignment/#rotateTextWithShape--) プロパティを **false** に設定し、[出力Excelファイル](64716897.xlsx)として保存します。これにより、Microsoft Excelで出力ファイルを開き三角形を回転させても、テキストは回転しません。サンプルExcelファイルに対するこのコードの効果のスクリーンショットを参照してください。

![todo:image_alt_text](rotate-text-with-shape-inside-the-worksheet_1.png)

## **サンプルコード**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Rotate Text With Shape</title>
    </head>
    <body>
        <h1>Rotate Text With Shape Example</h1>
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
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by loading the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet.
            const worksheet = workbook.worksheets.get(0);

            // Access cell B4 and add message inside it.
            const cellB4 = worksheet.cells.get("B4");
            cellB4.value = "Text is not rotating with shape because RotateTextWithShape is false.";

            // Access first shape.
            const shape = worksheet.shapes.get(0);

            // Access shape text alignment.
            const shapeTextAlignment = shape.textBody.textAlignment;

            // Do not rotate text with shape by setting RotateTextWithShape as false.
            shapeTextAlignment.rotateTextWithShape = false;

            // Saving the modified Excel file and providing download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputRotateTextWithShapeInsideWorksheet.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
