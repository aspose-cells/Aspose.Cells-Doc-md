---
title: JavaScript を C++ で使用して前提セルと従属セルを追跡
linktitle: 先行および従属
type: docs
weight: 230
url: /ja/javascript-cpp/precedents-and-dependents/
description: Aspose.Cells for JavaScript を C++ で使用してスプレッドシート内の前提セルと従属セルを追跡する方法を学び、複雑な財務ワークシートのリンクされたセルを特定する方法を理解します。
---

{{% alert color="primary" %}} 

特に共同で開発された複雑な財務ワークシートは、最も恥ずかしいエラーを隠すことがあります。式の正確さをチェックし、エラーの原因を特定することは、先行セルおよび従属セルを使用する式をチェックする際に困難になるかもしれません。

{{% /alert %}} 
## **紹介**
- **先行セル** は、他のセルの数式で参照されているセルです。たとえば、セル D10 が数式 =B5 を含む場合、セル B5 はセル D10 の先行セルです。
- **従属セル** は、他のセルを参照する数式を含むセルです。例えば、セル D10 に式 `=B5` がある場合、D10 は B5 に依存しています。

スプレッドシートをわかりやすくするために、スプレッドシートに含まれるセルが式で使用されているかを明確に表示することがあります。同様に、他のセルの従属セルを抽出することがあります。

Aspose.Cells を使用すると、セルをトレースしてリンクされているセルを特定することができます。
## **先行および従属セルのトレース： Microsoft Excel**
例えば、セル C1 が式を含む C3 および C4 に依存しており、C1 が変更される場合（つまり式が上書きされる場合）、C3 および C4 などの他のセルは、ビジネスルールに基づいてスプレッドシートをバランスさせるために変更する必要があります。

同様に、C1 に式 "=(B1*22)/(M2*N32)" を含むとします。C1 が依存しているセルである先行セル B1、M2、N32 を見つけたいとします。

特定のセルの依存関係を他のセルにトレースする必要があるかもしれません。ビジネスルールが式に埋め込まれている場合、依存関係を見つけ、それに基づいていくつかのルールを実行したいと思うかもしれません。同様に、特定のセルの値が変更される場合、その変更に影響を受けるワークシート内のセルを見つけたいと思うかもしれません。

Microsoft Excel を使用すると、先行および従属をトレースすることができます。

1. **表示ツールバー**から**数式監査**を選択します。数式監査ダイアログが表示されます。
1. 先行をトレース：
   1. 先行セルを特定したい式を含むセルを選択します。
   1. 直接データを提供する各セルにトレーサーアローを表示するには、 **式監査** ツールバーの **先行をトレース** をクリックします。
1. 特定のセルを参照する式をトレースする（従属）
   1. 従属セルを特定したいセルを選択します。
   1. アクティブセルに依存する各セルにトレーサー矢印を表示するには、数式監査ツールバーの **参照先トレース** をクリックします。
## **先行および従属セルをトレース： Aspose.Cells**
### **先行をトレース**
Aspose.Cells を使用すると、先行セルを取得することが容易になります。シンプルな式の先行セルに提供されているセルだけでなく、名前付き範囲で複雑な式の先行セルに提供されているセルを見つけることもできます。

以下の例では、テンプレートの Excel ファイルである Book1.xls を使用しています。スプレッドシートには最初のワークシートにデータと数式が含まれています。

Aspose.Cells は、[Cell](https://reference.aspose.com/cells/javascript-cpp/cell) クラスの [Cell.precedents()](https://reference.aspose.com/cells/javascript-cpp/cell/#precedents--) メソッドを提供し、セルの前提セルを追跡します。これは参照範囲のコレクションを返します。上記の例では、Book1.xls のセル B7 に "=SUM(A1:A3)" という数式があり、A1:A3 のセルが B7 の前提セルです。次の例は、テンプレートファイル Book1.xls を使用した前提セル追跡機能のデモです。


```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Get Cell Precedents Example</h1>
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

            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet's cells
            const cells = workbook.worksheets.get(0).cells;

            // Get cell B4
            const cell = cells.get("B4");

            if (cell) {
                // Get precedents (converted from getPrecedents)
                const ret = cell.precedents;

                if (!ret.isNull() && ret.count > 0) {
                    const area = ret.get(0);

                    const sheetName = area.sheetName;
                    const startAddress = AsposeCells.CellsHelper.cellIndexToName(area.startRow, area.startColumn);
                    const endAddress = AsposeCells.CellsHelper.cellIndexToName(area.endRow, area.endColumn);

                    console.log(sheetName);
                    console.log(startAddress);
                    console.log(endAddress);

                    document.getElementById('result').innerHTML = `<pre>Sheet: ${sheetName}\nStart: ${startAddress}\nEnd: ${endAddress}</pre>`;
                } else {
                    document.getElementById('result').innerHTML = '<p style="color: red;">No precedents found for the cell.</p>';
                }
            } else {
                document.getElementById('result').innerHTML = '<p style="color: red;">Cell B4 is null.</p>';
            }
        });
    </script>
</html>
```
### **従属をトレース**
Aspose.Cellsは、スプレッドシート内の依存セルを取得できます。Aspose.Cellsは、単純な数式のデータを提供するセルだけでなく、名前付き範囲を含む複雑な数式の従属セルも見つけることができます。

Aspose.Cells は、[Cell](https://reference.aspose.com/cells/javascript-cpp/cell) クラスの [Cell.dependents(boolean)](https://reference.aspose.com/cells/javascript-cpp/cell/#dependents-boolean-) メソッドを提供し、セルの従属セルを追跡します。例えば、Book1.xlsx の B2 に "=A1+20"、C2 に "=A1+30" の数式があり、これらの例を示します。


```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Get Cell Dependents Example</h1>
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

            // Loads the workbook which contains hidden external links
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            const cells = workbook.worksheets.get(0).cells;
            const cell = cells.get("B2");
            // Ensure dependents is accessed as a property (converted from getDependents)
            const dependents = cell.dependents;

            if (Array.isArray(dependents)) {
                let out = '<p>Dependents found:</p><ul>';
                for (const c of dependents) {
                    console.log(c.name);
                    out += `<li>${c.name}</li>`;
                }
                out += '</ul>';
                resultDiv.innerHTML = out;
            } else {
                console.error("Dependents is not an array");
                resultDiv.innerHTML = '<p style="color: red;">Dependents is not an array</p>';
            }
        });
    </script>
</html>
```
### **計算チェーンに従って直前および依存セルを追跡する**
 上記の前提セルと従属セルの追跡APIは、数式式そのものに基づいています。これは、複数の数式の内部依存関係を追跡するための便利な方法です。ワークブックに多くの数式がある場合や、全セルの前提セルと従属セルを追跡する必要がある場合、パフォーマンスは低下します。その場合、[Cell.precedentsInCalculation()](https://reference.aspose.com/cells/javascript-cpp/cell/#precedentsInCalculation--) と [Cell.dependentsInCalculation(boolean)](https://reference.aspose.com/cells/javascript-cpp/cell/#dependentsInCalculation-boolean-) 方法の使用を検討してください。これらの2つのメソッドは、計算チェーンに従った依存関係を追跡します。使用前に [FormulaSettings.enableCalculationChain()](https://reference.aspose.com/cells/javascript-cpp/formulasettings/#enableCalculationChain--) で計算チェーンを有効にし、その後 [Workbook.calculateFormula()](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--) でワークブックの完全な計算を行う必要があります。その後、必要なセルの前提セルや従属セルを追跡できます。

 一部の数式については、前提セルや従属セルの結果が [precedents] と [precedentsInCalculation] で異なる場合や、[dependents] と [dependentsInCalculation] で異なる場合があります。例えば、セルA1の数式が "=IF(TRUE,B2,C3)" の場合、前提セルはB2とC3です。同時に、依存セルとしてA1に向かいます。ただし、この数式の計算では、B2 のみが結果に影響します。したがって、precedentsInCalculation では C3 を提供せず、dependentsInCalculation では A1 を提供しません。場合によっては、現在のワークブックのデータに基づき、実際に計算結果に影響を与える内部依存関係だけを追跡したい場合もあります。その場合、dependentsInCalculation と precedentsInCalculation の使用を検討してください。

次の例は、計算チェーンに沿って前提セルと従属セルを追跡する方法を示しています:


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
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '';
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet and its cells
            const cells = workbook.worksheets.get(0).cells;

            // Setting formulas
            cells.get("A1").formula = "=B1+SUM(B1:B10)+[Book1.xls]Sheet1!B2";
            cells.get("A2").formula = "=IF(TRUE,B2,B1)";

            // Enable calculation chain
            workbook.settings.formulaSettings.enableCalculationChain = true;

            // Calculate formulas
            workbook.calculateFormula();

            // Collect output
            let output = '';

            let en = cells.get("B1").dependentsInCalculation;
            output += "B1's calculation dependents:\n";
            if (en && en.length !== undefined) {
                for (var cell of en) {
                    output += (cell.name || '') + "\n";
                }
            } else if (en) {
                // If it's an iterable but doesn't have length
                for (var cell of en) {
                    output += (cell.name || '') + "\n";
                }
            }
            output += "\n";

            en = cells.get("B2").dependentsInCalculation;
            output += "B2's calculation dependents:\n";
            if (en && en.length !== undefined) {
                for (var cell of en) {
                    output += (cell.name || '') + "\n";
                }
            } else if (en) {
                for (var cell of en) {
                    output += (cell.name || '') + "\n";
                }
            }
            output += "\n";

            en = cells.get("A1").precedentsInCalculation;
            output += "A1's calculation precedents:\n";
            if (en && en.length !== undefined) {
                for (var area of en) {
                    output += area.toString() + "\n";
                }
            } else if (en) {
                for (var area of en) {
                    output += area.toString() + "\n";
                }
            }
            output += "\n";

            en = cells.get("A2").precedentsInCalculation;
            output += "A2's calculation precedents:\n";
            if (en && en.length !== undefined) {
                for (var area of en) {
                    output += area.toString() + "\n";
                }
            } else if (en) {
                for (var area of en) {
                    output += area.toString() + "\n";
                }
            }

            resultDiv.innerHTML = '<pre>' + output.replace(/</g, '&lt;') + '</pre>';

            // Save the modified workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';
        });
    </script>
</html>
```
