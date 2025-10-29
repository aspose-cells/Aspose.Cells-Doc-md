---
title: Filtrer le projet VBA lors du chargement d un classeur avec JavaScript via C++
linktitle: Filtrer le projet VBA lors du chargement d un classeur
type: docs
weight: 140
url: /fr/javascript-cpp/filter-vba-project-while-loading-a-workbook/
description: Apprenez à filtrer les projets VBA lors du chargement des classeurs Excel en utilisant Aspose.Cells for JavaScript via C++.
---

## **Filtrer le projet VBA lors du chargement d’un classeur Excel en JavaScript via C++**

Certains fichiers .xlsm/.xslb contiennent une quantité extrêmement importante de macros (ou des macros très longues). Aspose.Cells for JavaScript via C++ chargera inconditionnellement ces métadonnées lors de l’ouverture de tels classeurs. Vous pourriez avoir besoin de contrôler cela [**LoadDataFilterOptions**](https://reference.aspose.com/cells/javascript-cpp/loaddatafilteroptions) lorsque vous souhaitez uniquement extraire les noms des feuilles pour un grand nombre de classeurs, évitant ainsi de charger ce contenu inutile. Ce filtre est fourni en introduisant une nouvelle option, [**LoadDataFilterOptions.VBA**](https://reference.aspose.com/cells/javascript-cpp/loaddatafilteroptions).

## **Code d'exemple**

Le code d'exemple suivant charge un classeur de telle sorte que seul le VBA est filtré. Un fichier exemple pour tester cette fonctionnalité peut être téléchargé à partir du lien suivant :

[sampleMacroEnabledWorkbook.xlsm](79527938.xlsm)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Sample Macro-Enabled Workbook to XLSM</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsm,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions, LoadFormat, LoadFilter, LoadDataFilterOptions } = AsposeCells;

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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel macro-enabled (.xlsm) file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Set the load options, we do not want to load VBA
            const loadOptions = new LoadOptions(LoadFormat.Auto);
            const loadFilter = new LoadFilter(LoadDataFilterOptions.All & ~LoadDataFilterOptions.VBA);
            loadOptions.loadFilter = loadFilter;

            // Create workbook object from uploaded file using load options
            const book = new Workbook(new Uint8Array(arrayBuffer), loadOptions);

            // Save the output in xlsm format
            const outputData = book.save(SaveFormat.Xlsm);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'OutputSampleMacroEnabledWorkbook.xlsm';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download OutputSampleMacroEnabledWorkbook.xlsm';

            document.getElementById('result').innerHTML = '<p style="color: green;">Processing completed. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
