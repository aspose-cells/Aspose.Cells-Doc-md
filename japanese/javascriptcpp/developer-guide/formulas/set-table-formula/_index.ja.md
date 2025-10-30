---
title: JavaScriptを通じてC++で新しい行にデータを入力する間に、表またはリストオブジェクトでの式を自動的に展開する方法
linktitle: テーブルの数式を設定する
type: docs
weight: 260
url: /ja/javascript-cpp/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/
description: C++を通じてAspose.Cells for JavaScriptを使用し、新しい行にデータを入力する際に表やリストオブジェクトでの式を自動的に展開する方法を学ぶ。
---

## **可能な使用シナリオ**
時々、表やリストオブジェクトの式が新しいデータ入力時に自動的に展開されることを望むことがあります。これはMicrosoft Excelのデフォルトの動作です。C++を通じてAspose.Cells for JavaScriptで同じ機能を実現するには、[ListColumn.formula](https://reference.aspose.com/cells/javascript-cpp/listcolumn/#formula--) プロパティを使用してください。

## ** 新しい行にデータを入力しながら表またはリストオブジェクトで数式を自動的に伝播させる**
次のサンプルコードは、列Bの数式が新しいデータを入力すると自動的に新しい行に伝播するように表またはリストオブジェクトを作成します。このコードで生成された[出力エクセルファイル](5115469.xlsx)を確認してください。セルA3に数字を入力すると、セルB2の数式が自動的にセルB3に伝播するのが分かります。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells ListObject Example</h1>
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
            // Create workbook object
            const book = new Workbook();

            // Access first worksheet
            const sheet = book.worksheets.get(0);

            // Add column headings in cell A1 and B1
            sheet.cells.get(0, 0).value = "Column A";
            sheet.cells.get(0, 1).value = "Column B";

            // Add list object, set its name and style
            const listObject = sheet.listObjects.get(
                sheet.listObjects.add(0, 0, 1, sheet.cells.maxColumn, true)
            );
            listObject.tableStyleType = AsposeCells.TableStyleType.TableStyleMedium2;
            listObject.displayName = "Table";

            // Set the formula of second column so that it propagates to new rows automatically while entering data
            listObject.listColumns.get(1).formula = "=[Column A] + 1";

            // Save the workbook in xlsx format
            const outputData = book.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
