---
title: セルからテーブルをアクセスし、行と列のオフセットを使用して値を追加する方法をC++のJavaScriptを使って説明
linktitle: セルからテーブルにアクセスし、行と列のオフセットを使用して値を追加する
type: docs
weight: 230
url: /ja/javascript-cpp/accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets/
---

{{% alert color="primary" %}}  

通常、テーブルまたはリストオブジェクト内に値を追加する場合は [**Cell.putValue(boolean)**](https://reference.aspose.com/cells/javascript-cpp/cell/#putValue-boolean-) メソッドを使用します。ただし、時々、行と列のオフセットを使用してテーブルまたはリストオブジェクト内に値を追加する必要があることがあります。  

セルからテーブルまたはリストオブジェクトにアクセスするには[**Cell.table**](https://reference.aspose.com/cells/javascript-cpp/cell/#table--)プロパティを使用します。行と列のオフセットを使って値を追加するには[**ListObject.putCellValue(number, number, object)**](https://reference.aspose.com/cells/javascript-cpp/listobject/#putCellValue-number-number-object-)メソッドを使用します。  

{{% /alert %}}  

次のスクリーンショットは、コード内で使用されているソースExcelファイルを示しています。空のテーブルが含まれ、テーブル内にあるセルD5がハイライト表示されています。このテーブルには[**Cell.table**](https://reference.aspose.com/cells/javascript-cpp/cell/#table--)プロパティを使用してセルD5からアクセスし、その後、[**Cell.putValue(boolean)**](https://reference.aspose.com/cells/javascript-cpp/cell/#putValue-boolean-)と[**ListObject.putCellValue(number, number, object)**](https://reference.aspose.com/cells/javascript-cpp/listobject/#putCellValue-number-number-object-)の両方のメソッドを使用して値を追加します。  

## 例  

### ソースファイルと出力ファイルの比較のスクリーンショット  

|![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_1.png)|  
| :- |  

以下のスクリーンショットは、コードによって生成された出力エクセルファイルを示しています。セル D5 に値が設定されており、テーブル内のオフセット 2,2 のセル F6 にも値が設定されています。  

|![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_2.png)|  
| :- |  

### セルからテーブルにアクセスし、行と列のオフセットを使用して値を追加するJavaScriptコード  

以下のサンプルコードは、上記のスクリーンショットに示されているソースエクセルファイルを読み込み、テーブル内に値を追加し、それに基づいて出力エクセルファイルを生成します。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Accessing Table Example</h1>
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

            // Create workbook from uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access cell D5 which lies inside the table
            const cell = worksheet.cells.get("D5");

            // Put value inside the cell D5
            cell.value = "D5 Data";

            // Access the Table from this cell
            const table = cell.table;

            // Add some value using Row and Column Offset
            table.putCellValue(2, 2, "Offset [2,2]");

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
