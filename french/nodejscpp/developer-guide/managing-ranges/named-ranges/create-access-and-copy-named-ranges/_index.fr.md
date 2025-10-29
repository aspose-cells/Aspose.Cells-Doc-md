---  
title: Créer et copier des plages nommées avec Node.js via C++  
linktitle: Créer un accès et copier les plages nommées  
type: docs  
weight: 200  
url: /fr/nodejs-cpp/create-access-and-copy-named-ranges/  
description: Apprenez comment créer, accéder et copier des plages nommées dans Excel en utilisant Aspose.Cells for Node.js via C++.  
---  

## **Introduction**  

Normalement, les étiquettes de colonne et de ligne sont utilisées pour faire référence à des cellules individuelles. Il est possible de créer des noms descriptifs pour représenter des cellules, plages de cellules, formules ou valeurs constantes. Le mot **nom** peut se référer à une chaîne de caractères représentant une cellule, une plage de cellules, une formule ou une valeur constante. Assigner un nom à une plage signifie que cette plage de cellules peut être référencée par son nom. Utilisez des noms faciles à comprendre, comme Produits, pour faire référence à des plages difficiles à comprendre, comme Ventes!C20:C30. Les étiquettes peuvent être utilisées dans des formules qui font référence à des données sur la même feuille; si vous souhaitez représenter une plage sur une autre feuille, vous pouvez utiliser un nom. *Les plages nommées sont parmi les fonctionnalités les plus puissantes de Microsoft Excel, en particulier lorsqu'elles sont utilisées comme plage source pour des contrôles de liste, des tableaux croisés dynamiques, des graphiques, etc.*  

## **Travailler avec les plages nommées en utilisant Microsoft Excel**  

### **Créer des plages nommées**  

 Les étapes suivantes décrivent comment nommer une cellule ou une plage de cellules en utilisant **MS Excel**. Cette méthode s'applique à **Microsoft Office Excel 2003**, **Microsoft Excel 97**, **2000**, et **2002**.  

1. Sélectionnez la cellule ou la plage de cellules que vous souhaitez nommer.  
2. Cliquez sur la **zone de nom** à l'extrémité gauche de la barre de formule.  
3. Tapez le nom pour les cellules.  
4. Appuyez sur ENTER.  

{{% alert color="primary" %}}  
Vous ne pouvez pas nommer une cellule pendant que vous modifiez le contenu de la cellule.  
{{% /alert %}}  

## **Travailler avec la plage nommée en utilisant Aspose.Cells**  

Ici, nous utilisons l'API Aspose.Cells pour effectuer la tâche.  
Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contient une collection [**getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) qui permet d'accéder à chaque feuille de calcul dans un fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) fournit une collection [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells).  

### **Créer une plage nommée**  

Il est possible de créer une plage nommée en appelant la méthode surchargée [**createRange(string, string)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#createRange-string-string-) de la collection [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells). Une version typique de la méthode [**createRange(string)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#createRange-string-) prend les paramètres suivants :  

- Nom de la cellule en haut à gauche, nom de la cellule en haut à gauche dans la plage.  
- Nom de la cellule inférieure droite, le nom de la cellule inférieure droite de la plage.  

Lorsque la méthode [**createRange(string)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#createRange-string-) est appelée, elle renvoie la plage nouvellement créée en tant qu'instance de la classe [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range). Utilisez cet objet [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range) pour configurer la plage nommée. Par exemple, définissez le nom de la plage en utilisant la propriété [**getName()**](https://reference.aspose.com/cells/nodejs-cpp/range/#getName--). L'exemple suivant montre comment créer une plage nommée de cellules qui s'étend de B4 à G14.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1.xls"));

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Creating a named range
const range = worksheet.getCells().createRange("B4", "G14");

// Setting the name of the named range
range.setName("TestRange");

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.out.xls"));
```  

### **Saisir des données dans les cellules de la plage nommée**  

Vous pouvez insérer des données dans les cellules individuelles d'une plage en suivant le modèle  

- **JavaScript**: Plage[ligne,colonne]  

Disons que vous avez une plage nommée de cellules qui s'étend de A1 à C4. La matrice comprend 4 * 3 = 12 cellules. Les cellules individuelles de la plage sont disposées séquentiellement : Plage[0,0], Plage[0,1], Plage[0,2], Plage[1,0], Plage[1,1], Plage[1,2], Plage[2,0], Plage[2,1], Plage[2,2], Plage[3,0], Plage[3,1], Plage[3,2].  

Utilisez les propriétés suivantes pour identifier les cellules dans la plage :  

- firstRow renvoie l'indice de la première ligne dans la plage nommée.  
- firstColumn renvoie l'indice de la première colonne dans la plage nommée.  
- rowCount renvoie le nombre total de lignes dans la plage nommée.  
- columnCount renvoie le nombre total de colonnes dans la plage nommée.  

L'exemple suivant montre comment saisir certaines valeurs dans les cellules d'une plage spécifiée.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook();

// Get the first worksheet in the workbook.
const worksheet1 = workbook.getWorksheets().get(0);

// Create a range of cells based on H1:J4.
const range = worksheet1.getCells().createRange("H1", "J4");

// Name the range.
range.setName("MyRange");

// Input some data into cells in the range.
range.get(0, 0).setValue("USA");
range.get(0, 1).setValue("SA");
range.get(0, 2).setValue("Israel");
range.get(1, 0).setValue("UK");
range.get(1, 1).setValue("AUS");
range.get(1, 2).setValue("Canada");
range.get(2, 0).setValue("France");
range.get(2, 1).setValue("India");
range.get(2, 2).setValue("Egypt");
range.get(3, 0).setValue("China");
range.get(3, 1).setValue("Philipine");
range.get(3, 2).setValue("Brazil");

// Save the excel file.
workbook.save(path.join(dataDir, "rangecells.out.xls"));
```  

### **Identifier les cellules dans la plage nommée**  

Vous pouvez insérer des données dans les cellules individuelles d'une plage en suivant le schéma :  

- **JavaScript**: Plage[ligne,colonne]  

Si vous avez une plage nommée qui s'étend de A1 à C4, la matrice contient 4 * 3 = 12 cellules. Les cellules individuelles de la plage sont disposées séquentiellement : Plage[0,0], Plage[0,1], Plage[0,2], Plage[1,0] ,Plage[1,1], Plage[1,2], Plage[2,0], Plage[2,1], Plage[2,2], Plage[3,0], Plage[3,1], Plage[3,2].  

Utilisez les propriétés suivantes pour identifier les cellules dans la plage :  

- firstRow renvoie l'indice de la première ligne dans la plage nommée.  
- firstColumn renvoie l'indice de la première colonne dans la plage nommée.  
- rowCount renvoie le nombre total de lignes dans la plage nommée.  
- columnCount renvoie le nombre total de colonnes dans la plage nommée.  

L'exemple suivant montre comment saisir certaines valeurs dans les cellules d'une plage spécifiée.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1_testrange.xls"));

// Getting the specified named range
const range = workbook.getWorksheets().getRangeByName("TestRange");

// Identify range cells.
console.log("First Row : " + range.getFirstRow());
console.log("First Column : " + range.getFirstColumn());
console.log("Row Count : " + range.getRowCount());
console.log("Column Count : " + range.getColumnCount());
```  

### **Accéder aux plages nommées**  

#### **Accéder à une plage nommée spécifique**  

Appelez la méthode [**getRangeByName(string)**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#getRangeByName-string-) de la collection [**worksheets**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection) pour obtenir une plage par le nom spécifié. Une méthode [**getRangeByName(string)**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#getRangeByName-string-) typique prend le nom de la plage nommée et renvoie la plage nommée spécifiée en tant qu'instance de la classe [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range). L'exemple suivant montre comment accéder à une plage spécifiée par son nom.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1_testrange.xls"));

// Getting the specified named range
const range = workbook.getWorksheets().getRangeByName("TestRange");

if (range !== null) 
{
console.log("Named Range : " + range.getRefersTo());
}
```  

#### **Accéder à toutes les plages nommées dans une feuille de calcul**  

Appelez la méthode [**getNamedRanges()**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#getNamedRanges--) de la collection [**worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection) pour obtenir toutes les plages nommées dans une feuille de calcul. La méthode [**getNamedRanges()**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#getNamedRanges--) retourne un tableau de toutes les plages nommées dans la collection [**worksheets**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection).  

L'exemple suivant montre comment accéder à toutes les plages nommées dans un classeur.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1.xls"));

// Getting all named ranges
const ranges = workbook.getWorksheets().getNamedRanges();

if (ranges != null) {
console.log("Total Number of Named Ranges: " + ranges.length);
}
```  

### **Copier les plages nommées**  

Aspose.Cells fournit la méthode [**range.copy(Range, PasteOptions)**](https://reference.aspose.com/cells/nodejs-cpp/range/#copy-range-pasteoptions-) pour copier une plage de cellules avec mise en forme dans une autre plage.  

L'exemple suivant montre comment copier une plage source de cellules dans une autre plage nommée.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook();

// Get all the worksheets in the book.
const worksheets = workbook.getWorksheets();

// Get the first worksheet in the worksheets collection.
const worksheet = workbook.getWorksheets().get(0);

// Create a range of cells.
const range1 = worksheet.getCells().createRange("E12", "I12");

// Name the range.
range1.setName("MyRange");

// Set the outline border to the range.
range1.setOutlineBorder(AsposeCells.BorderType.TopBorder, AsposeCells.CellBorderType.Medium, new AsposeCells.Color(0, 0, 128));
range1.setOutlineBorder(AsposeCells.BorderType.BottomBorder, AsposeCells.CellBorderType.Medium, new AsposeCells.Color(0, 0, 128));
range1.setOutlineBorder(AsposeCells.BorderType.LeftBorder, AsposeCells.CellBorderType.Medium, new AsposeCells.Color(0, 0, 128));
range1.setOutlineBorder(AsposeCells.BorderType.RightBorder, AsposeCells.CellBorderType.Medium, new AsposeCells.Color(0, 0, 128));

// Input some data with some formattings into
// A few cells in the range.
range1.get(0, 0).putValue("Test");
range1.get(0, 4).putValue("123");

// Create another range of cells.
const range2 = worksheet.getCells().createRange("B3", "F3");

// Name the range.
range2.setName("testrange");

// Copy the first range into second range.
range2.copy(range1);

// Save the excel file.
workbook.save(path.join(dataDir, "copyranges.out.xls"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
