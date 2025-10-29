---
title: 使用C++通过JavaScript追踪前导和依赖单元格
linktitle: 先例和从属
type: docs
weight: 230
url: /zh/javascript-cpp/precedents-and-dependents/
description: 学习如何使用C++通过Aspose.Cells for JavaScript追踪电子表格中的前导和依赖单元格。了解如何识别复杂财务工作表中的链接单元。
---

{{% alert color="primary" %}} 

复杂的财务工作表，尤其是合作开发的工作表，可能隐藏最令人尴尬的错误。当公式使用先例单元格和从属单元格时，检查公式的准确性并找到错误的来源可能很困难。

{{% /alert %}} 
## **介绍**
- **前代单元格** 是由另一个单元格的公式引用的单元格。例如，如果单元格D10包含公式=B5，则单元格B5是单元格D10的前代。
- **依赖单元格**包含引用其他单元格的公式。例如，若单元格D10包含公式 =B5，D10依赖于B5单元格。

为了使电子表格易于阅读，您可能希望清楚地显示电子表格中用于公式的单元格。同样，您可能需要提取其他单元格的依赖单元格。

Aspose.Cells 允许您跟踪单元格并找出哪些是相互关联的。
## **跟踪先例和依赖单元格：Microsoft Excel**
公式可能会根据客户做出的修改而改变。例如，如果单元格 C1 依赖于包含公式的 C3 和 C4，并且更改了 C1（使公式被覆盖），则根据业务规则需要更改 C3 和 C4，或其他单元格，以使电子表格保持平衡。

类似地，假设 C1 包含公式"=(B1*22)/(M2*N32)"。我想找到 C1 依赖的单元格，即先例单元格 B1、M2 和 N32。

您可能需要跟踪特定单元格到其他单元格的依赖关系。如果业务规则嵌入在公式中，我们希望找出依赖关系，并根据此执行一些规则。同样，如果特定单元格的值被修改，那么工作表中哪些单元格受到此变化的影响？

Microsoft Excel 允许用户跟踪先例和依赖。

1. 在**查看工具栏**上选择**公式审计**。将显示公式审计对话框。
1. 跟踪先例：
   1. 选择包含您想要查找先例单元格的公式的单元格。
   1. 要向每个直接提供数据给活动单元格的单元格显示跟踪箭头，请单击**公式审计**工具栏上的**跟踪先例**。
1. 跟踪引用特定单元格的公式（依赖项）
   1. 选择要识别其依赖单元格的单元格。
   1. 若要在依赖于活动单元格的每个单元格上显示追踪箭头，请点击公式审计工具栏上的**追踪依赖项**。
## **跟踪先例和依赖单元格：Aspose.Cells**
### **跟踪先例**
Aspose.Cells 使得获取先例单元格变得容易。它不仅可以检索为简单公式先例提供数据的单元格，还可以找到为具有命名范围的复杂公式先例提供数据的单元格。

在下面的示例中，使用了模板Excel文件《Book1.xls》。电子表格在第一个工作表上包含数据和公式。

Aspose.Cells提供[Cell](https://reference.aspose.com/cells/javascript-cpp/cell)类的[Cell.precedents()](https://reference.aspose.com/cells/javascript-cpp/cell/#precedents--)方法，用于追踪一个单元格的前导。它返回一个引用区域的集合。如上所示，在Book1.xls中，单元格B7包含公式"=SUM(A1:A3)"。因此，A1:A3是B7的前导单元。以下示例演示了使用模板文件Book1.xls进行追踪前导的功能。


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
### **跟踪依赖项**
Aspose.Cells 让你能够获取电子表格中的依赖单元格。Aspose.Cells 不仅可以检索提供简单公式数据的单元格，还能找到为复杂公式依赖项提供数据的带有命名范围的单元格。

Aspose.Cells提供[Cell](https://reference.aspose.com/cells/javascript-cpp/cell)类的[Cell.dependents(boolean)](https://reference.aspose.com/cells/javascript-cpp/cell/#dependents-boolean-)方法，用于追踪某个单元格的依赖。比如在Book1.xlsx中，B2和C2单元格中有公式：“=A1+20”和“=A1+30”。以下示例演示如何使用模板文件Book1.xlsx追踪A1的依赖单元。


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
### **根据计算链跟踪先行单元格和依赖单元格**
上述追踪前导和依赖单元的API是根据公式表达式本身设计的。它们为用户提供了一种方便的方式来追踪少数公式的相互依赖关系。如果工作簿中有大量公式且用户需要对每个单元格进行追踪，性能会变差。对于这种情况，用户应考虑使用[Cell.precedentsInCalculation()](https://reference.aspose.com/cells/javascript-cpp/cell/#precedentsInCalculation--)和[Cell.dependentsInCalculation(boolean)](https://reference.aspose.com/cells/javascript-cpp/cell/#dependentsInCalculation-boolean-)方法。这两个方法根据计算链追踪依赖关系。因此，你需要先启用计算链[FormulaSettings.enableCalculationChain()](https://reference.aspose.com/cells/javascript-cpp/formulasettings/#enableCalculationChain--)，然后通过[Workbook.calculateFormula()](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--)对工作簿进行全面计算。之后，就可以对所有需要追踪的单元格进行前导或依赖追踪了。

对于某些公式，前导结果可能与precedes和precedesInCalculation不同，依赖关系可能与dependents和dependentsInCalculation不同。例如，单元格A1的公式为"=IF(TRUE,B2,C3)"，precedes将提供B2和C3为A1的前导。而在依赖检查中，B2和C3都依赖A1。然而，对于该公式的计算，显然只有B2会影响结果。因此，依赖关系中的dependentsInCalculation不会提供C3，precedesInCalculation也不会提供C3。有时候用户仅需要追踪那些真正影响基于当前数据的公式计算结果的相互依赖关系，此时应使用dependentsInCalculation或precedesInCalculation，而非dependents或precedes。

以下示例演示如何根据计算链追踪单元格的前置项和依赖项：


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
