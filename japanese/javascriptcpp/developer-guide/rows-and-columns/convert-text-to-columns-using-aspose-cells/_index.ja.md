---
title: Aspose.Cells for JavaScriptを使ったテキストの列への変換
linktitle: テキストを列に変換
type: docs
weight: 30
url: /ja/javascript-cpp/convert-text-to-columns-using-aspose-cells/
description: Excelでのテキストを列に変換する方法を学びます（C++経由のAspose.Cells for JavaScript使用）
---

## **可能な使用シナリオ**  

Microsoft Excelを使用してテキストを列に変換できます。この機能は、「データ」タブの「データツール」から利用可能です。列の内容を複数の列に分割するには、カンマ（または他の文字）などの区切り文字を含む必要があります。その基準に基づき、Microsoft Excelはセルの内容を複数のセルに分割します。C++を用いたAspose.Cells for JavaScriptもこの機能を[**Cells.textToColumns(number, number, number, TxtLoadOptions)**](https://reference.aspose.com/cells/javascript-cpp/cells/#textToColumns-number-number-number-txtloadoptions-)で提供します。  

## **Aspose.Cells for JavaScriptを使ったテキストの列への変換（C++経由）**  

以下のサンプルコードは[**Cells.textToColumns(number, number, number, TxtLoadOptions)**](https://reference.aspose.com/cells/javascript-cpp/cells/#textToColumns-number-number-number-txtloadoptions-)メソッドの使い方を説明します。最初のワークシートのA列に人名を追加し、名字と名前はスペースで区切っています。その後、A列に対して[**Cells.textToColumns(number, number, number, TxtLoadOptions)**](https://reference.aspose.com/cells/javascript-cpp/cells/#textToColumns-number-number-number-txtloadoptions-)メソッドを適用し、出力Excelファイルに保存します。もし[出力Excelファイル](25395213.xlsx)を開けば、名前がA列に、苗字がB列に表示されているのが確認できます。  

![todo:image_alt_text](convert-text-to-columns-using-aspose-cells_1.png)  

## **サンプルコード**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Text to Columns Example</h1>
        <p>Select an optional Excel file to start from, or leave empty to create a new workbook.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, TxtLoadOptions, Utils } = AsposeCells;

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

            // Basic validation only: file is optional
            let workbook;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                // Create a new workbook if no file is provided
                workbook = new Workbook();
            }

            // Access first worksheet.
            const ws = workbook.worksheets.get(0);

            // Add people name in column A. First name and last name are separated by space.
            ws.cells.get("A1").value = "John Teal";
            ws.cells.get("A2").value = "Peter Graham";
            ws.cells.get("A3").value = "Brady Cortez";
            ws.cells.get("A4").value = "Mack Nick";
            ws.cells.get("A5").value = "Hsu Lee";

            // Create text load options with space as separator.
            const opts = new TxtLoadOptions();
            opts.separator = ' ';

            // Split the column A into two columns using TextToColumns() method.
            // Now column A will have first name and column B will have second name.
            ws.cells.textToColumns(0, 0, 5, opts);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputTextToColumns.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
