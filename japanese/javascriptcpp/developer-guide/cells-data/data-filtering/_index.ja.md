---
title: データフィルタリング
type: docs
weight: 85
url: /ja/javascript-cpp/data-filtering/
description: C++ APIを使用してAspose.Cells for JavaScriptでデータフィルタを追加する方法を学習します。
keywords: C++を使用した色によるフィルタ追加JavaScript、日付フィルタ追加JavaScript、数値フィルタ追加JavaScript、ダイナミックフィルタ追加JavaScript、テキストフィルタ追加JavaScript、包含によるカスタムフィルタ追加JavaScript、含まないによるカスタムフィルタ追加JavaScript、先頭一致によるカスタムフィルタ追加JavaScript、末尾一致によるカスタムフィルタ追加JavaScript
---

{{% alert color="primary" %}}
Microsoft Excelはワークシートのデータを自動フィルタリングする優れた機能を提供します。Aspose.CellsはMicrosoft Excelの自動フィルタ機能を完全にサポートしています。この記事では、Microsoft Excelの機能の使い方と、C++を使用したAspose.Cells for JavaScriptでのコーディング方法について説明します。
{{% /alert %}}

## **データの自動フィルタリング**

自動フィルタリングは、リスト内で表示したいアイテムのみを素早く選択できる最も簡単な方法です。自動フィルタ機能により、リスト内のアイテムを特定の基準に従ってフィルタリングできます。テキスト、数値、または日付に基づいてフィルタリングできます。

### **Microsoft Excelの自動フィルタ**

Microsoft Excelで自動フィルタ機能を有効にするには：

1. ワークシート内の見出し行をクリックします。
1. **データ** メニューから、**フィルタ** を選択し、その後** 自動フィルタ** を選択します。

ワークシートに自動フィルタを適用すると、フィルタスイッチ（黒い矢印）が列見出しの右側に表示されます。

1. フィルタ矢印をクリックして、フィルタオプションのリストを表示します。

自動フィルタのオプションには次のものがあります:

|**オプション**|**説明**|
| :- | :- |
|All|リストのすべてのアイテムを一度に表示します。|
|Custom|含む/含まないなどのフィルター条件をカスタマイズします|
|Filter by Color|塗りつぶし色に基づくフィルター|
|Date Filters|日付に基づくさまざまな条件で行をフィルター|
|Number Filters|比較、平均、トップ10など、数値に関する異なるタイプのフィルタ。
|Text Filters|始まり、終わり、含むなどのさまざまなフィルター|
|Blanks/Non Blanks|これらのフィルターはテキストフィルター空白を通じて実装できます|

Microsoft Excelのユーザーは、これらのオプションを使用してワークシートデータを手動でフィルタリングします。

### **C++による自動フィルタの実装例**

Aspose.CellsはExcelファイルを表すWorkbookクラスを提供します。WorkbookクラスにはワークシートにアクセスできるWorksheetsコレクションが含まれています

ワークシートは、ワークシートクラスによって表されます。ワークシートクラスには、ワークシートを管理するための広範なプロパティとメソッドが含まれています。Autofilterを作成するには、ワークシートクラスのAutoFilterプロパティを使用します。AutoFilterプロパティはAutoFilterクラスのオブジェクトであり、ヘッダ行を構成するセル範囲を指定するRangeプロパティが提供されています。オートフィルタは、ヘッダ行を構成するセル範囲に適用されます。

各ワークシートで、1つのフィルタ範囲のみを指定できます。これはMicrosoft Excelによって制限されています。カスタムデータフィルタリングには、AutoFilter.Customメソッドを使用します。

下記の例では、上記のMicrosoft Excelで作成したのと同じAutoFilterをC++を用いてAspose.Cells for JavaScriptで作成しています。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells AutoFilter Example</title>
    </head>
    <body>
        <h1>AutoFilter Example</h1>
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Creating AutoFilter by giving the cells range of the heading row
            worksheet.autoFilter.range = "A1:B1";

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">AutoFilter created successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

#### **異なる種類のフィルタ**

Aspose.Cellsでは、カラーフィルタ、日付フィルタ、数値フィルタ、テキストフィルタ、ブランクフィルタ、およびノンブランクフィルタなど、さまざまな種類のフィルタを適用するための複数のオプションが提供されます。

##### **塗りつぶし色**

Aspose.Cellsでは、セルの塗りつぶし色プロパティに基づいてデータをフィルタリングするためのAddFillColorFilter関数が提供されています。以下の例では、シートの最初の列に異なる塗りつぶし色を持つテンプレートファイルを使用して色のフィルタリング機能をテストしています。サンプルファイルは以下からダウンロードできます

1. [ColouredCells.xlsx](72417315.xlsx)
1. [FilteredColouredCells.xlsx](72417316.xlsx)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Filter Coloured Cells Example</h1>
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Instantiating a CellsColor object for foreground color
            const clrForeground = workbook.createCellsColor();
            clrForeground.color = AsposeCells.Color.fromArgb(255, 0, 0); // Red color

            // Instantiating a CellsColor object for background color
            const clrBackground = workbook.createCellsColor();
            clrBackground.color = AsposeCells.Color.fromArgb(255, 255, 255); // White color

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Call AddFillColorFilter function to apply the filter
            worksheet.autoFilter.addFillColorFilter(0, AsposeCells.BackgroundType.Solid, clrForeground, clrBackground);

            // Call refresh function to update the worksheet
            worksheet.autoFilter.refresh();

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'FilteredColouredCells.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Filtered Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Filter applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


##### **日付**

2018年1月のすべての日付を持つ行をフィルタリングするなど、さまざまなタイプの日時フィルターを実装できます。以下のサンプルコードは、AddDateFilter関数を使用してこのフィルターを示しています。サンプルファイルは以下にあります。

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDate.xlsx](72417318.xlsx)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Date Filter</title>
    </head>
    <body>
        <h1>Date Filter Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
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

            // Instantiating a Workbook object
            // Opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Call AddDateFilter function to apply the filter
            worksheet.autoFilter.addDateFilter(0, AsposeCells.DateTimeGroupingType.Month, 2018, 1, 0, 0, 0, 0);

            // Call refresh function to update the worksheet
            worksheet.autoFilter.refresh();

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'FilteredDate.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Filtered Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Filter applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


##### **動的日付**

時々動的なフィルタが必要な場合があります。例えば、年を問わず1月の日付を持つすべてのセル。この場合、DynamicFilter関数を使用します。以下のサンプルコードでこのフィルタを示しています。サンプルファイルは以下に示されています。

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDynamicDate.xlsx](72417319.xlsx)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Filter Dynamic Date Example</h1>
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

            // Instantiating a Workbook object
            // Opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Call DynamicFilter function to apply the filter
            worksheet.autoFilter.dynamic_Filter(0, AsposeCells.DynamicFilterType.January);

            // Call refresh function to update the worksheet
            worksheet.autoFilter.refresh();

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'FilteredDynamicDate.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Filtered Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Filter applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


##### **番号**

Aspose.Cellsを使用して数値の範囲内のセルを選択するなど、カスタムフィルタを適用できます。以下の例では、Custom()関数を使用して数値をフィルタする方法を示しています。サンプルファイルは以下にあります

1. [Number.xlsx](72417320.xlsx)
1. [FilteredNumber.xlsx](72417321.xlsx)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Filter Numbers</title>
    </head>
    <body>
        <h1>Filter Numbers Example</h1>
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

            // Instantiating a Workbook object
            // Opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Call Custom function to apply the filter
            worksheet.autoFilter.custom(0, AsposeCells.FilterOperatorType.GreaterOrEqual, 5, true, AsposeCells.FilterOperatorType.LessOrEqual, 10);

            // Call refresh function to update the worksheet
            worksheet.autoFilter.refresh();

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'FilteredNumber.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Filtered Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Filter applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


##### **テキスト**

列にテキストが含まれていて、特定のテキストを含むセルを選択したい場合、Filter()関数を使用できます。以下の例では、テンプレートファイルに国のリストがあり、特定の国名を含む行を選択します。以下のコードはテキストのフィルタリングを示しています。サンプルファイルは以下にあります。

1. [Text.xlsx](72417322.xlsx)
1. [FilteredText.xlsx](72417323.xlsx)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Filter AutoFilter Example</h1>
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

            // Instantiating a Workbook object
            // Opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Call Filter function to apply the filter
            const autoFilter = worksheet.autoFilter;
            autoFilter.filter(0, "Angola");

            // Call refresh function to update the worksheet
            autoFilter.refresh();

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'FilteredText.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Filtered Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Filter applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


##### **空欄**

テキストが含まれ、空白のセルを選択し、それらの行のみを選択するフィルタが必要な場合、MatchBlanks()関数を使用します。以下に、それを実証しているサンプルコードが示されています。サンプルファイルは以下に示されています。

1. [Blank.xlsx](72417324.xlsx)
1. [FilteredBlank.xlsx](72417325.xlsx)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Filter Blank Rows Example</title>
    </head>
    <body>
        <h1>Filter Blank Rows Example</h1>
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

            // Instantiating a Workbook object
            // Opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Call MatchBlanks function to apply the filter
            worksheet.autoFilter.matchBlanks(0);

            // Call refresh function to update the worksheet
            worksheet.autoFilter.refresh();

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'FilteredBlank.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Filtered Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Filtering completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


##### **非空白セル**

テキストを含むセルをフィルタする必要がある場合は、MatchNonBlanksフィルタ関数を使用します。以下のサンプルコードが示されています。サンプルファイルは以下に示されています。

1. [Blank.xlsx](72417324.xlsx)
1. [FilteredNonBlank.xlsx](72417326.xlsx)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Filter Non-Blank Example</h1>
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            // Read the selected file
            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Call MatchNonBlanks function to apply the filter
            worksheet.autoFilter.matchNonBlanks(0);

            // Call refresh function to update the worksheet
            worksheet.autoFilter.refresh();

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'FilteredNonBlank.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Filtered Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Filter applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


##### **Contains カスタムフィルタ**

Excelは、特定の文字列を含む行をフィルタリングするなど、カスタムフィルターを提供しています。この機能はAspose.Cellsで利用可能で、以下ではサンプルファイルの名前をフィルタリングすることで、デモンストレーションしています。

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx)
1. [outSourseSampleCountryNames.xlsx](outSourseSampleCountryNames.xlsx).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells AutoFilter Example</title>
    </head>
    <body>
        <h1>AutoFilter Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, FilterOperatorType } = AsposeCells;

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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Creating AutoFilter by giving the cells range
            worksheet.autoFilter.range = "A1:A18";

            // Initialize filter for rows containing string "Ba"
            worksheet.autoFilter.custom(0, FilterOperatorType.Contains, "Ba");

            // Refresh the filter to show/hide filtered rows
            worksheet.autoFilter.refresh();

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outSourseSampleCountryNames.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Filter applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


##### **NotContains カスタムフィルタ**

Excelは特定の文字列を含まない行をフィルタリングするカスタムフィルタを提供しています。この機能はAspose.Cellsで利用可能で、以下のサンプルファイル内の名前のフィルタリングにより実演しています。

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells AutoFilter Example</title>
    </head>
    <body>
        <h1>AutoFilter Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, FilterOperatorType } = AsposeCells;

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

            // Instantiating a Workbook object by opening the Excel file from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Creating AutoFilter by giving the cells range
            worksheet.autoFilter.range = "A1:A18";

            // Initialize filter for rows not containing string "Be"
            worksheet.autoFilter.custom(0, FilterOperatorType.NotContains, "Be");

            // Refresh the filter to show/hide filtered rows
            worksheet.autoFilter.refresh();

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outSourseSampleCountryNames.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Filter applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


##### **BeginsWith カスタムフィルタ**

Excelは特定の文字列で始まる行をフィルタリングするカスタムフィルタを提供しています。この機能はAspose.Cellsで利用可能で、以下のサンプルファイル内の名前のフィルタリングにより実演しています。

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Filter Countries Starting With "Ba"</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, FilterOperatorType } = AsposeCells;

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

            // Instantiating a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Creating AutoFilter by giving the cells range
            worksheet.autoFilter.range = "A1:A18";

            // Initialize filter for rows starting with string "Ba"
            worksheet.autoFilter.custom(0, FilterOperatorType.BeginsWith, "Ba");

            // Refresh the filter to show/hide filtered rows
            worksheet.autoFilter.refresh();

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outSourseSampleCountryNames.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Filtered Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Filter applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


##### **EndsWith カスタムフィルタ**

Excel は特定の文字列で終わる行をフィルタするなど、カスタムフィルタを提供しています。この機能は Aspose.Cells で利用可能であり、以下で示されているサンプルファイル内の名前をフィルタリングしています。

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Apply AutoFilter Example</h1>
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
            const resultDiv = document.getElementById('result');
            const downloadLink = document.getElementById('downloadLink');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Creating AutoFilter by giving the cells range
            const autoFilter = worksheet.autoFilter;
            autoFilter.range = "A1:A18";

            // Initialize filter for rows end with string "ia"
            autoFilter.custom(0, AsposeCells.FilterOperatorType.BeginsWith, "ia");

            // Refresh the filter to show/hide filtered rows
            autoFilter.refresh();

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outSourseSampleCountryNames.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Filter applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


## **高度なトピック**
- [複雑な基準を満たすレコードを表示するMicrosoft Excelの高度なフィルタの適用](/cells/ja/javascript-cpp/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/)
- [オートフィルタの更新後の非表示行インデックスの取得](/cells/ja/javascript-cpp/get-all-hidden-rows-indices-after-refreshing-autofilter/)
