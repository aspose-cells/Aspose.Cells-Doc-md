---
title: JavaScriptを用いてExcelを開かずに固定状態を確認する方法（C++経由）
linktitle: 凍結状態
type: docs
weight: 190
url: /ja/javascript-cpp/how-to-check-frozen-state-of-excel-worksheet
description: この記事では、C++ライブラリを使用してExcelワークシートの固定状態をプログラム的に確認する方法を学びます。
---

## **紹介**

この資料では、Excelワークシートの固定状態をプログラム的に確認する方法を学びます。Microsoft Excelではシートが固定または分割されているかを簡単に確認できます。 JavaScriptで固定または分割されているかを確認する方法はありますか？C++経由のAspose.Cells for JavaScriptでこれを簡単に行えます。

## **ウィンドウペインは凍っていますか**
C++を使用したAspose.Cells for JavaScriptでウィンドウが固定されているかどうか、固定されている行と列数を確認できます。

ウィンドウのペイン状態を確認し、ロックされた行と列を取得するには、[**Worksheet.paneState**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#paneState--)プロパティを使用し、[**Worksheet.freezedPanes**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#freezedPanes--)プロパティを利用してください。
1. ファイルを開くためのワークブックを作成します。
2. ワークシートが凍結しているかどうかを確認します。
3. ロックされている行と列を取得します。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Check Frozen Panes Example</title>
    </head>
    <body>
        <h1>Check Frozen Panes Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PaneStateType, Utils } = AsposeCells;

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

            // Loading the workbook which contains frozen panes
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            const sheet = workbook.worksheets.get(0);

            // Check whether worksheet is frozen.
            const paneState = sheet.paneState;
            if (paneState === PaneStateType.Frozen || paneState === PaneStateType.FrozenSplit) {
                // Gets locked rows and columns.
                const panes = sheet.freezedPanes;
                let html = '<p style="color: green;">Worksheet has frozen panes. Details:</p><ul>';
                panes.forEach((value) => {
                    const row = value[0];
                    const column = value[1];
                    const rows = value[2];
                    const columns = value[3];
                    html += `<li>row: ${row}, column: ${column}, rows: ${rows}, columns: ${columns}</li>`;
                });
                html += '</ul>';
                document.getElementById('result').innerHTML = html;
            } else {
                document.getElementById('result').innerHTML = '<p>Worksheet is not frozen.</p>';
            }
        });
    </script>
</html>
```
