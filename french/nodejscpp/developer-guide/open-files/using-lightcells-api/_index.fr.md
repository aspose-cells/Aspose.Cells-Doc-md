---  
title: Utiliser l API LightCells avec Node.js via C++  
linktitle: Utilisation de l API LightCells  
type: docs  
weight: 160  
url: /fr/nodejs-cpp/using-lightcells-api/  
description: Apprenez à lire et écrire de grands fichiers Excel en utilisant l API LightCells dans Node.js via C++. Améliorez les performances et l efficacité avec une consommation moindre de mémoire.  
---  

{{% alert color="primary" %}}  

Parfois, vous devez lire et écrire de gros fichiers Microsoft Excel avec une énorme liste de données ou de contenu dans la feuille de calcul. L'API LightCells est utile pour créer d'énormes feuilles de calcul Excel : avec celle-ci, vous avez besoin de moins de mémoire et obtenez de meilleures performances et une meilleure efficacité.  

{{% /alert %}}  
# Architecture orientée événements  
Aspose.Cells fournit l'API LightCells, principalement conçue pour manipuler les données de cellules une par une sans construire un bloc de modèle de données complet (en utilisant la collection Cell, etc.) en mémoire. Il fonctionne en mode orienté événements.  

Pour enregistrer des classeurs, fournissez le contenu des cellules une par une lors de l'enregistrement, et le composant l'enregistre directement dans le fichier de sortie.  

Lors de la lecture de fichiers de modèle, le composant analyse chaque cellule et fournit leur valeur une par une.  

Dans les deux procédures, un objet Cell est traité puis abandonné ; l'objet Workbook ne détient pas la collection. Dans ce mode, la mémoire est donc économisée lors de l'importation et de l'exportation de fichiers Microsoft Excel ayant un grand ensemble de données qui sinon utiliserait beaucoup de mémoire.  

Bien que l'API LightCells traite les cellules de la même manière pour les fichiers XLSX et XLS (elle ne charge pas réellement toutes les cellules en mémoire mais traite une cellule puis la rejette), elle économise plus efficacement la mémoire pour les fichiers XLSX que pour les fichiers XLS en raison des différents modèles de données et structures des deux formats.  

Cependant, **pour les fichiers XLS**, pour économiser plus de mémoire, les développeurs peuvent spécifier un emplacement temporaire pour sauvegarder les données temporaires générées lors du processus d'enregistrement. Généralement, **l'utilisation de l'API LightCells pour sauvegarder les fichiers XLSX peut économiser 50% ou plus de mémoire** par rapport à la méthode classique ; **l'enregistrement des XLS peut économiser environ 20-40% de mémoire**.  

## Écriture d'un grand fichier Excel  
Aspose.Cells fournit une interface, `LightCellsDataProvider`, qui doit être implémentée dans votre programme. L'interface représente le fournisseur de données pour la sauvegarde de grands fichiers de tableur en mode léger.  

Lors de l'enregistrement d'un classeur avec ce mode, `StartSheet(int)` est vérifié lors de l'enregistrement de chaque feuille de calcul. Pour une feuille, si `StartSheet(int)` est vrai, alors toutes les données et propriétés des lignes et cellules de cette feuille à enregistrer sont fournies par cette implémentation. En premier lieu, `NextRow()` est appelé pour obtenir l'index de la ligne suivante à enregistrer. Si un index de ligne valide est retourné (l'index doit être en ordre croissant pour les lignes à sauvegarder), alors un objet Row représentant cette ligne est fourni pour que l'implémentation puisse définir ses propriétés avec `StartRow(Row)`.  

Pour une ligne, `NextCell()` est vérifié en premier. Si un index de colonne valide est retourné (l'index de colonne doit être en ordre croissant pour toutes les cellules d'une ligne à sauvegarder), alors un objet Cell représentant cette cellule est fourni pour que l'implémentation définisse ses données et propriétés avec `StartCell(Cell)`. Après avoir défini les données de la cellule, celle-ci est enregistrée directement dans le fichier de feuille de calcul généré, et la cellule suivante est vérifiée et traitée.  
### Écriture d'un grand fichier Excel : Exemple  
Veuillez consulter le code d'exemple suivant pour voir le fonctionnement de l'API LightCells. Ajoutez et supprimez, ou mettez à jour les segments de code selon vos besoins.  

Le programme crée un fichier énorme avec **10 000 (matrice 10000x30) enregistrements** dans une feuille de calcul et la remplit avec des données fictives. Vous pouvez spécifier votre propre matrice en modifiant les variables `rowsCount` et `colsCount` dans la méthode `Main()`.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

class TestDataProvider {
constructor(workbook, maxRows, maxColumns) {
this._workbook = workbook;
this.maxRows = maxRows;
this.maxColumns = maxColumns;
this._row = -1;
this._column = -1;
}

isGatherString() {
return false;
}

nextCell() {
this._column++;
if (this._column < this.maxColumns) {
return this._column;
} else {
this._column = -1;
return -1;
}
}

nextRow() {
this._row++;
if (this._row < this.maxRows) {
this._column = -1;
return this._row;
} else {
return -1;
}
}

startCell(cell) {
cell.putValue(this._row + this._column);
if (this._row !== 1) {
cell.setFormula("=Rand() + A2");
}
}

startRow(row) {
}

startSheet(sheetIndex) {
return sheetIndex === 0;
}
}

const run = async () => {
const dataDir = path.join(__dirname, "data");

const rowsCount = 10000;
const colsCount = 30;

const workbook = new AsposeCells.Workbook();
const ooxmlSaveOptions = new AsposeCells.OoxmlSaveOptions();

ooxmlSaveOptions.setLightCellsDataProvider(new TestDataProvider(workbook, rowsCount, colsCount));

await workbook.saveAsync(path.join(dataDir, "output.out.xlsx"), ooxmlSaveOptions);
};

run();
```  

## Lecture de grands fichiers Excel  
Aspose.Cells fournit une interface, `LightCellsDataHandler`, qui doit être implémentée dans votre programme. L'interface représente le fournisseur de données pour la lecture de grands fichiers Excel en mode léger.  

Lors de la lecture d'un classeur en mode léger, `StartSheet` est vérifié lors de la lecture de chaque feuille de calcul. Pour une feuille, si `StartSheet` retourne vrai, alors toutes les données et propriétés des cellules dans les lignes et colonnes de la feuille sont vérifiées et traitées par l'implémentation de cette interface. Pour chaque ligne, `StartRow` est appelée pour vérifier si elle doit être traitée. Si une ligne doit être traitée, ses propriétés sont lues en premier, et le développeur peut accéder à ses propriétés avec `ProcessRow`. Si les cellules de la ligne doivent également être traitées, alors `ProcessRow` doit retourner vrai, puis `StartCell` est appelé pour chaque cellule existante dans la ligne pour vérifier si une cellule doit être traitée. Si une cellule doit être traitée, alors `ProcessCell` est appelée pour traiter la cellule par l'implémentation de cette interface.  
### Lecture de grands fichiers Excel : Exemple  
Veuillez consulter le code d'exemple suivant pour voir le fonctionnement de l'API LightCells. Ajoutez et supprimez, ou mettez à jour les segments de code selon vos besoins.  

Le programme lit un immense fichier avec des millions d'enregistrements dans une feuille. La lecture de chaque feuille du classeur prend peu de temps. Le code d'exemple lit le fichier et récupère le nombre total de cellules, le nombre de chaînes, et le nombre de formules dans chaque feuille.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

class LightCellsDataHandlerVisitCells {
constructor() {
this.cellCount = 0;
this.formulaCount = 0;
this.stringCount = 0;
}

get CellCount() {
return this.cellCount;
}

get FormulaCount() {
return this.formulaCount;
}

get StringCount() {
return this.stringCount;
}

StartSheet(sheet) {
console.log("Processing sheet[" + sheet.getName() + "]");
return true;
}

StartRow(rowIndex) {
return true;
}

ProcessRow(row) {
return true;
}

StartCell(column) {
return true;
}

ProcessCell(cell) {
this.cellCount++;
if (cell.isFormula()) {
this.formulaCount++;
} else if (cell.getType() === AsposeCells.CellValueType.IsString) {
this.stringCount++;
}
return false;
}
}

async function run() {
const dataDir = path.join(__dirname, "data");
const opts = new AsposeCells.LoadOptions();
const v = new LightCellsDataHandlerVisitCells();
opts.setLightCellsDataHandler(v);
const wb = new AsposeCells.Workbook(path.join(dataDir, "LargeBook1.xlsx"), opts);
const sheetCount = wb.getWorksheets().getCount();
console.log("Total sheets: " + sheetCount + ", cells: " + v.CellCount
+ ", strings: " + v.StringCount + ", formulas: " + v.FormulaCount);
}

run();
```  

