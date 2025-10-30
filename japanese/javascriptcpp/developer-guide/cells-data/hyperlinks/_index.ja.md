---
title: ExcelまたはOpenOfficeにハイパーリンクを挿入する
linktitle: ハイパーリンクの管理
type: docs
weight: 45
url: /ja/javascript-cpp/insert-hyperlinks-to-excel/
description: MS Excelを使用せずにAspose.CellsライブラリでExcelファイルにハイパーリンクを挿入する方法（JavaScript経由のC++）
keywords: Excelにハイパーリンクを挿入（追加・挿入）JavaScript経由のC++、URLへのリンクを追加・挿入、セルにリンクを追加・挿入、外部ファイルへのリンクを追加・挿入JavaScript経由のC++
---

{{% alert color="primary" %}} 

ハイパーリンクは、2つのエンティティ間のリンクを作成するために使用されます。特にウェブサイトを含め、誰もがハイパーリンクの使用に慣れています。
Aspose.Cellsを使用することで、開発者はMicrosoft Excelファイルでさまざまな種類のハイパーリンクを作成することができます。このトピックではAspose.Cellsでサポートされているハイパーリンクの種類と、Excelファイルでどのように使用できるかについて説明しています。

{{% /alert %}} 

## **ハイパーリンクの追加**
Aspose.Cellsは、APIまたはデザイナースプレッドシート（手動でハイパーリンクを作成し、それを他のスプレッドシートにインポートするためにAspose.Cellsを使用する）を使って、開発者がExcelファイルにハイパーリンクを追加できるようにします。

Aspose.Cellsは[Workbook](https://reference.aspose.com/cells/javascript-cpp/workbook)クラスを提供し、これはMicrosoft Excelファイルを表します。[Workbook](https://reference.aspose.com/cells/javascript-cpp/workbook)クラスにはExcelファイル内の各ワークシートにアクセスできる[WorksheetCollection](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection)が含まれています。ワークシートは[Worksheet](https://reference.aspose.com/cells/javascript-cpp/worksheet)クラスで表されます。このクラスは異なるハイパーリンクの追加に対応したさまざまなメソッドを提供します。
## **URLへのリンクの追加**
[Worksheet](https://reference.aspose.com/cells/javascript-cpp/worksheet)クラスには[hyperlinks](https://reference.aspose.com/cells/javascript-cpp/worksheet/#hyperlinks--)コレクションが含まれます。各アイテムは[Hyperlink](https://reference.aspose.com/cells/javascript-cpp/hyperlink)を表します。[Hyperlinks](https://reference.aspose.com/cells/javascript-cpp/hyperlinkcollection)コレクションの[add](https://reference.aspose.com/cells/javascript-cpp/hyperlinkcollection/#add-string-number-number-string-)メソッドを呼び出すことでURLへのハイパーリンクを追加できます。[add]メソッドは次のパラメータを取ります。

- セル名、ハイパーリンクが追加されるセルの名前。
- 行数、このハイパーリンク範囲の行数。
- 列数、このハイパーリンク範囲の列数。
- URL、URLアドレス。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Add Hyperlink Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example (Create Workbook & Add Hyperlink)</button>
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
            // Instantiate a new Workbook
            const workbook = new Workbook();

            // Obtain the reference of the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Add a hyperlink to a URL at "A1" cell
            worksheet.hyperlinks.add("A1", 1, 1, "http://www.aspose.com");

            // Save the Excel file and provide a download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and hyperlink added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


{{% alert color="primary" %}} 

上記の例では、空のセル**A1**にURLへのハイパーリンクが追加されます。このような場合、セルが空の場合、URLアドレスもその空のセルの値として追加されます。セルが空でない場合は、ハイパーリンクが追加されても、セルの値はプレーンテキストのように見えます。それをハイパーリンクのように見えるようにするには、そのセルに適切な書式設定を適用します。

{{% /alert %}} 
## **同じファイル内のセルへのリンクの追加**
同じExcelファイル内のセルにハイパーリンクを追加するには、[Hyperlinks](https://reference.aspose.com/cells/javascript-cpp/hyperlinkcollection)コレクションの[add](https://reference.aspose.com/cells/javascript-cpp/hyperlinkcollection/#add-string-number-number-string-)メソッドを呼び出します。この[add]メソッドは内部および外部のハイパーリンクの両方に対応します。オーバーロードされた一つのバージョンは次のパラメータを取ります。

- セル名、ハイパーリンクが追加されるセルの名前。
- 行数、このハイパーリンク範囲の行数。
- 列数、このハイパーリンク範囲の列数。
- URL、対象セルのアドレス。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Add Internal Hyperlink Example</h1>
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
            // Create a new Workbook
            const workbook = new Workbook();

            // Adding a new worksheet to the Workbook object
            workbook.worksheets.add();

            // Obtaining the reference of the first (default) worksheet
            const worksheet = workbook.worksheets.get(0);

            // Adding an internal hyperlink to the "B3" cell of the other worksheet "Sheet2" in the same Excel file
            worksheet.hyperlinks.add("B3", 1, 1, "Sheet2!B9");

            // Saving the Excel file and providing a download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Excel file created successfully. Click the download link to save it.</p>';
        });
    </script>
</html>
```


## **外部ファイルへのリンクの追加**
外部Excelファイルへのハイパーリンクを追加するには、[Hyperlinks](https://reference.aspose.com/cells/javascript-cpp/hyperlinkcollection)コレクションの[add](https://reference.aspose.com/cells/javascript-cpp/hyperlinkcollection/#add-string-number-number-string-)メソッドを呼び出します。この[add]メソッドは次のパラメータを取ります。

- セル名、ハイパーリンクが追加されるセルの名前。
- 行数、このハイパーリンク範囲の行数。
- 列数、このハイパーリンク範囲の列数。
 - URL、対象のアドレス、外部のExcelファイル。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <p>Select an optional Excel file to use its filename as the hyperlink target (or leave empty to use "book1.xls"):</p>
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
            let targetFileName = 'book1.xls';
            if (fileInput.files.length) {
                targetFileName = fileInput.files[0].name;
            }

            // Instantiating a Workbook object
            const workbook = new Workbook();

            // Adding a new worksheet to the Excel object
            const i = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(i);

            // Adding an internal hyperlink to the "A5" cell of the other worksheet "Sheet2" in the same Excel file
            worksheet.hyperlinks.add("A5", 1, 1, targetFileName);

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Hyperlink added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```



## **高度なトピック**
- [画像ハイパーリンクを追加する](/cells/ja/javascript-cpp/add-image-hyperlinks/)
- [ハイパーリンクのタイプの検出](/cells/ja/javascript-cpp/detect-hyperlink-type/)
- [ワークシートのハイパーリンクの編集](/cells/ja/javascript-cpp/editing-hyperlinks-of-worksheet/)
- [範囲内のハイパーリンクを取得](/cells/ja/javascript-cpp/get-hyperlinks-in-range/)
