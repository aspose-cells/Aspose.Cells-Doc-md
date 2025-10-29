---
title: Создавать, манипулировать или удалять сценарии в листах с помощью JavaScript через C++
linktitle: Управление сценариями
type: docs
weight: 190
url: /ru/javascript-cpp/create-manipulate-or-remove-scenarios-from-worksheets/
description: Узнайте, как создавать, манипулировать или удалять сценарии в листах Excel программно с помощью API JavaScript через C++.
keywords: создавать сценарий листа JavaScript через C++, удалять сценарий листа Excel JavaScript через C++, манипулировать сценарием листа JavaScript через C++
---

{{% alert color="primary" %}}

Иногда вам может понадобиться создавать, изменять или удалять сценарии в электронных таблицах. Сценарий - это именованная модель «что если?», которая включает в себя переменные ввода, связанные одной или несколькими формулами. Перед созданием сценария разработайте лист книги так, чтобы в нем была по крайней мере одна формула, зависимая от ячеек, в которые можно вводить различные значения. В следующем примере показано, как создавать и удалять сценарии из листа книги в книге с помощью API Aspose.Cells.

{{% /alert %}}

Aspose.Cells предоставляет полезные классы, например, [**ScenarioCollection**](https://reference.aspose.com/cells/javascript-cpp/scenariocollection), [**Scenario**](https://reference.aspose.com/cells/javascript-cpp/scenario), [**ScenarioInputCellCollection**](https://reference.aspose.com/cells/javascript-cpp/scenarioinputcellcollection) и [**ScenarioInputCell**](https://reference.aspose.com/cells/javascript-cpp/scenarioinputcell). Также есть свойство [**Worksheet.scenarios**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#scenarios--). В примере кода ниже открывается файл XLSX, содержащий сценарии, и удаляется существующий сценарий. Также добавляется новый сценарий перед сохранением файла Excel. В качестве шаблона используется очень простой файл, содержащий сценарий.

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
