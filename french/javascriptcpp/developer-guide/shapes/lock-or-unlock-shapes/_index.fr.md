---
title: Bloquer ou déverrouiller les formes avec JavaScript via C++
linktitle: Verrouiller ou déverrouiller les formes
type: docs
weight: 200
url: /fr/javascript-cpp/lock-or-unlock-shapes/
description: Cet article vous montre du code expliquant comment bloquer ou déverrouiller les formes pour les protéger en utilisant la bibliothèque Aspose.Cells pour JavaScript via C++.
keywords: JavaScript via C++ Lock Shapes to Protect Them, Comment bloquer ou déverrouiller des formes en utilisant JavaScript via C++, Bloquer ou déverrouiller des formes pour les protéger en JavaScript via C++.
---

## **Scénarios d'utilisation possibles**

Parfois, vous devez protéger toutes les formes dans certaines feuilles de calcul pour les empêcher d'être détruites par des situations non désirées. Dans ce cas, vous devez verrouiller toutes les formes dans la feuille de calcul spécifiée. 

Verrouiller des formes dans une feuille de calcul ou un document peut être bénéfique pour plusieurs raisons :
1. Empêcher les modifications accidentelles : Verrouiller des formes garantit qu'elles ne soient pas déplacées, redimensionnées ou supprimées accidentellement par les utilisateurs. Cela est particulièrement important dans des documents complexes où les formes peuvent être utilisées pour les annotations, illustrations ou comme partie du design du document.
1. Maintenir la mise en page et le design : Les formes jouent souvent un rôle crucial dans la mise en page et le design visuel d'un document. Leur verrouillage préserve l'apparence souhaitée, assurant que le document reste professionnel et attractif visuellement.
1. Intégrité des données : Dans les feuilles de calcul, les formes peuvent être utilisées pour mettre en évidence des points de données importants, ajouter des commentaires ou fournir des explications visuelles. Le verrouillage de ces formes garantit que les informations contextuelles qu'elles fournissent restent précises et intactes.
1. Cohérence dans les documents partagés : Lors de la collaboration sur des documents, différents utilisateurs peuvent avoir des niveaux de compétence variés. Le verrouillage des formes aide à maintenir la cohérence à travers le document en empêchant les modifications non intentionnelles.
1. Sécurité : Dans des documents sensibles, verrouiller des formes peut faire partie d'une stratégie plus large pour protéger l'information. Par exemple, dans les rapports financiers ou documents légaux, des formes verrouillées peuvent être utilisées pour sécuriser des annotations ou des surlignages spécifiques qui fournissent un contexte critique.

Parfois, vous devez pouvoir modifier certaines formes dans certaines feuilles protégées, auquel cas, vous devez déverrouiller ces formes. Cet article expliquera en détail comment verrouiller et déverrouiller des formes spécifiques.

## **Comment verrouiller des formes pour les protéger dans Excel**

Voici comment verrouiller des cellules dans Microsoft Excel :

1. Ouvrez votre fichier Excel : Ouvrez le fichier Excel contenant les formes que vous souhaitez verrouiller.

1. Sélectionnez la forme : Cliquez sur la forme que vous souhaitez verrouiller. Vous pouvez également sélectionner plusieurs formes en maintenant la touche Ctrl enfoncée et en cliquant sur chaque forme.

1. Ouvrir le panneau Format de forme : Faites clic droit sur la ou les formes sélectionnées et choisissez « Taille et propriétés ». Alternativement, vous pouvez aller à l'onglet « Format » dans le ruban, et dans le groupe « Taille », cliquer sur le lanceur de dialogue (une petite flèche) pour ouvrir le volet « Format de forme ».
1. Verrouiller la forme : Dans le volet « Format de forme », allez à l'onglet « Taille & Propriétés » (l'icône ressemble à un carré avec des flèches). Sous la section « Propriétés », cochez la case « Verrouillé ».
<br>
<img src="1.png" width=60% />
1. Protéger la feuille : Allez dans l'onglet "Révision" du ruban. Cliquez sur "Protéger la feuille." Définissez un mot de passe (optionnel) et choisissez les permissions que vous souhaitez autoriser (par exemple, sélectionner des cellules verrouillées, formater des cellules, etc.). Cliquez sur "OK."
<br>
<img src="2.png" width=60% />

## **Comment verrouiller toutes les formes dans une feuille spécifiée**

Pour protéger toutes les formes dans une feuille spécifiée, utilisez la méthode `worksheet.protect(ProtectionType.Objects)`, comme montré dans le code d'exemple suivant.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Lock Shapes Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ProtectionType } = AsposeCells;

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

            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const text = "This is a test";
            const worksheet = workbook.worksheets.get(0);

            let shape = worksheet.shapes.addTextBox(1, 0, 1, 0, 30, 100);
            shape.text = text;

            shape = worksheet.shapes.addRectangle(5, 0, 1, 0, 30, 100);
            shape.text = text;

            shape = worksheet.shapes.addButton(9, 0, 1, 0, 30, 100);
            shape.text = text;

            shape = worksheet.shapes.addOval(13, 0, 1, 0, 50, 100);
            shape.text = text;

            // Protect all shapes in the specified worksheet
            shape.worksheet.protect(ProtectionType.Objects);

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Locked.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Locked.xlsx';

            document.getElementById('result').innerHTML = '<p style="color: green;">Shapes locked successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Comment déverrouiller des formes spécifiques dans une feuille protégée**

Pour déverrouiller une forme spécifique dans une feuille protégée, utilisez `shape.isLocked`, comme illustré dans l'exemple de code suivant.

Remarque : `shape.isLocked` n'a de sens que lorsque la feuille est protégée.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Unlock Shape</title>
    </head>
    <body>
        <h1>Unlock Shape Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
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

            // Loads the workbook which contains hidden external links
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get protected worksheet
            const worksheet = workbook.worksheets.get(0);

            // Get the specified shape to be unlocked
            const shape = worksheet.shapes.get("TextBox 1");

            if (!shape) {
                resultDiv.innerHTML = '<p style="color: red;">Shape "TextBox 1" not found.</p>';
                return;
            }

            // Unlock the specified shape
            if (!worksheet.protection.allowEditingObject && shape.isLocked) {
                shape.isLocked = false;
            }

            // Save the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'UnLocked.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Shape unlocked successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
