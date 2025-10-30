---
title: セルの形式を変更
linktitle: セルの形式を変更
description: JavaScript経由のAspose.Cellsライブラリを使用してセルのフォーマット（フォント、色、境界線など）を変更する方法。これらのプロパティを調整することで、セルの外観をより詳細に制御できます。
keywords: Aspose.Cells、セルのフォーマット、JavaScriptをC++経由、フォント、色、境界線
type: docs
weight: 20
url: /ja/javascript-cpp/how-to-change-format-of-cell/
---

## **可能な使用シナリオ**
特定のデータを強調表示したい場合、セルのスタイルを変更できます。

## **Excelのセルのフォーマットを変更する方法**

Excelの単一のセルのフォーマットを変更するには、次の手順に従います。

1. Excelを開き、セルのフォーマットを変更したいワークブックを開きます。

2. フォーマットを変更したいセルを見つけます。

3. セルを右クリックして、コンテキストメニューから"セルの書式設定"を選択します。または、セルを選択し、Excelリボンのホームタブに移動し、"セル"グループの"書式"ドロップダウンをクリックし、「セルの書式設定」を選択することもできます。

4. 「セルの書式設定」ダイアログボックスが表示されます。ここでは、選択したセルに適用するさまざまな書式オプションを選択できます。たとえば、フォントスタイル、フォントサイズ、フォントの色、数値形式、罫線、背景色などを変更できます。ダイアログボックスのさまざまなタブを探索して、さまざまな書式オプションにアクセスできます。

5. 所望の書式設定変更を行った後、「OK」ボタンをクリックして、選択したセルに書式を適用します。


## **JavaScriptを使用してセルのフォーマットを変更する方法**

Aspose.Cellsを使ってセルの書式を変更するには、以下の方法を使用できます：
1. [Cell.style(Style)](https://reference.aspose.com/cells/javascript-cpp/cell/#style-style-)
2. [Cell.style(Style, explicitFlag)](https://reference.aspose.com/cells/javascript-cpp/cell/#style-style-boolean-)
3. [Cell.style(Style, StyleFlag)](https://reference.aspose.com/cells/javascript-cpp/cell/#style-style-styleflag-)


## **サンプルコード**
この例では、Excelワークブックを作成し、サンプルデータを追加し、最初のワークシートにアクセスして、「A2」と「B3」の2つのセルを取得します。その後、セルのスタイルを取得し、フォント色や太字などさまざまな書式設定を行い、セルのフォーマットを変更します。最後に、新しいファイルとしてワークブックを保存します。
![todo:image_alt_text](change-format.png)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
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
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet
            const ws = workbook.worksheets.get(0);
            const cells = ws.cells;

            // Setting the value to the cells
            let cell = cells.get("A1");
            cell.value = "Fruit";
            cell = cells.get("B1");
            cell.value = "Count";
            cell = cells.get("C1");
            cell.value = "Price";

            cell = cells.get("A2");
            cell.value = "Apple";
            cell = cells.get("A3");
            cell.value = "Mango";
            cell = cells.get("A4");
            cell.value = "Blackberry";
            cell = cells.get("A5");
            cell.value = "Cherry";

            cell = cells.get("B2");
            cell.value = 5;
            cell = cells.get("B3");
            cell.value = 3;
            cell = cells.get("B4");
            cell.value = 6;
            cell = cells.get("B5");
            cell.value = 4;

            cell = cells.get("C2");
            cell.value = 5;
            cell = cells.get("C3");
            cell.value = 20;
            cell = cells.get("C4");
            cell.value = 30;
            cell = cells.get("C5");
            cell.value = 60;

            // Access the worksheet
            const worksheet = workbook.worksheets.get(0);

            const a2 = worksheet.cells.get("A2");

            // Get style of A2
            const style = a2.style;

            // Change the format
            style.font.color = AsposeCells.Color.Red;
            style.font.isBold = true;

            const flag = new AsposeCells.StyleFlag();
            flag.fontColor = true;
            // Apply style (assignment per conversion rules)
            a2.style = style;

            const b3 = worksheet.cells.get("B3");
            // Get style of B3
            const style2 = b3.style;

            // Change the format
            style2.font.color = AsposeCells.Color.Blue;
            style2.font.isItalic = true;
            b3.style = style2;

            // Saving the modified workbook and offering it for download
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
