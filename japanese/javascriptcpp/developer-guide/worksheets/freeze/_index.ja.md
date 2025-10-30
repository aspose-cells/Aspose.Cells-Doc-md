---
title: C++を使用したJavaScriptでExcelワークシートのペインを固定
linktitle: ウィンドウ枠の固定
type: docs
weight: 190
url: /ja/javascript-cpp/how-to-freeze-panes-of-excel-worksheet
description: この記事では、C++を使用してAspose.Cells for JavaScriptでExcelワークシートのペインをプログラム的に固定する方法について説明します。
keywords: ペインを固定、ウィンドウを固定。
---

## **紹介**  

この記事では、ペインを固定する方法を学びます。共通の見出しの下に大量のデータがある場合、ヘッダーがスクロールダウン時に見えなくなることがあります。このとき、ペインを固定すると、その固定部分はスクロールしても見えるままです。ヘッダー行や最初の列を簡単に見ることができます。ペインの固定と解除は、データの表示を変更せずにデータ自体を変更しません。  

## **Excelで**  

**![Excelでのウィンドウ枠の固定](Freeze-panes.png)**  

1. 固定ペインを作成したい場合は、行と列を固定します。まずセル（例：B2）を選択してください。  
2. 表示 > ウィンドウ枠の固定をクリックします。  
3. ドロップダウンメニューで、ウィンドウ枠の固定をクリックします。  
4. 下または右にスクロールすると、最初の行と列が固定されます。  

**![固定ペイン](Frozen-Panes.png)**  

ご覧のとおり、最初の行と列Aが固定されており、2行目は32、2番目に見える列はDです。  

固定ペインは、大きなデータを閲覧しながら行や列のラベルを追跡しなくても済むようにする機能です。  

## **Aspose.Cells for JavaScriptを使用したペインの固定（C++）**  
Aspose.Cells for JavaScriptを使えば簡単にペインを固定できます。 [**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#freezePanes-number-number-number-number-)メソッドを使用して選択したセルでペインを固定してください。  
1. ファイルを開くためにワークブックを作成します。または空のファイルを作成します。  
2. Worksheet.freezePanes()メソッドを使用して固定ペインを設定。  
3. ファイルを保存します。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Freeze Panes Example</title>
    </head>
    <body>
        <h1>Freeze Panes Example</h1>
        <p>Select an Excel file (Freeze.xlsx) and click "Run Example" to freeze panes at B2.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>

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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Freezing panes at the cell B2
            worksheet.freezePanes("B2", 1, 1);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'frozen.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Frozen Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Panes frozen successfully! Click the download link to get the modified file.</p>';
        });
    </script>
    </body>
</html>
```  

添付 [サンプルExcelファイル](Freeze.xlsx)。
