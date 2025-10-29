---
title: 使用C++的JavaScript创建、操作或删除工作表中的方案
linktitle: 管理场景
type: docs
weight: 190
url: /zh/javascript-cpp/create-manipulate-or-remove-scenarios-from-worksheets/
description: 学习如何通过C++ API以编程方式创建、操作或删除Excel工作表中的方案。
keywords: 通过C++的JavaScript创建方案工作表，删除方案工作表，操作方案工作表
---

{{% alert color="primary" %}}

有时，您需要在电子表格中创建、操作或删除方案。方案是一个命名的“假设”模型，其中包含由一个或多个公式链接的可变输入单元格。在创建方案之前，设计工作表，使其至少包含一个依赖于可以插入不同值的单元格的公式。以下示例演示了如何通过Aspose.Cells API在工作簿中的工作表中创建和删除方案。

{{% /alert %}}

 Aspose.Cells提供一些有用的类，例如[**ScenarioCollection**](https://reference.aspose.com/cells/javascript-cpp/scenariocollection)、[**Scenario**](https://reference.aspose.com/cells/javascript-cpp/scenario)、[**ScenarioInputCellCollection**](https://reference.aspose.com/cells/javascript-cpp/scenarioinputcellcollection)和[**ScenarioInputCell**](https://reference.aspose.com/cells/javascript-cpp/scenarioinputcell)类。还提供[**Worksheet.scenarios**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#scenarios--)属性。下面的示例代码打开一个包含一些场景的Excel文件（XLSX格式），删除一个现有的场景，并在保存前向工作表中添加一个新场景。示例使用非常简单的模板文件。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Scenarios Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Scenarios Example</h1>
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

            // Instantiate the Workbook by loading the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            if (worksheet.scenarios.count > 0) {
                // Remove the existing first scenario from the sheet
                worksheet.scenarios.removeAt(0);
            }

            // Create a scenario
            const i = worksheet.scenarios.add("MyScenario");
            // Get the scenario
            const scenario = worksheet.scenarios.get(i);
            // Add comment to it
            scenario.comment = "Test scenario is created.";
            // Get the input cells for the scenario
            const sic = scenario.inputCells;
            // Add the scenario on B4 (as changing cell) with default value
            sic.add(3, 1, "1100000");

            // Save the Excel file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outBk_scenarios1.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Process completed successfully. File ready for download.</p>';
        });
    </script>
</html>
```
