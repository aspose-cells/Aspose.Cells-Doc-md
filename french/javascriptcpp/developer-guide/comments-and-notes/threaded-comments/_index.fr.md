---
title: Commentaires en fil de discussion avec JavaScript via C++
linktitle: Commentaires en fil
type: docs
weight: 140
url: /fr/javascript-cpp/threaded-comments/
description: Gérer les commentaires en fil de discussion dans les documents Excel avec Aspose.Cells for JavaScript via C++. Apprenez à ajouter, lire, modifier et supprimer des commentaires en fil de discussion.
---

## **Commentaires en fil**

MS Excel 365 offre la possibilité d'ajouter des commentaires en fil. Ces commentaires fonctionnent comme des conversations et peuvent être utilisés pour des discussions. Les commentaires sont maintenant dotés d'une boîte de réponse qui permet des conversations en fil. Les anciens commentaires sont appelés Notes dans Excel 365. La capture d'écran ci-dessous montre comment les commentaires en fil sont affichés lorsqu'ils sont ouverts dans Excel.

![todo:image_alt_text](threaded-comments_1.jpg)

Les commentaires en fil sont affichés comme ceci dans les anciennes versions d'Excel. Les images suivantes ont été prises en ouvrant le fichier d'exemple dans Excel 2016.

![todo:image_alt_text](threaded-comments_2.jpg)

![todo:image_alt_text](threaded-comments_3.jpg)

Aspose.Cells fournit également la fonctionnalité pour gérer les commentaires en fil.

## **Ajouter des commentaires en fil**

### **Ajouter un commentaire en fil avec Excel**

Pour ajouter des commentaires enfilés dans Excel 365, suivez les étapes suivantes.

- Méthode 1
  - Cliquez sur l'onglet **Révision**
  - Cliquez sur le bouton **Nouveau commentaire**
  - Cela ouvrira une boîte de dialogue pour saisir des commentaires dans la cellule active.
  - ![todo:image_alt_text](threaded-comments_4.jpg)
- Méthode 2
  - Cliquez avec le bouton droit sur la cellule où vous souhaitez insérer le commentaire.
  - Cliquez sur l'option **Nouveau commentaire**
  - Cela ouvrira une boîte de dialogue pour saisir des commentaires dans la cellule active.
  - ![todo:image_alt_text](threaded-comments_5)

### **Ajouter un commentaire enfilé à l'aide d'Aspose.Cells**

Aspose.Cells fournit la méthode [**Comments.AddThreadedComment**](https://reference.aspose.com/cells/javascript-cpp/commentcollection/#addthreadedcomment-string-string-ThreadedCommentAuthor-) pour ajouter des commentaires filaires. La méthode [**Comments.AddThreadedComment**](https://reference.aspose.com/cells/javascript-cpp/commentcollection/#addthreadedcomment-string-string-ThreadedCommentAuthor-) accepte les trois paramètres suivants.

- Nom de la cellule : Le nom de la cellule où le commentaire sera inséré.
- Texte du commentaire : Le texte du commentaire.
- [**ThreadedCommentAuthor**](https://reference.aspose.com/cells/javascript-cpp/threadedcommentauthor) : L'auteur du commentaire

L'exemple de code ci-dessous illustre l'utilisation de la méthode [**Comments.AddThreadedComment**](https://reference.aspose.com/cells/javascript-cpp/commentcollection/#addthreadedcomment-string-string-ThreadedCommentAuthor-) pour ajouter un commentaire filaire à la cellule A1. Veuillez consulter le [fichier Excel de sortie](89849859.xlsx) généré par le code pour référence.

#### **Code d'exemple**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add Threaded Comment</title>
    </head>
    <body>
        <h1>Add Threaded Comment Example</h1>
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
            // Create a new workbook
            const workbook = new Workbook();

            // Add Author
            const authorIndex = workbook.worksheets.threadedCommentAuthors.add("Aspose Test", "", "");
            const author = workbook.worksheets.threadedCommentAuthors.get(authorIndex);

            // Add Threaded Comment to cell A1 in the first worksheet
            const worksheet = workbook.worksheets.get(0);
            worksheet.comments.addThreadedComment("A1", "Test Threaded Comment", author);

            // Save the modified workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'AddThreadedComments_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Threaded comment added successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **Lire les Commentaires enfilés**

### **Lire des commentaires enfilés avec Excel**

Pour lire des commentaires enfilés dans Excel, survolez simplement la cellule contenant les commentaires pour les afficher. La vue des commentaires ressemblera à la vue dans l'image suivante.

![todo:image_alt_text](threaded-comments_1.jpg)

### **Lire des commentaires enfilés à l'aide d'Aspose.Cells**

Aspose.Cells fournit la méthode [**Comments.threadedComments**](https://reference.aspose.com/cells/javascript-cpp/commentcollection/#threadedComments-string-) pour récupérer les commentaires en fil pour la colonne spécifiée. La méthode [**Comments.threadedComments**](https://reference.aspose.com/cells/javascript-cpp/commentcollection/#threadedComments-string-) accepte le nom de colonne en tant que paramètre et retourne le [**ThreadedCommentCollection**](https://reference.aspose.com/cells/javascript-cpp/threadedcommentcollection). Vous pouvez itérer sur le [**ThreadedCommentCollection**](https://reference.aspose.com/cells/javascript-cpp/threadedcommentcollection) pour afficher les commentaires.

L'exemple suivant démontre la lecture des commentaires de la colonne A1 en chargeant le [Fichier Excel d'exemple](89849861.xlsx). Veuillez consulter la sortie de la console générée par le code pour référence.

#### **Code d'exemple**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Threaded Comments Example</title>
    </head>
    <body>
        <h1>Threaded Comments Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Get Threaded Comments for cell A1
            const threadedComments = worksheet.comments.threadedComments("A1");

            const count = threadedComments.count;
            let html = '<h2>Threaded Comments</h2>';
            if (count === 0) {
                html += '<p>No threaded comments found for A1.</p>';
            } else {
                html += '<ul>';
                for (let i = 0; i < count; i++) {
                    const comment = threadedComments.get(i);
                    const notes = comment.notes;
                    const authorName = comment.author.name;
                    html += `<li><strong>Author:</strong> ${authorName} <br/><strong>Comment:</strong> ${notes}</li>`;
                }
                html += '</ul>';
            }

            resultDiv.innerHTML = html;
        });
    </script>
</html>
```

#### **Sortie console**

{{< highlight javascript >}}

Comment: Test Threaded Comment

Author: Aspose Test

{{< /highlight >}}

### **Lire l'heure de création des commentaires en fil**

Aspose.Cells fournit la méthode [**Comments.threadedComments**](https://reference.aspose.com/cells/javascript-cpp/commentcollection/#threadedComments-string-) pour récupérer les commentaires filaires pour la colonne spécifiée. La méthode [**Comments.threadedComments**](https://reference.aspose.com/cells/javascript-cpp/commentcollection/#threadedComments-string-) accepte le nom de colonne en paramètre et retourne le [**ThreadedCommentCollection**](https://reference.aspose.com/cells/javascript-cpp/threadedcommentcollection). Vous pouvez parcourir le [**ThreadedCommentCollection**](https://reference.aspose.com/cells/javascript-cpp/threadedcommentcollection) et utiliser la propriété [**ThreadedComment.createdTime**](https://reference.aspose.com/cells/javascript-cpp/threadedcomment/#createdTime--).

L'exemple suivant démontre la lecture de l'heure de création des commentaires en fil en chargeant le [Fichier Excel d'exemple](89849861.xlsx). Veuillez consulter la sortie de la console générée par le code pour référence.

#### **Code d'exemple**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Threaded Comments Example</title>
    </head>
    <body>
        <h1>Threaded Comments Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');
            const downloadLink = document.getElementById('downloadLink');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            // No try-catch: allow errors to propagate for testing
            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Loads the workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Get Threaded Comments for cell A1
            const threadedComments = worksheet.comments.threadedComments("A1");

            const count = threadedComments.count;

            let html = '<h2>Threaded Comments (Cell A1)</h2>';
            if (count === 0) {
                html += '<p>No threaded comments found in cell A1.</p>';
            } else {
                html += '<ul>';
                for (let i = 0; i < count; i++) {
                    const comment = threadedComments.get(i);
                    const notes = comment.notes;
                    const authorName = comment.author.name;
                    const createdTime = comment.createdTime;

                    console.log("Comment: " + notes);
                    console.log("Author: " + authorName);
                    console.log("Created Time: " + createdTime);

                    html += `<li><strong>Author:</strong> ${authorName} <br/><strong>Created:</strong> ${createdTime} <br/><strong>Comment:</strong> ${notes}</li>`;
                }
                html += '</ul>';
            }

            resultDiv.innerHTML = html;

            // No file modifications or save in this example; hide download link
            downloadLink.style.display = 'none';
        });
    </script>
</html>
```

#### **Sortie console**

{{< highlight javascript >}}

Comment: Test Threaded Comment

Author: Aspose Test

Created Time: 5/15/2019 12:46:23 PM

{{< /highlight >}}

## **Modifier les commentaires en fil**

### **Modifier le commentaire en fil avec Excel**

Pour modifier un commentaire en fil dans Excel, cliquez sur le lien **Modifier** sur le commentaire comme indiqué dans l'image suivante.

![todo:image_alt_text](threaded-comments_7.jpg)

### **Modifier le commentaire en fil en utilisant Aspose.Cells**

Aspose.Cells fournit la méthode [**Comments.threadedComments**](https://reference.aspose.com/cells/javascript-cpp/commentcollection/#threadedComments-string-) pour récupérer les commentaires filaires pour la colonne spécifiée. La méthode [**Comments.threadedComments**](https://reference.aspose.com/cells/javascript-cpp/commentcollection/#threadedComments-string-) accepte le nom de colonne en paramètre et retourne le [**ThreadedCommentCollection**](https://reference.aspose.com/cells/javascript-cpp/threadedcommentcollection). Vous pouvez mettre à jour le commentaire requis dans le [**ThreadedCommentCollection**](https://reference.aspose.com/cells/javascript-cpp/threadedcommentcollection) et sauvegarder le classeur.

L’exemple suivant montre comment modifier le premier commentaire en fil de discussion dans la colonne A1 en chargeant le [fichier Excel d’échantillon](89849861.xlsx). Veuillez voir le [fichier Excel de sortie](89849862.xlsx) généré par le code montrant le commentaire mis à jour en référence.

#### **Code d'exemple**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Edit Threaded Comments Example</h1>
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the Excel file from the file input
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Get Threaded Comment from cell A1
            const comment = worksheet.comments.threadedComments("A1").get(0);

            // Update the threaded comment notes
            comment.notes = "Updated Comment";

            // Save the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'EditThreadedComments.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Edited Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Threaded comment updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Supprimer les commentaires en filigrane**

### **Supprimer les commentaires en filigrane avec Excel**

Pour supprimer les commentaires en filigrane dans Excel, cliquez avec le bouton droit sur la cellule contenant les commentaires et cliquez sur l'option **Supprimer le commentaire** comme indiqué dans l'image suivante.

![todo:image_alt_text](threaded-comments_8.jpg)
