---
title: リンクされた図形の値をJavaScriptでC++を利用して更新
linktitle: リンクされた形状の値をリフレッシュ
type: docs
weight: 3200
url: /ja/javascript-cpp/refresh-values-of-linked-shapes/
description: C++を使用したAspose.Cells for JavaScriptでExcelのリンクされた図形の値を更新する方法を学びます。
---

{{% alert color="primary" %}}

時々、Excelファイルにリンクされた図形があり、その図形は特定のセルにリンクしています。Microsoft Excelでは、リンクされたセルの値を変更すると、リンクされた図形の値も変わります。これはAspose.Cells for JavaScriptをC++で使用してXLSまたはXLSX形式でブックを保存した場合も同様に動作します。ただし、PDFまたはHTML形式で保存したい場合は、[**ShapeCollection.updateSelectedValue()**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#updateSelectedValue--)メソッドを呼び出してリンクされた図形の値を更新する必要があります。

{{% /alert %}}

## 例

以下のスクリーンショットは、サンプルコードで使用されているソースExcelファイルを示しています。このファイルには、セルA1からE4にリンクされた画像があります。Aspose.Cellsを使ってセルB4の値を変更し、その後[**ShapeCollection.updateSelectedValue()**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#updateSelectedValue--)メソッドを呼び出して画像の値を更新し、PDF形式で保存します。

![todo:image_alt_text](refresh-values-of-linked-shapes_1.jpg)

指定されたリンク済みExcelファイル（[ソースExcelファイル](95584291.xlsx)）と出力PDF（[出力PDF](95584292.pdf)）はリンクからダウンロード可能です。

### リンクされた図形の値を更新するJavaScriptコード

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Refresh Value Of Linked Shapes Example</title>
    </head>
    <body>
        <h1>Refresh Value Of Linked Shapes Example</h1>
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

            // Create workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Change the value of cell B4
            const cell = worksheet.cells.get("B4");
            cell.value = 100;

            // Update the value of the Linked Picture which is linked to cell B4
            worksheet.shapes.updateSelectedValue();

            // Save the workbook in PDF format
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputRefreshValueOfLinkedShapes.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the PDF.</p>';
        });
    </script>
</html>
```
