---
title: C++を使用したJavaScriptによるスライサーの更新
linktitle: スライサーの更新
type: docs
weight: 50
url: /ja/javascript-cpp/updating-slicer/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
description: この記事では、Aspose.Cells for JavaScript via C++を使用してスライサーを更新し、リンクされたピボットテーブルまたはテーブルのデータをフィルター処理する方法を示します。
keywords: Aspose.Cells JavaScript via C++、JavaScript スライサーの更新、JavaScriptでスライサーを変更する方法、JavaScriptでスライサーによるピボットテーブルのフィルター方法、Slicer selectItems、Slicer clearFilter、Slicer unselectItems。
---

## **可能な使用シナリオ**
スライサーの更新とは、スライサーが接続されているピボットテーブルまたはテーブルのデータをフィルター処理することを意味します。Microsoft Excelでスライサーのアイテムを選択または選択解除すると、リンクされたピボットテーブルまたはテーブルがそれに応じて再計算されます。Aspose.Cells for JavaScript via C++では、スライサーキャッシュアイテムを反復処理してスライサーを手動でリフレッシュする必要はありません。[**Slicer.selectItems(labels, append)**](https://reference.aspose.com/cells/javascript-cpp/slicer/)メソッドがスライサーを更新し、フィルターアイテムから直接、リンクされたピボットテーブルまたはテーブルを再計算します：
- `Slicer.selectItems(labels, append)` — 指定されたラベルを選択し、リンクされたピボットテーブルまたはテーブルを再計算します。`append`が`true`の場合は元々選択されていたラベルが保持され、指定されたラベルが選択に追加されます。`append`が`false`の場合は元の選択がすべてクリアされ、指定されたラベルのみが選択された状態になります。
- `Slicer.unselectItems(labels)` — 現在選択されているアイテムの一部を選択解除します。
- `Slicer.clearFilter()` — フィルターを解除してすべてのアイテムを選択します。

{{% alert color="primary" %}}
Aspose.Cells for JavaScript via C++ 26.10以降、`SlicerCacheItem.selected`プロパティは読み取り専用になり、そのセッターはサポートされなくなります。`SlicerCacheItem.selected`をアイテムごとに設定する代わりに、`Slicer.selectItems`、`Slicer.unselectItems`、`Slicer.clearFilter`メソッドを使用してください。
{{% /alert %}}

## **スライサーの更新方法**
次のサンプルコードは、ピボットテーブルに接続された既存のスライサーを含む[サンプルExcelファイル](67338475.xlsx)を読み込みます。`Slicer.selectItems(labels, false)`を使用してスライサーの"Blue"と"Pink"のアイテムのみを選択すると、ピボットテーブルはフィルターアイテムから直接再計算され、手動での`Slicer.refresh()`の呼び出しは不要です。その後、ワークブックを[出力Excelファイル](67338476.xlsx)として保存します。次のスクリーンショットは、サンプルコードがサンプルExcelファイルに与える影響を示しています。スクリーンショットでわかるように、ピボットテーブルにはフィルターされたアイテムのみが表示されます。

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

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const ws = workbook.worksheets.get(0);

            // Access the first slicer inside the slicer collection
            const slicer = ws.slicers.get(0);

            // Select only "Blue" and "Pink"; the linked pivot table or table
            // is recalculated directly from the filter items
            slicer.selectItems(["Blue", "Pink"], false);

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

現在選択されているラベルを保持したまま、さらにアイテムを選択します：

```javascript
// Keep the current selection and add "Red" to it.
slicer.selectItems(["Red"], true);
```

選択されたアイテムの一部を選択解除します：

```javascript
// Remove "Pink" from the current selection.
slicer.unselectItems(["Pink"]);
```

フィルターを解除します（すべてのアイテムを選択します）：

```javascript
// Clear the filter; all slicer items become selected again.
slicer.clearFilter();
```

{{< app/cells/assistant language="javascript-cpp" >}}