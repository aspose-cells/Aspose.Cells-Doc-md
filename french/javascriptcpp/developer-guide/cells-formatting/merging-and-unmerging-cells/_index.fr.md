---
title: Fusionner et dissocier des cellules avec JavaScript via C++
linktitle: Fusionner et séparer des cellules
description: Aspose.Cells est une bibliothèque JavaScript pour travailler avec des fichiers de tableur, qui supporte la fusion et la défusion des cellules. Cet article présentera comment fusionner et dé fusionner des cellules en utilisant la bibliothèque Aspose.Cells, avec des options de personnalisation du style des cellules fusionnées.
keywords: Aspose.Cells, bibliothèque JavaScript, tableur, fusionner des cellules, dé fusionner des cellules, paramètres de style, styles personnalisés
type: docs
weight: 190
url: /fr/javascript-cpp/merging-and-unmerging-cells/
---

{{% alert color="primary" %}} 

Aspose.Cells prend en charge cette fonctionnalité et peut également fusionner des cellules dans une feuille de calcul. Vous pouvez également séparer, ou diviser, les cellules fusionnées. La référence de cellule d'une cellule fusionnée est la référence de la cellule en haut à gauche de la plage sélectionnée d'origine.

{{% /alert %}} 
## **Introduction**
Vous ne souhaitez pas toujours le même nombre de cellules dans chaque ligne ou colonne. Par exemple, vous pouvez vouloir mettre un titre dans une cellule qui s'étend sur plusieurs colonnes. Ou, si vous créez une facture, vous souhaitez peut-être moins de colonnes pour le total. Pour fusionner deux cellules ou plus en une seule cellule, utilisez la fusion. Microsoft Excel permet aux utilisateurs de sélectionner des fichiers et de les fusionner pour structurer le tableur à leur convenance.

{{% alert color="primary" %}} 

Notez que lorsque des cellules sont fusionnées, seules les données de la cellule en haut à gauche sont conservées. S'il y a des données dans les autres cellules de la plage, ces données sont supprimées. La mise en forme, de même, est basée sur la cellule de référence, de sorte que lorsque vous fusionnez des cellules, les paramètres de mise en forme de la cellule en haut à gauche de la plage sont appliqués à la cellule fusionnée. Lorsque la cellule est divisée, les nouvelles cellules conservent leurs paramètres de mise en forme d'origine.

{{% /alert %}} 
## **Fusion de cellules dans une feuille de calcul**
### **Fusionner des cellules dans Microsoft Excel**
Les étapes suivantes décrivent comment fusionner des cellules dans la feuille de calcul à l'aide de MS Excel.

1. Copiez les données que vous souhaitez dans la cellule en haut à gauche dans la plage.
1. Sélectionnez les cellules que vous souhaitez fusionner.
1. Pour fusionner des cellules dans une ligne ou une colonne et centrer le contenu de la cellule, cliquez sur l'icône **Fusionner et centrer** dans la barre d'outils **Mise en forme**.

### **Fusion de cellules avec Aspose.Cells**
La classe Aspose.Cells.Cells possède des méthodes utiles pour cette tâche. Par exemple, la méthode `merge()` fusionne les cellules en une seule dans une plage spécifiée.

L'exemple suivant montre comment fusionner des cellules (C6:E7) dans une feuille de calcul.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Merging Cells Example</h1>
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
            // Create a Workbook.
            const wbk = new Workbook();

            // Create a Worksheet and get the first sheet.
            const worksheet = wbk.worksheets.get(0);

            // Create a Cells object to fetch all the cells.
            const cells = worksheet.cells;

            // Merge some Cells (C6:E7) into a single C6 Cell.
            cells.merge(5, 2, 2, 3);

            // Input data into C6 Cell.
            const cell = cells.get(5, 2);
            cell.value = "This is my value";

            // Create a Style object to fetch the Style of C6 Cell.
            const style = cell.style;

            // Create a Font object
            const font = style.font;

            // Set the name.
            font.name = "Times New Roman";

            // Set the font size.
            font.size = 18;

            // Set the font color
            font.color = AsposeCells.Color.Blue;

            // Bold the text
            font.isBold = true;

            // Make it italic
            font.isItalic = true;

            // Set the background color of C6 Cell to Red
            style.foregroundColor = AsposeCells.Color.Red;
            style.pattern = AsposeCells.BackgroundType.Solid;

            // Apply the Style to C6 Cell.
            cell.style = style;

            // Saving the Workbook and providing download link
            const outputData = wbk.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'mergingcells.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and styled successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **Dissocier (diviser) les cellules fusionnées**
### **Utilisation de Microsoft Excel**
Les étapes suivantes décrivent comment diviser les cellules fusionnées à l'aide de Microsoft Excel.

1. Sélectionnez la cellule fusionnée.
   Lorsque les cellules ont été combinées, **Fusionner et centrer** est sélectionné dans la barre d'outils **Mise en forme**.
1. Cliquez sur **Fusionner et centrer** dans la barre d'outils **Mise en forme**.

### **Utilisation d'Aspose.Cells**
La classe Aspose.Cells.Cells possède une méthode appelée `unmerge()` qui divise les cellules dans leur état d'origine. La méthode désfusionne les cellules en utilisant la référence de la cellule dans la plage fusionnée.

L'exemple suivant montre comment diviser les cellules fusionnées (C6). L'exemple utilise le fichier créé dans l'exemple précédent et divise les cellules fusionnées.

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>Unmerge Cells Example</title>
    </head>
    <body>
        <h1>Unmerge Cells Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Create a Workbook by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create a Worksheet and get the first sheet.
            const worksheet = workbook.worksheets.get(0);

            // Create a Cells object to fetch all the cells.
            const cells = worksheet.cells;

            // Unmerge the cells at row 5, column 2 spanning 2 rows and 3 columns
            cells.unMerge(5, 2, 2, 3);

            // Save the file and provide a download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'unmergingcells.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Cells unmerged successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Sujets avancés**
- [Détecter les cellules fusionnées dans une feuille de calcul](/cells/fr/javascript-cpp/detect-merged-cells-in-a-worksheet/)
