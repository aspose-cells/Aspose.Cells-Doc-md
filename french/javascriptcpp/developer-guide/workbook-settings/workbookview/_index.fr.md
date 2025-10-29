---
title: Comment contrôler l affichage du classeur avec JavaScript via C++
linktitle: Comment contrôler la vue du classeur
type: docs
weight: 600
url: /fr/javascript-cpp/how-to-control-workbook-view/
description: Apprenez comment contrôler l affichage du classeur à travers le script Aspose.Cells for Java via l API C++.
keywords: Comment contrôler l affichage du classeur en JavaScript via C++, régler l affichage Excel en JavaScript via C++, opérer l affichage du classeur en JavaScript via C++, définir l affichage du classeur en JavaScript via C++, contrôler l affichage Excel en JavaScript via C++.
---

## **Scénarios d'utilisation possibles**
Lorsque vous devez ajuster l'affichage des pages Excel, vous devez savoir comment contrôler chaque module, comme les barres de défilement horizontale et verticale, si vous souhaitez cacher les fichiers Excel ouverts, etc. Le script Aspose.Cells for Java via C++ offre cette fonctionnalité. Le script Aspose.Cells for Java via C++ fournit les propriétés et méthodes suivantes pour vous aider à atteindre vos objectifs.

- [**WorkbookSettings.isHScrollBarVisible()**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#isHScrollBarVisible--)
- [**WorkbookSettings.isVScrollBarVisible()**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#isVScrollBarVisible--)
- [**WorkbookSettings.isHidden()**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#isHidden--)
- [**WorkbookSettings.isMinimized()**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#isMinimized--)
- [**WorkbookSettings.windowHeight**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#windowHeight--)
- [**WorkbookSettings.windowWidth**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#windowWidth--)
- [**WorkbookSettings.windowLeft**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#windowLeft--)
- [**WorkbookSettings.windowTop**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#windowTop--)

## **Comment contrôler l'affichage du classeur en utilisant le script Aspose.Cells for Java via C++**
Cet exemple montre comment :

1. Créer un classeur.
1. Ajouter des données aux cellules dans la première feuille de calcul.
1. Masquer les barres de défilement horizontales et verticales de la vue du classeur.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>Aspose.Cells Example - Create/Modify Workbook</h1>
        <p>Select an existing .xls/.xlsx file to modify, or leave empty to create a new workbook.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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
            // If a file is selected, open it; otherwise create a new workbook (matches original Node behavior)
            let workbook;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Obtaining the reference of the first worksheet
            const ws = workbook.worksheets.get(0);
            const cells = ws.cells;

            // Setting the value to the cells (converted putValue => value)
            let cell = cells.get("A1");
            cell.value = "Fruit";
            cell = cells.get("B1");
            cell.value = "Count";
            cell = cells.get("C1");
            cell.value = "Price";

            cell = cells.get("A2");
            cell.value = "Apple";
            cell = cells.get("A3");
            cell.value = "Mango";
            cell = cells.get("A4");
            cell.value = "Blackberry";
            cell = cells.get("A5");
            cell.value = "Cherry";

            cell = cells.get("B2");
            cell.value = 5;
            cell = cells.get("B3");
            cell.value = 3;
            cell = cells.get("B4");
            cell.value = 6;
            cell = cells.get("B5");
            cell.value = 4;

            cell = cells.get("C2");
            cell.value = 5;
            cell = cells.get("C3");
            cell.value = 20;
            cell = cells.get("C4");
            cell.value = 30;
            cell = cells.get("C5");
            cell.value = 60;

            // Apply style: createStyle(), font/color adjustments converted from get/set to properties
            cell = cells.get("E10");
            const temp = workbook.createStyle();
            temp.font.color = AsposeCells.Color.Red;
            cell.style = temp;

            // Hide horizontal and vertical scrollbars (converted getSettings().set... -> settings.is... = ...)
            workbook.settings.isHScrollBarVisible = false;
            workbook.settings.isVScrollBarVisible = false;

            // Save the modified workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

Aperçu du fichier résultat:
<br>
<image src="result.png" width="70%" />
