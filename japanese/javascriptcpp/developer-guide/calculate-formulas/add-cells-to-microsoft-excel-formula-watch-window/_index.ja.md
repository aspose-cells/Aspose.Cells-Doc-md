---
title: JavaScriptを介したC++を使ってMicrosoft Excelの数式ウォッチウィンドウにセルを追加する
linktitle: Microsoft Excelフォーミュラ監視ウィンドウにセルを追加する
description: Aspose.Cellsライブラリを使用してJavaScriptを介してC++でExcelの数式ウォッチウィンドウにセルを追加する方法。既存のExcelファイルを読み込むか、新しいファイルを作成し、セルを操作して数式を設定します。最後に変更したExcelファイルをディスクに保存します。
keywords: Aspose.Cells、Excel、式ウォッチウィンドウ、セル、追加、JavaScriptを介したC++
type: docs
weight: 60
url: /ja/javascript-cpp/add-cells-to-microsoft-excel-formula-watch-window/
---

## **可能な使用シナリオ**

Microsoft Excelのウォッチウィンドウは、セルの値とその式を便利に監視できるツールです。Excelで*Watch Window*を開くには、*数式 > 監視 > ウィンドウ*をクリックします。*Add Watch*ボタンでセルを検査のために追加できます。同様に、[**CellWatchCollection.add(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cellwatchcollection/#add-number-number-)メソッドを使用してAspose.Cells APIでセルを*ウォッチウィンドウ*に追加できます。

## **Microsoft Excelフォーミュラ計算エンジンのAspose.Cells**

以下のサンプルコードは、セルC1とE1の式を設定し、それらをウォッチウィンドウに追加しています。その後、ワークブックを[出力Excelファイル](67338481.xlsx)として保存します。出力Excelファイルを開き、*ウォッチウィンドウ*を確認すると、両方のセルがこのスクリーンショットのように表示されます。

![todo:image_alt_text](add-cells-to-microsoft-excel-formula-watch-window_1.png)

## **サンプルコード**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Add Cells to Formula Watch Window</h1>
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
            // This example creates a new workbook (like the original JavaScript example).
            // If a user-selected file is provided, it will be ignored for this specific example.
            if (!fileInput) {
                document.getElementById('result').innerHTML = '<p style="color: red;">File input not available.</p>';
                return;
            }

            // Instantiate a new empty workbook
            const wb = new Workbook();

            // Access first worksheet
            const ws = wb.worksheets.get(0);

            // Put some integer values in cell A1 and A2
            ws.cells.get("A1").value = 10;
            ws.cells.get("A2").value = 30;

            // Access cell C1 and set its formula
            const c1 = ws.cells.get("C1");
            c1.formula = "=Sum(A1,A2)";

            // Add cell C1 into cell watches by name
            ws.cellWatches.add(c1.name);

            // Access cell E1 and set its formula
            const e1 = ws.cells.get("E1");
            e1.formula = "=A2*A1";

            // Add cell E1 into cell watches by its row and column indices
            ws.cellWatches.add(e1.row, e1.column);

            // Save workbook to output XLSX format and provide download link
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputAddCellsToMicrosoftExcelFormulaWatchWindow.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created. Click the download link to get the file.</p>';
        });
    </script>
</html>
```
