---
title: データの検索または検索
type: docs
weight: 50
url: /ja/javascript-cpp/find-or-search-data/
description: 指定されたデータを含むセルを検索または見つける方法をC++ APIで学習します。
keywords: C++経由のJavaScriptでデータを検索する方法、C++経由のJavaScriptでデータを検索する方法、Excelのセルに式を含むセルを検索するJavaScript経由のC++、Excelのセルに式を含むセルを検索するJavaScript経由のC++、FindOptionsを使用してデータまたは式を検索するJavaScript経由のC++、FindOptionsを使用してデータまたは式を検索するJavaScript経由のC++、指定された文字列値または数値を含むセルを検索または見つけるJavaScript経由のC++、指定されたデータを含むセルを見つけるまたは検索する
---

{{% alert color="primary" %}}  
Microsoft Excelユーザーは、指定したデータを含むセルを見つけることができます。  
{{% /alert %}}  

## **指定されたデータを含むセルの検索**  

### **Microsoft Excel の使用**  

Microsoft Excelユーザーは、指定したデータを含むセルを見つけることができます。Microsoft Excelの[検索]メニューから[編集]を選択すると、検索値を指定できるダイアログが表示されます。  

ここでは、「オレンジ」の値を検索しています。Aspose.Cellsでは、指定された値を含むワークシート内のセルを検索できます。  

### **C++経由のAspose.Cells for JavaScriptの使用例**  

Aspose.Cellsは、Microsoft Excelファイルを表すクラス[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)を提供します。[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)クラスには、Excelファイルの各ワークシートにアクセスできる[**Workbook.worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--)コレクションが含まれます。ワークシートは[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)クラスは、ワークシート内のすべてのセルを表す[**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--)コレクションを提供します。[**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells)コレクションは、ユーザー指定のデータを含むセルを検索するためのさまざまなメソッドを提供します。これらのメソッドのいくつかについては、以下で詳述します。  

{{% alert color="primary" %}}  
すべての検索メソッドは、指定されたデータを検索するセルの参照を返します。  
{{% /alert %}}  

## **指定された数式を含むセルの検索**  

開発者は、[**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells)コレクションの[**find**](https://reference.aspose.com/cells/javascript-cpp/cells/#find-object-cell-findoptions-)メソッドを呼び出すことによって、指定された数式をワークシート内で見つけることができます。通常、[**find**](https://reference.aspose.com/cells/javascript-cpp/cells/#find-object-cell-findoptions-)メソッドは3つのパラメータを受け取ります。  

- 検索する対象のオブジェクト。その型はint、double、DateTime、string、boolである必要があります。  
- 前回と同じオブジェクトを含むセル。そのパラメータはnullに設定できます。  
- 必要なオブジェクトを見つけるためのオプション。  

以下の例では、検索メソッドの練習にワークシートデータを使用します:  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Find Cell Containing Formula</title>
    </head>
    <body>
        <h1>Find Cell Containing Formula</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, FindOptions, LookInType } = AsposeCells;

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

            // Instantiate FindOptions Object and set to look in formulas
            const findOptions = new FindOptions();
            findOptions.lookInType = LookInType.Formulas;

            // Finding the cell containing the specified formula
            const cell = worksheet.cells.find("=SUM(A5:A10)", null, findOptions);

            // Displaying the name of the cell found after searching worksheet
            document.getElementById('result').innerHTML = `<p style="color: green;">Name of the cell containing formula: ${cell.name}</p>`;
        });
    </script>
</html>
```  


## **FindOptionsを使用したデータまたは式の検索**  

さまざまな[**FindOptions**](https://reference.aspose.com/cells/javascript-cpp/findoptions)を用いて、[**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells)コレクションの[**Cells.find(object, Cell)**](https://reference.aspose.com/cells/javascript-cpp/cells/#find-object-cell-)メソッドを呼び出すことで、指定された値を検索可能です。通常、[**find**](https://reference.aspose.com/cells/javascript-cpp/cells/#find-object-cell-findoptions-)メソッドは次のパラメータを受け取ります。  

- **検索値**、検索するデータまたは値。  
- **前のセル**、同じ値を含んでいた最後のセル。最初から検索する場合は、このパラメーターをnullに設定できます。  
- **検索オプション**、検索オプション。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Find Using FindOptions</title>
    </head>
    <body>
        <h1>Find Using FindOptions Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, FindOptions, CellArea, LookInType, LookAtType } = AsposeCells;

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

            // Calculate formulas in workbook
            workbook.calculateFormula();

            // Get Cells collection from first worksheet
            const cells = workbook.worksheets.get(0).cells;

            // Instantiate FindOptions Object
            const findOptions = new FindOptions();

            // Create a Cells Area
            const ca = new CellArea();
            ca.startRow = 8;
            ca.startColumn = 2;
            ca.endRow = 17;
            ca.endColumn = 13;

            // Set cells area for find options
            findOptions.range = ca;

            // Set searching properties
            findOptions.searchBackward = false;
            findOptions.searchOrderByRows = true;

            // Set the lookintype, you may specify, values, formulas, comments etc.
            findOptions.lookInType = LookInType.Values;

            // Set the lookattype, you may specify Match entire content, endswith, startswith etc.
            findOptions.lookAtType = LookAtType.EntireContent;

            // Find the cell with value
            const cell = cells.find(341, null, findOptions);

            if (cell !== null) {
                document.getElementById('result').innerHTML = `<p>Name of the cell containing the value: ${cell.name}</p>`;
            } else {
                document.getElementById('result').innerHTML = '<p>Record not found</p>';
            }
        });
    </script>
</html>
```  


## **指定された文字列値を見つけることが可能です。異なる{2}を持つ{1}コレクション内に見つかった{0}メソッドを呼び出すことで。**  

同じ[**find**](https://reference.aspose.com/cells/javascript-cpp/cells/#find-object-cell-findoptions-)メソッドを[**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells)コレクションで呼び出し、さまざまな[**FindOptions**](https://reference.aspose.com/cells/javascript-cpp/findoptions)を用いて文字列値を検索できる。  

[**FindOptions.lookInType**](https://reference.aspose.com/cells/javascript-cpp/findoptions/#lookInType-lookintype-)と[**FindOptions.lookAtType**](https://reference.aspose.com/cells/javascript-cpp/findoptions/#lookAtType-lookattype-)のプロパティを指定します。以下の例では、これらのプロパティを使用してセルの文字列の最初、中央、最後にあるさまざまな数の文字列を持つセルを見つける方法を示しています。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Find Examples</h1>
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

            // Instantiate the workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get Cells collection
            const cells = workbook.worksheets.get(0).cells;

            const opts = new AsposeCells.FindOptions();
            opts.lookInType = AsposeCells.LookInType.Values;
            opts.lookAtType = AsposeCells.LookAtType.EntireContent;

            let messages = '';

            // Find the cell with the input integer or double
            let cell1 = cells.find(205, null, opts);

            if (cell1 !== null) {
                messages += '<p>Name of the cell containing the value: ' + cell1.name + '</p>';
            } else {
                messages += '<p>Record not found</p>';
            }

            // Find the cell with the input string
            let cell2 = cells.find("Items A", null, opts);

            if (cell2 !== null) {
                messages += '<p>Name of the cell containing the value: ' + cell2.name + '</p>';
            } else {
                messages += '<p>Record not found</p>';
            }

            // Find the cell containing the input string (partial match)
            opts.lookAtType = AsposeCells.LookAtType.Contains;
            let cell3 = cells.find("Data", null, opts);

            if (cell3 !== null) {
                messages += '<p>Name of the cell containing the value: ' + cell3.name + '</p>';
            } else {
                messages += '<p>Record not found</p>';
            }

            document.getElementById('result').innerHTML = messages;
        });
    </script>
</html>
``` 



## **高度なトピック**  
- [指定したスタイルのセルを見つける](/cells/ja/javascript-cpp/find-cells-with-specific-style/)  
- [セルの値がシングルクォートマークで始まるかどうかを検索](/cells/ja/javascript-cpp/find-if-the-cell-value-starts-with-single-quote-mark/)  
- [元の値を使用したデータの検索](/cells/ja/javascript-cpp/search-data-using-original-values/)
