---
title: Créer et gérer des tableaux dans des fichiers Microsoft Excel avec Node.js via C++
linktitle: Tableaux
type: docs
weight: 150
url: /fr/nodejs-cpp/create-and-format-table/
description: Insérer, redimensionner, éditer, supprimer, et formater des tableaux dans des fichiers Excel utilisant Aspose.Cells for Node.js via C++.
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

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contient une collection [**getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) qui permet d'accéder à chaque feuille de calcul dans un fichier Excel.

Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) offre une large gamme de propriétés et de méthodes pour gérer une feuille de calcul. Pour créer un [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject/) dans une feuille, utilisez la propriété de collection [**getListObjects()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getListObjects--) de la classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). Chaque [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject/) est, en fait, un objet de la classe [**ListObjectCollection**](https://reference.aspose.com/cells/nodejs-cpp/listobjectcollection/), qui fournit également la méthode [**add(number, number, number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/listobjectcollection/#add-number-number-number-number-boolean-) pour ajouter un objet Liste et spécifier une plage de cellules pour la liste.

Selon la plage de cellules spécifiée, l'objet Liste est créé par Aspose.Cells. Utilisez des attributs (par exemple, [**getShowTotals()**](https://reference.aspose.com/cells/nodejs-cpp/listobject/#getShowTotals--), [**getListColumns()**](https://reference.aspose.com/cells/nodejs-cpp/listobject/#getListColumns--), etc.) de la classe [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject/) pour contrôler la liste.

Dans l'exemple ci-dessous, nous avons créé le même [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject/) en utilisant l'API Aspose.Cells comme nous avons créé avec Microsoft Excel dans la section ci-dessus.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Create a Workbook object.
// Open a template excel file.
const workbook = new AsposeCells.Workbook(filePath);

// Get the List objects collection in the first worksheet.
const listObjects = workbook.getWorksheets().get(0).getListObjects();

// Add a List based on the data source range with headers on.
listObjects.add(1, 1, 7, 5, true);

// Show the total row for the List.
listObjects.get(0).setShowTotals(true);

// Calculate the total of the last (5th) list column.
listObjects.get(0).getListColumns().get(4).setTotalsCalculation(AsposeCells.TotalsCalculation.Sum);

// Save the excel file.
workbook.save(path.join(dataDir, "output.xls"));
```

## **Formater un Tableau**

Pour gérer et analyser un groupe de données connexes, il est possible de transformer une plage de cellules en objet liste (également connu sous le nom de tableau Excel). Un tableau est une série de lignes et de colonnes contenant des données connexes gérées indépendamment des données dans les autres lignes et colonnes. Par défaut, chaque colonne du tableau a la fonction de filtre activée dans la ligne d'en-tête afin que vous puissiez filtrer ou trier rapidement vos données d'objet liste. Vous pouvez ajouter une ligne totale (une ligne spéciale dans une liste qui propose une sélection de fonctions d'agrégation utiles pour travailler avec des données numériques) à l'objet liste qui fournit une liste déroulante de fonctions d'agrégation pour chaque cellule de la ligne totale. Aspose.Cells propose des options pour créer et gérer des listes (ou tableaux).

### **Formatage d'un Objet Liste**

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contient une collection [**getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) qui permet d'accéder à chaque feuille de calcul dans un fichier Excel.

Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) offre une large gamme de propriétés et de méthodes pour gérer les feuilles de calcul. Pour créer un [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject/) dans une feuille, utilisez la propriété de collection [**getListObjects()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getListObjects--) de la classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). Chaque [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject/) est, en fait, un objet de la classe [**ListObjectCollection**](https://reference.aspose.com/cells/nodejs-cpp/listobjectcollection/), qui fournit la méthode [**add(number, number, number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/listobjectcollection/#add-number-number-number-number-boolean-) pour ajouter un objet Liste et spécifier la plage de cellules qu'il doit englober. Selon la plage de cellules spécifiée, un [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject/) est créé dans la feuille par Aspose.Cells. Utilisez des attributs (par exemple, [**TableStyleType**](https://reference.aspose.com/cells/nodejs-cpp/tablestyletype/)) de la classe [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject/) pour formater la table selon vos besoins.

L'exemple ci-dessous ajoute des données d'exemple à une feuille, ajoute un [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject/) et lui applique des styles par défaut. Les styles [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject/) sont supportés par Microsoft Excel 2007/2010.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a workbook.
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the default(first) worksheet
const sheet = workbook.getWorksheets().get(0);

// Obtaining Worksheet's cells collection
const cells = sheet.getCells();

// Setting the value to the cells
cells.get(1, 1).putValue("Employee");
cells.get(1, 2).putValue("Quarter");
cells.get(1, 3).putValue("Product");
cells.get(1, 4).putValue("Continent");
cells.get(1, 5).putValue("Country");
cells.get(1, 6).putValue("Sale");

cells.get(2, 1).putValue("David");
cells.get(3, 1).putValue("David");
cells.get(4, 1).putValue("David");
cells.get(5, 1).putValue("David");
cells.get(6, 1).putValue("James");
cells.get(7, 1).putValue("James");
cells.get(8, 1).putValue("James");
cells.get(9, 1).putValue("James");
cells.get(10, 1).putValue("James");
cells.get(11, 1).putValue("Miya");
cells.get(12, 1).putValue("Miya");
cells.get(13, 1).putValue("Miya");
cells.get(14, 1).putValue("Miya");
cells.get(15, 1).putValue("Miya");
cells.get(2, 2).putValue(1);
cells.get(3, 2).putValue(2);
cells.get(4, 2).putValue(3);
cells.get(5, 2).putValue(4);
cells.get(6, 2).putValue(1);
cells.get(7, 2).putValue(2);
cells.get(8, 2).putValue(3);
cells.get(9, 2).putValue(4);
cells.get(10, 2).putValue(4);
cells.get(11, 2).putValue(1);
cells.get(12, 2).putValue(1);
cells.get(13, 2).putValue(2);
cells.get(14, 2).putValue(2);
cells.get(15, 2).putValue(2);

cells.get(2, 3).putValue("Maxilaku");
cells.get(3, 3).putValue("Maxilaku");
cells.get(4, 3).putValue("Chai");
cells.get(5, 3).putValue("Maxilaku");
cells.get(6, 3).putValue("Chang");
cells.get(7, 3).putValue("Chang");
cells.get(8, 3).putValue("Chang");
cells.get(9, 3).putValue("Chang");
cells.get(10, 3).putValue("Chang");
cells.get(11, 3).putValue("Geitost");
cells.get(12, 3).putValue("Chai");
cells.get(13, 3).putValue("Geitost");
cells.get(14, 3).putValue("Geitost");
cells.get(15, 3).putValue("Geitost");

cells.get(2, 4).putValue("Asia");
cells.get(3, 4).putValue("Asia");
cells.get(4, 4).putValue("Asia");
cells.get(5, 4).putValue("Asia");
cells.get(6, 4).putValue("Europe");
cells.get(7, 4).putValue("Europe");
cells.get(8, 4).putValue("Europe");
cells.get(9, 4).putValue("Europe");
cells.get(10, 4).putValue("Europe");
cells.get(11, 4).putValue("America");
cells.get(12, 4).putValue("America");
cells.get(13, 4).putValue("America");
cells.get(14, 4).putValue("America");
cells.get(15, 4).putValue("America");

cells.get(2, 5).putValue("China");
cells.get(3, 5).putValue("India");
cells.get(4, 5).putValue("Korea");
cells.get(5, 5).putValue("India");
cells.get(6, 5).putValue("France");
cells.get(7, 5).putValue("France");
cells.get(8, 5).putValue("Germany");
cells.get(9, 5).putValue("Italy");
cells.get(10, 5).putValue("France");
cells.get(11, 5).putValue("U.S.");
cells.get(12, 5).putValue("U.S.");
cells.get(13, 5).putValue("Brazil");
cells.get(14, 5).putValue("U.S.");
cells.get(15, 5).putValue("U.S.");

cells.get(2, 6).putValue(2000);
cells.get(3, 6).putValue(500);
cells.get(4, 6).putValue(1200);
cells.get(5, 6).putValue(1500);
cells.get(6, 6).putValue(500);
cells.get(7, 6).putValue(1500);
cells.get(8, 6).putValue(800);
cells.get(9, 6).putValue(900);
cells.get(10, 6).putValue(500);
cells.get(11, 6).putValue(1600);
cells.get(12, 6).putValue(600);
cells.get(13, 6).putValue(2000);
cells.get(14, 6).putValue(500);
cells.get(15, 6).putValue(900);

// Adding a new List Object to the worksheet
const index = sheet.getListObjects().add("A1", "F15", true);

const listObject = sheet.getListObjects().get(index);

// Adding Default Style to the table
listObject.setTableStyleType(AsposeCells.TableStyleType.TableStyleMedium10);

// Show Total
listObject.setShowTotals(true);

// Set the Quarter field's calculation type
listObject.getListColumns().get(1).setTotalsCalculation(AsposeCells.TotalsCalculation.Count);

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xlsx"));
```

## **Sujets avancés**
- [Convertir un Tableau en ODS](/cells/fr/nodejs-cpp/convert-table-to-ods/)
- [Trouver des Tables de Requête et des Objets Liste liés aux Connexions de Données Externes](/cells/fr/nodejs-cpp/find-query-tables-and-list-objects-related-to-external-data-connections/)
- [Lire et Écrire un Tableau avec une Source de Données de Table de Requête](/cells/fr/nodejs-cpp/read-and-write-table-with-query-table-data-source/)
- [Définir le Commentaire d'un Tableau ou Objet Liste à l'intérieur de la Feuille de Calcul](/cells/fr/nodejs-cpp/set-the-comment-of-table-or-list-object-inside-the-worksheet/)
- [Tables et Plages](/cells/fr/nodejs-cpp/tables-and-ranges/)

{{< app/cells/assistant language="nodejs-cpp" >}}
