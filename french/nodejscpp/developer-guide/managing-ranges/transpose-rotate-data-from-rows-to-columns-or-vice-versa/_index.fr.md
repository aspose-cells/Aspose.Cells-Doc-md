---
title: Transpose Range
linktitle: Transpose Range
description: This article explains how to transpose or rotate data from rows to columns or vice versa in Excel files using Aspose.Cells for Node.js via C++ with three different approaches.
keywords: Aspose.Cells, bibliothèque Node.js via C++, tableur, transposer une plage, faire pivoter les données, fonction TRANSPOSE, formule de tableau dynamique, formule de tableau, Excel TRANSPOSE, lignes vers colonnes
type: docs
weight: 80
url: /fr/nodejs-cpp/transpose-rotate-data-from-rows-to-columns-or-vice-versa/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells for Node.js via C++ permet de transposer (faire pivoter) les données de sorte que les lignes deviennent des colonnes et les colonnes deviennent des lignes, de trois façons différentes. La première approche utilise la méthode `range.transpose()` sur place et fonctionne avec toutes les versions d’Excel, tandis que la deuxième utilise `cell.setDynamicArrayFormula()` pour écrire une formule de tableau dynamique moderne `=TRANSPOSE(...)` qui se déverse automatiquement dans Excel 365 ou Excel 2021. La troisième approche utilise `cell.setArrayFormula()` pour écrire une formule de tableau classique Ctrl+Shift+Enter (CSE) compatible avec les versions antérieures d’Excel. Cet article présente chaque approche avec des instructions pas à pas et des exemples de code complets.
{{% /alert %}}

## **Introduction**
Transposer une plage consiste à la pivoter de telle sorte qu’une ligne devienne une colonne et qu’une colonne devienne une ligne, ce qui revient à refléter les données sur sa diagonale principale. Dans Microsoft Excel, la fonction de feuille de calcul `TRANSPOSE` effectue cette opération, et la référence conceptuelle est documentée à l’adresse [https://support.microsoft.com/en-us/excel/functions/transpose-function](https://support.microsoft.com/en-us/excel/functions/transpose-function). Ce concept peut être appliqué par programme à une plage de cellules, ce qui est utile dans de nombreux scénarios commerciaux et de reporting.
- Réorienter les rapports de ventes trimestriels ou annuels dans lesquels les trimestres s’étendent normalement horizontalement sur la page et les régions verticalement, ou inversement.
- Inverser l’orientation des axes dans les tableaux de bord ou les graphiques afin qu’une série temporelle descende le long de la page au lieu de s’étendre horizontalement.
- Reformater les données importées de systèmes externes afin qu’elles correspondent à la disposition attendue par les analyses en aval ou les modèles de reporting.
Pour rendre le reste de l’article concret, chaque exemple utilise le petit tableau de ventes par région et par trimestre suivant. Dans le classeur d’exemple, ce tableau occupe la plage **A1:D5**, la cellule **A1** étant laissée vide dans le coin supérieur gauche, **B1:D1** contenant les en-têtes de région et **A2:A5** contenant les en-têtes de trimestre.
| Région            | Europe    | Asie      | Amérique du Nord |
|-------------------|-----------|-----------|---------------|
| 1er trimestre     | 21704714  | 8774099   | 12094215      |
| 2e trimestre      | 17987034  | 12214447  | 10873099      |
| 3e trimestre      | 19485029  | 14356879  | 15689543      |
| 4e trimestre      | 22567894  | 15763492  | 17456723      |
L’article présente ensuite trois façons différentes de transposer ces données à l’aide d’Aspose.Cells for Node.js via C++, chacune adaptée à une version différente d’Excel et à un cas d’utilisation particulier.

## **Approach 1 — Transpose Range in Place (range.transpose)**
Utilisez cette approche lorsque vous souhaitez transposer des données sans utiliser la fonction de feuille de calcul `TRANSPOSE`. Elle fonctionne avec **toutes les versions d’Excel** et ne dépend pas des tableaux dynamiques, ce qui en fait l’option la plus sûre en matière de compatibilité entre les versions. Elle est idéale lorsque vous avez uniquement besoin du résultat transposé final et ne souhaitez pas conserver la formule `TRANSPOSE` d’origine dans le classeur.

### **API used**
`range.transpose()` est une méthode d’instance de la classe `Aspose.Cells.Range`. Son appel inverse la plage sur place en échangeant ses lignes et ses colonnes, de sorte qu’une ligne devienne une colonne et qu’une colonne devienne une ligne. La méthode modifie directement les cellules sous-jacentes sans écrire de formule.

### **Steps**
1. Ouvrir le classeur source avec `LoadOptions` configuré pour le format `.xlsx` en appelant `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))`.
2. Récupérer la première feuille de calcul du classeur à l’aide de `workbook.getWorksheets().get(0)`.
3. Accéder à la collection de cellules de la feuille de calcul via `worksheet.getCells()`.
4. Créer la plage source couvrant **A1:D5** en appelant `cells.createRange("A1:D5")`.
5. Appeler `source.transpose()` pour pivoter la plage sur place, en échangeant les lignes et les colonnes.
6. Enregistrer le classeur avec `workbook.save(outputFile)`.
Après la transposition, la plage d’ancrage initiale contient les données pivotées. La première ligne contient (vide, **Europe**, **Asie**, **Amérique du Nord**) et la première colonne contient (vide, **1er trimestre**, **2e trimestre**, **3e trimestre**, **4e trimestre**). Chaque colonne de ventes d’origine devient une ligne dans la plage transposée.

```javascript
const AsposeCells = require("aspose.cells.node");
var srcFile = "source.xlsx";
var outputFile = "transposed.xlsx";
var workbook = new AsposeCells.Workbook(srcFile, new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx));
var worksheet = workbook.getWorksheets().get(0);
var cells = worksheet.getCells();
var source = cells.createRange("A1:D5");
source.transpose();
workbook.save(outputFile);
```

## **Approach 2 — Transpose with a Dynamic Array Formula (Excel 365 / 2021)**
Utilisez cette approche lorsque vous souhaitez conserver la formule `=TRANSPOSE(A1:D5)` comme formule active dans le classeur de sortie, afin que le résultat se mette à jour automatiquement si les données source changent, et que le fichier Excel cible soit ouvert dans **Excel 365 / Excel 2021 ou une version ultérieure**, où les tableaux dynamiques et l’opérateur de déversement sont pris en charge.

### **API used**
`cell.setDynamicArrayFormula(string formula, FormulaParseOptions options, bool calculateValue)` est une méthode de `Aspose.Cells.Cell` qui définit la formule de la cellule sous forme de **formule de tableau dynamique**. Excel évalue la formule une seule fois et déverse automatiquement le résultat dans les cellules environnantes. Le troisième paramètre, lorsqu’il est défini sur `true`, indique à Aspose.Cells de calculer également les valeurs résultantes au moment de l’écriture.

### **Steps**
1. Charger le classeur source à l’aide de `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))`.
2. Récupérer la première feuille de calcul et accéder à sa collection `Cells`.
3. Placer la formule de tableau dynamique dans la cellule **A6**, juste sous la plage source, en appelant `cells.get("A6").setDynamicArrayFormula("=TRANSPOSE(A1:D5)", null, true)`.
4. L’argument `null` transmet l’objet `FormulaParseOptions` par défaut, et le troisième argument `true` indique à Aspose.Cells de traiter la formule comme une formule de tableau dynamique et de l’évaluer afin que les valeurs déversées soient écrites dans le classeur.
5. Enregistrer le classeur avec `workbook.save(outputFile)`.
La cellule **A6** contient la formule `=TRANSPOSE(A1:D5)` et Excel déverse automatiquement le résultat dans la plage **A6:D10**, un bloc de 5 lignes sur 4 colonnes égal aux données transposées.

{{% alert color="primary" %}}
Cette approche fonctionne **uniquement sur Excel 365 / 2021 ou une version ultérieure**. Les versions antérieures d’Excel ne déverseront pas correctement les formules de tableau dynamique.
{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells.node");
const srcFile = "source.xlsx";
const outFile = "output_transpose_dynamic.xlsx";
const opts = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx);
const workbook = new AsposeCells.Workbook(srcFile, opts);
const worksheet = workbook.getWorksheets().get(0);
const cells = worksheet.getCells();
cells.get("A6").setDynamicArrayFormula("=TRANSPOSE(A1:D5)", new AsposeCells.FormulaParseOptions(), true);
workbook.save(outFile, AsposeCells.SaveFormat.Xlsx);
```

## **Approach 3 — Transpose with a Classic Array Formula (CSE)**
Utilisez cette approche lorsque vous souhaitez conserver une formule `TRANSPOSE` dans le classeur, mais que le fichier Excel cible pourrait être ouvert dans **des versions antérieures d’Excel (avant 2021, notamment 2019, 2016, 2013, etc.)**, où le déversement des tableaux dynamiques n’est pas pris en charge. La formule de tableau classique CSE (Ctrl+Shift+Enter) est l’alternative compatible avec les versions historiques que toutes les versions d’Excel peuvent évaluer.

### **API used**
`cell.setArrayFormula(string arrayFormula, int nRows, int nColumns)` est une méthode de `Aspose.Cells.Cell` qui affecte une **formule de tableau classique (CSE)** à la cellule d’ancrage et déclare les dimensions du tableau résultant. Aspose.Cells écrit le marqueur de formule de tableau multicellulaire afin qu’Excel évalue la formule comme une expression de tableau unique qui remplit la plage déclarée.

### **Steps**
1. Charger le classeur source comme décrit dans les approches précédentes.
2. Récupérer la première feuille de calcul et accéder à sa collection `Cells`.
3. Appeler `cells.get("A6").setArrayFormula("=TRANSPOSE(A1:D5)", 4, 5)`. Le deuxième argument `4` correspond au nombre de lignes du tableau de destination et le troisième argument `5` au nombre de colonnes.
4. Enregistrer le classeur avec `workbook.save(outputFile)`.
La cellule **A6** est la cellule d’ancrage de la formule de tableau et le tableau évalué s’étend sur 4 lignes et 5 colonnes à partir de A6, ce qui correspond aux dimensions transposées de la source A1:D5. Excel écrit un seul marqueur de formule de tableau sur toute la plage résultante afin que les versions antérieures d’Excel l’évaluent correctement.

{{% alert color="primary" %}}
Les formules de tableau CSE sont la manière classique dont Excel évalue une expression `TRANSPOSE`, et cette approche est compatible avec toutes les versions d’Excel.
{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells.node");
// Load the source workbook with xlsx LoadOptions
const srcFile = "source.xlsx";
const workbook = new AsposeCells.Workbook(srcFile, new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx));
// Access the first worksheet and its Cells collection
const worksheet = workbook.getWorksheets().get(0);
const cells = worksheet.getCells();
// Set the classic CSE array formula on cell A6.
// The formula =TRANSPOSE(A1:D5) rotates the 5-row x 4-column source range
// into a 4-row x 5-column array. The second argument (4) is the number of rows
// and the third argument (5) is the number of columns of the resulting array.
// Aspose.Cells writes the CSE array-formula marker so Excel evaluates it as
// a single multi-cell array formula, compatible with older Excel versions
// (2019, 2016, 2013, etc.) that do not support dynamic array spilling.
cells.get("A6").setArrayFormula("=TRANSPOSE(A1:D5)", 4, 5);
// Save the workbook so the array-formula marker is persisted
workbook.save("output.xlsx");
```

## **Comparison — When to Use Each Approach**
| Approche | API / Méthode | Version d’Excel | Formule source conservée ? | Plage de sortie |
|----------|---------------|-----------------|---------------------------|-----------------|
| Approche 1 — Transposition sur place | `range.transpose()` | Toutes les versions d’Excel | Non (valeurs uniquement) | Plage d’ancrage initiale, 5×4 |
| Approche 2 — Formule de tableau dynamique | `cell.setDynamicArrayFormula` | Excel 365 / 2021+ | Oui (déversement dynamique) | Déversée depuis la cellule d’ancrage |
| Approche 3 — Formule de tableau classique (CSE) | `cell.setArrayFormula` | Toutes les versions d’Excel | Oui (formule de tableau multicellulaire) | Taille explicite, 4×5 |
Utilisez **Approche 1** lorsque vous avez besoin d’une transformation rapide compatible entre les versions et que vous souhaitez uniquement écrire les valeurs transposées dans le fichier. Utilisez **Approche 2** lorsque vous pouvez garantir l’utilisation d’Excel moderne et souhaitez que la formule reste active et se mette à jour si la source change. Utilisez **Approche 3** lorsque vous avez besoin de la compatibilité la plus large avec une formule conservée sur toutes les versions d’Excel, y compris les anciennes versions qui ne prennent pas en charge les tableaux dynamiques.

## **Related Articles**
- [Rendu de tableau à cellule unique SmartMarker](/cells/fr/nodejs-cpp/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)
- [Insertion d’une image dans une cellule](/cells/fr/nodejs-cpp/inserting-an-image-into-a-cell/)
- [Fractionnement de fichiers Excel en plusieurs fichiers](/cells/fr/nodejs-cpp/splitting-excel-files-into-multiple-files/)

{{< app/cells/assistant language="nodejs-cpp" >}}