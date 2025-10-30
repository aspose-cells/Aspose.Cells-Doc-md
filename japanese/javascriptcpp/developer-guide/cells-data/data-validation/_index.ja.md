---
title: データ検証
type: docs
weight: 90
url: /ja/javascript-cpp/data-validation/
description: C++ APIを使用したデータ検証の追加方法を学習します。
keywords: JavaScriptによるデータ検証の追加JavaScript、検証値取得JavaScript、整数データ検証追加JavaScript、リストデータ検証追加JavaScript、日付データ検証追加JavaScript、時間データ検証追加JavaScript、テキスト長データ検証追加JavaScript、既存検証へのセルエリア追加JavaScript、セルにドロップダウンがあるか確認JavaScript、カスタム検証追加JavaScript
---

{{% alert color="primary" %}}
Microsoft Excelはワークシートのデータを自動フィルタや検証するための優れた機能を提供します。Aspose.CellsはMicrosoft Excelのデータ検証と自動フィルタ機能を完全にサポートしています。この記事では、これらの機能の使い方と、C++を使用したAspose.Cells for JavaScriptでのコーディング方法について説明します。
{{% /alert %}}

## **データ検証の種類と実行**

データ検証は、ワークシートに入力されたデータに関するルールを設定する機能です。たとえば、「日付」と記載された列には日付のみが含まれるようにし、他の列には数字のみが含まれるようにすることができます。あるいは、「日付」と記載された列には特定の範囲内の日付のみが含まれるようにすることもできます。データ検証を使用すると、ワークシートのセルに入力される内容を制御することができます。

Microsoft Excel はさまざまな種類のデータ検証をサポートしています。それぞれの種類は、セルまたはセル範囲に入力されるデータの種類を制御するために使用されます。以下は、それぞれの種類を確認するためのコードスニペットの例です。

- 数値が整数で、つまり小数部を持たないこと。
- 小数点以下の桁に構造が正しいこと。コード例では、セルの範囲に2つの小数点以下があることを定義しています。
- 一覧からの値に制限されていること。一覧の検証では、セルやセル範囲に適用する別々の値の一覧が定義されます。
- 特定の範囲内の日付であること。
- 特定の範囲内の時間であること。
- 指定された文字長内のテキストであること。

### **Microsoft Excel でデータ検証**

Microsoft Excel を使用して検証を作成するには:

1. ワークシートで、検証を適用したいセルを選択します。
2. **データ** メニューから **検証** を選択します。 検証のダイアログが表示されます。
3. **設定** タブをクリックし、設定を入力します。

### **C++によるデータ検証Aspose.Cells for JavaScript**

データ検証は、ワークシートに入力された情報を検証するための強力な機能です。データ検証を使用すると、開発者はユーザーに選択肢のリストを提供したり、データの入力を特定のタイプやサイズに制限したりすることができます。
C++のAspose.Cells for JavaScriptでは、各[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)クラスに[**validations**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#validations--)コレクションがあり、これは[**Validation**](https://reference.aspose.com/cells/javascript-cpp/validation)オブジェクトのコレクションを表します。検証を設定するには、[**Validation**](https://reference.aspose.com/cells/javascript-cpp/validation)クラスのいくつかのプロパティを次のように設定します。

- 種類 – 検証タイプを表し、[**ValidationType**](https://reference.aspose.com/cells/javascript-cpp/validationtype)列挙体の事前定義された値の1つを使用して指定できます。
- オペレーター – 検証で使用されるオペレーターを表し、[**OperatorType**](https://reference.aspose.com/cells/javascript-cpp/operatortype)列挙体の事前定義された値のいずれかを使用して指定できます。
- Formula1：データ検証の最初の部分に関連付けられた値または式を表します。
- Formula2：データ検証の2番目の部分に関連付けられた値または式を表します。

[**Validation**](https://reference.aspose.com/cells/javascript-cpp/validation)オブジェクトのプロパティが設定されたら、開発者は[**CellArea**](https://reference.aspose.com/cells/javascript-cpp/cellarea)構造体を使用して、作成された検証を使用して検証されるセル範囲に関する情報を格納できます。

#### **データ検証の種類**

[**ValidationType**](https://reference.aspose.com/cells/javascript-cpp/validationtype)列挙体には次のメンバーがあります：

|**メンバー名**|**説明**|
| :- | :- |
|AnyValue|任意の型の値を示します。
|WholeNumber|整数の検証タイプを示します。
|Decimal|10進数の検証タイプを示します。 |
|List|ドロップダウンリストの検証タイプを示します。 |
|Date|日付の検証タイプを示します。 |
|Time|時刻の検証タイプを示します。 |
|TextLength|テキストの長さの検証タイプを示します。 |
|Custom|カスタム検証タイプを示します。 |

##### **整数データの検証**

このタイプの検証では、ユーザーは指定された範囲内の整数のみを検証されたセルに入力できます。以下のコード例は、整数の検証タイプの実装方法を示しており、上記のMicrosoft Excelで作成したのと同じ検証をC++でAspose.Cells for JavaScriptを使って作成しています。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Validation Example</h1>
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
            const resultDiv = document.getElementById('result');
            const fileInput = document.getElementById('fileInput');

            if (fileInput.files.length > 0) {
                // If a file is provided, we will open it; otherwise create a new workbook
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                // Instantiate workbook from uploaded file
                var workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                // Create a new workbook
                var workbook = new Workbook();
            }

            // Create a worksheet and get the first worksheet.
            const ExcelWorkSheet = workbook.worksheets.get(0);

            // Accessing the Validations collection of the worksheet
            const validations = workbook.worksheets.get(0).validations;

            // Create Cell Area
            const ca = new AsposeCells.CellArea();
            ca.startRow = 0;
            ca.endRow = 0;
            ca.startColumn = 0;
            ca.endColumn = 0;

            // Creating a Validation object
            const idx = validations.add(ca);
            const validation = validations.get(idx);

            // Setting the validation type to whole number
            validation.type = AsposeCells.ValidationType.WholeNumber;

            // Setting the operator for validation to Between
            validation.operator = AsposeCells.OperatorType.Between;

            // Setting the minimum value for the validation
            validation.formula1 = "10";

            // Setting the maximum value for the validation
            validation.formula2 = "1000";

            // Applying the validation to a range of cells from A1 to B2 using the CellArea structure
            const area = new AsposeCells.CellArea();
            area.startRow = 0;
            area.endRow = 1;
            area.startColumn = 0;
            area.endColumn = 1;

            // Adding the cell area to Validation
            validation.addArea(area);

            // Save the workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData], { type: "application/vnd.ms-excel" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Validation added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


##### **リストデータの検証**

この種類の検証では、ユーザーはドロップダウンリストから値を入力できます。リストにはデータを含む一連の行があります。この例では、リストのソースを保持するために2番目のワークシートが追加されます。ユーザーはリストからのみ値を選択できます。検証エリアは最初のワークシートのセル範囲 A1:A5 です。

ここで重要なのは、[**Validation.inCellDropDown(boolean)**](https://reference.aspose.com/cells/javascript-cpp/validation/#inCellDropDown-boolean-)プロパティを**true**に設定することです。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Validation List Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellArea, ValidationType, OperatorType, ValidationAlertType } = AsposeCells;

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
            // This example creates a new workbook in the browser (file input is optional here).
            const workbook = new Workbook();

            // Get the first worksheet.
            const worksheet1 = workbook.worksheets.get(0);

            // Add a new worksheet and access it.
            const i = workbook.worksheets.add();
            const worksheet2 = workbook.worksheets.get(i);

            // Create a range in the second worksheet.
            const range = worksheet2.cells.createRange("E1", "E4");

            // Name the range.
            range.name = "MyRange";

            // Fill different cells with data in the range.
            range.get(0, 0).value = "Blue";
            range.get(1, 0).value = "Red";
            range.get(2, 0).value = "Green";
            range.get(3, 0).value = "Yellow";

            // Get the validations collection.
            const validations = worksheet1.validations;

            // Create Cell Area
            const ca = new CellArea();
            ca.startRow = 0;
            ca.endRow = 0;
            ca.startColumn = 0;
            ca.endColumn = 0;

            // Create a new validation to the validations list.
            const validation = validations.get(validations.add(ca));

            // Set the validation type.
            validation.type = ValidationType.List;

            // Set the operator.
            validation.operator = OperatorType.None;

            // Set the in cell drop down.
            validation.inCellDropDown = true;

            // Set the formula1.
            validation.formula1 = "=MyRange";

            // Enable it to show error.
            validation.showError = true;

            // Set the alert type severity level.
            validation.alertStyle = ValidationAlertType.Stop;

            // Set the error title.
            validation.errorTitle = "Error";

            // Set the error message.
            validation.errorMessage = "Please select a color from the list";

            // Specify the validation area.
            const area = new CellArea();
            area.startRow = 0;
            area.endRow = 4;
            area.startColumn = 0;
            area.endColumn = 0;

            // Add the validation area.
            validation.addArea(area);

            // Save the Excel file.
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Validation list created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```


##### **日付データの検証**

このタイプの検証では、ユーザーは検証済みのセルに特定の範囲内の日付値、または特定の条件を満たす日付値を入力できます。例では、ユーザーは1970年から1999年の間の日付を入力することに制限されます。ここでは、検証領域はB1セルです。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Date Validation Example</h1>
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
            // This example creates a new workbook in the browser (no file input required)
            const workbook = new Workbook();

            // Obtain the cells of the first worksheet.
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;

            // Put a string value into the A1 cell.
            const cellA1 = cells.get("A1");
            cellA1.value = "Please enter Date b/w 1/1/1970 and 12/31/1999";

            // Set row height and column width for the cells by accessing row/column objects
            const row0 = cells.rows.get(0);
            row0.height = 31;
            const col0 = cells.columns.get(0);
            col0.width = 35;

            // Get the validations collection.
            const validations = worksheet.validations;

            // Create Cell Area
            const ca = new AsposeCells.CellArea();
            ca.startRow = 0;
            ca.endRow = 0;
            ca.startColumn = 0;
            ca.endColumn = 0;

            // Add a new validation.
            const validationIndex = validations.add(ca);
            const validation = validations.get(validationIndex);

            // Set the data validation type.
            validation.type = AsposeCells.ValidationType.Date;

            // Set the operator for the data validation
            validation.operator = AsposeCells.OperatorType.Between;

            // Set the value or expression associated with the data validation.
            validation.formula1 = "1/1/1970";

            // The value or expression associated with the second part of the data validation.
            validation.formula2 = "12/31/1999";

            // Enable the error.
            validation.showError = true;

            // Set the validation alert style.
            validation.alertStyle = AsposeCells.ValidationAlertType.Stop;

            // Set the title of the data-validation error dialog box
            validation.errorTitle = "Date Error";

            // Set the data validation error message.
            validation.errorMessage = "Enter a Valid Date";

            // Set and enable the data validation input message.
            validation.inputMessage = "Date Validation Type";
            validation.ignoreBlank = true;
            validation.showInput = true;

            // Set a collection of CellArea which contains the data validation settings.
            const cellArea = new AsposeCells.CellArea();
            cellArea.startRow = 0;
            cellArea.endRow = 0;
            cellArea.startColumn = 1;
            cellArea.endColumn = 1;

            // Add the validation area.
            validation.addArea(cellArea);

            // Save the Excel file and provide download link.
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData], { type: "application/vnd.ms-excel" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and validation added. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

##### **時間データの検証**

このタイプの検証では、ユーザーは検証済みのセルに特定の範囲内の時刻、または特定の条件を満たす時刻を入力できます。例では、ユーザーは午前09:00から11:30の間の時間のみを入力するように制限されます。ここでは、検証領域はB1セルです。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Time Validation Example</h1>
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

            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                // Create a new workbook if no file is provided
                workbook = new Workbook();
            }

            // Obtain the cells of the first worksheet.
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;

            // Put a string value into A1 cell.
            const a1 = cells.get("A1");
            a1.value = "Please enter Time b/w 09:00 and 11:30 'o Clock";

            // Set the row height and column width for the cells using row/column objects.
            cells.rows.get(0).height = 31;
            cells.columns.get(0).width = 35;

            // Get the validations collection.
            const validations = worksheet.validations;

            // Create Cell Area
            const ca = new AsposeCells.CellArea();
            ca.startRow = 0;
            ca.endRow = 0;
            ca.startColumn = 0;
            ca.endColumn = 0;

            // Add a new validation and obtain it.
            const validationIndex = validations.add(ca);
            const validation = validations.get(validationIndex);

            // Set the data validation type and other properties.
            validation.type = AsposeCells.ValidationType.Time;
            validation.operator = AsposeCells.OperatorType.Between;
            validation.formula1 = "09:00";
            validation.formula2 = "11:30";
            validation.showError = true;
            validation.alertStyle = AsposeCells.ValidationAlertType.Information;
            validation.errorTitle = "Time Error";
            validation.errorMessage = "Enter a Valid Time";
            validation.inputMessage = "Time Validation Type";
            validation.ignoreBlank = true;
            validation.showInput = true;

            // Set a collection of CellArea which contains the data validation settings.
            const cellArea = new AsposeCells.CellArea();
            cellArea.startRow = 0;
            cellArea.endRow = 0;
            cellArea.startColumn = 1;
            cellArea.endColumn = 1;

            // Add the validation area.
            validation.addArea(cellArea);

            // Save the Excel file.
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData], { type: 'application/vnd.ms-excel' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


##### **テキスト長のデータ検証**

このタイプの検証を使用すると、ユーザーは検証されたセルに指定された長さのテキスト値を入力できます。例では、ユーザーは5文字を超えない文字列値を入力することが制限されています。検証エリアはB1セルです。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Add Text Length Validation</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellArea, ValidationType, OperatorType, ValidationAlertType } = AsposeCells;

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
            // Create a new workbook.
            const workbook = new Workbook();

            // Obtain the cells of the first worksheet.
            const cells = workbook.worksheets.get(0).cells;

            // Put a string value into A1 cell.
            const cellA1 = cells.get("A1");
            cellA1.value = "Please enter a string not more than 5 chars";

            // Set row height and column width for the cell.
            cells.rows.get(0).height = 31;
            cells.columns.get(0).width = 35;

            // Get the validations collection.
            const validations = workbook.worksheets.get(0).validations;

            // Create Cell Area
            const ca = new CellArea();
            ca.startRow = 0;
            ca.endRow = 0;
            ca.startColumn = 0;
            ca.endColumn = 0;

            // Add a new validation.
            const validationIndex = validations.add(ca);
            const validation = validations.get(validationIndex);

            // Set the data validation type.
            validation.type = ValidationType.TextLength;

            // Set the operator for the data validation.
            validation.operator = OperatorType.LessOrEqual;

            // Set the value or expression associated with the data validation.
            validation.formula1 = "5";

            // Enable the error.
            validation.showError = true;

            // Set the validation alert style.
            validation.alertStyle = ValidationAlertType.Warning;

            // Set the title of the data-validation error dialog box.
            validation.errorTitle = "Text Length Error";

            // Set the data validation error message.
            validation.errorMessage = " Enter a Valid String";

            // Set and enable the data validation input message.
            validation.inputMessage = "TextLength Validation Type";
            validation.ignoreBlank = true;
            validation.showInput = true;

            // Set a collection of CellArea which contains the data validation settings.
            const cellArea = new CellArea();
            cellArea.startRow = 0;
            cellArea.endRow = 0;
            cellArea.startColumn = 1;
            cellArea.endColumn = 1;

            // Add the validation area.
            validation.addArea(cellArea);

            // Save the Excel file.
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">File created successfully. Click the download link to get the file.</p>';
        });
    </script>
</html>
```


### **データ検証ルール**

データ検証が実装されると、セルに異なる値を割り当てて検証を確認できます。[**cell.validationValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#validationValue--)を使用して検証結果を取得できます。以下の例では、異なる値を使用してこの機能を示しています。テスト用のサンプルファイルは以下のリンクからダウンロードできます：

[sampleDataValidationRules.xlsx](77496339.xlsx)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Data Validation Check Example</h1>
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
            resultDiv.innerHTML = '';

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate the workbook from the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access Cell C1
            // Cell C1 has the Decimal Validation applied on it.
            // It can take only the values Between 10 and 20
            const cell = worksheet.cells.get("C1");

            const messages = [];

            // Enter 3 inside this cell
            // Since it is not between 10 and 20, it should fail the validation
            cell.value = 3;

            // Check if number 3 satisfies the Data Validation rule applied on this cell
            const isValid3 = cell.validationValue;
            messages.push(`Is 3 a Valid Value for this Cell: ${isValid3}`);

            // Enter 15 inside this cell
            // Since it is between 10 and 20, it should succeed the validation
            cell.value = 15;

            // Check if number 15 satisfies the Data Validation rule applied on this cell
            const isValid15 = cell.validationValue;
            messages.push(`Is 15 a Valid Value for this Cell: ${isValid15}`);

            // Enter 30 inside this cell
            // Since it is not between 10 and 20, it should fail the validation again
            cell.value = 30;

            // Check if number 30 satisfies the Data Validation rule applied on this cell
            const isValid30 = cell.validationValue;
            messages.push(`Is 30 a Valid Value for this Cell: ${isValid30}`);

            // Display results
            resultDiv.innerHTML = messages.map(m => `<p>${m}</p>`).join('');

            // Save the modified workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';
        });
    </script>
</html>
```


## **セルの検証がドロップダウンであるかどうかをチェック**

セルに実装できる検証の種類はさまざまです。検証がドロップダウンかどうかを確認したい場合は、[**validation.inCellDropDown**](https://reference.aspose.com/cells/javascript-cpp/validation/#inCellDropDown--)メソッドを使用してこれをテストできます。以下のサンプルコードはこのプロパティの使用例を示しています。テスト用のサンプルファイルは以下のリンクからダウンロードできます：

[sampleValidation.xlsx](79527947.xlsx)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Check Data Validation Drop-downs</h1>
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
            resultDiv.innerHTML = '';

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the worksheet named "Sheet1"
            const sheet = workbook.worksheets.get("Sheet1");
            const cells = sheet.cells;

            const appendMessage = (msg, color = 'black') => {
                const p = document.createElement('p');
                p.style.color = color;
                p.textContent = msg;
                resultDiv.appendChild(p);
            };

            const checkDropDown = (cell, cellRef) => {
                const validation = cell.validation;
                if (validation.inCellDropDown) {
                    appendMessage(`${cellRef} is a dropdown`, 'green');
                } else {
                    appendMessage(`${cellRef} is NOT a dropdown`, 'orange');
                }
            };

            checkDropDown(cells.get("A2"), "A2");
            checkDropDown(cells.get("B2"), "B2");
            checkDropDown(cells.get("C2"), "C2");
        });
    </script>
</html>
```


## **既存の検証にCellAreaを追加**

既存の[**Validation**](https://reference.aspose.com/cells/javascript-cpp/validation)に[**CellArea**](https://reference.aspose.com/cells/javascript-cpp/cellarea)を追加したい場合があります。[**Validation.addArea(CellArea)**](https://reference.aspose.com/cells/javascript-cpp/validation/#addArea-cellarea-)を使用して[**CellArea**](https://reference.aspose.com/cells/javascript-cpp/cellarea)を追加すると、Aspose.Cellsは既存のすべての範囲を確認し、新しい範囲が既に存在しているかどうかを判断します。検証が多いファイルでは、パフォーマンスに影響を及ぼす可能性があります。これを回避するために、APIは[**Validation.addArea(CellArea, boolean, boolean)**](https://reference.aspose.com/cells/javascript-cpp/validation/#addArea-cellarea-boolean-boolean-)メソッドを提供しています。*checkIntersection*パラメータは、指定された範囲と既存の検証範囲の交差を確認するかどうかを示します。これを**false**に設定すると、他の範囲のチェックが無効になります。*checkEdge*パラメータは、適用された範囲をチェックするかどうかを示します。新しい範囲が左上の範囲になる場合、内部設定が再構築されます。新しい範囲が左上の範囲でないことが確実な場合、このパラメータを**false**に設定できます。

以下のコードスニペットは、[**Validation.addArea(CellArea, boolean, boolean)**](https://reference.aspose.com/cells/javascript-cpp/validation/#addArea-cellarea-boolean-boolean-)メソッドを使用して既存の[**Validation**](https://reference.aspose.com/cells/javascript-cpp/validation)に新しい[**CellArea**](https://reference.aspose.com/cells/javascript-cpp/cellarea)を追加する例を示しています。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Validations</title>
    </head>
    <body>
        <h1>Validations Example</h1>
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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet.
            const worksheet = workbook.worksheets.get(0);

            // Accessing the Validations collection of the worksheet
            const validation = worksheet.validations.get(0);

            // Create your cell area.
            const cellArea = AsposeCells.CellArea.createCellArea("D5", "E7");

            // Adding the cell area to Validation
            validation.addArea(cellArea, false, false);

            // Save the output workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'ValidationsSample_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Validation area added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

ソースエクセルファイルと出力エクセルファイルが添付されています。

[ソースファイル](96928093.xlsx)

[出力ファイル](96928220.xlsx)

## **高度なトピック**
- [ODS ファイルでのセル検証を取得](/cells/ja/javascript-cpp/get-cell-validation-in-ods-files/)
- [セルに適用された検証を取得する](/cells/ja/javascript-cpp/get-validation-applied-on-a-cell/)
- [セルの値がデータ検証ルールを満たすかどうかを確認する](/cells/ja/javascript-cpp/verify-that-cell-value-satisfies-data-validation-rules/)
