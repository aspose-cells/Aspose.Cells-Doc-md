---
title: Szenarien in Arbeitsblättern mit JavaScript über C++ erstellen, bearbeiten oder entfernen
linktitle: Szenarien verwalten
type: docs
weight: 190
url: /de/javascript-cpp/create-manipulate-or-remove-scenarios-from-worksheets/
description: Erfahren Sie, wie Sie Szenarien in Excel Arbeitsblättern programmatisch mit JavaScript über C++ API erstellen, manipulieren oder entfernen.
keywords: Szenario Arbeitsblatt mit JavaScript über C++ erstellen, Szenarien in Excel Arbeitsblättern mit JavaScript über C++ entfernen, Szenarien in Arbeitsblättern mit JavaScript über C++ manipulieren
---

{{% alert color="primary" %}}

Manchmal müssen Sie Szenarien in Tabellenkalkulationen erstellen, manipulieren oder löschen. Ein Szenario ist ein benanntes 'Was-wäre-wenn?'-Modell, das variable Eingabezellen enthält, die durch eine oder mehrere Formeln verknüpft sind. Vor dem Erstellen eines Szenarios entwerfen Sie das Arbeitsblatt so, dass es mindestens eine Formel enthält, die von Zellen abhängt, in die unterschiedliche Werte eingegeben werden können. Das folgende Beispiel zeigt, wie Sie Szenarien in einem Arbeitsblatt einer Arbeitsmappe über die Aspose.Cells-APIs erstellen und entfernen.

{{% /alert %}}

Aspose.Cells bietet einige nützliche Klassen, zum Beispiel die Klassen [**ScenarioCollection**](https://reference.aspose.com/cells/javascript-cpp/scenariocollection), [**Scenario**](https://reference.aspose.com/cells/javascript-cpp/scenario), [**ScenarioInputCellCollection**](https://reference.aspose.com/cells/javascript-cpp/scenarioinputcellcollection) und [**ScenarioInputCell**](https://reference.aspose.com/cells/javascript-cpp/scenarioinputcell). Es bietet auch die Eigenschaft [**Worksheet.scenarios**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#scenarios--). Der folgende Beispielcode öffnet eine XLSX-Excel-Datei, die einige Szenarien enthält, entfernt ein bestehendes Szenario und fügt vor dem Speichern der Excel-Datei ein neues Szenario hinzu. Das Beispiel verwendet eine sehr einfache Vorlage, die ein Szenario enthält.

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
