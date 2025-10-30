---
title: JavaScriptを使用してC++経由で範囲の境界線を設定
linktitle: 範囲のボーダーを設定
type: docs
weight: 600
url: /ja/javascript-cpp/set-range-border/
---

## **可能な使用シナリオ**  
範囲の境界線を設定したい場合、各セルを個別に設定する必要はありません。範囲に対して境界線を設定できます。C++を通じてAspose.Cells for JavaScriptはこの機能を提供します。  
この記事は、C++を使用してAspose.Cells for JavaScriptで範囲の境界線を設定するサンプルコードを提供します。  

## **Excelで範囲のボーダーを設定する**  
Excelで範囲のボーダーを設定するには、次の手順に従います:  
1. ボーダーを適用する範囲のセルを選択します。  
2. リボンの「ホーム」タブに移動し、「フォント」グループを検索します。  
3. 「フォント」グループ内で、「ボーダー」ドロップダウンボタンをクリックします。  
<br>  
<img src="border.png" />  
4. ドロップダウンメニュー内のオプションから適用するボーダーの種類を選択します。プリセットのボーダースタイルを選択するか、独自のボーダーをカスタマイズすることができます。  
5. 希望のボーダースタイルを選択したら、そのボーダーが選択したセル範囲に適用されます。  

## **C++を通じてAspose.Cells for JavaScriptを使用して範囲の境界線を設定**  
この例では、次のことができます:  

1. ワークブックを作成する。  
2. 最初のワークシートのセルにデータを追加します。  
3. [**Range**](https://reference.aspose.com/cells/javascript-cpp/range)を作成します。  
4. 範囲の内側の境界線を設定します。  
5. 範囲の外側の境界線を設定します。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Create Workbook Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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
            // Instantiate a new workbook
            const workbook = new Workbook();
            // Obtaining the reference of the newly added worksheet
            const ws = workbook.worksheets.get(0);
            const cells = ws.cells;

            // Setting the value to the cells
            let cell = cells.get("A1");
            cell.putValue("Fruit");
            cell = cells.get("B1");
            cell.putValue("Count");
            cell = cells.get("C1");
            cell.putValue("Price");

            cell = cells.get("A2");
            cell.putValue("Apple");
            cell = cells.get("A3");
            cell.putValue("Mango");
            cell = cells.get("A4");
            cell.putValue("Blackberry");
            cell = cells.get("A5");
            cell.putValue("Cherry");

            cell = cells.get("B2");
            cell.putValue(5);
            cell = cells.get("B3");
            cell.putValue(3);
            cell = cells.get("B4");
            cell.putValue(6);
            cell = cells.get("B5");
            cell.putValue(4);

            cell = cells.get("C2");
            cell.putValue(5);
            cell = cells.get("C3");
            cell.putValue(20);
            cell = cells.get("C4");
            cell.putValue(30);
            cell = cells.get("C5");
            cell.putValue(60);

            // Create a range (A1:C5).
            const range = cells.createRange("A1", "C5");

            // set inner border of range
            const innerColor = workbook.createCellsColor();
            innerColor.color = AsposeCells.Color.Red;
            range.insideBorders = {
                borderType: AsposeCells.BorderType.Vertical,
                cellBorderType: AsposeCells.CellBorderType.Thin,
                color: innerColor
            };
            innerColor.color = AsposeCells.Color.Green;
            range.insideBorders = {
                borderType: AsposeCells.BorderType.Horizontal,
                cellBorderType: AsposeCells.CellBorderType.Thin,
                color: innerColor
            };

            // set outer border of range
            const outerColor = workbook.createCellsColor();
            outerColor.color = AsposeCells.Color.Blue;
            range.outlineBorders = {
                cellBorderType: AsposeCells.CellBorderType.Thin,
                color: outerColor
            };

            // Saving the modified Excel file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
