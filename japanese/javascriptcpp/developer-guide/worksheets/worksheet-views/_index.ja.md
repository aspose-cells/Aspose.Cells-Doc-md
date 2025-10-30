---
title: JavaScriptを使用したワークシートビューの操作とC++による連携
linktitle: ワークシートビュー
type: docs
weight: 40
url: /ja/javascript-cpp/worksheet-views/
description: この記事では、JavaScriptとJavaScript APIを使用してExcelブックやワークシートのページ区切りプレビューと対話する方法を説明します。分割ペイン、固定ペイン、ズーム倍率も扱います。
---

## **ページブレークプレビュー**

すべてのワークシートは次の2つのモードで表示できます:

- 通常の表示。
- ページブレークプレビュー。

通常ビューはワークシートのデフォルトビューです。ページ区切りプレビューは印刷プレビューの編集ビューで、印刷されるデータを表示します。ページ区切りプレビューでは、各ページに配置されるデータを確認し、印刷範囲やページ区切りを調整できます。C++のAspose.Cells for JavaScriptを使用して、開発者は通常ビューやページ区切りプレビューモードを有効にできます。

### **表示モードの制御**

Aspose.Cellsは、Microsoft Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)クラスを提供します。[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)クラスには、Excelファイル内の各ワークシートにアクセスするための[**workbook.worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--)コレクションが含まれています。

ワークシートは[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)クラスには、ワークシートを管理するための多くのプロパティやメソッドが含まれています。通常またはページ休止プレビューモードを有効にするには、[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)クラスの[**Worksheet.isPageBreakPreview()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isPageBreakPreview--)プロパティを使用します。[**Worksheet.isPageBreakPreview()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isPageBreakPreview--)はブールプロパティであり、**true** または **false** の値のいずれかを格納できるためです。

#### **通常の表示の有効化**

[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)クラスの[**Worksheet.isPageBreakPreview()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isPageBreakPreview--)プロパティを **false** に設定することで、ワークシートを通常ビューに設定します。

#### **ページブレークプレビューの有効化**

[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)クラスの[**Worksheet.isPageBreakPreview()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isPageBreakPreview--)プロパティを **true** に設定することで、任意のワークシートをページ休止プレビューに設定します。これにより、ワークシートが通常ビューからページ休止プレビューに切り替わります。

次の例は、[**Worksheet.isPageBreakPreview()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isPageBreakPreview--)プロパティを使用してExcelファイルの最初のワークシートのページ休止プレビューモードを有効にする方法を示しています。

book1.xlsファイルは、[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)クラスのインスタンスを作成して開きます。最初のワークシートのビューは、[**Worksheet.isPageBreakPreview()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isPageBreakPreview--)プロパティを**true**に設定することでページ休止プレビューに切り替えます。変更されたファイルは、output.xlsとして保存されます。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Page Break Preview</title>
    </head>
    <body>
        <h1>Page Break Preview Example</h1>
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

            // Instantiating a Workbook object using the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Displaying the worksheet in page break preview
            worksheet.isPageBreakPreview = true;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **ズームファクター**

### **Microsoft Excel の使用**

Microsoft Excel には、ワークシートのズームやスケーリング要素を設定する機能があります。この機能は、ユーザーがワークシートの内容を小さなビューまたは大きなビューで表示するのに役立ちます。ユーザーは、ズーム要素を任意の値に設定できます。

### **Aspose.Cells & ズーム要素**

Aspose.Cellsを使用すると、開発者はワークシートのズームファクタを設定できます。
Aspose.CellsはMicrosoft Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)クラスを提供します。 [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)クラスには、Excelファイル内の各ワークシートにアクセスできる[**workbook.worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--)コレクションが含まれています。

ワークシートは[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)クラスで表されます。 [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)クラスには、ワークシートを管理するための多くのプロパティとメソッドが用意されています。ワークシートのズームファクタを設定するには、[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)クラスの[**Worksheet.zoom**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#zoom--)プロパティを使用します。ズームファクタは、[**Worksheet.zoom**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#zoom--)プロパティに数値（整数）を割り当てることで設定されます。

以下に完全な例を示します。これは、[**Worksheet.zoom**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#zoom--)プロパティを使用してExcelファイルの最初のワークシートのズーム倍率を設定する方法を示しています。

book1.xlsファイルは、[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)クラスのインスタンスを作成することで開かれます。最初のワークシートのズームファクタは75に設定され、変更されたファイルはoutput.xlsとして保存されます。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells: Set Worksheet Zoom Example</h1>
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

            // Instantiating a Workbook object by opening the Excel file from the uploaded file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Setting the zoom factor of the worksheet to 75
            worksheet.zoom = 75;

            // Saving the modified Excel file (Excel97-2003 format for .xls)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Zoom set to 75 successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **ウィンドウ枠の固定**

### **Microsoft Excel の使用**

ウィンドウ枠の固定は、Microsoft Excel が提供する機能です。枠を固定すると、ワークシートをスクロールしても表示され続けるデータを選択できます。

### **Aspose.Cells & ウィンドウ枠の固定**

Aspose.Cellsを使用すると、開発者は実行時にワークシートにウィンドウ枠を適用できます。

Aspose.CellsはMicrosoft Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)クラスを提供します。 [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)クラスには、Excelファイル内の各ワークシートにアクセスできる[**workbook.worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--)コレクションが含まれています。

ワークシートは[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)クラスは、ワークシートの管理に豊富なプロパティやメソッドを提供します。フリーズペインを設定するには、Worksheetクラスの[**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#freezePanes-number-number-number-number-)メソッドを呼び出します。[**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#freezePanes-number-number-number-number-)メソッドは以下のパラメータを取ります：

- **行**、枠が開始するセルの行インデックス。
- **列**、枠が開始するセルの列インデックス。
- **固定行**、上部枠内に表示される行数。
- **フリーズされた列**、左側のペインに表示される列数。

book1.xlsファイルは、[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)クラスのコンストラクタを呼び出してインスタンス化し、最初のワークシートでいくつかの行と列が固定されます。変更されたファイルはoutput.xlsとして保存されます。

以下に、Excelファイルの最初のワークシートの4行目および3列目（行と列は0から始まるインデックスで表される、C4から始まる）の行と列を固定する方法を示す完全な例が示されています。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Freeze Panes Example</title>
    </head>
    <body>
        <h1>Freeze Panes Example</h1>
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

            // Instantiating a Workbook object using the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Applying freeze panes settings: topRows = 3, leftColumns = 2, top = 3, left = 2
            worksheet.freezePanes(3, 2, 3, 2);

            // Saving the modified Excel file in Excel97-2003 format (.xls)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData], { type: "application/octet-stream" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Freeze panes applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **画面の分割**

ワークシート内で二つの異なるビューを取得するには、画面を分割する必要があります。Microsoft Excel は、ワークシートのコピーを複数表示し、各パネで独立してスクロールできる非常に便利な機能を提供しています：画面の分割。

パネは同時に動作します。片方で変更を加えると、同時に他方にも変更が表示されます。Aspose.Cells は、ユーザーに対して画面の分割機能を提供しています。

### **画面の分割の適用と解除**

#### **画面の分割**

Aspose.CellsはMicrosoft Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)クラスを提供します。 [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)クラスには、Excelファイルを管理するための多くのプロパティとメソッドが提供されます。分割ビューを実装するには、[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)クラスの[**Worksheet.split()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#split--)を使用します。パネルを解除するには、[**Worksheet.removeSplit()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#removeSplit--)メソッドを使用します。

例では、シンプルなテンプレート ファイルをロードして、最初のワークシートのセルに分割パネル機能を適用し、更新されたファイルを保存します。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Split Window Example</title>
    </head>
    <body>
        <h1>Split Worksheet Window Example</h1>
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a new workbook and open the uploaded file
            const book = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const sheet = book.worksheets.get(0);

            // Set the active cell (converted from setActiveCell -> activeCell)
            sheet.activeCell = "A20";

            // Split the worksheet window
            sheet.split();

            // Save the excel file (SaveFormat.Xls -> SaveFormat.Excel97To2003)
            const outputData = book.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Worksheet window split and active cell set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

上記のコードを実行すると、生成されたファイルには分割ビューが表示されます。

#### **パネルの削除**

分割ペインを[**Worksheet.removeSplit()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#removeSplit--)メソッドを使用して削除します。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Set Active Cell and Remove Split Example</h1>
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

            // Instantiate a new workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet in the workbook
            const worksheet = workbook.worksheets.get(0);

            // Set the active cell
            worksheet.activeCell = "A20";

            // Split the worksheet window - remove any existing split
            worksheet.removeSplit();

            // Save the modified workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **高度なトピック**
- [ワークシートでゼロの値の表示を非表示にする](/cells/ja/javascript-cpp/hiding-the-display-of-zero-values-in-the-worksheet/)
- [ワークシートタブの色を設定する](/cells/ja/javascript-cpp/set-worksheet-tab-color/)
- [グリッド線と行列見出しの表示と非表示](/cells/ja/javascript-cpp/show-and-hide-gridlines-and-row-column-headers/)
- [行と列、スクロールバーの表示と非表示](/cells/ja/javascript-cpp/show-and-hide-rows-columns-and-scroll-bars/)
- [ワークシートとタブの表示と非表示](/cells/ja/javascript-cpp/show-and-hide-worksheets-and-tabs/)
- [ワークシートで値の代わりに数式を表示する](/cells/ja/javascript-cpp/show-formulas-instead-of-values-in-a-worksheet/)
- [エラーチェックオプションを使用する](/cells/ja/javascript-cpp/use-error-checking-options/)
