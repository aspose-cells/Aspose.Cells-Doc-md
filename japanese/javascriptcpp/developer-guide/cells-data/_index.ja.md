---
title: Excelファイルのデータ管理
linktitle: セルのデータ
type: docs
weight: 110
url: /ja/javascript-cpp/view-and-edit-excel-data/
description: この記事では、Aspose.Cellsを使用したJavaScript経由のExcelファイルのデータ表示・編集方法について説明します。
keywords: Aspose.Cells JavaScript経由のC++を使ったExcelファイルのデータ管理、データ追加、データ取得、効率的なデータ追加、セルデータの管理、セルデータの更新、セルデータの取得、セルの挿入方法
---

{{% alert color="primary" %}}

[ワークシートのセルアクセス](/cells/ja/javascript-cpp/accessing-cells-of-a-worksheet/)で、セルにアクセスする基本的な方法について説明しました。この記事では、その方法の一つを使い、さまざまなタイプのデータをセルに追加します。

{{% /alert %}}

## **セルにデータを追加する方法**

C++を経由したスクリプトは、Microsoft Excelファイルを表すクラス**[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)**を提供します。**[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)**クラスは、Excelファイル内の各ワークシートにアクセスできる**[**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--)**コレクションを持ちます。ワークシートは**[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)**クラスによって表されます。**[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)**クラスは、**[**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--)**コレクションを提供します。**[**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--)**コレクションの各アイテムは、**[**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell)**クラスのオブジェクトを表します。

Aspose.Cellsでは、[**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell)クラスの[**putValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#putValue-boolean-)メソッドを呼び出すことで、ワークシートのセルにデータを追加可能です。Aspose.Cellsは、[**putValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#putValue-boolean-)メソッドのオーバーロード版を提供しており、さまざまな種類のデータ（ブール値、文字列、倍精度浮動小数点、整数、日時など）をセルに追加できます。

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
            // If a file is provided, open it; otherwise create a new workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Obtaining the reference of the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Adding values to cells
            const cells = worksheet.cells;
            const cellA1 = cells.get("A1");
            cellA1.value = "Hello World";

            const cellA2 = cells.get("A2");
            cellA2.value = 20.5;

            const cellA3 = cells.get("A3");
            cellA3.value = 15;

            const cellA4 = cells.get("A4");
            cellA4.value = true;

            const cellA5 = cells.get("A5");
            cellA5.value = new Date();

            // Setting the display format of the date
            let style = cellA5.style;
            style.number = 15;
            cellA5.style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created/modified successfully. Click the download link to get the file.</p>';
        });
    </script>
</html>
```


## **効率を向上させる方法**

大量のデータをシートに配置する場合は、まず行ごとに値を追加し、その後列に追加すると効率が大幅に向上します。

## **セルからデータを取得する方法**

Aspose.Cells for JavaScript via C++は、Microsoft Excelファイルを表すクラス[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)を提供します。[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)クラスは、ファイル内のワークシートにアクセスできる[**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--)コレクションを含んでいます。ワークシートは、[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)クラスによって表されます。[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)クラスは[**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--)コレクションを提供します。[**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--)コレクションの各アイテムは、[**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell)クラスのオブジェクトを表します。

[**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell)クラスは、データタイプに応じたセルの値を取得するいくつかのプロパティを提供します。これらのプロパティには：

- [**stringValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#stringValue--): セルの文字列値を返します。
- [**doubleValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#doubleValue--): セルの倍精度値を返します。
- [**boolValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#boolValue--): セルのブール値を返します。
- [**dateTimeValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#dateTimeValue--): セルの日時値を返します。
- [**floatValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#floatValue--): セルの浮動小数点値を返します。
- [**intValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#intValue--): セルの整数値を返します。

フィールドが未入力の場合、[**doubleValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#doubleValue--)または[**floatValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#floatValue--)を持つセルは例外をスローします。

セルに含まれるデータタイプは、[**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell)クラスの[**type**](https://reference.aspose.com/cells/javascript-cpp/cell/#type--)メソッドを使用しても確認できます。実際、[**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell)クラスの[**type**](https://reference.aspose.com/cells/javascript-cpp/cell/#type--)メソッドは、以下にリストされた事前定義済みの値を持つ[**CellValueType**](https://reference.aspose.com/cells/javascript-cpp/cellvaluetype)列挙体に基づいています：

|**セル値の種類**|**説明**|
| :- | :- |
|IsBool|セルの値がブール型であることを指定します。|
|IsDateTime|セルの値が日付/時刻であることを指定します。|
|IsNull|空白セルを表します。|
|IsNumeric|セルの値が数値であることを指定します。|
|IsString|セルの値が文字列であることを指定します。|
|IsUnknown|セルの値が不明であることを指定します。|

上記の事前定義されたセル値タイプを使用して、各セルに存在するデータのタイプと比較することもできます。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Read Cell Values Example</h1>
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

            // Opening an existing workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing first worksheet
            const worksheet = workbook.worksheets.get(0);

            var cells = worksheet.cells;
            var maxRow = cells.maxRow;
            var maxColumn = cells.maxColumn;
            let logs = [];
            for (let i = 0; i <= maxRow; i++) {
                for (let j = 0; j <= maxColumn; j++) 
                {
                    const cell1 = cells.get(i, j);
                    if (!cell1) {
                        continue;
                    }
                    // Variables to store values of different data types
                    let stringValue;
                    let doubleValue;
                    let boolValue;
                    let dateTimeValue;

                    // Passing the type of the data contained in the cell for evaluation
                    switch (cell1.type) {
                        // Evaluating the data type of the cell data for string value
                        case AsposeCells.CellValueType.IsString:
                            stringValue = cell1.stringValue;
                            console.log("String Value: " + stringValue);
                            logs.push("String Value: " + stringValue);
                            break;

                        // Evaluating the data type of the cell data for double value
                        case AsposeCells.CellValueType.IsNumeric:
                            doubleValue = cell1.doubleValue;
                            console.log("Double Value: " + doubleValue);
                            logs.push("Double Value: " + doubleValue);
                            break;

                        // Evaluating the data type of the cell data for boolean value
                        case AsposeCells.CellValueType.IsBool:
                            boolValue = cell1.boolValue;
                            console.log("Bool Value: " + boolValue);
                            logs.push("Bool Value: " + boolValue);
                            break;

                        // Evaluating the data type of the cell data for date/time value
                        case AsposeCells.CellValueType.IsDateTime:
                            dateTimeValue = cell1.dateTimeValue;
                            console.log("DateTime Value: " + dateTimeValue);
                            logs.push("DateTime Value: " + dateTimeValue);
                            break;

                        // Evaluating the unknown data type of the cell data
                        case AsposeCells.CellValueType.IsUnknown:
                            stringValue = cell1.stringValue;
                            console.log("Unknown Value: " + stringValue);
                            logs.push("Unknown Value: " + stringValue);
                            break;

                        // Terminating the type checking of type of the cell data is null
                        case AsposeCells.CellValueType.IsNull:
                            break;
                    }
                }
            }

            document.getElementById('result').innerHTML = `<p style="color: green;">Operation completed successfully! See console for detailed cell values.</p><pre>${logs.join("\n")}</pre>`;
        });
    </script>
</html>
```


{{% alert color="primary" %}}

Worksheetの操作中に、ユーザーはセルにさまざまな種類のデータを追加することがあります。これらのデータタイプには、ブール値、整数、浮動小数点、テキスト、または日時値が含まれる場合があります。Aspose.Cellsを使用すると、それぞれのデータタイプに応じた適切な値をセルから取得できます。

{{% /alert %}}

## **高度なトピック**
- [ワークシートのセルへのアクセス](/cells/ja/javascript-cpp/accessing-cells-of-a-worksheet/)
- [テキスト数値データを数値に変換](/cells/ja/javascript-cpp/convert-text-numeric-data-to-number/)
- [小計を作成する](/cells/ja/javascript-cpp/creating-subtotals/)
- [データのフィルタリング](/cells/ja/javascript-cpp/data-filtering/)
- [データのソート](/cells/ja/javascript-cpp/sort-data-of-excel/)
- [データの検証](/cells/ja/javascript-cpp/data-validation/)
- [データの検索](/cells/ja/javascript-cpp/find-or-search-data/)
- [書式設定ありおよびなしでセル文字列の値を取得](/cells/ja/javascript-cpp/get-cell-string-value-with-and-without-formatting/)
- [セル内に HTML リッチテキストを追加](/cells/ja/javascript-cpp/adding-html-rich-text-inside-the-cell/)
- [ExcelまたはOpenOfficeにハイパーリンクを挿入](/cells/ja/javascript-cpp/insert-hyperlinks-to-excel/)
- [列挙子の使用方法と場所](/cells/ja/javascript-cpp/how-and-where-to-use-enumerators/)
- [セル値の幅と高さをピクセル単位で計測](/cells/ja/javascript-cpp/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/)
- [複数スレッドで同時にセル値を読み取る](/cells/ja/javascript-cpp/reading-cell-values-in-multiple-threads-simultaneously/)
- [セル名と行/列インデックスの変換](/cells/ja/javascript-cpp/names-and-indices/)
- [最初に行ごと、次に列ごとにデータを取得](/cells/ja/javascript-cpp/populate-data-first-by-row-then-by-column/)
- [セル値または範囲の先頭にシングルクォートのプレフィックスを保存](/cells/ja/javascript-cpp/preserve-single-quote-prefix-of-cell-value-or-range/)
- [セルのリッチテキストの部分にアクセスして更新](/cells/ja/javascript-cpp/access-and-update-the-portions-of-rich-text-of-cell/)
