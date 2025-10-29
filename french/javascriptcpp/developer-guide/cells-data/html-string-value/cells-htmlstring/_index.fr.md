---
title: Gérer les chaînes HTML des cellules
type: docs
weight: 600
url: /fr/javascript-cpp/manage-cells-html-string/
description: Apprenez à gérer les chaînes HTML des cellules via le Script Aspose.Cells for JavaAPI C++.
keywords: Ajouter une chaîne HTML à l intérieur de la cellule JavaScript via C++, Définir une chaîne HTML à l intérieur de la cellule JavaScript via C++, Ajouter une chaîne HTML JavaScript via C++, Obtenir la chaîne HTML de la cellule JavaScript via C++, Gérer les chaînes HTML des cellules JavaScript via C++
---

## **Scénarios d'utilisation possibles**
 Lorsque vous devez définir des données stylisées pour une cellule spécifique, vous pouvez attribuer une chaîne HTML à la cellule. Bien sûr, vous pouvez également obtenir la chaîne HTML de la cellule. Le Script Aspose.Cells for JavaAPI C++ offre cette fonctionnalité. Aspose.Cells fournit les propriétés et méthodes suivantes pour vous aider à atteindre vos objectifs.
- [**Cell.htmlString(string)**](https://reference.aspose.com/cells/javascript-cpp/cell/#htmlString-string-)

## ** Obtenir et définir une chaîne HTML en utilisant le Script Aspose.Cells for JavaAPI C++**
Cet exemple montre comment :

1. Créer un classeur et ajouter des données.
1. Obtenez la cellule spécifique dans la première feuille de calcul.
1. Définir la chaîne HTML dans la cellule.
1. Obtenez la chaîne HTML de la cellule.

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
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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

            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Obtaining the reference of the newly added worksheet
            let ws = workbook.worksheets.get(0);
            let cells = ws.cells;

            // Setting the value to the cells
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

            let c3 = cells.get("C3");
            // set html string for C3 cell.
            c3.htmlString = "<b>test bold</b>";

            let c4 = cells.get("C4");
            // set html string for C4 cell.
            c4.htmlString = "<i>test italic</i>";

            // get the html string of specific cell.
            console.log(c3.htmlString);
            console.log(c4.htmlString);

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


## Sortie générée par le code d'exemple

La capture d'écran suivante montre la sortie du code d'exemple ci-dessus.

![todo:image_alt_text](htmlstring.png)
