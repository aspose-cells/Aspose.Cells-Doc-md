---
title: Gestion des images avec JavaScript via C++
linktitle: Gestion des images
type: docs
weight: 10
url: /fr/javascript-cpp/managing-pictures/
description: Apprenez comment ajouter et positionner des images dans des feuilles de calcul en utilisant Aspose.Cells for JavaScript via C++.
---

Aspose.Cells permet aux développeurs d'ajouter des images à des feuilles de calcul en cours d'exécution. De plus, le positionnement de ces images peut être contrôlé en cours d'exécution, ce qui est discuté plus en détail dans les sections suivantes.

Cet article explique comment ajouter des images et comment insérer une image qui montre le contenu de certaines cellules.

## **Ajout d'images**

Ajouter des images à une feuille de calcul est très facile. Il suffit de quelques lignes de code :  
Il suffit d'appeler la méthode [**Add**](https://reference.aspose.com/cells/javascript-cpp/picturecollection/#add-number-number-string-) de la collection [**Pictures**](https://reference.aspose.com/cells/javascript-cpp/picturecollection) (encapsulée dans l'objet [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)). La méthode [**Add**](https://reference.aspose.com/cells/javascript-cpp/picturecollection/#add-number-number-string-) prend les paramètres suivants :

- **Index de la ligne supérieure gauche**, l'index de la ligne supérieure gauche.
- **Index de la colonne supérieure gauche**, l'index de la colonne supérieure gauche.
- **Nom du fichier image**, le nom du fichier image, complet avec le chemin.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Add Picture to Workbook Example</h1>
        <p>Select an optional Excel file to update (or leave empty to create a new workbook), and select an image file to insert as a picture.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <input type="file" id="imageInput" accept="image/*" />
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
            const imageInput = document.getElementById('imageInput');
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '';

            if (!imageInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an image file to insert.</p>';
                return;
            }

            // Load existing workbook if provided, otherwise create a new one
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Adding a new worksheet to the Workbook object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Read image file bytes
            const imageFile = imageInput.files[0];
            const imageArrayBuffer = await imageFile.arrayBuffer();
            const imageBytes = new Uint8Array(imageArrayBuffer);

            // Adding a picture at the location of a cell whose row and column indices are 5 (F6)
            worksheet.pictures.add(5, 5, imageBytes);

            // Saving the Excel file (Excel 97-2003 .xls format)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Picture added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Positionnement des images**

Il existe deux façons possibles de contrôler le positionnement des images à l'aide d'Aspose.Cells :

- Positionnement proportionnel: définir une position proportionnelle à la hauteur et à la largeur de la ligne.
- Positionnement absolu : définissez la position exacte sur la page où l'image sera insérée, par exemple, 40 pixels à gauche et 20 pixels en dessous du bord de la cellule.

### **Positionnement proportionnel**

Les développeurs peuvent positionner les images proportionnellement à la hauteur des lignes et à la largeur des colonnes en utilisant les propriétés [**upperDeltaX**](https://reference.aspose.com/cells/javascript-cpp/shape/#upperDeltaX--) et [**upperDeltaY**](https://reference.aspose.com/cells/javascript-cpp/shape/#upperDeltaY--) de l'objet [**Picture**](https://reference.aspose.com/cells/javascript-cpp/picture/). Un objet [**Picture**](https://reference.aspose.com/cells/javascript-cpp/picture/) peut être obtenu de la collection [**Pictures**](https://reference.aspose.com/cells/javascript-cpp/picturecollection) en passant son index d'image. Cet exemple place une image dans la cellule F6.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Add Picture to New Workbook</h1>
        <p>Select an image to insert into a new Excel workbook. The picture will be placed at cell F6 (row 5, column 5).</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <br/><br/>
        <label for="imageInput">Select image to insert:</label>
        <input type="file" id="imageInput" accept="image/*" />
        <br/><br/>
        <button id="runExample">Create Workbook and Add Picture</button>
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
            const imageInput = document.getElementById('imageInput');
            if (!imageInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an image file to insert.</p>';
                return;
            }

            // Instantiate a new Workbook
            const workbook = new Workbook();

            // Add a new worksheet to the Workbook object
            const sheetIndex = workbook.worksheets.add();

            // Obtain the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Read the selected image file as bytes
            const imageFile = imageInput.files[0];
            const arrayBuffer = await imageFile.arrayBuffer();
            const imageBytes = new Uint8Array(arrayBuffer);

            // Adding a picture at the location of a cell whose row and column indices are 5 (F6)
            const pictureIndex = worksheet.pictures.add(5, 5, imageBytes);

            // Accessing the newly added picture
            const picture = worksheet.pictures.get(pictureIndex);

            // Positioning the picture proportional to row height and column width (property assignments)
            picture.upperDeltaX = 200;
            picture.upperDeltaY = 200;

            // Saving the Excel file (Excel 97-2003 format)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and picture added successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

### **Positionnement Absolu**

Les développeurs peuvent également positionner les images de façon absolue en utilisant les propriétés [**left**](https://reference.aspose.com/cells/javascript-cpp/shape/#left--) et [**top**](https://reference.aspose.com/cells/javascript-cpp/shape/#top--) de l'objet [**Picture**](https://reference.aspose.com/cells/javascript-cpp/picture/). Cet exemple place une image dans la cellule F6, à 60 pixels du bord gauche et à 10 pixels du haut de la cellule.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add Picture</title>
    </head>
    <body>
        <h1>Add Picture to Workbook Example</h1>
        <p>Select an image file to insert into a new Excel workbook:</p>
        <input type="file" id="fileInput" accept="image/*" />
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
                resultDiv.innerHTML = '<p style="color: red;">Please select an image file.</p>';
                return;
            }

            // Read image file as bytes
            const imageFile = fileInput.files[0];
            const arrayBuffer = await imageFile.arrayBuffer();
            const imageBytes = new Uint8Array(arrayBuffer);

            // Instantiating a Workbook object
            const workbook = new Workbook();

            // Adding a new worksheet to the Workbook object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding a picture at the location of a cell whose row and column indices are 5 in the worksheet ("F6")
            const pictureIndex = worksheet.pictures.add(5, 5, imageBytes);

            // Accessing the newly added picture
            const picture = worksheet.pictures.get(pictureIndex);

            // Absolute positioning of the picture in unit of pixels
            picture.left = 60;
            picture.top = 10;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Picture added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Insérer une image basée sur la référence de cellule**

Aspose.Cells vous permet d'afficher le contenu d'une cellule de feuille de calcul dans une forme d'image. Vous pouvez lier l'image à la cellule qui contient les données que vous souhaitez afficher. Étant donné que la cellule ou la plage de cellules est liée à l'objet graphique, les modifications apportées aux données dans cette cellule ou plage de cellules apparaissent automatiquement dans l'objet graphique.

Ajoutez une image à la feuille en appelant la méthode [**ShapeCollection.addPicture(number, number, number, number, Uint8Array)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addPicture-number-number-number-number-uint8array-) de la collection [**ShapeCollection**](https://reference.aspose.com/cells/javascript-cpp/shapecollection) (encapsulée dans l'objet [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)). Spécifiez la plage de cellules en utilisant l'attribut [**formula**](https://reference.aspose.com/cells/javascript-cpp/picture/#formula--) de l'objet [**Picture**](https://reference.aspose.com/cells/javascript-cpp/picture/).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
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
            // This example creates a new workbook, modifies cells and pictures, and saves it.
            const workbook = new Workbook();

            // Get the first worksheet's cells collection
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;

            // Add string values to the cells
            cells.get("A1").value = "A1";
            cells.get("C10").value = "C10";

            // Get pictures collection and add a blank picture to the D1 cell
            const picts = worksheet.pictures;
            const picIndex = picts.add(0, 3, 10, 6, null);
            const pic = picts.get(picIndex);

            // Specify the formula that refers to the source range of cells
            pic.formula = "A1:C10";

            // Update the shapes selected value in the worksheet
            worksheet.shapes.updateSelectedValue();

            // Save the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Sujets avancés**
- [Ajouter un ensemble d'icônes conditionnelles avec le texte de la cellule](/cells/fr/javascript-cpp/add-conditional-icons-set-with-the-cell-text/)
- [Insérer une image liée à partir d'une adresse web](/cells/fr/javascript-cpp/insert-a-linked-picture-from-web-address/)
- [Insérer une image en fonction de la référence de la cellule](/cells/fr/javascript-cpp/insert-a-picture-based-on-cell-reference/)
- [Charger une image Web à partir d'une URL dans une feuille de calcul Excel](/cells/fr/javascript-cpp/load-a-web-image-from-a-url-into-an-excel-worksheet/)
