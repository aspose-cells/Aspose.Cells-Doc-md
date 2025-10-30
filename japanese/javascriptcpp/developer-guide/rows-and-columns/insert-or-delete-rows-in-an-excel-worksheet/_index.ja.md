---
title: JavaScriptをC++経由でExcelワークシートに行を挿入または削除
linktitle: Excelワークシートで行を挿入または削除する
type: docs
weight: 20
url: /ja/javascript-cpp/insert-or-delete-rows-in-an-excel-worksheet/
description: この記事は、C++を使用したJavaScriptコードを使ってExcelワークシートに行を挿入および削除する方法を提供します。
keywords: JavaScriptを使ったExcelワークシートの行の挿入または削除、Excelへの行の挿入や削除、Excelにおける行の挿入と削除、JavaScriptを用いたExcelの行の挿入と削除、ワークシートの行の挿入または削除にJavaScriptを使用
---

{{% alert color="primary" %}}  

新しいワークシートを作成する場合や既存のワークシートを操作する場合、データに合わせて追加の行や列を追加する必要がある場合があります。その他のときには、指定された位置から行または列を削除する必要があることもあります。  

{{% /alert %}}  

C++を通じてAspose.Cells for JavaScriptは、行の挿入と削除の2つのメソッド[**Cells.insertRows(number, number, boolean)**](https://reference.aspose.com/cells/javascript-cpp/cells/#insertRows-number-number-boolean-)と[**Cells.deleteRows(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#deleteRows-number-number-)を提供します。これらのメソッドはパフォーマンスに最適化されており、非常に高速に処理を行います。  

行の挿入または削除の際は、ループ内で[**Cells.insertRow(number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#insertRow-number-)や[**Cells.deleteRow(number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#deleteRow-number-)メソッドを使用するのではなく、常に[**Cells.insertRows(number, number, boolean)**](https://reference.aspose.com/cells/javascript-cpp/cells/#insertRows-number-number-boolean-)と[**Cells.deleteRows(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#deleteRows-number-number-)メソッドを使用することを推奨します。  

Aspose.CellsはMicrosoft Excelと同様に動作します。行または列が追加されると、ワークシートの内容は下方向や右方向にシフトされます。行または列が削除されると、ワークシートの内容は上方向や左方向にシフトされます。行が追加または削除された場合、他のワークシートやセル内の参照が更新されます。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Insert and Delete Rows</title>
    </head>
    <body>
        <h1>Insert and Delete Rows Example</h1>
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

            // Instantiate a Workbook object and load the selected file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet in the book
            const sheet = workbook.worksheets.get(0);

            // Insert 10 rows at row index 2 (insertion starts at 3rd row)
            sheet.cells.insertRows(2, 10);

            // Delete 5 rows now. (8th row - 12th row)
            sheet.cells.deleteRows(7, 5);

            // Save the excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out_book1.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Rows modified successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
