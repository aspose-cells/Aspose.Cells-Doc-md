---
title: Comment définir les titres d impression avec JavaScript via C++
linktitle: Comment définir des titres d impression
type: docs
weight: 200
url: /fr/javascript-cpp/how-to-set-print-titles/
description: Cet article vous montre comment définir les titres d impression en utilisant la bibliothèque Aspose.Cells pour JavaScript via C++.
keywords: Imprimer les lignes et colonnes en boucle, JavaScript Comment définir les titres d impression, Définir et effacer les titres d impression avec JavaScript, Comment effacer les titres d impression en JavaScript, Comment ajouter des titres d impression avec JavaScript, Comment supprimer des titres d impression avec JavaScript, Comment définir les titres d impression dans Excel, Comment effacer les titres d impression dans Excel.  
---

## **Scénarios d'utilisation possibles**  

La définition des titres d'impression dans Excel garantit que certaines lignes ou colonnes sont répétées sur chaque page imprimée, ce qui est particulièrement utile pour les grands tableaux qui s'étendent sur plusieurs pages. Voici quelques raisons pour lesquelles vous pourriez définir des titres d'impression :  

1. Amélioration de la lisibilité : Les titres d'impression aident les lecteurs à comprendre les données en maintenant les en-têtes visibles sur toutes les pages, ce qui facilite l'interprétation des informations sur chaque page sans avoir à revenir à la première.  

1. Présentation professionnelle : Afficher de manière cohérente les en-têtes ou étiquettes sur chaque page donne un aspect plus soigné et professionnel aux documents imprimés.  

1. Navigation améliorée : Pour les documents avec beaucoup de données, répéter les en-têtes sur chaque page facilite la navigation et la référence, réduisant la nécessité de feuilleter entre les pages.  

1. Réduction des erreurs : Lorsque les en-têtes sont présents sur chaque page, cela minimise les risques de mauvaise interprétation ou d'erreurs de saisie, car les utilisateurs peuvent facilement voir le contexte des données.  

1. Cohérence : S'assurer que des informations importantes, telles que les en-têtes de colonnes ou les étiquettes de lignes, sont toujours visibles maintient la cohérence et la clarté dans tout le document.  

## **Comment définir des titres d'impression dans Excel**  

Pour définir des titres d'impression dans Excel, suivez ces étapes :  

1. Ouvrir l'onglet Mise en Page : Cliquez sur l'onglet « Mise en Page » dans le ruban en haut de la fenêtre Excel.  
1. Accéder aux Titres d'Impression : Dans le groupe « Mise en Page », cliquez sur « Titres d'impression ».  
1. Définir les lignes à répéter : Dans la boîte de dialogue "Mise en page", allez à l'onglet "Feuille". Dans la section "Titres d'impression", spécifiez les lignes à répéter en haut en cliquant sur la case à côté de "Lignes à répéter en haut" et en sélectionnant la ou les lignes souhaitées.  
1. Définir les colonnes à répéter (si nécessaire) : De même, vous pouvez spécifier les colonnes à répéter à gauche en cliquant sur la case à côté de "Colonnes à répéter à gauche" et en sélectionnant la ou les colonnes souhaitées.  
<br>  
<img src="3.png" width=60% />  

1. Confirmer et Imprimer : Cliquez sur « OK » pour appliquer les paramètres. Lors de l'impression de la feuille de calcul, les lignes ou colonnes spécifiées apparaîtront sur chaque page imprimée.  

## **Comment supprimer les titres d'impression dans Excel**  

Pour supprimer les titres d'impression dans Excel, il faut retirer les lignes ou colonnes programmées pour se répéter sur chaque page imprimée. Voici comment faire :  

1. Ouvrir l'onglet Mise en Page : Cliquez sur l'onglet « Mise en Page » dans le ruban en haut de la fenêtre Excel.  
1. Accéder aux Titres d'Impression : Dans le groupe « Mise en Page », cliquez sur « Titres d'impression ».  
1. Supprimer les Titres d'Impression : Dans la boîte de dialogue « Mise en Page », allez à l'onglet « Feuille ». Effacez le contenu des zones de texte « Répéter les lignes en haut » et « Répéter les colonnes à gauche » en supprimant leur contenu.  
<br>  
<img src="4.png" width=60% />  

1. Confirmer et Fermer : Cliquez sur « OK » pour appliquer les modifications.  

## **Comment définir les titres d'impression en utilisant Aspose.Cells for JavaScript via C++**  

Pour définir des titres d'impression dans une feuille spécifique : Tout d'abord, chargez le [fichier d'exemple](input.xlsx), puis vous devez modifier les propriétés [**Worksheet.pageSetup**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#pageSetup--) et [**Worksheet.pageSetup**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#pageSetup--) de l'objet [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/) pour la feuille souhaitée. Définir ces propriétés avec une chaîne de plage configurera les titres d'impression.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Set Print Titles</title>
    </head>
    <body>
        <h1>Set Print Titles Example</h1>
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

            // Load the workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the desired worksheet
            const worksheet = workbook.worksheets.get(0);

            // Set rows to repeat at the top (e.g., rows 1 and 2)
            worksheet.pageSetup.printTitleRows = "$1:$2";

            // Set columns to repeat at the left (e.g., columns A and B)
            worksheet.pageSetup.printTitleColumns = "$A:$B";

            // Save the workbook as PDF
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: "application/pdf" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'set_print_titles.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Print titles set successfully! Click the download link to get the PDF.</p>';
        });
    </script>
</html>
```  

Le résultat en sortie :  
<br>  
<img src="1.png" width=60% />  

## **Comment effacer les titres d'impression en utilisant Aspose.Cells for JavaScript via C++**  

Pour supprimer les titres d'impression dans une feuille spécifique : Tout d'abord, chargez le [fichier d'exemple](input.xlsx), puis modifiez les propriétés [**Worksheet.pageSetup**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#pageSetup--) et [**Worksheet.pageSetup**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#pageSetup--) de l'objet [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/) pour la feuille souhaitée. En définissant ces propriétés comme une chaîne vide, vous supprimerez les titres d'impression.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Clear Print Titles Example</title>
    </head>
    <body>
        <h1>Clear Print Titles Example</h1>
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

            // Load the workbook from the selected file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the desired worksheet
            const worksheet = workbook.worksheets.get(0);

            // Clear the rows and columns set to repeat
            worksheet.pageSetup.printTitleRows = "";
            worksheet.pageSetup.printTitleColumns = "";

            // Save the workbook as PDF
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'clear_print_titles.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Print titles cleared successfully! Click the download link to get the PDF.</p>';
        });
    </script>
</html>
```  

Le résultat en sortie :  
<br>  
<img src="2.png" width=60% />
