---
title: Comment filtrer les cellules vides ou non vides
type: docs
weight: 85
url: /fr/javascript-cpp/how-to-filter-blanks-and-non-blanks/
description: Apprenez comment filtrer les valeurs vides et non vides en utilisant le script Aspose.Cells for Java via API C++.
keywords: Filtrer les cellules vides, Filtrer les cellules non vides, Filtrer les cellules vides dans la feuille de calcul, Filtrer les cellules non vides dans la feuille de calcul, Filtrer les cellules vides dans Excel, Filtrer les cellules non vides dans Excel, Filtrer les cellules vides et non vides dans Excel
---

## **Scénarios d'utilisation possibles**
Filtrer les données dans Excel est un outil précieux qui améliore l'analyse, l'exploration et la présentation des données en permettant aux utilisateurs de se concentrer sur des sous-ensembles spécifiques de données en fonction de leurs critères, rendant ainsi le processus global de manipulation et d'interprétation des données plus efficace et plus efficace.

## **Comment filtrer les cellules vides ou non vides dans Excel**
Dans Excel, vous pouvez facilement filtrer les cellules vides ou non vides en utilisant les options de filtrage. Voici comment vous pouvez le faire :

### **Comment filtrer les cellules vides dans Excel**
1. Sélectionnez la plage : Cliquez sur la lettre de l'en-tête de colonne pour sélectionner la colonne entière ou sélectionnez la plage où vous souhaitez filtrer les cellules vides.
1. Ouvrez le menu Filtre : Allez à l'onglet "Données" dans le ruban.
<br>
<image src="1.png" width="70%" />
1. Options de filtre : Cliquez sur le bouton "Filtrer". Cela ajoutera des flèches de filtre à la plage sélectionnée.
1. Filtrer les cellules vides : Cliquez sur la flèche de filtrage dans la colonne que vous souhaitez filtrer les cellules vides. Désélectionnez toutes les options sauf « Vides » et cliquez sur OK. Cela affichera uniquement les cellules vides de cette colonne.
<br>
<image src="2.png" width="70%" />
1. Le résultat est le suivant :
<br>
<image src="3.png" width="70%" />

### **Comment filtrer les cellules non vides dans Excel**
1. Sélectionnez la plage : Cliquez sur la lettre de l'en-tête de colonne pour sélectionner la colonne entière ou sélectionnez la plage où vous souhaitez filtrer les cellules non vides.
1. Ouvrez le menu Filtre : Allez à l'onglet "Données" dans le ruban.
<br>
<image src="1.png" width="70%" />
1. Options de filtre : Cliquez sur le bouton "Filtrer". Cela ajoutera des flèches de filtre à la plage sélectionnée.
1. Filtrer les cellules non vides : Cliquez sur la flèche de filtre dans la colonne que vous souhaitez filtrer pour les cellules non vides. Désélectionnez toutes les options sauf "Non vides" ou "Personnalisé" et définissez les conditions en conséquence. Cliquez sur OK. Cela affichera uniquement les cellules qui ne sont pas vides dans cette colonne.
<br>
<image src="4.png" width="70%" />
1. Le résultat est le suivant :
<br>
<image src="5.png" width="70%" />

## **Comment filtrer les valeurs vides avec le script Aspose.Cells for Java via C++**
Si une colonne contient du texte tel que quelques cellules sont vides, et qu'il est nécessaire de filtrer ces lignes uniquement où des cellules vides sont présentes, les fonctions [**AutoFilter.matchBlanks(number)**](https://reference.aspose.com/cells/javascript-cpp/autofilter/#matchBlanks-number-) et [**AutoFilter.addFilter(number, string)**](https://reference.aspose.com/cells/javascript-cpp/autofilter/#addFilter-number-string-) peuvent être utilisées comme démontré ci-dessous. 

Veuillez consulter le code d'exemple suivant qui charge le [fichier Excel d'exemple](sample.xlsx) contenant certaines données fictives. Le code d'exemple utilise trois méthodes pour filtrer les cellules vides. Ensuite, il enregistre le classeur sous forme de [fichier Excel de sortie](FilteredBlanks.xlsx). 

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Apply Filter for Blank Cells Example</h1>
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            const worksheet = workbook.worksheets.get(0);

            worksheet.autoFilter.addFilter(1, null);
            worksheet.autoFilter.refresh();

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'FilteredBlanks.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download FilteredBlanks.xlsx';

            resultDiv.innerHTML = '<p style="color: green;">Filter applied and file ready for download.</p>';
        });
    </script>
</html>
```


## **Comment filtrer les valeurs non vides avec le script Aspose.Cells for Java via C++**

Veuillez voir l'exemple de code suivant qui charge le [fichier Excel d'exemple](sample.xlsx) contenant des données fictives. Après avoir chargé le fichier, appelez la fonction [AutoFilter.matchNonBlanks(number)](https://reference.aspose.com/cells/javascript-cpp/autofilter/#matchNonBlanks-number-) pour filtrer les données non vides, et enfin sauvegardez le classeur sous forme de [fichier Excel de sortie](FilteredNonBlanks.xlsx). 

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Filter NonBlanks Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Call MatchNonBlanks function to apply the filter
            worksheet.autoFilter.matchNonBlanks(1);

            // Call refresh function to update the worksheet
            worksheet.autoFilter.refresh();

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'FilteredNonBlanks.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Filtered Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Filter applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
