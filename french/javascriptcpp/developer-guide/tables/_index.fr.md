---
title: Créer et gérer des tableaux de fichiers Microsoft Excel avec JavaScript via C++
linktitle: Tableaux
type: docs
weight: 150
url: /fr/javascript-cpp/create-and-format-table/
description: Insérer, redimensionner, modifier, supprimer, et formater des tableaux de fichiers Excel en utilisant Aspose.Cells for JavaScript via C++.
---

## **Créer un tableau**

L'un des avantages des feuilles de calcul est qu'elles vous permettent de créer différents types de listes, par exemple des listes de téléphones, des listes de tâches, des listes de transactions, d'actifs ou de passifs. Plusieurs utilisateurs peuvent travailler ensemble pour utiliser, créer et maintenir des listes variées.

Aspose.Cells prend en charge la création et la gestion de listes.

### **Avantages d'un objet Liste**

Il y a quelques avantages lorsque vous convertissez une liste de données en un véritable objet Liste

- De nouvelles lignes et colonnes sont automatiquement incluses.
- Une ligne de total en bas de votre liste peut être facilement ajoutée pour afficher la SOMME, la MOYENNE, le NOMBRE, etc.
- Les colonnes ajoutées à droite sont automatiquement incorporées dans l'objet Liste.
- Les graphiques basés sur les lignes et colonnes seront automatiquement étendus.
- Les plages nommées affectées aux lignes et colonnes seront automatiquement étendues.
- La liste est protégée contre les suppressions accidentelles de lignes et de colonnes.

### **Création d'un objet Liste à l'aide de Microsoft Excel**

- Sélectionner la plage de données pour créer un objet Liste
- Cela affiche la boîte de dialogue Créer Liste.
- Implémenter l'objet Liste pour les données et spécifier la ligne totale (Sélectionner **Données**, puis **Liste**, puis **Ligne Totale**).

### **Utilisation de l'API Aspose.Cells**

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) contient une collection [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) qui permet d'accéder à chaque feuille de calcul dans un fichier Excel.

Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) offre une large gamme de propriétés et de méthodes pour gérer une feuille de calcul. Pour créer un [**ListObject**](https://reference.aspose.com/cells/javascript-cpp/listobject/) dans une feuille, utilisez la propriété de collection [**listObjects**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#listObjects--) de la classe [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). Chaque [**ListObject**](https://reference.aspose.com/cells/javascript-cpp/listobject/) est, en fait, un objet de la classe [**ListObjectCollection**](https://reference.aspose.com/cells/javascript-cpp/listobjectcollection/), qui fournit également la méthode [**add(number, number, number, number, boolean)**](https://reference.aspose.com/cells/javascript-cpp/listobjectcollection/#add-number-number-number-number-boolean-) pour ajouter un objet Liste et spécifier une plage de cellules pour la liste.

Selon la plage de cellules spécifiée, l'objet Liste est créé par Aspose.Cells. Utilisez des attributs (par exemple, [**showTotals**](https://reference.aspose.com/cells/javascript-cpp/listobject/#showTotals--), [**listColumns**](https://reference.aspose.com/cells/javascript-cpp/listobject/#listColumns--), etc.) de la classe [**ListObject**](https://reference.aspose.com/cells/javascript-cpp/listobject/) pour contrôler la liste.

Dans l'exemple ci-dessous, nous avons créé le même [**ListObject**](https://reference.aspose.com/cells/javascript-cpp/listobject/) en utilisant l'API Aspose.Cells comme nous avons créé avec Microsoft Excel dans la section ci-dessus.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells ListObjects Example</title>
    </head>
    <body>
        <h1>ListObjects Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, TotalsCalculation } = AsposeCells;

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

            const listObjects = workbook.worksheets.get(0).listObjects;

            listObjects.add(1, 1, 7, 5, true);

            const firstList = listObjects.get(0);
            firstList.showTotals = true;

            firstList.listColumns.get(4).totalsCalculation = TotalsCalculation.Sum;

            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">List created and totals calculated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Formater un Tableau**

Pour gérer et analyser un groupe de données connexes, il est possible de transformer une plage de cellules en objet liste (également connu sous le nom de tableau Excel). Un tableau est une série de lignes et de colonnes contenant des données connexes gérées indépendamment des données dans les autres lignes et colonnes. Par défaut, chaque colonne du tableau a la fonction de filtre activée dans la ligne d'en-tête afin que vous puissiez filtrer ou trier rapidement vos données d'objet liste. Vous pouvez ajouter une ligne totale (une ligne spéciale dans une liste qui propose une sélection de fonctions d'agrégation utiles pour travailler avec des données numériques) à l'objet liste qui fournit une liste déroulante de fonctions d'agrégation pour chaque cellule de la ligne totale. Aspose.Cells propose des options pour créer et gérer des listes (ou tableaux).

### **Formatage d'un Objet Liste**

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) contient une collection [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) qui permet d'accéder à chaque feuille de calcul dans un fichier Excel.

Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) offre une large gamme de propriétés et de méthodes pour gérer les feuilles de calcul. Pour créer un [**ListObject**](https://reference.aspose.com/cells/javascript-cpp/listobject/) dans une feuille, utilisez la propriété de collection [**listObjects**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#listObjects--) de la classe [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). Chaque [**ListObject**](https://reference.aspose.com/cells/javascript-cpp/listobject/) est, en fait, un objet de la classe [**ListObjectCollection**](https://reference.aspose.com/cells/javascript-cpp/listobjectcollection/), qui fournit la méthode [**add(number, number, number, number, boolean)**](https://reference.aspose.com/cells/javascript-cpp/listobjectcollection/#add-number-number-number-number-boolean-) pour ajouter un objet Liste et spécifier la plage de cellules qu'il doit englober. Selon la plage de cellules spécifiée, un [**ListObject**](https://reference.aspose.com/cells/javascript-cpp/listobject/) est créé dans la feuille par Aspose.Cells. Utilisez des attributs (par exemple, [**TableStyleType**](https://reference.aspose.com/cells/javascript-cpp/tablestyletype/)) de la classe [**ListObject**](https://reference.aspose.com/cells/javascript-cpp/listobject/) pour formater la table selon vos besoins.

L'exemple ci-dessous ajoute des données d'exemple à une feuille, ajoute un [**ListObject**](https://reference.aspose.com/cells/javascript-cpp/listobject/) et lui applique des styles par défaut. Les styles [**ListObject**](https://reference.aspose.com/cells/javascript-cpp/listobject/) sont supportés par Microsoft Excel 2007/2010.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells ListObject Example</h1>
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
            // This example does not require an input file; it creates a new workbook
            const workbook = new Workbook();

            // Obtaining the reference of the default(first) worksheet
            const sheet = workbook.worksheets.get(0);

            // Obtaining Worksheet's cells collection
            const cells = sheet.cells;

            // Setting the value to the cells (converted putValue -> value)
            cells.get(1, 1).value = "Employee";
            cells.get(1, 2).value = "Quarter";
            cells.get(1, 3).value = "Product";
            cells.get(1, 4).value = "Continent";
            cells.get(1, 5).value = "Country";
            cells.get(1, 6).value = "Sale";

            cells.get(2, 1).value = "David";
            cells.get(3, 1).value = "David";
            cells.get(4, 1).value = "David";
            cells.get(5, 1).value = "David";
            cells.get(6, 1).value = "James";
            cells.get(7, 1).value = "James";
            cells.get(8, 1).value = "James";
            cells.get(9, 1).value = "James";
            cells.get(10, 1).value = "James";
            cells.get(11, 1).value = "Miya";
            cells.get(12, 1).value = "Miya";
            cells.get(13, 1).value = "Miya";
            cells.get(14, 1).value = "Miya";
            cells.get(15, 1).value = "Miya";
            cells.get(2, 2).value = 1;
            cells.get(3, 2).value = 2;
            cells.get(4, 2).value = 3;
            cells.get(5, 2).value = 4;
            cells.get(6, 2).value = 1;
            cells.get(7, 2).value = 2;
            cells.get(8, 2).value = 3;
            cells.get(9, 2).value = 4;
            cells.get(10, 2).value = 4;
            cells.get(11, 2).value = 1;
            cells.get(12, 2).value = 1;
            cells.get(13, 2).value = 2;
            cells.get(14, 2).value = 2;
            cells.get(15, 2).value = 2;

            cells.get(2, 3).value = "Maxilaku";
            cells.get(3, 3).value = "Maxilaku";
            cells.get(4, 3).value = "Chai";
            cells.get(5, 3).value = "Maxilaku";
            cells.get(6, 3).value = "Chang";
            cells.get(7, 3).value = "Chang";
            cells.get(8, 3).value = "Chang";
            cells.get(9, 3).value = "Chang";
            cells.get(10, 3).value = "Chang";
            cells.get(11, 3).value = "Geitost";
            cells.get(12, 3).value = "Chai";
            cells.get(13, 3).value = "Geitost";
            cells.get(14, 3).value = "Geitost";
            cells.get(15, 3).value = "Geitost";

            cells.get(2, 4).value = "Asia";
            cells.get(3, 4).value = "Asia";
            cells.get(4, 4).value = "Asia";
            cells.get(5, 4).value = "Asia";
            cells.get(6, 4).value = "Europe";
            cells.get(7, 4).value = "Europe";
            cells.get(8, 4).value = "Europe";
            cells.get(9, 4).value = "Europe";
            cells.get(10, 4).value = "Europe";
            cells.get(11, 4).value = "America";
            cells.get(12, 4).value = "America";
            cells.get(13, 4).value = "America";
            cells.get(14, 4).value = "America";
            cells.get(15, 4).value = "America";

            cells.get(2, 5).value = "China";
            cells.get(3, 5).value = "India";
            cells.get(4, 5).value = "Korea";
            cells.get(5, 5).value = "India";
            cells.get(6, 5).value = "France";
            cells.get(7, 5).value = "France";
            cells.get(8, 5).value = "Germany";
            cells.get(9, 5).value = "Italy";
            cells.get(10, 5).value = "France";
            cells.get(11, 5).value = "U.S.";
            cells.get(12, 5).value = "U.S.";
            cells.get(13, 5).value = "Brazil";
            cells.get(14, 5).value = "U.S.";
            cells.get(15, 5).value = "U.S.";

            cells.get(2, 6).value = 2000;
            cells.get(3, 6).value = 500;
            cells.get(4, 6).value = 1200;
            cells.get(5, 6).value = 1500;
            cells.get(6, 6).value = 500;
            cells.get(7, 6).value = 1500;
            cells.get(8, 6).value = 800;
            cells.get(9, 6).value = 900;
            cells.get(10, 6).value = 500;
            cells.get(11, 6).value = 1600;
            cells.get(12, 6).value = 600;
            cells.get(13, 6).value = 2000;
            cells.get(14, 6).value = 500;
            cells.get(15, 6).value = 900;

            // Adding a new List Object to the worksheet
            const index = sheet.listObjects.add("A1", "F15", true);

            const listObject = sheet.listObjects.get(index);

            // Adding Default Style to the table (converted setter -> property)
            listObject.tableStyleType = AsposeCells.TableStyleType.TableStyleMedium10;

            // Show Total
            listObject.showTotals = true;

            // Set the Quarter field's calculation type (converted getter/setter -> property)
            listObject.listColumns.get(1).totalsCalculation = AsposeCells.TotalsCalculation.Count;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and table added successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **Sujets avancés**
- [Convertir un Tableau en ODS](/cells/fr/javascript-cpp/convert-table-to-ods/)
- [Trouver des Tables de Requête et des Objets Liste liés aux Connexions de Données Externes](/cells/fr/javascript-cpp/find-query-tables-and-list-objects-related-to-external-data-connections/)
- [Lire et Écrire un Tableau avec une Source de Données de Table de Requête](/cells/fr/javascript-cpp/read-and-write-table-with-query-table-data-source/)
- [Définir le Commentaire d'un Tableau ou Objet Liste à l'intérieur de la Feuille de Calcul](/cells/fr/javascript-cpp/set-the-comment-of-table-or-list-object-inside-the-worksheet/)
- [Tables et Plages](/cells/fr/javascript-cpp/tables-and-ranges/)
