---  
title: Comment et où utiliser les énumérateurs avec Node.js via C++  
linktitle: Itérer les données  
type: docs  
weight: 55  
url: /fr/nodejs-cpp/how-and-where-to-use-enumerators/  
description: Découvrez comment utiliser les énumérateurs via l API Aspose.Cells for Node.js via C++.  
keywords: Comment utiliser les énumérateurs en Node.js via C++, l Énumérateur de cellules en Node.js via C++, l Énumérateur de lignes en Node.js via C++, l Énumérateur de colonnes en Node.js via C++  
---  

{{% alert color="primary" %}}  

Un énumérateur est un objet qui offre la possibilité de parcourir un conteneur ou une collection. Les énumérateurs peuvent être utilisés pour lire les données de la collection, mais ils ne peuvent pas être utilisés pour modifier la collection sous-jacente, tandis qu'Array est une interface qui définit une méthode `getEnumerator` qui retourne une interface `IEnumerator`, ce qui permet un accès en lecture seule à une collection.  

Les API Aspose.Cells fournissent une multitude d'énumérateurs, cependant, cet article traite principalement des trois types énumérés ci-dessous.  

1. Énumérateur de cellules  
1. Énumérateur de lignes  
1. Énumérateur de colonnes  

{{% /alert %}}  

## **Comment utiliser des énumérateurs**  

### **Énumérateur de cellules**  

Il existe diverses façons d'accéder à l'énumérateur de cellules, et l'on peut utiliser l'une de ces méthodes en fonction des besoins de l'application. Voici les méthodes qui renvoient l'énumérateur de cellules.  

1. [**Cells.getEnumerator()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getEnumerator--)  
1. [**Row.getEnumerator()**](https://reference.aspose.com/cells/nodejs-cpp/row/#getEnumerator--)  
1. [**Range.getEnumerator()**](https://reference.aspose.com/cells/nodejs-cpp/range/#getEnumerator--)  

Toutes les méthodes mentionnées ci-dessus renvoient l'énumérateur qui permet de parcourir la collection de cellules qui ont été initialisées.  

{{% alert color="primary" %}}  

En parcourant les cellules, la collection ne doit pas être modifiée (des opérations qui entraîneront l'instanciation d'une nouvelle cellule ou la suppression d'une cellule existante). Sinon, l'énumérateur risque de ne pas pouvoir parcourir toutes les cellules correctement (certains éléments peuvent être parcourus de manière répétitive ou sautés).  

{{% /alert %}}  

L'exemple de code suivant démontre la mise en œuvre de l'interface `IEnumerator` pour une collection de cellules.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

const cells = workbook.getWorksheets().get(0).getCells().getEnumerator();
for (const cell of cells) {
console.log(`${cell.getName()} ${cell.getValue()}`);
}

const rowCells = workbook.getWorksheets().get(0).getCells().getRows().get(0).getEnumerator();
for (const cell of rowCells) {
console.log(`${cell.getName()} ${cell.getValue()}`);
}

const rangeCells = workbook.getWorksheets().get(0).getCells().createRange("A1:B10").getEnumerator();
for (const cell of rangeCells) {
console.log(`${cell.getName()} ${cell.getValue()}`);
}
```  

### **Itérateur de lignes**  

L'Énumérateur de lignes peut être accédé lors de l'utilisation de la méthode [**RowCollection.getEnumerator()**](https://reference.aspose.com/cells/nodejs-cpp/rowcollection/#getEnumerator--). L'exemple ci-dessous montre la mise en œuvre de l'interface `IEnumerator` pour [**RowCollection**](https://reference.aspose.com/cells/nodejs-cpp/rowcollection).  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Get RowCollection and iterate using index
const rows = workbook.getWorksheets().get(0).getCells().getRows();
const rowCount = rows.getCount();

// Traverse rows in the collection
for (let i = 0; i < rowCount; i++) {
const row = rows.get(i);
console.log(row.getIndex());
}
```  

### **Itérateur de colonnes**  

L'Énumérateur de colonnes peut être accédé lors de l'utilisation de la méthode [**ColumnCollection.getEnumerator**](https://reference.aspose.com/cells/nodejs-cpp/columncollection). L'exemple ci-dessous montre la mise en œuvre de l'interface `IEnumerator` pour [**ColumnCollection**](https://reference.aspose.com/cells/nodejs-cpp/columncollection).  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Get columns collection
const columns = workbook.getWorksheets().get(0).getCells().getColumns();
// Traverse columns using index
const count = columns.getCount();
for (let i = 0; i < count; i++) {
const col = columns.get(i);
console.log(col.getIndex());
}
```  

## **Où utiliser les énumérateurs**  

Pour discuter des avantages de l'utilisation des énumérateurs, prenons un exemple en temps réel.  

**Scénario**  

Une exigence de l'application est de parcourir toutes les cellules dans un [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) donné pour lire leurs valeurs. Il pourrait y avoir plusieurs façons de mettre en œuvre cet objectif. Quelques exemples sont indiqués ci-dessous.  

### **Utilisation de la plage d'affichage**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Get Cells collection of first worksheet
const cells = workbook.getWorksheets().get(0).getCells();

// Get the MaxDisplayRange
const displayRange = cells.getMaxDisplayRange();

// Loop over all cells in the MaxDisplayRange
for (let row = displayRange.getFirstRow(); row < displayRange.getRowCount(); row++) {
for (let col = displayRange.getFirstColumn(); col < displayRange.getColumnCount(); col++) {
// Read the Cell value
console.log(displayRange.get(row, col).getStringValue());
}
}
```  

### **Utilisation de MaxDataRow & MaxDataColumn**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Get Cells collection of first worksheet
const cells2 = workbook.getWorksheets().get(0).getCells();
const maxDataRow = cells2.getMaxDataRow();
const maxDataColumn = cells2.getMaxDataColumn();

// Loop over all cells
for (let row = 0; row <= maxDataRow; row++) {
for (let col = 0; col <= maxDataColumn; col++) {
// Read the Cell value
const currentCell = cells2.checkCell(row, col);
if (currentCell) {
console.log(currentCell.getStringValue());
}
}
}
```  

Comme vous pouvez le constater, les deux approches ci-dessus utilisent plus ou moins une logique similaire, c'est-à-dire parcourir toutes les cellules de la collection pour lire les valeurs des cellules. Cela pourrait poser problème pour un certain nombre de raisons, comme discuté ci-dessous.  

1. Les API telles que [**getMaxRow()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxRow--), [**getMaxDataRow()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxDataRow--), [**getMaxColumn()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxColumn--), [**getMaxDataColumn()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxDataColumn--) & [**getMaxDisplayRange()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxDisplayRange--) nécessitent du temps supplémentaire pour rassembler les statistiques correspondantes. Dans le cas où la matrice de données (lignes x colonnes) est grande, l'utilisation de ces API pourrait entraîner une pénalité de performance.  
1. Dans la plupart des cas, toutes les cellules dans une plage donnée ne sont pas instanciées. Dans de telles situations, vérifier chaque cellule dans la matrice n'est pas aussi efficace que de vérifier uniquement les cellules initialisées.  
1. Accéder à une cellule dans une boucle en tant que Cells row, column entraînera l'instanciation de tous les objets de cellules dans une plage, ce qui pourrait finalement entraîner une OutOfMemoryException.  

## **Conclusion**  

Sur la base des faits mentionnés ci-dessus, voici les scénarios possibles où les énumérateurs doivent être utilisés.  

1. Un accès en lecture seule de la collection de cellules est requis, c'est-à-dire; la nécessité est uniquement d'inspecter les cellules.  
1. Un grand nombre de cellules doit être parcouru.  
1. Seules les cellules/rangées/colonnes initialisées doivent être parcourues.  

