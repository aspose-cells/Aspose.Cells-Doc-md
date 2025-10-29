---
title: Comment échelle une feuille de calcul avec JavaScript via C++
linktitle: Comment mettre à l échelle une feuille de calcul
type: docs
weight: 130
url: /fr/javascript-cpp/how-to-scale-a-worksheet/
description: Cet article vous montre un exemple de code expliquant comment mettre à l échelle une feuille de calcul en utilisant Aspose.Cells for JavaScript via C++.
keywords: JavaScript pour mettre à l échelle une feuille de calcul, Comment mettre à l échelle une feuille de calcul en utilisant JavaScript via C++, Mettre à l échelle une feuille en JavaScript via C++.
---

## **Scénarios d'utilisation possibles**
Mettre à l'échelle une feuille de calcul peut être utile pour diverses raisons, en fonction du contexte dans lequel vous travaillez. Voici quelques raisons courantes :
1. Adapter à la page : pour s'assurer que tout le contenu tient sur une seule page ou un nombre spécifique de pages lors de l'impression, ce qui facilite la lecture et la gestion sans avoir à faire défiler plusieurs pages.

1. Présentation : pour rendre la feuille de calcul plus organisée et professionnelle, notamment lorsqu'elle est partagée lors de réunions ou dans des rapports.

1. Lisibilité : pour ajuster la taille du texte et d'autres éléments pour une meilleure lisibilité, en particulier pour les personnes ayant des difficultés à lire de petites polices.

1. Gestion de l'espace : pour optimiser l'utilisation de l'espace sur une feuille de calcul, en veillant à ce qu'il n'y ait pas d'espace blanc inutile et que toutes les informations importantes soient visibles sans défilement excessif.

1. Visualisation des données : dans le cas de graphiques et de diagrammes, la mise à l'échelle peut aider à les rendre plus compréhensibles en ajustant leur taille pour s'adapter à l'espace disponible.

1. Cohérence : pour maintenir une apparence cohérente à travers plusieurs feuilles de calcul ou documents, ce qui est particulièrement important dans des contextes professionnels et éducatifs.

## **Comment mettre à l'échelle une feuille de calcul dans Excel**
Mettre à l'échelle une feuille de calcul dans Excel peut vous aider à faire tenir votre contenu sur une seule page ou un nombre spécifié de pages lors de l'impression. Voici les étapes pour mettre à l'échelle une feuille :

1. Ouvrir votre feuille de calcul : ouvrez la feuille Excel que vous souhaitez mettre à l'échelle.

1. Aller à l'onglet Mise en Page : cliquez sur l'onglet Mise en Page dans le ruban.

1. Groupe Mise à l’échelle : dans l'onglet Mise en Page, trouvez le groupe Mise à l’échelle. Vous avez ici des options pour ajuster la mise à l’échelle. Largeur : permet de spécifier le nombre de pages en largeur pour l'impression. Hauteur : permet de spécifier le nombre de pages en hauteur pour l'impression. Échelle : vous pouvez également définir un pourcentage de mise à l’échelle personnalisé.
<br>
<img src="1.png" width=60% />

1. Ajuster la largeur et la hauteur : définir la largeur et la hauteur selon le nombre de pages souhaité. Par exemple, définir les deux à 1 page si vous souhaitez que la feuille tienne sur une seule page.

1. Ajuster le pourcentage de mise à l’échelle (si nécessaire) : si vous préférez définir un pourcentage spécifique, ajustez la case Échelle. Par exemple, le réglage à 50 % réduira tout à la moitié de la taille.


## **Comment mettre à l'échelle une feuille de calcul en utilisant JavaScript via C++**
Aspose.Cells for JavaScript via C++ est une bibliothèque puissante pour travailler avec des fichiers Excel de manière programmatique. Pour mettre à l'échelle une feuille de calcul en utilisant Aspose.Cells, vous devez suivre ces étapes : charger [fichier d'exemple](sample.xlsx) et ajuster les paramètres d'impression afin que le contenu tienne sur le nombre souhaité de pages ou un pourcentage spécifique de la taille originale.

### **Exemple : Ajuster à la page**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Fit To Page Example</title>
    </head>
    <body>
        <h1>Fit Worksheet to One Page</h1>
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

            // Access the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Access the PageSetup object
            const pageSetup = sheet.pageSetup;

            // Set the worksheet to fit to 1 page wide and 1 page tall
            pageSetup.fitToPagesWide = 1;
            pageSetup.fitToPagesTall = 1;

            // Saving the modified workbook and providing a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_fit_to_page.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet fitted to one page. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
<br>
<img src="3.png" width=60% />

### **Exemple : Mettre à l'échelle en pourcentage**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Scale Worksheet</title>
    </head>
    <body>
        <h1>Scale Worksheet Example</h1>
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

            // Access the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Access the PageSetup object
            const pageSetup = sheet.pageSetup;

            // Set the scaling to a specific percentage (e.g., 75%)
            pageSetup.zoom = 75;

            // Save the modified workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_scaled_percentage.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Scaled Workbook';

            document.getElementById('result').innerHTML = '<p style="color: green;">Scaling applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
<br>
<img src="2.png" width=60% />
