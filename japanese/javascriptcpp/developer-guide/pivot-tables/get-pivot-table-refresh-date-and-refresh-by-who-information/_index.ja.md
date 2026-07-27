---
title: ピボットテーブルのリフレッシュ日時とリフレッシュ実行者情報の取得
type: docs
weight: 100
url: /ja/javascript-cpp/get-pivot-table-refresh-date-and-refresh-by-who-information/
description: Aspose.Cells for JavaScriptを使用してピボットテーブルの更新日時と更新者情報を取得する方法。
keywords: Excel、Excel JavaScriptライブラリを用いたAspose.Cells for JavaScriptによるピボットテーブルの更新日時と更新者情報の取得。
---

{{% alert color="primary" %}}

 現在、Aspose.Cells for JavaScriptはワークブックからの更新日時および更新者情報の取得に対応しています。

{{% /alert %}}

## **ピボットテーブルの更新日付と更新者情報を取得する方法**
[**PivotTable.refreshDate**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#refreshDate--)はピボットテーブルレポートが最後に更新された日付を返します。同様に、[**PivotTable.refreshedByWho**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#refreshedByWho--)プロパティはレポートを最後に更新したユーザーの名前を返します。以下の例はこの機能をデモンストレーションし、サンプルファイルは以下のリンクからダウンロードできます。

[SourcePivotTable.xlsx](77496335.xlsx)

**サンプルコード**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Pivot Table Info</title>
    </head>
    <body>
        <h1>Pivot Table Information</h1>
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

            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            const worksheet = workbook.worksheets.get(0);
            const pivotTable = worksheet.pivotTables.get(0);

            const refreshedByWho = pivotTable.refreshedByWho;
            const refreshDate = pivotTable.refreshDate;

            console.log("Pivot table refresh by who = " + refreshedByWho);
            console.log("Pivot table refresh date = " + refreshDate);

            document.getElementById('result').innerHTML = `
                <p>Pivot table refresh by who = ${refreshedByWho}</p>
                <p>Pivot table refresh date = ${refreshDate}</p>
            `;
        });
    </script>
</html>
```
