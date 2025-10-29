---
title: Créer un objet Style en utilisant la classe CellsFactory
linktitle: Créer un objet Style en utilisant la classe CellsFactory
description: Apprenez comment créer un objet style de cellule en utilisant la classe CellsFactory dans Aspose.Cells for JavaScript via C++. Personnalisez l apparence des cellules de la feuille de calcul selon vos besoins.
keywords: Aspose.Cells, JavaScript via C++, feuille de calcul électronique, objet style, style de cellule, personnalisation
type: docs
weight: 70
url: /fr/javascript-cpp/create-style-object-using-cellsfactory-class/
---

## **Créer un objet Style en utilisant la classe CellsFactory**
Le code exemple suivant crée un objet [Style](https://reference.aspose.com/cells/javascript-cpp/style) en utilisant la classe [CellsFactory](https://reference.aspose.com/cells/javascript-cpp/cellsfactory) puis définit le style par défaut du classeur. Veuillez télécharger le [fichier Excel de sortie](5115153.xlsx) pour voir les résultats de ce code pour référence.


```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Create Workbook with Default Style</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellsFactory, BackgroundType, Color, Utils } = AsposeCells;

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
            // Create a Style object using CellsFactory class
            const cf = new CellsFactory();
            const st = cf.createStyle();

            // Set the Style fill color to Yellow
            st.pattern = BackgroundType.Solid;
            st.foregroundColor = Color.Yellow;

            // Create a workbook and set its default style using the created Style object
            const wb = new Workbook();
            wb.defaultStyle = st;

            // Save the workbook
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully. Click the download link to save the file.</p>';
        });
    </script>
</html>
```
