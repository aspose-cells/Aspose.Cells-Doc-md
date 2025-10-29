---
title: Gérer les commentaires et notes avec JavaScript via C++
linktitle: Commentaires et notes
type: docs
weight: 128
url: /fr/javascript-cpp/comments-and-notes/
description: Insérez et gérez les commentaires ou notes avec Aspose.Cells for JavaScript via C++.
keywords: insérer des commentaires, insérer des notes JavaScript via C++
---

## **Introduction**

Les commentaires sont utilisés pour ajouter des informations supplémentaires aux cellules. Aspose.Cells for JavaScript via C++ fournit deux méthodes pour ajouter des commentaires aux cellules. La première consiste à créer manuellement des commentaires dans un fichier de conception. Ces commentaires sont ensuite importés à l'aide d'Aspose.Cells. La deuxième consiste à ajouter des commentaires en utilisant l'API Aspose.Cells en temps réel. Ce sujet discute de l'ajout de commentaires aux cellules avec l'API Aspose.Cells. La mise en forme des commentaires sera également expliquée.

## **Ajouter un commentaire**

Ajouter un commentaire à une cellule en appelant la méthode [**CommentCollection.add(number, number)**](https://reference.aspose.com/cells/javascript-cpp/commentcollection/#add-number-number-) de la collection [**Comments**](https://reference.aspose.com/cells/javascript-cpp/commentcollection) (encapsulée dans l'objet [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)). Le nouvel objet [**Comment**](https://reference.aspose.com/cells/javascript-cpp/comment) peut être accessible à partir de la collection [**Comments**](https://reference.aspose.com/cells/javascript-cpp/commentcollection) en passant l'index du commentaire. Après avoir accès à l'objet [**Comment**](https://reference.aspose.com/cells/javascript-cpp/comment), personnalisez la note du commentaire en utilisant la propriété [**note**](https://reference.aspose.com/cells/javascript-cpp/comment/#note--).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Add Comment Example</h1>
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
            // Instantiating a Workbook object
            const workbook = new Workbook();

            // Adding a new worksheet to the Workbook object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding a comment to "F5" cell
            const commentIndex = worksheet.comments.add("F5");

            // Accessing the newly added comment
            const comment = worksheet.comments.get(commentIndex);

            // Setting the comment note
            comment.note = "Hello Aspose!";

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Comment added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Mise en forme des commentaires**

Il est également possible de formater l'apparence des commentaires en configurant leur hauteur, leur largeur et leurs paramètres de police.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add Comment</title>
    </head>
    <body>
        <h1>Add Comment Example</h1>
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
            // Creating a new Workbook object
            const workbook = new Workbook();

            // Adding a new worksheet to the Workbook object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding a comment to "F5" cell
            const commentIndex = worksheet.comments.add("F5");

            // Accessing the newly added comment
            const comment = worksheet.comments.get(commentIndex);

            // Setting the comment note
            comment.note = "Hello Aspose!";

            // Setting the font size of a comment to 14
            comment.font.size = 14;

            // Setting the font of a comment to bold
            comment.font.isBold = true;

            // Setting the height of the font to 10
            comment.heightCM = 10;

            // Setting the width of the font to 2
            comment.widthCM = 2;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and saved. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **Ajouter une image au commentaire**

Avec Microsoft Excel 2007, il est également possible d'avoir une image en arrière-plan d'un commentaire de cellule. Dans Excel 2007, cela se fait en suivant les étapes suivantes. (Ils supposent que vous avez déjà ajouté un commentaire de cellule.)

1. Faites un clic droit sur la cellule qui contient le commentaire.
1. Sélectionnez **Afficher/masquer les commentaires**, et effacez tout texte du commentaire.
1. Cliquez sur le bord du commentaire pour le sélectionner.
1. Sélectionnez **Format**, puis **Commentaire**.
1. Sur l'onglet **Couleurs et traits**, développez la liste **Couleur**.
1. Cliquez sur **Remplissage**.
1. Sur l'onglet **Image**, cliquez sur **Sélectionner une image**.
1. Localisez et sélectionnez l'image.
1. Cliquez sur **OK** jusqu'à ce que tous les dialogues se ferment.

Aspose.Cells propose également cette fonctionnalité. Ci-dessous se trouve un exemple de code qui crée un fichier XLSX à partir de zéro, en ajoutant un commentaire à la cellule "A1" avec une image définie comme arrière-plan.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add Comment with Image</title>
    </head>
    <body>
        <h1>Add Comment with Image Example</h1>
        <p>
            Select an existing Excel file to modify (optional). If no file is selected, a new workbook will be created.
        </p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <p>
            Select an image file to attach to the comment (required):
        </p>
        <input type="file" id="imageInput" accept="image/*" />
        <br/><br/>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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
            const resultEl = document.getElementById('result');
            resultEl.innerHTML = '';

            const fileInput = document.getElementById('fileInput');
            const imageInput = document.getElementById('imageInput');

            if (!imageInput.files.length) {
                resultEl.innerHTML = '<p style="color: red;">Please select an image file for the comment.</p>';
                return;
            }

            // Load or create workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Get a reference of comments collection with the first sheet
            const comments = workbook.worksheets.get(0).comments;

            // Add a comment to cell A1
            const commentIndex = comments.add(0, 0);
            const comment = comments.get(commentIndex);

            // Set the comment note and font name (converted from set/get to properties)
            comment.note = "First note.";
            comment.font.name = "Times New Roman";

            // Load image file data
            const imgFile = imageInput.files[0];
            const imgArrayBuffer = await imgFile.arrayBuffer();
            const imgUint8 = new Uint8Array(imgArrayBuffer);

            // Set image data to the shape associated with the comment
            comment.commentShape.fill.imageData = imgUint8;

            // Save the workbook to browser-downloadable file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultEl.innerHTML = '<p style="color: green;">Comment added with image successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Sujets avancés**
- [Modifier la direction du texte du commentaire](/cells/fr/javascript-cpp/change-text-direction-of-the-comment/)
- [Comment changer la couleur de police du commentaire](/cells/fr/javascript-cpp/how-to-change-the-comment-font-color/)
- [Comment définir l'arrière-plan du commentaire](/cells/fr/javascript-cpp/how-to-set-comment-background/)
- [Commentaires en fil](/cells/fr/javascript-cpp/threaded-comments/)
