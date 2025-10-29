---
title: Insérer des images et des formes dans les fichiers Excel avec JavaScript via C++  
linktitle: Formes  
type: docs  
weight: 140  
url: /fr/javascript-cpp/insert-shapes/  
description: Gérer les images, objets OLE et formes dans les fichiers Excel en utilisant Aspose.Cells for JavaScript via C++.  
---  

{{% alert color="primary" %}}  
Parfois, vous avez besoin d'insérer des formes nécessaires dans la feuille de calcul. Vous pouvez devoir insérer la même forme à différentes positions de la feuille. Ou vous devez insérer en batch des formes dans la feuille.  
Ne vous inquiétez pas! [Aspose.Cells](https://products.aspose.com/cells/) prend en charge toutes ces opérations.  
{{% /alert %}}  

Les formes dans Excel sont principalement divisées en types suivants :  
- **Images**  
- **Objets OLE**  
- **Lignes**  
- **Rectangles**  
- **Formes de base**  
- **Flèches de base**  
- **Formes d'équation**  
- **Organigrammes**  
- **Étoiles et bannières**  
- **Appels**  

Ce document guide sélectionnera une ou deux formes de chaque type pour faire des exemples. À travers ces exemples, vous apprendrez comment utiliser [Aspose.Cells](https://products.aspose.com/cells/) pour insérer la forme spécifiée dans la feuille.  

## **Ajouter des images dans la feuille Excel en utilisant JavaScript**  

Ajouter des images à une feuille de calcul est très facile. Il suffit de quelques lignes de code :  
Il suffit d'appeler la méthode [**PictureCollection.add(number, number, number, number, Uint8Array)**](https://reference.aspose.com/cells/javascript-cpp/picturecollection/#add-number-number-number-number-uint8array-) de la collection [**Pictures**](https://reference.aspose.com/cells/javascript-cpp/picturecollection) (encapsulée dans l'objet [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)). La méthode [**PictureCollection.add(number, number, number, number, Uint8Array)**](https://reference.aspose.com/cells/javascript-cpp/picturecollection/#add-number-number-number-number-uint8array-) prend les paramètres suivants :  

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
        <p>
            Optional: select an existing Excel file to modify, or leave empty to create a new workbook.
        </p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <p>
            Select an image to insert into the worksheet (required):
        </p>
        <input type="file" id="imageInput" accept="image/*" />
        <br/><br/>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;"></a>
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

            if (!imageInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an image file to insert.</p>';
                return;
            }

            // If an Excel file is provided, open it; otherwise create a new workbook
            let workbook;
            if (fileInput.files.length) {
                const excelFile = fileInput.files[0];
                const arrayBuffer = await excelFile.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Add a new worksheet to the Workbook object
            const sheetIndex = workbook.worksheets.add();

            // Obtain the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Read the selected image file as Uint8Array
            const imageFile = imageInput.files[0];
            const imageArrayBuffer = await imageFile.arrayBuffer();
            const imageBytes = new Uint8Array(imageArrayBuffer);

            // Adding a picture at the location of a cell whose row and column indices are 5 (F6)
            worksheet.pictures.add(5, 5, imageBytes);

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Resulting Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Picture inserted successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

## **Insérer des objets OLE dans une feuille Excel en utilisant JavaScript**  

Aspose.Cells prend en charge l'ajout, l'extraction et la manipulation d'objets OLE dans les feuilles de calcul. Pour cette raison, Aspose.Cells possède la classe [**OleObjectCollection**](https://reference.aspose.com/cells/javascript-cpp/oleobjectcollection), utilisée pour ajouter un nouvel Objet OLE à la liste de collection. Une autre classe, [**OleObject**](https://reference.aspose.com/cells/javascript-cpp/oleobject), représente un objet OLE. Elle possède quelques membres importants :  

- La propriété [**OleObject.imageData**](https://reference.aspose.com/cells/javascript-cpp/oleobject/#imageData--) spécifie les données d'image (icône) de type tableau d'octets. L'image sera affichée pour montrer l'objet OLE dans la feuille de calcul.  
- La propriété [**OleObject.objectData**](https://reference.aspose.com/cells/javascript-cpp/oleobject/#objectData--) spécifie les données de l'objet sous forme de tableau d'octets. Ces données seront affichées dans leur programme associé lors d'un double-clic sur l'icône de l'objet OLE.  

L'exemple suivant montre comment ajouter un ou des objets OLE dans une feuille de calcul.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Insert OLE Object Example</h1>
        <p>
            Select an image to display as the OLE object's icon and an Excel file to embed as the OLE object.
        </p>
        <input type="file" id="imageInput" accept="image/*" />
        <input type="file" id="excelInput" accept=".xls,.xlsx" />
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
            const imageInput = document.getElementById('imageInput');
            const excelInput = document.getElementById('excelInput');
            const resultDiv = document.getElementById('result');

            if (!imageInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an image file for the OLE icon.</p>';
                return;
            }
            if (!excelInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file to embed.</p>';
                return;
            }

            const imageFile = imageInput.files[0];
            const excelFile = excelInput.files[0];

            // Read files as ArrayBuffers
            const imageArrayBuffer = await imageFile.arrayBuffer();
            const excelArrayBuffer = await excelFile.arrayBuffer();

            // Convert to Uint8Array for Aspose.Cells
            const imageData = new Uint8Array(imageArrayBuffer);
            const objectData = new Uint8Array(excelArrayBuffer);

            // Instantiate a new Workbook.
            const workbook = new Workbook();

            // Get the first worksheet.
            const sheet = workbook.worksheets.get(0);

            // Add an Ole object into the worksheet with the image shown in MS Excel.
            sheet.oleObjects.add(14, 3, 200, 220, imageData);

            // Set embedded ole object data.
            sheet.oleObjects.get(0).objectData = objectData;

            // Save the excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData], { type: 'application/vnd.ms-excel' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">OLE object embedded successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

## **Insérer une ligne dans la feuille Excel en utilisant JavaScript**  

La forme de la ligne appartient à la catégorie **lignes**.  

*  

- Sélectionnez la cellule où vous souhaitez insérer la ligne  
- Cliquez sur le menu Insérer, puis sur Formes.  
- Ensuite, sélectionnez la ligne dans 'Formes récemment utilisées' ou 'Lignes'  

![](line.png)  

***Utilisation d'Aspose.Cells***  

Vous pouvez utiliser la méthode suivante pour insérer une ligne dans la feuille de calcul.  

{{% alert color="primary" %}}  
[**ShapeCollection.addLine(number, number, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addLine-number-number-number-number-number-number-)  
La méthode renvoie un objet [LineShape](https://reference.aspose.com/cells/javascript-cpp/lineshape).  
{{% /alert %}}  

L'exemple suivant montre comment insérer une ligne dans une feuille de calcul.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Add Line Example</h1>
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
            document.getElementById('runExample').addEventListener('click', async () => {
                const fileInput = document.getElementById('fileInput');
                if (!fileInput.files.length) {
                    document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                    return;
                }

                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();

                // Create workbook from uploaded file
                const workbook = new Workbook(new Uint8Array(arrayBuffer));

                // Access first worksheet from the collection
                const sheet = workbook.worksheets.get(0);

                // Add the line to the worksheet
                sheet.shapes.addLine(2, 0, 2, 0, 100, 300);

                // Save workbook to XLSX format and create download link
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = 'sample.xlsx';
                downloadLink.style.display = 'block';
                downloadLink.textContent = 'Download Excel File';

                document.getElementById('result').innerHTML = '<p style="color: green;">Line added successfully! Click the download link to get the modified file.</p>';
            });
        });
    </script>
</html>
```  

Exécutez le code ci-dessus, vous obtiendrez les résultats suivants:  

![](line2.png)  

## **Insérer une flèche en ligne dans la feuille Excel en utilisant JavaScript**  

La forme de la flèche de ligne appartient à la catégorie **Lignes**. C'est un cas particulier de ligne.  

*  

- Sélectionnez la cellule où vous souhaitez insérer la flèche de ligne  
- Cliquez sur le menu Insérer, puis sur Formes.  
- Ensuite, sélectionnez la flèche dans 'Formes récemment utilisées' ou 'Lignes'  

![](line_arrow1.png)  

***Utilisation d'Aspose.Cells***  

Vous pouvez utiliser la méthode suivante pour insérer une flèche de ligne dans la feuille de calcul.  

{{% alert color="primary" %}}  
[**ShapeCollection.addLine(number, number, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addLine-number-number-number-number-number-number-)  
La méthode renvoie un objet [LineShape](https://reference.aspose.com/cells/javascript-cpp/lineshape).  
{{% /alert %}}  

L'exemple suivant montre comment insérer une flèche de ligne dans une feuille de calcul.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Add Line Arrow Example</h1>
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

            // Loads the workbook which contains shapes
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet from the collection
            const sheet = workbook.worksheets.get(0);

            // Add the line arrow to the worksheet
            let s = sheet.shapes.addLine(2, 0, 2, 0, 100, 300); // method 1
            // let s = sheet.shapes.addAutoShape(AsposeCells.AutoShapeType.Line, 2, 0, 2, 0, 100, 300); // method 2
            // let s = sheet.shapes.addShape(AsposeCells.MsoDrawingType.Line, 2, 0, 2, 0, 100, 300); // method 3

            // add a arrow at the line begin
            s.line.beginArrowheadStyle = AsposeCells.MsoArrowheadStyle.Arrow; // arrow type
            s.line.beginArrowheadWidth = AsposeCells.MsoArrowheadWidth.Wide; // arrow width
            s.line.beginArrowheadLength = AsposeCells.MsoArrowheadLength.Short; // arrow length

            // add a arrow at the line end
            s.line.endArrowheadStyle = AsposeCells.MsoArrowheadStyle.ArrowOpen; // arrow type
            s.line.endArrowheadWidth = AsposeCells.MsoArrowheadWidth.Narrow; // arrow width
            s.line.endArrowheadLength = AsposeCells.MsoArrowheadLength.Long; // arrow length

            // Save and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sample.with_arrow.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File with Arrow';

            document.getElementById('result').innerHTML = '<p style="color: green;">Arrow added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

Exécutez le code ci-dessus, vous obtiendrez les résultats suivants:  

![](line_arrow2.png)  

## **Insérer un rectangle dans la feuille Excel en utilisant JavaScript**  

La forme du rectangle appartient à la catégorie **Rectangles**.  

*  

- Sélectionnez la cellule où vous souhaitez insérer le rectangle  
- Cliquez sur le menu Insérer, puis sur Formes.  
- Ensuite, sélectionnez le rectangle dans 'Formes récemment utilisées' ou 'Rectangles'  

![](rectangle.png)  

***Utilisation d'Aspose.Cells***  

Vous pouvez utiliser la méthode suivante pour insérer un rectangle dans la feuille de calcul.  

{{% alert color="primary" %}}  
[**ShapeCollection.addRectangle(number, number, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addRectangle-number-number-number-number-number-number-)  
La méthode renvoie un objet [RectangleShape](https://reference.aspose.com/cells/javascript-cpp/rectangleshape).  
{{% /alert %}}  

L'exemple suivant montre comment insérer un rectangle dans une feuille de calcul.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add Rectangle</title>
    </head>
    <body>
        <h1>Add Rectangle to Worksheet</h1>
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

            // Create workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet from the collection
            const sheet = workbook.worksheets.get(0);

            // Add the rectangle to the worksheet
            sheet.shapes.addRectangle(2, 0, 2, 0, 100, 300);

            // Save and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sample.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Rectangle added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

Exécutez le code ci-dessus, vous obtiendrez les résultats suivants:  

![](rectangle2.png)  

## **Insérer un cube dans la feuille Excel en utilisant JavaScript**  

La forme du cube appartient à la catégorie **Formes de base**.  

*  

- Sélectionnez la cellule où vous souhaitez insérer le cube  
- Cliquez sur le menu Insérer, puis sur Formes.  
- Ensuite, sélectionnez le Cube dans **Formes de base**  

![](cube.png)  

***Utilisation d'Aspose.Cells***  

Vous pouvez utiliser la méthode suivante pour insérer un cube dans la feuille de calcul.  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
La méthode renvoie un objet [Shape](https://reference.aspose.com/cells/javascript-cpp/shape).  
{{% /alert %}}  

L'exemple suivant montre comment insérer un cube dans une feuille de calcul.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add Cube</title>
    </head>
    <body>
        <h1>Add Cube to Worksheet</h1>
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
            const result = document.getElementById('result');
            if (!fileInput.files.length) {
                result.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet from the collection
            const sheet = workbook.worksheets.get(0);

            // Add the cube to the worksheet
            sheet.shapes.addAutoShape(AsposeCells.AutoShapeType.Cube, 2, 0, 2, 0, 100, 300);

            // Save and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sample.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            result.innerHTML = '<p style="color: green;">Cube added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

Exécutez le code ci-dessus, vous obtiendrez les résultats suivants:  

![](cube2.png)  

## **Insérer une flèche de type callout quad dans la feuille Excel en utilisant JavaScript**  

La forme de la flèche de légende de type callout appartient à la catégorie **Flèches de bloc**.  

*  

- Sélectionnez la cellule où vous souhaitez insérer la flèche de callout quad  
- Cliquez sur le menu Insérer, puis sur Formes.  
- Ensuite, sélectionnez la flèche de légende de type callout dans **Flèches de bloc**  

![](callout_quad_arrow.png)  

***Utilisation d'Aspose.Cells***  

Vous pouvez utiliser la méthode suivante pour insérer une flèche de callout quad dans la feuille de calcul.  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
La méthode retourne un objet [Shape](https://reference.aspose.com/cells/javascript-cpp/shape).  
{{% /alert %}}  

L'exemple suivant montre comment insérer une flèche de légende de type callout dans une feuille de calcul.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add Callout Quad Arrow</title>
    </head>
    <body>
        <h1>Add Callout Quad Arrow Shape</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, AutoShapeType } = AsposeCells;

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

            const sheet = workbook.worksheets.get(0);

            sheet.shapes.addAutoShape(AutoShapeType.QuadArrowCallout, 2, 0, 2, 0, 100, 100);

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sample.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Shape added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

Exécutez le code ci-dessus, vous obtiendrez les résultats suivants:  

![](callout_quad_arrow2.png)  

## **Insertion d’un signe de multiplication dans une feuille Excel en utilisant JavaScript**  

La forme du symbole de multiplication appartient à la catégorie **Formes d'équation**.  

*  

- Sélectionnez la cellule où vous souhaitez insérer le signe de multiplication  
- Cliquez sur le menu Insérer, puis sur Formes.  
- Ensuite, sélectionnez le symbole de multiplication dans **Formes d'équation**  

![](multiplication_sign.png)  

***Utilisation d'Aspose.Cells***  

Vous pouvez utiliser la méthode suivante pour insérer un signe de multiplication dans la feuille de calcul.  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
La méthode retourne un objet [Shape](https://reference.aspose.com/cells/javascript-cpp/shape).  
{{% /alert %}}  

L'exemple suivant montre comment insérer un symbole de multiplication dans une feuille de calcul.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add Multiply Sign</title>
    </head>
    <body>
        <h1>Add Multiplication Sign to Worksheet</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, AutoShapeType } = AsposeCells;

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

            // Instantiating a Workbook object by opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet from the collection
            const sheet = workbook.worksheets.get(0);

            // Add the multiplication sign to the worksheet
            sheet.shapes.addAutoShape(AsposeCells.AutoShapeType.MathMultiply, 2, 0, 2, 0, 100, 100);

            // Save and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sample.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Multiplication sign added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

Exécutez le code ci-dessus, vous obtiendrez les résultats suivants:  

![](multiplication_sign2.png)  

## **Insertion d’un document multidocument dans une feuille Excel en utilisant JavaScript**  

La forme du multidocument appartient à la catégorie **Diagrammes de flux**.  

*  

- Sélectionnez la cellule où vous souhaitez insérer le multimédia  
- Cliquez sur le menu Insérer, puis sur Formes.  
- Ensuite, sélectionnez le multidocument dans **Diagrammes de flux**  

![](multidocument.png)  

***Utilisation d'Aspose.Cells***  

Vous pouvez utiliser la méthode suivante pour insérer un multimédia dans la feuille de calcul.  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
La méthode retourne un objet [Shape](https://reference.aspose.com/cells/javascript-cpp/shape).  
{{% /alert %}}  

L'exemple suivant montre comment insérer un multidocument dans une feuille de calcul.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
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
        const { Workbook, SaveFormat, AutoShapeType } = AsposeCells;

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

            // Create workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet from the collection
            const sheet = workbook.worksheets.get(0);

            // Add the multidocument to the worksheet
            sheet.shapes.addAutoShape(AutoShapeType.FlowChartMultidocument, 2, 0, 2, 0, 100, 100);

            // Save and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sample.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

Exécutez le code ci-dessus, vous obtiendrez les résultats suivants:  

![](multidocument2.png)  

## **Insertion d’une étoile à cinq branches dans une feuille Excel en utilisant JavaScript**  

La forme de l'étoile à cinq branches appartient à la catégorie **Étoiles et Bannières**.  

*  

- Sélectionnez la cellule où vous souhaitez insérer l'étoile à cinq branches  
- Cliquez sur le menu Insérer, puis sur Formes.  
- Ensuite, sélectionnez l'étoile à cinq branches dans **Étoiles et Bannières**  

![](star_5_points.png)  

***Utilisation d'Aspose.Cells***  

Vous pouvez utiliser la méthode suivante pour insérer une étoile à cinq branches dans la feuille de calcul.  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
La méthode retourne un objet [Shape](https://reference.aspose.com/cells/javascript-cpp/shape).  
{{% /alert %}}  

L'exemple suivant montre comment insérer une étoile à cinq branches dans une feuille de calcul.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add Star Shape</title>
    </head>
    <body>
        <h1>Add Five-Pointed Star to Worksheet</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, AutoShapeType } = AsposeCells;

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

            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const sheet = workbook.worksheets.get(0);

            // Add the Five-pointed star to the worksheet
            sheet.shapes.addAutoShape(AutoShapeType.Star5, 2, 0, 2, 0, 100, 100);

            // Save and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sample.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Star shape added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

Exécutez le code ci-dessus, vous obtiendrez les résultats suivants:  

![](star_5_points2.png)  

## **Insertion d’un nuage de bulle de pensée dans une feuille Excel en utilisant JavaScript**  

La forme du nuage de bulle de pensée appartient à la catégorie **Callouts**.  

*  

- Sélectionnez la cellule où vous souhaitez insérer le nuage de bulles de pensée  
- Cliquez sur le menu Insérer, puis sur Formes.  
- Ensuite, sélectionnez le nuage de bulle de pensée dans **Callouts**  

![](thought_bubble_cloud.png)  

***Utilisation d'Aspose.Cells***  

Vous pouvez utiliser la méthode suivante pour insérer un nuage de bulles de pensée dans la feuille de calcul.  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
La méthode retourne un objet [Shape](https://reference.aspose.com/cells/javascript-cpp/shape).  
{{% /alert %}}  

L'exemple suivant montre comment insérer un nuage de bulle de pensée dans une feuille de calcul.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Add Cloud Callout Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, AutoShapeType } = AsposeCells;

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

            // Access first worksheet from the collection
            const sheet = workbook.worksheets.get(0);

            // Add the thought bubble cloud to the worksheet
            sheet.shapes.addAutoShape(AutoShapeType.CloudCallout, 2, 0, 2, 0, 100, 100);

            // Save and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sample.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Cloud callout added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

Exécutez le code ci-dessus, vous obtiendrez les résultats suivants:  

![](thought_bubble_cloud2.png)  

## **Sujets avancés**  
- [Modifier les valeurs d'ajustement de la forme](/cells/fr/javascript-cpp/change-adjustment-values-of-the-shape/)  
- [Copier des formes entre les feuilles de calcul](/cells/fr/javascript-cpp/copy-shapes-between-worksheets/)  
- [Données dans une forme non primitive](/cells/fr/javascript-cpp/data-in-non-primitive-shape/)  
- [Trouver la position absolue de la forme dans la feuille de calcul](/cells/fr/javascript-cpp/finding-absolute-position-of-shape-inside-the-worksheet/)  
- [Obtenir les points de connexion de la forme](/cells/fr/javascript-cpp/get-connection-points-from-shape/)  
- [Gestion des contrôles](/cells/fr/javascript-cpp/managing-controls/)  
- [Ajouter des icônes à la feuille de calcul](/cells/fr/javascript-cpp/insert-svg-to-excel/)  
- [Gestion des objets OLE](/cells/fr/javascript-cpp/managing-ole-objects/)  
- [Gestion des images](/cells/fr/javascript-cpp/managing-pictures/)  
- [Gérer les Smart Art](/cells/fr/javascript-cpp/managing-smartart/)  
- [Gestion de la zone de texte](/cells/fr/javascript-cpp/managing-textbox-of-excel/)  
- [Ajouter un filigrane WordArt à la feuille de calcul](/cells/fr/javascript-cpp/add-wordart-watermark-to-worksheet/)  
- [Actualiser les valeurs des formes liées](/cells/fr/javascript-cpp/refresh-values-of-linked-shapes/)  
- [Envoyer la forme à l'avant ou à l'arrière dans la feuille de calcul](/cells/fr/javascript-cpp/send-shape-front-or-back-inside-the-worksheet/)  
- [Gérer les options de la forme](/cells/fr/javascript-cpp/managing-shape-options/)  
- [Gérer les options de texte de la forme](/cells/fr/javascript-cpp/managing-shape-text-options/)  
- [Extensions Web - Compléments Office](/cells/fr/javascript-cpp/web-extensions-office-add-ins/)
