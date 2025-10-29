---
title: Prédécesseurs et Dépendants avec Node.js via C++
linktitle: Prédécesseurs et dépendants
type: docs
weight: 230
url: /fr/nodejs-cpp/precedents-and-dependents/
description: Apprenez à tracer les cellules prédécesseurs et dépendantes dans les feuilles de calcul en utilisant Aspose.Cells for Node.js via C++. Comprenez comment identifier les cellules liées dans des feuilles financières complexes.
---

{{% alert color="primary" %}} 

Les feuilles de calcul financières complexes, en particulier celles développées en collaboration, peuvent cacher les erreurs les plus gênantes. Vérifier la précision des formules et trouver la source d'une erreur peut être difficile lorsque la formule utilise des cellules précédentes et des cellules dépendantes.

{{% /alert %}} 
## **Introduction**
- **Cellules précédentes** sont des cellules auxquelles une formule d'une autre cellule fait référence. Par exemple, si la cellule D10 contient la formule =B5, la cellule B5 est une cellule précédente de la cellule D10.
- **Cellules dépendantes** contiennent des formules qui référencent d'autres cellules. Par exemple, si la cellule D10 contient la formule =B5, la cellule D10 dépend de la cellule B5.

Pour rendre la feuille de calcul facile à lire, vous voudrez peut-être clairement indiquer quelles cellules d'une feuille de calcul sont utilisées dans une formule. De même, vous voudrez peut-être extraire les cellules dépendantes d'autres cellules.

Aspose.Cells vous permet de tracer les cellules et de savoir lesquelles sont liées.
## **Tracer les cellules précédentes et dépendantes : Microsoft Excel**
Les formules peuvent changer en fonction des modifications apportées par un client. Par exemple, si la cellule C1 dépend de C3 et C4 contenant une formule, et que C1 est modifiée (la formule étant remplacée), C3 et C4, ou d'autres cellules, doivent changer pour équilibrer la feuille de calcul en fonction des règles métier.

De même, supposons que C1 contient la formule "=(B1*22)/(M2*N32)". Je veux trouver les cellules dont C1 dépend, c'est-à-dire les cellules précédentes B1, M2 et N32.

Il se peut que vous deviez retracer la dépendance d'une cellule particulière à d'autres cellules. Si des règles métier sont intégrées dans des formules, nous aimerions connaître la dépendance et exécuter certaines règles en fonction de celle-ci. De même, si la valeur d'une cellule particulière est modifiée, quelles cellules dans la feuille de calcul sont impactées par ce changement ?

Microsoft Excel permet aux utilisateurs de tracer les cellules précédentes et dépendantes.

1. Sur la **Barre d'outils Affichage**, sélectionnez **Audit des formules**. La boîte de dialogue Audit des formules s'affichera.
1. Tracer les cellules précédentes :
   1. Sélectionnez la cellule contenant la formule pour laquelle vous souhaitez trouver les cellules précédentes.
   1. Pour afficher une flèche de traçage vers chaque cellule qui fournit directement des données à la cellule active, cliquez sur **Tracer les cellules précédentes** sur la **Barre d'outils Audit de formules**.
1. Tracer les formules qui référencent une cellule particulière (dépendantes)
   1. Sélectionnez la cellule pour laquelle vous souhaitez identifier les cellules dépendantes.
   1. Pour afficher une flèche de traçage vers chaque cellule dépendante de la cellule active, cliquez sur **Tracer les dépendants** dans la barre d'outils d'audit de formule.
## **Tracer les cellules précédentes et dépendantes : Aspose.Cells**
### **Tracer les cellules précédentes**
Aspose.Cells facilite l'obtention de cellules précédentes. Il peut non seulement récupérer les cellules fournissant des données aux précédents de formule simples, mais aussi trouver les cellules fournissant des données aux précédents de formule complexes avec des plages nommées.

Dans l'exemple ci-dessous, un fichier excel modèle, Book1.xls, est utilisé. La feuille de calcul contient des données et des formules sur la première feuille de calcul.

Aspose.Cells fournit la méthode [Cell.getPrecedents()](https://reference.aspose.com/cells/nodejs-cpp/cell/#getPrecedents--) de la classe [Cell](https://reference.aspose.com/cells/nodejs-cpp/cell) utilisée pour tracer les antécédents d'une cellule. Elle retourne une collection de zones référencées. Comme vous pouvez le voir ci-dessus, dans Book1.xls, la cellule B7 contient la formule "=SUM(A1:A3)". Ainsi, les cellules A1:A3 sont les antécédents de la cellule B7. L'exemple suivant démontre la fonction de traçage des antécédents en utilisant le fichier modèle Book1.xls.


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
const cells = workbook.getWorksheets().get(0).getCells();
const cell = cells.get("B4");
// Check if the cell object is not null before proceeding
if (cell) 
{
const ret = cell.getPrecedents();
if (!ret.isNull() && ret.getCount() > 0)
{
const area = ret.get(0);
console.log(area.getSheetName());
console.log(AsposeCells.CellsHelper.cellIndexToName(area.getStartRow(), area.getStartColumn()));
console.log(AsposeCells.CellsHelper.cellIndexToName(area.getEndRow(), area.getEndColumn()));
}
else
{
console.error("No precedents found for the cell.");
}
} 
else 
{
console.error("Cell B4 is null.");
}
```
### **Tracé des dépendances**
Aspose.Cells vous permet d'obtenir les cellules dépendantes dans les feuilles de calcul. Aspose.Cells peut non seulement récupérer les cellules qui fournissent des données concernant une formule simple mais aussi trouver celles qui fournissent des données aux dépendants de formules complexes avec des plages nommées.

Aspose.Cells offre la méthode [Cell.getDependents(boolean)](https://reference.aspose.com/cells/nodejs-cpp/cell/#getDependents-boolean-) de la classe [Cell](https://reference.aspose.com/cells/nodejs-cpp/cell) utilisée pour tracer les dependants d'une cellule. Par exemple, dans Book1.xlsx, il y a des formules : "=A1+20" et "=A1+30" dans les cellules B2 et C2 respectivement. L'exemple suivant montre comment tracer les dependants pour la cellule A1 en utilisant le fichier modèle Book1.xlsx.


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
const cells = workbook.getWorksheets().get(0).getCells();
const cell = cells.get("B2");
// Ensure dependents is an array
const dependents = cell.getDependents(true);

if (Array.isArray(dependents)) 
{
for (const c of dependents) 
{
console.log(c.getName());
}
} 
else 
{
console.error("Dependents is not an array");
}
```
### **Tracer les cellules précédentes et dépendantes selon la chaîne de calcul**
Les API ci-dessus de traçage des antécédents et des dépendants sont basées sur l'expression de formule elle-même. Elles offrent simplement une manière pratique pour les utilisateurs de suivre les interdépendances pour quelques formules. Si le classeur contient un grand nombre de formules et que l'utilisateur doit suivre les antécédents et dépendants pour chaque cellule, cela entraînera de mauvaises performances. Pour une telle situation, l'utilisateur devrait envisager d'utiliser [Cell.getPrecedentsInCalculation()](https://reference.aspose.com/cells/nodejs-cpp/cell/#getPrecedentsInCalculation--) et [Cell.getDependentsInCalculation(boolean)](https://reference.aspose.com/cells/nodejs-cpp/cell/#getDependentsInCalculation-boolean-) qui suivent les dépendances selon la chaîne de calcul. Il faut d'abord activer cette chaîne de calcul via [FormulaSettings.getEnableCalculationChain()](https://reference.aspose.com/cells/nodejs-cpp/formulasettings/#getEnableCalculationChain--). Ensuite, effectuer un calcul complet du classeur avec [Workbook.calculateFormula()](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--). Après cela, il est possible de suivre les antécédents ou dépendants de toutes les cellules nécessaires.

Pour certains formules, les précédents résultats peuvent différer entre getPrecedents et getPrecedentsInCalculation, et les dépendants peuvent différer entre getDependents et getDependentsInCalculation. Par exemple, si la formule de la cellule A1 est "=IF(TRUE,B2,C3)", getPrecedents donnera B2 et C3 comme antécédents de A1. En conséquence, B2 et C3 ont tous deux A1 comme dépendant selon getDependents. Cependant, pour le calcul de cette formule, il est évident que seule B2 peut affecter le résultat calculé. Donc, getPrecedentsInCalculation ne fournira pas C3 pour A1, et getDependentsInCalculation ne fournira pas A1 pour C3. Parfois, l'utilisateur ne veut tracer que les interdépendances qui affectent réellement le résultat calculé des formules en fonction des données actuelles du classeur, et doit utiliser getDependentsInCalculation/getPrecedentsInCalculation plutôt que getDependents/getPrecedents.

L'exemple suivant montre comment suivre les antécédents et dépendants selon la chaîne de calcul pour les cellules :


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
const cells = workbook.getWorksheets().get(0).getCells();
cells.get("A1").setFormula("=B1+SUM(B1:B10)+[Book1.xls]Sheet1!B2");
cells.get("A2").setFormula("=IF(TRUE,B2,B1)");
workbook.getSettings().getFormulaSettings().setEnableCalculationChain(true);
workbook.calculateFormula();

let en = cells.get("B1").getDependentsInCalculation(false);
console.log("B1's calculation dependents:");
for (var cell of en) {
console.log(cell.getName());
}


en = cells.get("B2").getDependentsInCalculation(false);
console.log("B2's calculation dependents:");
for (var cell of en) {
console.log(cell.getName());
}

en = cells.get("A1").getPrecedentsInCalculation();
console.log("A1's calculation precedents:");
for (var area of en) {
console.log(area.toString());
}


en = cells.get("A2").getPrecedentsInCalculation();
console.log("A2's calculation precedents:");
for (var area of en) {
console.log(area.toString());
}
```
{{< app/cells/assistant language="nodejs-cpp" >}}
