---
title: C++経由でJavaScriptを使用したMicrosoft Excelファイルのテーブルの作成と管理
linktitle: テーブル
type: docs
weight: 150
url: /ja/javascript-cpp/create-and-format-table/
description: Aspose.Cells for JavaScriptを使用して、Excelのテーブルの挿入、リサイズ、編集、削除、および書式設定を行います。
---

## **テーブルの作成**

スプレッドシートの利点の1つは、電話リスト、タスクリスト、取引のリスト、資産リスト、負債リストなど、さまざまなタイプのリストを作成できることです。複数のユーザーが協力して、さまざまなリストを利用、作成、維持することができます。

Aspose.Cellsはリストの作成と管理をサポートしています。

### **リストオブジェクトの利点**

実際のリストオブジェクトにデータのリストを変換するときの利点はいくつかあります。

- 新しい行や列が自動的に含まれます。
- リストの最下部に合計、平均、カウントなどを表示するために総合行を簡単に追加できます。
- 右に追加された列は自動的にリストオブジェクトに取り込まれます。
- 行と列に基づくチャートは自動的に拡張されます。
- 行と列に割り当てられた名前付き範囲は自動的に拡張されます。
- リストは誤って行や列が削除されないように保護されています。

### **Microsoft Excelを使用してリストオブジェクトを作成する**

- リストオブジェクト作成のためのデータ範囲選択
- これはリスト作成ダイアログを表示します。
- データ用のリストオブジェクトを実装し、合計行を指定します（**データ**を選択し、次に**リスト**、最後に**合計行**を選択）。

### **Aspose.Cells APIを使用する**

Aspose.Cellsは、Microsoft Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)クラスを提供します。[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)クラスには、Excelファイルの各ワークシートへのアクセスを可能にする[**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--)コレクションが含まれています。

ワークシートは {0} クラスで表されます。{1} クラスは、ワークシート管理のための多くのプロパティとメソッドを提供します。ワークシート内に {2} を作成するには、{4} クラスの {3} コレクションプロパティを使用します。各 {5} は実際には {6} クラスのオブジェクトであり、さらに {7} メソッドを使用してリストオブジェクトを追加し、セル範囲を指定します。指定されたセル範囲に基づいて、Aspose.Cellsがワークシート内に {8} を作成します。属性（例えば {9}）を {10} クラスの属性として使用し、表を要件に合わせてフォーマットします。

指定されたセル範囲に基づいて、ListオブジェクトはAspose.Cellsによって作成されます。リストを制御するために[**ListObject**](https://reference.aspose.com/cells/javascript-cpp/listobject/)クラスの属性（例：[**showTotals**](https://reference.aspose.com/cells/javascript-cpp/listobject/#showTotals--)、[**listColumns**](https://reference.aspose.com/cells/javascript-cpp/listobject/#listColumns--)など）を使用してください。

以下の例では、上記のセクションでMicrosoft Excelを使用して作成したのと同じ[**ListObject**](https://reference.aspose.com/cells/javascript-cpp/listobject/)をAspose.Cells APIを使用して作成しています。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells ListObjects Example</title>
    </head>
    <body>
        <h1>ListObjects Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, TotalsCalculation } = AsposeCells;

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
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const listObjects = workbook.worksheets.get(0).listObjects;

            listObjects.add(1, 1, 7, 5, true);

            const firstList = listObjects.get(0);
            firstList.showTotals = true;

            firstList.listColumns.get(4).totalsCalculation = TotalsCalculation.Sum;

            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">List created and totals calculated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **表の書式設定**

関連するデータのグループを管理および分析するには、セル範囲をリストオブジェクト（またはExcelテーブルとも呼ばれる）に変換することができます。 テーブルは、他の行や列のデータから独立して管理される関連データを含む行と列のシリーズです。 テーブルの各列には、ヘッダー行でフィルタリングが有効になっており、リストオブジェクトデータを迅速にフィルタリングまたは並べ替えることができます。 リストオブジェクトには特別な行（数値データで作業するために有用な集計関数の選択を提供するリスト内の特別な行）を追加することができます。 Aspose.Cellsには、リスト（またはテーブル）の作成と管理のためのオプションが用意されています。

### **リストオブジェクトの書式設定**

Aspose.Cellsは、Microsoft Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)クラスを提供します。[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)クラスには、Excelファイルの各ワークシートへのアクセスを可能にする[**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--)コレクションが含まれています。

ワークシートは[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)クラスは、ワークシートの管理に役立つ幅広いプロパティとメソッドを提供します。ワークシートに[**ListObject**](https://reference.aspose.com/cells/javascript-cpp/listobject/)を作成するには、[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)クラスの[**listObjects**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#listObjects--)コレクションプロパティを使用します。各[**ListObject**](https://reference.aspose.com/cells/javascript-cpp/listobject/)は実際には[**ListObjectCollection**](https://reference.aspose.com/cells/javascript-cpp/listobjectcollection/)クラスのオブジェクトであり、さらに[**add(number, number, number, number, boolean)**](https://reference.aspose.com/cells/javascript-cpp/listobjectcollection/#add-number-number-number-number-boolean-)メソッドを提供してListオブジェクトを追加し、その範囲を指定します。指定されたセル範囲に基づいて、Aspose.Cellsはワークシートに[**ListObject**](https://reference.aspose.com/cells/javascript-cpp/listobject/)を作成します。表を要件に合わせてフォーマットするには、[**ListObject**](https://reference.aspose.com/cells/javascript-cpp/listobject/)クラスの属性（例：[**TableStyleType**](https://reference.aspose.com/cells/javascript-cpp/tablestyletype/)）を使用してください。

以下の例では、サンプルデータをワークシートに追加し、[**ListObject**](https://reference.aspose.com/cells/javascript-cpp/listobject/)を追加してデフォルトスタイルを適用します。[**ListObject**](https://reference.aspose.com/cells/javascript-cpp/listobject/)スタイルはMicrosoft Excel 2007/2010に対応しています。

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
            // This example does not require an input file; it creates a new workbook
            const workbook = new Workbook();

            // Obtaining the reference of the default(first) worksheet
            const sheet = workbook.worksheets.get(0);

            // Obtaining Worksheet's cells collection
            const cells = sheet.cells;

            // Setting the value to the cells (converted putValue -> value)
            cells.get(1, 1).value = "Employee";
            cells.get(1, 2).value = "Quarter";
            cells.get(1, 3).value = "Product";
            cells.get(1, 4).value = "Continent";
            cells.get(1, 5).value = "Country";
            cells.get(1, 6).value = "Sale";

            cells.get(2, 1).value = "David";
            cells.get(3, 1).value = "David";
            cells.get(4, 1).value = "David";
            cells.get(5, 1).value = "David";
            cells.get(6, 1).value = "James";
            cells.get(7, 1).value = "James";
            cells.get(8, 1).value = "James";
            cells.get(9, 1).value = "James";
            cells.get(10, 1).value = "James";
            cells.get(11, 1).value = "Miya";
            cells.get(12, 1).value = "Miya";
            cells.get(13, 1).value = "Miya";
            cells.get(14, 1).value = "Miya";
            cells.get(15, 1).value = "Miya";
            cells.get(2, 2).value = 1;
            cells.get(3, 2).value = 2;
            cells.get(4, 2).value = 3;
            cells.get(5, 2).value = 4;
            cells.get(6, 2).value = 1;
            cells.get(7, 2).value = 2;
            cells.get(8, 2).value = 3;
            cells.get(9, 2).value = 4;
            cells.get(10, 2).value = 4;
            cells.get(11, 2).value = 1;
            cells.get(12, 2).value = 1;
            cells.get(13, 2).value = 2;
            cells.get(14, 2).value = 2;
            cells.get(15, 2).value = 2;

            cells.get(2, 3).value = "Maxilaku";
            cells.get(3, 3).value = "Maxilaku";
            cells.get(4, 3).value = "Chai";
            cells.get(5, 3).value = "Maxilaku";
            cells.get(6, 3).value = "Chang";
            cells.get(7, 3).value = "Chang";
            cells.get(8, 3).value = "Chang";
            cells.get(9, 3).value = "Chang";
            cells.get(10, 3).value = "Chang";
            cells.get(11, 3).value = "Geitost";
            cells.get(12, 3).value = "Chai";
            cells.get(13, 3).value = "Geitost";
            cells.get(14, 3).value = "Geitost";
            cells.get(15, 3).value = "Geitost";

            cells.get(2, 4).value = "Asia";
            cells.get(3, 4).value = "Asia";
            cells.get(4, 4).value = "Asia";
            cells.get(5, 4).value = "Asia";
            cells.get(6, 4).value = "Europe";
            cells.get(7, 4).value = "Europe";
            cells.get(8, 4).value = "Europe";
            cells.get(9, 4).value = "Europe";
            cells.get(10, 4).value = "Europe";
            cells.get(11, 4).value = "America";
            cells.get(12, 4).value = "America";
            cells.get(13, 4).value = "America";
            cells.get(14, 4).value = "America";
            cells.get(15, 4).value = "America";

            cells.get(2, 5).value = "China";
            cells.get(3, 5).value = "India";
            cells.get(4, 5).value = "Korea";
            cells.get(5, 5).value = "India";
            cells.get(6, 5).value = "France";
            cells.get(7, 5).value = "France";
            cells.get(8, 5).value = "Germany";
            cells.get(9, 5).value = "Italy";
            cells.get(10, 5).value = "France";
            cells.get(11, 5).value = "U.S.";
            cells.get(12, 5).value = "U.S.";
            cells.get(13, 5).value = "Brazil";
            cells.get(14, 5).value = "U.S.";
            cells.get(15, 5).value = "U.S.";

            cells.get(2, 6).value = 2000;
            cells.get(3, 6).value = 500;
            cells.get(4, 6).value = 1200;
            cells.get(5, 6).value = 1500;
            cells.get(6, 6).value = 500;
            cells.get(7, 6).value = 1500;
            cells.get(8, 6).value = 800;
            cells.get(9, 6).value = 900;
            cells.get(10, 6).value = 500;
            cells.get(11, 6).value = 1600;
            cells.get(12, 6).value = 600;
            cells.get(13, 6).value = 2000;
            cells.get(14, 6).value = 500;
            cells.get(15, 6).value = 900;

            // Adding a new List Object to the worksheet
            const index = sheet.listObjects.add("A1", "F15", true);

            const listObject = sheet.listObjects.get(index);

            // Adding Default Style to the table (converted setter -> property)
            listObject.tableStyleType = AsposeCells.TableStyleType.TableStyleMedium10;

            // Show Total
            listObject.showTotals = true;

            // Set the Quarter field's calculation type (converted getter/setter -> property)
            listObject.listColumns.get(1).totalsCalculation = AsposeCells.TotalsCalculation.Count;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and table added successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **高度なトピック**
- [テーブルをODSに変換する](/cells/ja/javascript-cpp/convert-table-to-ods/)
- [外部データ接続に関連するクエリテーブルとリストオブジェクトを見つける](/cells/ja/javascript-cpp/find-query-tables-and-list-objects-related-to-external-data-connections/)
- [クエリテーブルデータソースを持つテーブルの読み書き](/cells/ja/javascript-cpp/read-and-write-table-with-query-table-data-source/)
- [ワークシート内のテーブルまたはリストオブジェクトのコメントを設定してください](/cells/ja/javascript-cpp/set-the-comment-of-table-or-list-object-inside-the-worksheet/)
- [表と範囲](/cells/ja/javascript-cpp/tables-and-ranges/)
