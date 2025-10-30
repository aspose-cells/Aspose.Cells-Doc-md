---
title: JavaScriptを使用した範囲の書式設定（C++経由）
linktitle: 範囲の書式設定
type: docs
weight: 105
url: /ja/javascript-cpp/how-to-format-a-range/
description: Excelでセル範囲を書式設定する方法をAspose.Cells for JavaScriptをC++で学びましょう。
---

## **可能な使用シナリオ**  
範囲にスタイルを適用する必要がある場合は、範囲の書式設定を使用できます。  

## **Excelでの範囲の書式設定方法**  

Excelで範囲の書式を設定するには、Excelが提供する組み込みの書式設定オプションを使用します。Excelで範囲の書式を設定する方法は以下の通りです:  

1. Excelを開き、書式を設定したい範囲が含まれているワークブックを開きます。  

2. 書式を設定したい範囲を選択します。範囲を選択するには、範囲をクリックしてドラッグするか、ショートカットキーであるシフト+矢印キーを使用して選択を拡張することができます。  

3. 範囲が選択されたら、選択した範囲を右クリックし、コンテキストメニューから「セルの書式設定」を選択します。または、Excelリボンのホームタブに移動し、「セル」グループの「書式」ドロップダウンをクリックし、「セルの書式設定」を選択します。  

4. 「セルの書式設定」ダイアログボックスが表示されます。ここで、選択した範囲に適用するさまざまな書式設定オプションを選択できます。たとえば、フォントスタイル、フォントサイズ、フォント色、数値形式、罫線、背景色などを変更できます。 ダイアログボックス内の異なるタブを探索して、さまざまな書式設定オプションにアクセスできます。  

5.所望の書式設定を行った後、選択した範囲に書式を適用するには、「OK」ボタンをクリックします。  

## **JavaScriptを使用した範囲の書式設定方法**  

C++を使用して範囲を書式設定するには、次の方法を利用できます：  
1. [Range.applyStyle(スタイル, フラグ)](https://reference.aspose.com/cells/javascript-cpp/range/#applyStyle-style-styleflag-)  
2. [Range.style](https://reference.aspose.com/cells/javascript-cpp/range/#style-style-)  
3. [Range.style](https://reference.aspose.com/cells/javascript-cpp/range/#style-style-)  

## **サンプルコード**  
この例では、Excelワークブックを作成し、サンプルデータを追加し、最初のワークシートにアクセスし、2つの範囲("A1:C3"および"A4:C5")を定義します。次に、新しいスタイルを作成し、さまざまな書式設定オプション(たとえば、フォントの色、太字)を設定し、範囲にスタイルを適用します。最後に、ワークブックを新しいファイルとして保存します。  
<br>  
![todo:image_alt_text](format-range.png)  

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

            // Create the workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet
            const ws = workbook.worksheets.get(0);

            const cells = ws.cells;

            // Setting the value to the cells (converted putValue -> value)
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

            // Access the worksheet (already have ws, but keep variable for clarity)
            const worksheet = workbook.worksheets.get(0);

            // Define the range
            const range = worksheet.cells.createRange("A1:C3");

            // Apply formatting to the range
            const style = workbook.createStyle();
            style.font.color = AsposeCells.Color.Red;
            style.font.isBold = true;

            const flag = new AsposeCells.StyleFlag();
            flag.font = true;
            range.applyStyle(style, flag);

            // Define the range
            const range2 = worksheet.cells.createRange("A4:C5");

            // Apply formatting to the range
            const style2 = workbook.createStyle();
            style2.font.color = AsposeCells.Color.Blue;
            style2.font.isItalic = true;
            range2.setStyle(style2);

            // Save the modified workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook modified successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
