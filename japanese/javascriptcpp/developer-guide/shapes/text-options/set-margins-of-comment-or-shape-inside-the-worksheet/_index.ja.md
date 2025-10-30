---
title: C++経由のJavaScriptを使用して、ワークシート内のコメントやShapeのマージンを設定します。
linktitle: ワークシート内のコメントまたは図形の余白を設定する
type: docs
weight: 1500
url: /ja/javascript-cpp/set-margins-of-comment-or-shape-inside-the-worksheet/
description: Excelワークシート内のコメントまたはシェイプのマージンを設定する方法を、C++経由のAspose.Cells for JavaScriptを使用して学びます。
---

## **可能な使用シナリオ**  

Aspose.Cellsでは、[**Shape.textBody.textAlignment**](https://reference.aspose.com/cells/javascript-cpp/shapetextalignment/) プロパティを使用して、任意のShapeまたはコメントの余白を設定できます。このプロパティは [**Aspose.Cells.Drawing.Texts.ShapeTextAlignment**](https://reference.aspose.com/cells/javascript-cpp/shapetextalignment) クラスのオブジェクトを返し、上部、左、下、右の余白を設定するためにさまざまなプロパティ（例：[**ShapeTextAlignment.topMarginPt**](https://reference.aspose.com/cells/javascript-cpp/shapetextalignment/#topMarginPt--)、[**ShapeTextAlignment.leftMarginPt**](https://reference.aspose.com/cells/javascript-cpp/shapetextalignment/#leftMarginPt--)、[**ShapeTextAlignment.bottomMarginPt**](https://reference.aspose.com/cells/javascript-cpp/shapetextalignment/#bottomMarginPt--)、[**ShapeTextAlignment.rightMarginPt**](https://reference.aspose.com/cells/javascript-cpp/shapetextalignment/#rightMarginPt--)）を持ちます。  

## **ワークシート内のコメントまたは図形の余白を設定する**  

次のサンプルコードをご覧ください。二つの図形を含む[サンプルエクセルファイル](61767851.xlsx)をロードし、コードでそれぞれの図形にアクセスし、それらの上部、左側、下部、右側の余白を設定します。コードによって生成された[出力エクセルファイル](61767852.xlsx)と、出力エクセルファイルに対するコードの効果を示したスクリーンショットをご覧ください。  

![todo:image_alt_text](set-margins-of-comment-or-shape-inside-the-worksheet_1.png)  

## **サンプルコード**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Set Margins of Comment or Shape Example</title>
    </head>
    <body>
        <h1>Set Margins of Comment or Shape Inside The Worksheet</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const ws = workbook.worksheets.get(0);

            const shapes = ws.shapes;
            for (let i = 0; i < shapes.count; i++) {
                const sh = shapes.get(i);
                // Access the text alignment
                const txtAlign = sh.textBody.textAlignment;

                // Set auto margin false
                txtAlign.isAutoMargin = false;

                // Set the top, left, bottom and right margins
                txtAlign.topMarginPt = 10;
                txtAlign.leftMarginPt = 10;
                txtAlign.bottomMarginPt = 10;
                txtAlign.rightMarginPt = 10;
            }

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSetMarginsOfCommentOrShapeInsideTheWorksheet.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Margins updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
