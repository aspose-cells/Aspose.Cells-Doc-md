---
title: C++を使用したJavaScriptによるスライサーの更新
linktitle: スライサーの更新
type: docs
weight: 50
url: /ja/javascript-cpp/updating-slicer/
description: この記事では、C++のAspose.Cells for Javaスクリプトを使用してスライサーを更新し、リンクされたピボットテーブルを更新する方法を紹介します。
keywords: Aspose.Cells JavaScriptをC++で使用し、スライサーの更新、JavaScriptでのスライサーの変更方法、JavaScriptでのスライサーの調整方法、JavaScriptを通じてスライサーのアイテムの選択・解除方法について。
---

## **可能な使用シナリオ**

Microsoft Excelでスライサーを更新したい場合は、そのアイテムを選択または選択解除し、それに応じてスライサーテーブルまたはピボットテーブルが更新されます。Aspose.Cellsを使用してスライサーアイテムを選択または選択解除し、その後[**Slicer.slicerCacheItems**](https://reference.aspose.com/cells/javascript-cpp/slicercache/#slicerCacheItems--)を呼び出してスライサーまたはピボットテーブルを更新してください。

## **スライサーの更新方法**

次のサンプルコードは、既存のスライサーを含む [サンプルExcelファイル](67338475.xlsx) を読み込みます。スライサーの2番目と3番目の項目を選択解除し、スライサーを更新します。それからワークブックを[出力Excelファイル](67338476.xlsx)として保存します。スクリーンショットには、サンプルコードがサンプルExcelファイルに与えた影響が示されています。スクリーンショットでは、選択された項目を持つスライサーを更新することでピボットテーブルも更新されていることがわかります。

![todo:image_alt_text](updating-slicer_1.png)

## **サンプルコード**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Update Slicer</title>
    </head>
    <body>
        <h1>Update Slicer Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
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

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const ws = workbook.worksheets.get(0);

            // Access the first slicer inside the slicer collection
            const slicer = ws.slicers.get(0);

            // Access the slicer items via slicer cache
            const items = slicer.slicerCache.slicerCacheItems;

            // Iterate items and deselect "Pink" and "Green"
            for (let i = 0; i < items.count; i++) {
                const item = items.get(i);
                if (item.value === "Pink" || item.value === "Green") {
                    item.selected = false;
                }
            }

            // Refresh slicer to apply changes
            slicer.refresh();

            // Save modified workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Slicer updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
