---
title: JavaScriptを通じてC++で名前付き範囲に式を設定する方法
linktitle: 名前付き範囲の式の設定
type: docs
weight: 20
url: /ja/javascript-cpp/setting-formula-for-named-range/
description: C++を通じてAspose.Cells for JavaScriptを使用し、スプレッドシートの名前付き範囲に式を設定する方法を学ぶ。
---

## **名前付き範囲の式の設定**
Excelアプリケーションと同様に、Aspose.Cells APIは[Range.refersTo](https://reference.aspose.com/cells/javascript-cpp/range/#refersTo--) プロパティを使用して名前付き範囲に対して式を指定する機能を提供します。この機能には多くの実用的なシナリオがあり、以下にいくつか例を示します。

### **名前付き範囲に簡単な式を設定する**
簡単な式は、同じワークシート（または異なるワークシート）内の別のセルへの参照である場合があります。次の例は、新しいスプレッドシートで名前付き範囲を作成し、その参照先を別のセルに設定します。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Create Named Range Example</h1>
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
            // Create an instance of Workbook
            const book = new Workbook();

            // Get the WorksheetCollection
            const worksheets = book.worksheets;

            // Add a new Named Range with name "NewNamedRange"
            const index = worksheets.names.add("NewNamedRange");

            // Access the newly created Named Range
            const name = worksheets.names.get(index);

            // Set RefersTo property of the Named Range to a formula. Formula references another cell in the same worksheet
            name.refersTo = "=Sheet1!$A$3";

            // Set the formula in the cell A1 to the newly created Named Range
            worksheets.get(0).cells.get("A1").formula = "NewNamedRange";

            // Insert the value in cell A3 which is being referenced in the Named Range
            worksheets.get(0).cells.get("A3").value = "This is the value of A3";

            // Calculate formulas
            book.calculateFormula();

            // Save the result in XLSX format
            const outputData = book.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and saved. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

### **名前付き範囲に複雑な式を設定する**
複雑な式は、動的な範囲や異なるワークシートの複数のセルにまたがる式など、さまざまなものになります。次の例は、INDEX 関数を使用して、リスト内の位置に基づいて値を取得する動的な範囲を作成します。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Named Range Example</title>
    </head>
    <body>
        <h1>Named Range Example</h1>
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
            const result = document.getElementById('result');
            const downloadLink = document.getElementById('downloadLink');

            if (!fileInput.files.length) {
                // If no file selected, we'll create a new workbook (mirrors JavaScript creating a new Workbook)
            }

            // Load workbook from file if provided, otherwise create a new empty workbook
            let book;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                book = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                book = new Workbook();
            }

            // Get the WorksheetCollection
            const worksheets = book.worksheets;

            // Add a new Named Range with name "data"
            let index = worksheets.names.count;
            worksheets.names.add("data");

            // Access the newly created Named Range from the collection
            const data = worksheets.names.get(index);

            // Set RefersTo property of the Named Range to a cell range in same worksheet
            data.refersTo = "=Sheet1!$A$1:$A$10";

            // Add another Named Range with name "range"
            index = worksheets.names.count;
            worksheets.names.add("range");

            // Access the newly created Named Range from the collection
            const range = worksheets.names.get(index);

            // Set RefersTo property to a formula using the Named Range data
            range.refersTo = "=INDEX(data,Sheet1!$A$1,1):INDEX(data,Sheet1!$A$1,9)";

            // Save the workbook
            const outputData = book.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            result.innerHTML = '<p style="color: green;">Named ranges added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

異なるワークシートの2つのセルから値を合計する名前付き範囲を使用するもう1つの例がこちら

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Named Range and Formula Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

        const initPromise = AsposeCells.onReady({
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
            await initPromise;

            // Creating a new Workbook
            const book = new Workbook();

            // Get the WorksheetCollection
            const worksheets = book.worksheets;

            // Insert some data in cell A1 of Sheet1
            worksheets.get("Sheet1").cells.get("A1").value = 10;

            // Add a new Worksheet and insert a value to cell A1
            const newIndex1 = worksheets.add();
            worksheets.get(newIndex1).cells.get("A1").value = 10;

            // Add a new Named Range with name "range"
            const index = worksheets.names.add("range");

            // Access the newly created Named Range from the collection
            const range = worksheets.names.get(index);

            // Set RefersTo property of the Named Range to a SUM function
            range.refersTo = "=SUM(Sheet1!$A$1,Sheet2!$A$1)";

            // Insert the Named Range as formula to 3rd worksheet
            const newIndex2 = worksheets.add();
            worksheets.get(newIndex2).cells.get("A1").formula = "range";

            // Calculate formulas
            book.calculateFormula();

            // Save the result in XLSX format and provide download link
            const outputData = book.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the generated file.</p>';
        });
    </script>
</html>
```
