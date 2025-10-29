---
title: Comment changer l’arrière plan d’un commentaire dans Excel avec JavaScript via C++
linktitle: Arrière plan du commentaire
type: docs
weight: 190
url: /fr/javascript-cpp/how-to-set-comment-background/
description: Comment changer la couleur du commentaire et insérer une image ou une photo dans un commentaire dans Excel en utilisant Aspose.Cells for JavaScript via C++.
keywords: Ajouter une image, couleur de commentaire de fond dans Excel JavaScript via C++
---

{{% alert color="primary" %}}
Les commentaires sont ajoutés aux cellules pour enregistrer des remarques, des détails sur la manière dont une formule fonctionne, la provenance d'une valeur ou des questions des relecteurs. Les commentaires jouent un rôle extrêmement important lorsque plusieurs personnes discutent ou examinent le même document à différents moments. Comment distinguer les commentaires de différentes personnes ? Oui, nous pouvons définir une couleur de fond différente pour chaque commentaire. Mais lorsque nous devons traiter beaucoup de documents et de nombreux commentaires, le faire manuellement est un désastre. Heureusement, [**Aspose.Cells**](https://products.aspose.com/cells/javascript-cpp/) offre une API qui permet de faire cela dans le code.
{{% /alert %}}

## **Comment changer la couleur dans le commentaire dans Excel**

Lorsque vous n'avez pas besoin de la couleur de fond par défaut pour les commentaires, vous pouvez la remplacer par une couleur qui vous intéresse. Comment puis-je changer la couleur de l'arrière-plan de la boîte de commentaires dans Excel ?

Le code suivant vous guidera sur la façon d'utiliser [**Aspose.Cells**](https://products.aspose.com/cells/javascript-cpp/) pour ajouter votre couleur d'arrière-plan préférée aux commentaires de votre choix.

Voici un [fichier d'exemple](exmaple.xlsx) préparé pour vous. Ce fichier sert à initialiser l'objet Workbook dans le code ci-dessous.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Change Comment Background Color Example</title>
    </head>
    <body>
        <h1>Change Comment Background Color Example</h1>
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

            // Initialize a new workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the newly added comment
            const comment = workbook.worksheets.get(0).comments.get(0);

            // change background color
            const shape = comment.commentShape;
            shape.fill.solidFill.color = AsposeCells.Color.Red;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'result.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Comment background color changed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

Exécutez le code ci-dessus et vous obtiendrez un [fichier de sortie](result.xlsx).

## **Comment insérer une image ou une photo dans le commentaire dans Excel**

Microsoft Excel permet aux utilisateurs de personnaliser considérablement l'apparence des feuilles de calcul. Il est même possible d'ajouter des images de fond aux commentaires. L'ajout d'une image d'arrière-plan peut être un choix esthétique ou utilisé pour renforcer la marque.

Le code d'exemple ci-dessous crée un fichier XLSX à partir de zéro en utilisant l'API [**Aspose.Cells**](https://products.aspose.com/cells/javascript-cpp/), et ajoute un commentaire avec une image d'arrière-plan à la cellule A1.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Add Comment with Picture Example</h1>
        <p>
            Select an existing Excel file (optional) and an image file to attach to a comment in cell A1.
        </p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <br/><br/>
        <label for="imageInput">Select image to insert in comment (required):</label>
        <input type="file" id="imageInput" accept="image/*" />
        <br/><br/>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>

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
            const imageInput = document.getElementById('imageInput');
            const resultDiv = document.getElementById('result');

            if (!imageInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an image file to insert into the comment.</p>';
                return;
            }

            // Instantiate or load Workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Get comments collection for the first sheet
            const comments = worksheet.comments;

            // Add a comment to cell A1 (row 0, column 0)
            const commentIndex = comments.add(0, 0);
            const comment = comments.get(commentIndex);

            // Set comment text and font name (converted from setters to properties)
            comment.note = "First note.";
            comment.font.name = "Times New Roman";

            // Load the selected image file and set it to the comment's shape fill imageData
            const imageFile = imageInput.files[0];
            const imgArrayBuffer = await imageFile.arrayBuffer();
            const imageData = new Uint8Array(imgArrayBuffer);

            comment.commentShape.fill.imageData = imageData;

            // Save the workbook to a blob and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'commentwithpicture1.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Comment with picture added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</body>
</html>
```
