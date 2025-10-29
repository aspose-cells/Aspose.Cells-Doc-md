---
title: Gérer les données des fichiers Excel
linktitle: Données de cellules
type: docs
weight: 110
url: /fr/javascript-cpp/view-and-edit-excel-data/
description: Cet article décrit comment visualiser et éditer les données des fichiers Excel avec la bibliothèque Aspose.Cells pour JavaScript via C++.
keywords: Aspose.Cells JavaScript via C++, Gérer les données du fichier Excel, ajouter des données au fichier Excel, obtenir des données du fichier Excel, comment améliorer l efficacité de l ajout de données, gérer les données des cellules, mettre à jour les données des cellules, obtenir les données des cellules, insérer des données dans les cellules
---

{{% alert color="primary" %}}

Dans [Accéder aux cellules d'une feuille de calcul](/cells/fr/javascript-cpp/accessing-cells-of-a-worksheet/), nous avons abordé les approches de base pour accéder aux cellules d'une feuille de calcul. Cet article utilise l'une de ces approches pour ajouter différents types de données aux cellules.

{{% /alert %}}

## **Comment ajouter des données aux cellules**

Aspose.Cells for Java Script via C++ fournit une classe, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) contient une collection [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) qui permet d'accéder à chaque feuille de calcul dans le fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) fournit une collection [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--). Chaque élément de la collection [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--) représente un objet de la classe [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell).

Aspose.Cells permet aux développeurs d'ajouter des données dans les cellules des feuilles de calcul en appelant la méthode [**putValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#putValue-boolean-) de la classe [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell). Aspose.Cells propose des versions surchargeables de la méthode [**putValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#putValue-boolean-) qui permettent aux développeurs d'ajouter différents types de données dans les cellules. En utilisant ces versions surchargeables de la méthode [**putValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#putValue-boolean-), il est possible d’ajouter des valeurs de type Boolean, chaîne, double, entier, ou date/heure, etc. dans la cellule.

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
            // If a file is provided, open it; otherwise create a new workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Obtaining the reference of the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Adding values to cells
            const cells = worksheet.cells;
            const cellA1 = cells.get("A1");
            cellA1.value = "Hello World";

            const cellA2 = cells.get("A2");
            cellA2.value = 20.5;

            const cellA3 = cells.get("A3");
            cellA3.value = 15;

            const cellA4 = cells.get("A4");
            cellA4.value = true;

            const cellA5 = cells.get("A5");
            cellA5.value = new Date();

            // Setting the display format of the date
            let style = cellA5.style;
            style.number = 15;
            cellA5.style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created/modified successfully. Click the download link to get the file.</p>';
        });
    </script>
</html>
```


## **Comment améliorer l'efficacité**

Si vous utilisez la méthode [**putValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#putValue-boolean-) pour insérer une grande quantité de données dans une feuille de calcul, vous devriez d'abord ajouter des valeurs aux cellules, ligne par ligne puis colonnes par colonnes. Cette approche améliore considérablement l'efficacité de vos applications.

## **Comment récupérer des données à partir de cellules**

Aspose.Cells for JavaScript via C++ fournit une classe, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) contient une collection [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) qui permet d'accéder aux feuilles de calcul du fichier. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) fournit une collection [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--). Chaque élément de la collection [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--) représente un objet de la classe [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell).

La classe [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) fournit plusieurs propriétés permettant aux développeurs de récupérer les valeurs des cellules selon leurs types de données. Ces propriétés incluent :

- [**stringValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#stringValue--) : renvoie la valeur chaîne de la cellule.
- [**doubleValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#doubleValue--) : renvoie la valeur double de la cellule.
- [**boolValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#boolValue--) : renvoie la valeur booléenne de la cellule.
- [**dateTimeValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#dateTimeValue--) : renvoie la valeur date/heure de la cellule.
- [**floatValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#floatValue--) : renvoie la valeur float de la cellule.
- [**intValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#intValue--) : renvoie la valeur entière de la cellule.

Lorsqu'un champ n'est pas rempli, les cellules avec [**doubleValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#doubleValue--) ou [**floatValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#floatValue--) lèvent une exception.

Le type de données contenu dans une cellule peut également être vérifié en utilisant la méthode [**type**](https://reference.aspose.com/cells/javascript-cpp/cell/#type--) de la classe [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell). En fait, la méthode [**type**](https://reference.aspose.com/cells/javascript-cpp/cell/#type--) de la classe [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) est basée sur l'énumération [**CellValueType**](https://reference.aspose.com/cells/javascript-cpp/cellvaluetype) dont les valeurs prédéfinies sont listées ci-dessous :

|**Types de valeur de cellule**|**Description**|
| :- | :- |
|IsBool| Spécifie que la valeur de la cellule est un booléen.
|IsDateTime| Spécifie que la valeur de la cellule est une date/heure.
|IsNull| Représente une cellule vide.
|IsNumeric| Spécifie que la valeur de la cellule est numérique.
|IsString| Spécifie que la valeur de la cellule est une chaîne de caractères.
|IsUnknown| Spécifie que la valeur de la cellule est inconnue.

Vous pouvez également utiliser les types de valeur de cellule prédéfinis ci-dessus pour comparer avec le type de données présent dans chaque cellule.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Read Cell Values Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Opening an existing workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing first worksheet
            const worksheet = workbook.worksheets.get(0);

            var cells = worksheet.cells;
            var maxRow = cells.maxRow;
            var maxColumn = cells.maxColumn;
            let logs = [];
            for (let i = 0; i <= maxRow; i++) {
                for (let j = 0; j <= maxColumn; j++) 
                {
                    const cell1 = cells.get(i, j);
                    if (!cell1) {
                        continue;
                    }
                    // Variables to store values of different data types
                    let stringValue;
                    let doubleValue;
                    let boolValue;
                    let dateTimeValue;

                    // Passing the type of the data contained in the cell for evaluation
                    switch (cell1.type) {
                        // Evaluating the data type of the cell data for string value
                        case AsposeCells.CellValueType.IsString:
                            stringValue = cell1.stringValue;
                            console.log("String Value: " + stringValue);
                            logs.push("String Value: " + stringValue);
                            break;

                        // Evaluating the data type of the cell data for double value
                        case AsposeCells.CellValueType.IsNumeric:
                            doubleValue = cell1.doubleValue;
                            console.log("Double Value: " + doubleValue);
                            logs.push("Double Value: " + doubleValue);
                            break;

                        // Evaluating the data type of the cell data for boolean value
                        case AsposeCells.CellValueType.IsBool:
                            boolValue = cell1.boolValue;
                            console.log("Bool Value: " + boolValue);
                            logs.push("Bool Value: " + boolValue);
                            break;

                        // Evaluating the data type of the cell data for date/time value
                        case AsposeCells.CellValueType.IsDateTime:
                            dateTimeValue = cell1.dateTimeValue;
                            console.log("DateTime Value: " + dateTimeValue);
                            logs.push("DateTime Value: " + dateTimeValue);
                            break;

                        // Evaluating the unknown data type of the cell data
                        case AsposeCells.CellValueType.IsUnknown:
                            stringValue = cell1.stringValue;
                            console.log("Unknown Value: " + stringValue);
                            logs.push("Unknown Value: " + stringValue);
                            break;

                        // Terminating the type checking of type of the cell data is null
                        case AsposeCells.CellValueType.IsNull:
                            break;
                    }
                }
            }

            document.getElementById('result').innerHTML = `<p style="color: green;">Operation completed successfully! See console for detailed cell values.</p><pre>${logs.join("\n")}</pre>`;
        });
    </script>
</html>
```


{{% alert color="primary" %}}

Lors de la manipulation de feuilles de calcul, les utilisateurs peuvent ajouter différents types de données dans les cellules. Ces types de données peuvent inclure des valeurs Boolean, entiers, flottants, texte ou date/heure. Avec Aspose.Cells, vous pouvez obtenir les valeurs appropriées des cellules selon leurs types de données.

{{% /alert %}}

## **Sujets avancés**
- [Accès aux cellules d'une feuille de calcul](/cells/fr/javascript-cpp/accessing-cells-of-a-worksheet/)
- [Convertir des données numériques textuelles en nombre](/cells/fr/javascript-cpp/convert-text-numeric-data-to-number/)
- [Création de sous-totaux](/cells/fr/javascript-cpp/creating-subtotals/)
- [Filtrage des données](/cells/fr/javascript-cpp/data-filtering/)
- [Tri des données](/cells/fr/javascript-cpp/sort-data-of-excel/)
- [Validation des données](/cells/fr/javascript-cpp/data-validation/)
- [Trouver ou rechercher des données](/cells/fr/javascript-cpp/find-or-search-data/)
- [Obtenir la valeur de chaîne de cellule avec et sans mise en forme](/cells/fr/javascript-cpp/get-cell-string-value-with-and-without-formatting/)
- [Ajouter du texte enrichi HTML à l'intérieur de la cellule](/cells/fr/javascript-cpp/adding-html-rich-text-inside-the-cell/)
- [Insérer des hyperliens dans Excel ou OpenOffice](/cells/fr/javascript-cpp/insert-hyperlinks-to-excel/)
- [Comment et où utiliser des énumérateurs](/cells/fr/javascript-cpp/how-and-where-to-use-enumerators/)
- [Mesurer la largeur et la hauteur de la valeur de la cellule en pixels](/cells/fr/javascript-cpp/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/)
- [Lire les valeurs de cellule dans plusieurs threads simultanément](/cells/fr/javascript-cpp/reading-cell-values-in-multiple-threads-simultaneously/)
- [Conversion entre le nom de cellule et l'indice de ligne/colonne](/cells/fr/javascript-cpp/names-and-indices/)
- [Peupler d'abord les données par ligne puis par colonne](/cells/fr/javascript-cpp/populate-data-first-by-row-then-by-column/)
- [Préserver le préfixe d'apostrophe unique de la valeur de la cellule ou de la plage](/cells/fr/javascript-cpp/preserve-single-quote-prefix-of-cell-value-or-range/)
- [Accéder et mettre à jour les parties du texte enrichi de la cellule](/cells/fr/javascript-cpp/access-and-update-the-portions-of-rich-text-of-cell/)
