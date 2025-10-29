---
title: Créer, manipuler ou supprimer des scénarios des feuilles de calcul avec JavaScript via C++
linktitle: Gérer des scénarios
type: docs
weight: 190
url: /fr/javascript-cpp/create-manipulate-or-remove-scenarios-from-worksheets/
description: Apprenez comment créer, manipuler ou supprimer des scénarios dans les feuilles Excel de manière programmatique en utilisant JavaScript via l API C++.
keywords: Créer un scénario dans une feuille JavaScript via C++, supprimer un scénario dans une feuille Excel JavaScript via C++, manipuler un scénario dans une feuille de calcul JavaScript via C++
---

{{% alert color="primary" %}}

Parfois, vous devez créer, manipuler ou supprimer des scénarios dans des feuilles de calcul. Un scénario est un modèle nommé de 'et si ?' qui inclut des cellules d'entrée variables liées par une ou plusieurs formules. Avant de créer un scénario, concevez la feuille de calcul de manière à ce qu'elle contienne au moins une formule dépendant de cellules dans lesquelles différentes valeurs peuvent être insérées. L'exemple suivant montre comment créer et supprimer des scénarios à partir d'une feuille de calcul dans un classeur via les API Aspose.Cells.

{{% /alert %}}

Aspose.Cells fournit quelques classes utiles, par exemple, [**ScenarioCollection**](https://reference.aspose.com/cells/javascript-cpp/scenariocollection), [**Scenario**](https://reference.aspose.com/cells/javascript-cpp/scenario), [**ScenarioInputCellCollection**](https://reference.aspose.com/cells/javascript-cpp/scenarioinputcellcollection), et [**ScenarioInputCell**](https://reference.aspose.com/cells/javascript-cpp/scenarioinputcell). Elle offre également la propriété [**Worksheet.scenarios**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#scenarios--). Le code exemple ci-dessous ouvre un fichier Excel XLSX contenant quelques scénarios et supprime un scénario existant. Il ajoute également un nouveau scénario dans la feuille avant de sauvegarder le fichier Excel. L'exemple utilise un fichier modèle très simple contenant un scénario.

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
