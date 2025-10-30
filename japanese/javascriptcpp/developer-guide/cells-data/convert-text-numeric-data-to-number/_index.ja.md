---
title: テキスト数値データを数値に変換する
type: docs
weight: 900
url: /ja/javascript-cpp/convert-text-numeric-data-to-number/
description: Excelでテキストとして保存されている数字を数字に変換する方法を学びます。
keywords: Excelのテキストを数値に変換する、JavaScriptコードを使用したテキスト数字データを数値に変換する、数値テキストを数値に変換するJavaScriptコード、JavaScriptコードで数値テキストを数値に変換するなど。
---

## **可能な使用シナリオ**
時には、入力された数値データをテキストから数値に変換したい場合があります。Microsoft Excelでは、数字の前にアポストロフィを付けて入力することで、数字を文字列として扱います。例えば**'12345**。これにより、Excelはその数字を文字列として扱います。Aspose.Cells for JavaScript via C++は文字列を数値に変換することを可能にします。


## Excel でテキストとして保存されている数値を数値に変換する方法
いくつかの簡単な手順に従うことで、テキストとして保存された数値を数値に変換できます。
1. 左上隅にエラーインジケータが付いた単一のセルまたはセル範囲を選択します。
1. 選択したセルまたはセル範囲の隣に表示されるエラーボタンをクリックします。メニューで、**数値に変換**をクリックします。 
<br>
<img src="4.png" width=70% />
1. アラートボタンが利用できない場合は、この問題がある列を選択します。全列を変換したくない場合は、代わりに1つ以上のセルを選択できます。ただし、選択したセルが同じ列にあることを確認してください。そうでないと、このプロセスは機能しません。テキストを列分割ボタンは通常、列を分割するために使用されますが、単一のテキスト列を数値に変換するためにも使用できます。データタブで、テキストを列分割をクリックしてください。
<br>
<img src="1.png" width=70% />
1. ポップアップボックスの「完了」ボタンをクリックします。
<br>
<img src="2.png" width=70% />
1. テキストとして保存されている数値が数値に変換されます。
<br>
<img src="3.png" width=70% />

## Aspose.Cells for JavaScript via C++を使ったテキストとして保存された数字を数値に変換する方法
Aspose.Cells for JavaScript via C++は、すべての文字列またはテキスト型の数値データを数値に変換するために[**Cells.convertStringToNumericValue()**](https://reference.aspose.com/cells/javascript-cpp/cells/#convertStringToNumericValue--)メソッドを提供します。

次のスクリーンショットは、セル **A1:A17** に文字列の数値を示しています。文字列の数値は左寄せされています。
<br>
<img src="5.png" width=70% />

次のスクリーンショットでは、[**Cells.convertStringToNumericValue()**](https://reference.aspose.com/cells/javascript-cpp/cells/#convertStringToNumericValue--) を使用して文字列の数値を数値に変換しました。これらは今、右寄せになっています。
<br>
<img src="6.png" width=70% />

## 文字列の数値を実際の数値に変換するJavaScriptコード

以下のサンプルコードは、すべてのワークシートの文字列数値データを実際の数値に変換する方法を示しています。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Strings to Numeric Values in All Sheets</h1>
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

            // Instantiate workbook object with the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access worksheets collection
            const sheets = workbook.worksheets;
            const sheetcount = sheets.count;

            // Iterate through all worksheets and convert strings to numeric values
            for (let i = 0; i < sheetcount; i++) {
                const sheet = sheets.get(i);
                sheet.cells.convertStringToNumericValue();
            }

            // Save the modified workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
