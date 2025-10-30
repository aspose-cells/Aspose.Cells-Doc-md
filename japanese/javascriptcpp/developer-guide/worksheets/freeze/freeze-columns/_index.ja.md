---
title: Excelワークシートの最初の列を凍結するJavaScriptを介したC++
linktitle: 列を固定する
type: docs
weight: 190
url: /ja/javascript-cpp/how-to-freeze-columns-of-excel-worksheet
description: C++を使用したAspose.Cells for JavaScriptでExcelワークシートの左列をプログラム的に固定する方法を学びましょう。
keywords: 左の列を固定、最初の列を固定、列をロックする
---

## **紹介**  

この記事では、左列を固定する方法について学びます。行内の大量のデータを扱う場合、水平にスクロールしたときに左列が見えなくなることがあります。左列を固定してロックすれば、その固定部分を見ることができ、スクロールしてもヘッダーが見えるままです。  

## **Excelでの列の固定**  

**![Excelで左列を固定する](freeze-columns.png)**  

1. 左の列を固定したい場合、その列の下の列を最初に選択します。
2. 表示 > ウィンドウ枠の固定をクリックします。
3. ドロップダウンメニューで「最初の列を固定」をクリックします。
4. 下にスクロールしても、最初の列は常に左側のビューに固定されます。

**![固定された列](frozen-columns.png)**  

ご覧の通り、最左列が固定されており、横スクロールしても最上部にロックされたままです。

列を固定すると、長いデータも心配せずに閲覧できます。

## **C++を使用したAspose.Cells for JavaScriptで列を固定する**  
C++を使用したAspose.Cells for JavaScriptで最初の列を固定するのは簡単です。  
選択した列に列を固定するには、[**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#freezePanes-number-number-number-number-)メソッドを使用してください。  
1. ファイルを開くためにワークブックを作成します。または空のファイルを作成します。
2. Worksheet.freezePanes() メソッドを使用して最初の列を固定します。
3. ファイルを保存します。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Freeze Panes Example</title>
    </head>
    <body>
        <h1>Freeze Panes Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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

            // Instantiate a new Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Freezing panes at the second column on the first worksheet
            const worksheet = workbook.worksheets.get(0);
            worksheet.freezePanes("B1", 0, 1);

            // Saving the file and preparing download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'frozen.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Frozen Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Freeze panes applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

添付 [サンプルExcelファイル](Freeze.xlsx)。
