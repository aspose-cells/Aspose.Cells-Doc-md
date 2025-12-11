---
title: Create, Manipulate or Remove Scenarios from Worksheets with JavaScript via C++
linktitle: Manage Scenarios
type: docs
weight: 190
url: /javascript-cpp/create-manipulate-or-remove-scenarios-from-worksheets/
description: Learn how to create, manipulate, or remove scenarios from Excel Worksheets programmatically using JavaScript via C++ API.
keywords: create scenario worksheet JavaScript via C++, remove scenario excel worksheet JavaScript via C++, manipulate scenario worksheet JavaScript via C++
---

{{% alert color="primary" %}}

Sometimes, you need to create, manipulate, or delete scenarios in spreadsheets. A scenario is a named “what‑if?” model that includes variable input cells linked by one or more formulas. Before creating a scenario, design the worksheet so that it contains at least one formula that depends on cells into which different values can be inserted. The following example shows how to create and remove scenarios from a worksheet in a workbook via Aspose.Cells APIs.

{{% /alert %}}

Aspose.Cells provides some useful classes, for example, [**ScenarioCollection**](https://reference.aspose.com/cells/javascript-cpp/scenariocollection), [**Scenario**](https://reference.aspose.com/cells/javascript-cpp/scenario), [**ScenarioInputCellCollection**](https://reference.aspose.com/cells/javascript-cpp/scenarioinputcellcollection), and [**ScenarioInputCell**](https://reference.aspose.com/cells/javascript-cpp/scenarioinputcell) classes. It also provides the [**Worksheet.scenarios**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#scenarios--) property. The sample code below opens an XLSX Excel file that contains some scenarios and removes an existing scenario. It also adds a new scenario to the worksheet before saving the Excel file. The example uses a very simple template file that contains a scenario.

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

            // Access the first worksheet
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
            // Add the scenario on B4 (as the changing cell) with default value
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