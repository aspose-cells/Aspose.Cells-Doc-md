---
title: C++でJavaScriptを使用した印刷オプションの設定
linktitle: 印刷オプションの設定
type: docs
weight: 40
url: /ja/javascript-cpp/setting-print-options/
description: この記事では、JavaScript APIとC++ライブラリを使用してExcelワークシートのページ設定機能の印刷オプションをプログラム的に設定する方法を説明します。印刷範囲、印刷タイトル、ページ順序を設定できます。
keywords: C++でJavaScriptを使用してExcelの印刷範囲を設定する方法、JavaScriptでExcelの印刷タイトルを設定する方法、C++でJavaScriptを使用してExcelのページ順序を設定する方法
---

{{% alert color="primary" %}}

Microsoft Excel のページ設定設定には、ワークシートページが印刷される方法を制御するいくつかの印刷オプション (またはシートオプションとも呼ばれる) が含まれています。

{{% /alert %}}

## **印刷オプションの設定**

これらの印刷オプションにより、ユーザーは次のような操作を行うことができます:

- ワークシート上の特定の印刷範囲を選択する。
- タイトルを印刷する。
- グリッド線を印刷する。
- 行/列見出しを印刷します。
- 下書き品質を実現する。
- コメントを印刷する。
- セルエラーを印刷する。
- ページ順序を定義する。

Aspose.Cells for JavaScriptをC++でサポートし、Microsoft Excelが提供するすべての印刷オプションを利用できます。開発者は、[**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup)クラスが提供するプロパティを使用してこれらのオプションを簡単に設定できます。これらのプロパティの使用方法については、以下で詳しく説明します。

### **印刷範囲の設定**

デフォルトでは、印刷エリアにはデータを含むワークシートのすべての領域が組み込まれます。開発者はワークシートの特定の印刷エリアを設定することができます。

特定の印刷エリアを選択するには、[**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup)クラスの[**PageSetup.printArea**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printArea--)プロパティを使用します。このプロパティに印刷エリアを定義するセル範囲を割り当てます。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Set Print Area Example</title>
    </head>
    <body>
        <h1>Set Print Area Example</h1>
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
            // Instantiate a new Workbook object
            const workbook = new Workbook();

            // Obtaining the reference of the PageSetup of the first worksheet
            const pageSetup = workbook.worksheets.get(0).pageSetup;

            // Specifying the cells range (from A1 cell to T35 cell) of the print area
            pageSetup.printArea = "A1:T35";

            // Save the workbook and prepare download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'SetPrintArea_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Print area set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **印刷タイトルを設定する**

Aspose.Cellsでは、印刷されるワークシートのすべてのページで行見出しと列見出しを繰り返すことができます。これを行うには、[**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup)クラスの[**PageSetup.printTitleColumns**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printTitleColumns--)および[**PageSetup.printTitleRows**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printTitleRows--)プロパティを使用します。

繰り返す行または列は、その行番号または列番号を渡すことで定義されます。たとえば、行は$1:$2と定義され、列は$A:$Bと定義されます。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Set Print Title</title>
    </head>
    <body>
        <h1>Set Print Title Columns and Rows Example</h1>
        <p>You may optionally select an existing Excel file to modify. If no file is selected, a new workbook will be created.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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
            let workbook;

            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Obtaining the reference of the PageSetup of the first worksheet
            const pageSetup = workbook.worksheets.get(0).pageSetup;

            // Defining column numbers A & B as title columns
            pageSetup.printTitleColumns = "$A:$B";

            // Defining row numbers 1 & 2 as title rows
            pageSetup.printTitleRows = "$1:$2";

            // Save the workbook and provide download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'SetPrintTitle_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Print title columns and rows set successfully. Click the download link to save the file.</p>';
        });
    </script>
</html>
```

### **その他の印刷オプションの設定**

[**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup)クラスは、次の一般的な印刷オプションを設定するためのいくつかの他のプロパティも提供します。

- [**PageSetup.printGridlines**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printGridlines--): グリッド線を印刷するかどうかを定義するBoolean型のプロパティ。
- [**PageSetup.printHeadings**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printHeadings--): 行と列の見出しを印刷するかどうかを定義するBoolean型のプロパティ。
- [**PageSetup.blackAndWhite**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#blackAndWhite--): ワークシートを白黒モードで印刷するかどうかを定義するBoolean型のプロパティ。
- [**PageSetup.printComments**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printComments--): ワークシート上に印刷コメントを表示するか、もしくはワークシートの末尾に表示するかを定義します。
- [**PageSetup.printDraft**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printDraft--): グラフィックなしでシートを印刷するかどうかを定義するBoolean型のプロパティ。
- [**PageSetup.printErrors**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printErrors--): 表示されるままのセルエラー、空白、ダッシュ、またはN/A として印刷するかを定義する。

[**PageSetup.printComments**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printComments--)と[**PageSetup.printErrors**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printErrors--)のプロパティを設定するために、Aspose.Cells for JavaScriptをC++で使用すると、事前定義された値を含む[**PrintCommentsType**](https://reference.aspose.com/cells/javascript-cpp/printcommentstype)と[**PrintErrorsType**](https://reference.aspose.com/cells/javascript-cpp/printerrorstype)の二つの列挙型も提供されており、それぞれ[**PageSetup.printComments**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printComments--)と[**PageSetup.printErrors**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printErrors--)のプロパティに割り当てることができます。

[**PrintCommentsType**](https://reference.aspose.com/cells/javascript-cpp/printcommentstype) 列挙型の事前定義された値とその説明は以下の通りです。

|**コメント印刷タイプ**|**説明**|
| :- | :- |
|PrintInPlace|: ワークシート上に表示されているコメントを印刷することを指定。
|PrintNoComments|: コメントを印刷しないことを指定。
|PrintSheetEnd|: ワークシートの最後にコメントを印刷することを指定。

[**PrintErrorsType**](https://reference.aspose.com/cells/javascript-cpp/printerrorstype) 列挙型の事前定義された値とその説明は以下の通りです。

|**エラー印刷タイプ**|**説明**|
| :- | :- |
|PrintErrorsBlank|: エラーを印刷しないことを指定。
|PrintErrorsDash|: エラーを "--" として印刷することを指定。
|PrintErrorsDisplayed|: 表示されているエラーを印刷することを指定。
|PrintErrorsNA|: エラーを "#N/A" として印刷することを指定。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Other Print Options</title>
    </head>
    <body>
        <h1>Other Print Options Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PrintCommentsType, PrintErrorsType } = AsposeCells;

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
            let workbook;

            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                // Create a new workbook if no file provided
                workbook = new Workbook();
            }

            // Obtaining the reference of the PageSetup of the first worksheet
            const pageSetup = workbook.worksheets.get(0).pageSetup;

            // Allowing to print gridlines
            pageSetup.printGridlines = true;

            // Allowing to print row/column headings
            pageSetup.printHeadings = true;

            // Allowing to print worksheet in black & white mode
            pageSetup.blackAndWhite = true;

            // Allowing to print comments as displayed on worksheet
            pageSetup.printComments = PrintCommentsType.PrintInPlace;

            // Allowing to print worksheet with draft quality
            pageSetup.printDraft = true;

            // Allowing to print cell errors as N/A
            pageSetup.printErrors = PrintErrorsType.PrintErrorsNA;

            // Saving the modified workbook to Excel 97-2003 format
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'OtherPrintOptions_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **ページ順の設定**

[**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup) クラスは、複数のページを印刷する順序を設定するための [**PageSetup.order**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#order--) プロパティを提供します。ページの順序を設定する方法は以下の2つです。

-  すべてのページを左側に印刷する前にすべてのページを下に印刷します。
-  下のページを印刷する前に左から右へページを印刷します。

Aspose.Cellsは、すべての事前定義された順序タイプを含む列挙型 [**PrintOrderType**](https://reference.aspose.com/cells/javascript-cpp/printordertype) を提供しています。

[**PrintOrderType**](https://reference.aspose.com/cells/javascript-cpp/printordertype) 列挙型の事前定義された値は以下に一覧表示されています。

|**印刷順序タイプ**|**説明**|
| :- | :- |
|DownThenOver|: 下に印刷してから右に印刷するよう指定。
|OverThenDown|: 左から右に印刷してから下に印刷するよう指定。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Set Page Order Example</title>
    </head>
    <body>
        <h1>Set Page Order Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PrintOrderType } = AsposeCells;

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
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            const worksheet = workbook.worksheets.get(0);
            const pageSetup = worksheet.pageSetup;
            pageSetup.order = PrintOrderType.OverThenDown;

            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'SetPageOrder_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Page order set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
