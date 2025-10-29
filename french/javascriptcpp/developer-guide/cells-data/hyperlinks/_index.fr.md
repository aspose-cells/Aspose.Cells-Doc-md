---
title: Insérer des liens hypertexte dans Excel ou OpenOffice
linktitle: Gérer les liens hypertexte
type: docs
weight: 45
url: /fr/javascript-cpp/insert-hyperlinks-to-excel/
description: Comment insérer des hyperliens dans un fichier Excel avec la bibliothèque Aspose.Cells sans MS Excel en utilisant JavaScript via C++.
keywords: Insérer des hyperliens dans Excel JavaScript via C++, Ajouter ou insérer des hyperliens JavaScript via C++, Ajouter ou insérer un lien vers une URL JavaScript via C++, Ajouter ou insérer un lien dans une cellule JavaScript via C++, Ajouter un lien vers un fichier externe JavaScript via C++
---

{{% alert color="primary" %}} 

Un lien hypertexte est utilisé pour créer un lien entre deux entités. Tout le monde est familier avec l'utilisation des liens hypertexte, en particulier sur les sites Internet.
En utilisant Aspose.Cells, les développeurs peuvent créer différents types de liens hypertexte dans les fichiers Microsoft Excel. Ce sujet explique quels types de liens hypertexte sont pris en charge par Aspose.Cells et comment ils peuvent être utilisés dans nos fichiers Excel.

{{% /alert %}} 

## **Ajout de liens hypertexte**
Aspose.Cells permet aux développeurs d'ajouter des hyperliens aux fichiers Excel soit via l'API, soit en utilisant des feuilles de calcul de conception (feuilles où les hyperliens sont créés manuellement et Aspose.Cells est utilisé pour les importer dans d'autres feuilles).

Aspose.Cells fournit une classe, [Workbook](https://reference.aspose.com/cells/javascript-cpp/workbook) qui représente un fichier Microsoft Excel. La classe [Workbook](https://reference.aspose.com/cells/javascript-cpp/workbook) contient une [WorksheetCollection](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection) permettant d'accéder à chaque feuille du classeur Excel. Une feuille est représentée par la classe [Worksheet](https://reference.aspose.com/cells/javascript-cpp/worksheet). La classe [Worksheet](https://reference.aspose.com/cells/javascript-cpp/worksheet) offre différentes méthodes pour ajouter différents hyperliens aux fichiers Excel.
## **Ajout de lien vers une URL**
La collection [hyperliens](https://reference.aspose.com/cells/javascript-cpp/worksheet/#hyperlinks--) de la classe [Worksheet](https://reference.aspose.com/cells/javascript-cpp/worksheet) représente une collection de [Hyperlink](https://reference.aspose.com/cells/javascript-cpp/hyperlink). Ajoutez des hyperliens vers des URL en appelant la méthode [add](https://reference.aspose.com/cells/javascript-cpp/hyperlinkcollection/#add-string-number-number-string-). La méthode [add](https://reference.aspose.com/cells/javascript-cpp/hyperlinkcollection/#add-string-number-number-string-) prend les paramètres suivants :

- Nom de la cellule, le nom de la cellule à laquelle le lien hypertexte sera ajouté.
- Nombre de lignes, le nombre de lignes dans cette plage de liens hypertexte.
- Nombre de colonnes, le nombre de colonnes dans cette plage de liens hypertexte.
- URL, l'adresse URL.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Add Hyperlink Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example (Create Workbook & Add Hyperlink)</button>
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
            // Instantiate a new Workbook
            const workbook = new Workbook();

            // Obtain the reference of the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Add a hyperlink to a URL at "A1" cell
            worksheet.hyperlinks.add("A1", 1, 1, "http://www.aspose.com");

            // Save the Excel file and provide a download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and hyperlink added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


{{% alert color="primary" %}} 

Dans l'exemple ci-dessus, un lien hypertexte est ajouté à une URL dans une cellule vide, ** A1 **. Dans de tels cas, si une cellule est vide, l'adresse URL est également ajoutée à cette cellule vide en tant que sa valeur. Si la cellule n'est pas vide et qu'un lien hypertexte est ajouté, la valeur de la cellule ressemble à du texte brut. Pour le faire ressembler à un lien hypertexte, appliquez les paramètres de formatage appropriés sur cette cellule.

{{% /alert %}} 
## **Ajouter un lien vers une cellule dans le même fichier**
Il est possible d'ajouter des hyperliens dans des cellules du même fichier Excel en appelant la méthode [add](https://reference.aspose.com/cells/javascript-cpp/hyperlinkcollection/#add-string-number-number-string-). La méthode [add](https://reference.aspose.com/cells/javascript-cpp/hyperlinkcollection/#add-string-number-number-string-) fonctionne pour les hyperliens internes et externes. Une version surchargée de la méthode prend les paramètres suivants :

- Nom de la cellule, le nom de la cellule à laquelle le lien hypertexte sera ajouté.
- Nombre de lignes, le nombre de lignes dans cette plage de liens hypertexte.
- Nombre de colonnes, le nombre de colonnes dans cette plage de liens hypertexte.
- URL, l'adresse de la cellule cible.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Add Internal Hyperlink Example</h1>
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
            // Create a new Workbook
            const workbook = new Workbook();

            // Adding a new worksheet to the Workbook object
            workbook.worksheets.add();

            // Obtaining the reference of the first (default) worksheet
            const worksheet = workbook.worksheets.get(0);

            // Adding an internal hyperlink to the "B3" cell of the other worksheet "Sheet2" in the same Excel file
            worksheet.hyperlinks.add("B3", 1, 1, "Sheet2!B9");

            // Saving the Excel file and providing a download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Excel file created successfully. Click the download link to save it.</p>';
        });
    </script>
</html>
```


## **Ajouter un lien vers un fichier externe**
Il est possible d'ajouter des hyperliens vers des fichiers Excel externes en appelant la méthode [add](https://reference.aspose.com/cells/javascript-cpp/hyperlinkcollection/#add-string-number-number-string-). La méthode [add](https://reference.aspose.com/cells/javascript-cpp/hyperlinkcollection/#add-string-number-number-string-) prend les paramètres suivants :

- Nom de la cellule, le nom de la cellule à laquelle le lien hypertexte sera ajouté.
- Nombre de lignes, le nombre de lignes dans cette plage de liens hypertexte.
- Nombre de colonnes, le nombre de colonnes dans cette plage de liens hypertexte.
- URL, l'adresse de la cible, fichier Excel externe.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <p>Select an optional Excel file to use its filename as the hyperlink target (or leave empty to use "book1.xls"):</p>
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
            let targetFileName = 'book1.xls';
            if (fileInput.files.length) {
                targetFileName = fileInput.files[0].name;
            }

            // Instantiating a Workbook object
            const workbook = new Workbook();

            // Adding a new worksheet to the Excel object
            const i = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(i);

            // Adding an internal hyperlink to the "A5" cell of the other worksheet "Sheet2" in the same Excel file
            worksheet.hyperlinks.add("A5", 1, 1, targetFileName);

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Hyperlink added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```



## **Sujets avancés**
- [Ajouter des hyperliens d'image](/cells/fr/javascript-cpp/add-image-hyperlinks/)
- [Détecter le type de lien hypertexte](/cells/fr/javascript-cpp/detect-hyperlink-type/)
- [Modifier les hyperliens de la feuille de calcul](/cells/fr/javascript-cpp/editing-hyperlinks-of-worksheet/)
- [Obtenir des hyperliens dans la plage](/cells/fr/javascript-cpp/get-hyperlinks-in-range/)
