---
title: Transposer une plage
description: Cet article explique comment transposer ou faire pivoter des données de lignes vers des colonnes ou inversement dans des fichiers Excel à l'aide d'Aspose.Cells for Node.js via C++ avec trois approches différentes.
linktitle: Transposer une plage
url: /fr/nodejs-cpp/transpose-rotate-data-from-rows-to-columns-or-vice-versa/
keywords: Aspose.Cells, Node.js via C++ library, spreadsheet, transpose range, rotate data, transpose function, dynamic array formula, array formula, Excel TRANSPOSE, Rows to Columns
type: docs
weight: 80
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells for Node.js via C++ prend en charge la transposition (rotation) des données afin que les lignes deviennent des colonnes et les colonnes deviennent des lignes de trois manières différentes. La première approche utilise la méthode en place `range.transpose()` et fonctionne sur toutes les versions d'Excel, tandis que la seconde utilise `cell.setDynamicArrayFormula()` pour écrire une formule de tableau dynamique moderne `=TRANSPOSE(...)` qui se déverse automatiquement sur Excel 365 ou Excel 2021. La troisième approche utilise `cell.setArrayFormula()` pour écrire une formule de tableau classique Ctrl+Shift+Entrée (CSE) compatible avec les anciennes versions d'Excel. Cet article passe en revue chaque approche avec des instructions étape par étape et des exemples de code complets.
{{% /alert %}}

## **Introduction**
Transposer une plage signifie la faire pivoter afin que ce qui était une ligne devienne une colonne et ce qui était une colonne devienne une ligne, reflétant ainsi les données par rapport à sa diagonale principale. Dans Microsoft Excel, la fonction de feuille de calcul `TRANSPOSE` effectue cette opération, et la référence conceptuelle est documentée à [https://support.microsoft.com/en-us/excel/functions/transpose-function](https://support.microsoft.com/en-us/excel/functions/transpose-function). Ce concept peut être appliqué par programmation à une plage de cellules, ce qui est utile dans de nombreux scénarios métier et de reporting.
- Réorienter les rapports de ventes trimestriels ou annuels où les trimestres s'étendent normalement sur la page et les régions descendent sur la page, ou inversement.
- Inverser l'orientation des axes dans les tableaux de bord ou les graphiques afin qu'une série chronologique descende sur la page au lieu de s'étendre horizontalement.
- Restructurer les données importées de systèmes externes afin qu'elles correspondent à la disposition attendue par les modèles d'analyse ou de reporting en aval.
Pour rendre concret le reste de l'article, chaque exemple utilise le petit tableau suivant des ventes par région et par trimestre. Dans le classeur d'exemple, ce tableau occupe la plage **A1:D5**, avec **A1** laissé vide comme coin supérieur gauche, **B1:D1** contenant les en-têtes de région, et **A2:A5** contenant les en-têtes de trimestre.
| Région             | Europe    | Asie      | Amérique du Nord |
|--------------------|-----------|-----------|------------------|
| Trim 1             | 21704714  | 8774099   | 12094215         |
| Trim 2             | 17987034  | 12214447  | 10873099         |
| Trim 3             | 19485029  | 14356879  | 15689543         |
| Trim 4             | 22567894  | 15763492  | 17456723         |
L'article présente ensuite trois façons différentes de transposer ces données à l'aide d'Aspose.Cells for Node.js via C++, chacune adaptée à une version d'Excel et à un cas d'utilisation différents.

## **Approche 1 — Transposer une plage en place (range.transpose)**
Utilisez cette approche chaque fois que vous souhaitez transposer des données sans impliquer la fonction de feuille de calcul `TRANSPOSE`. Elle fonctionne sur **toutes les versions d'Excel** et n'a aucune dépendance vis-à-vis des tableaux dynamiques, ce qui en fait l'option compatible inter-versions la plus sûre. Elle est idéale lorsque vous n'avez besoin que du résultat transposé final et que vous n'avez pas besoin de conserver la formule `TRANSPOSE` d'origine dans le classeur.

### **API utilisée**
`range.transpose()` est une méthode d'instance de la classe `Aspose.Cells.Range`. L'appeler retourne la plage en place en échangeant ses lignes et ses colonnes, de sorte que ce qui était une ligne devient une colonne et ce qui était une colonne devient une ligne. La méthode modifie directement les cellules sous-jacentes sans écrire de formule.

### **Étapes**
1. Ouvrez le classeur source avec `LoadOptions` défini sur le format `.xlsx` en appelant `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))`.
2. Récupérez la première feuille de calcul du classeur à l'aide de `workbook.getWorksheets().get(0)`.
3. Accédez à la collection de cellules de la feuille de calcul via `worksheet.getCells()`.
4. Créez la plage source couvrant **A1:D5** en appelant `cells.createRange("A1:D5")`.
5. Appelez `source.transpose()` pour faire pivoter la plage en place, en échangeant les lignes et les colonnes.
6. Enregistrez le classeur avec `workbook.save(outputFile)`.
Après la transposition, la plage d'ancrage initiale contient les données pivotées. La première ligne lit (vide, **Europe**, **Asie**, **Amérique du Nord**) et la première colonne lit (vide, **Trim 1**, **Trim 2**, **Trim 3**, **Trim 4**). Chaque colonne de ventes d'origine devient une ligne dans la plage transposée.

```javascript
var srcFile = "source.xlsx";
var outputFile = "transposed.xlsx";
var workbook = new AsposeCells.Workbook(srcFile, new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx));
var worksheet = workbook.getWorksheets().get(0);
var cells = worksheet.getCells();
var source = cells.createRange("A1:D5");
source.transpose();
workbook.save(outputFile);
```

## **Approche 2 — Transposer avec une formule de tableau dynamique (Excel 365 / 2021)**
Utilisez cette approche lorsque vous souhaitez conserver la formule `=TRANSPOSE(A1:D5)` comme formule active dans le classeur de sortie afin que le résultat se mette à jour automatiquement si les données source changent, et que le fichier Excel cible sera ouvert dans **Excel 365 / Excel 2021 ou version ultérieure** où les tableaux dynamiques et l'opérateur de débordement sont pris en charge.

### **API utilisée**
`cell.setDynamicArrayFormula(string formula, FormulaParseOptions options, bool calculateValue)` est une méthode de `Aspose.Cells.Cell` qui définit la formule de la cellule comme une **formule de tableau dynamique**. Excel évalue la formule une seule fois et déverse automatiquement le résultat dans les cellules environnantes. Le troisième paramètre, lorsqu'il est défini sur `true`, demande à Aspose.Cells de calculer également les valeurs résultantes au moment de l'écriture.

### **Étapes**
1. Chargez le classeur source à l'aide de `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))`.
2. Récupérez la première feuille de calcul et accédez à sa collection `Cells`.
3. Placez la formule de tableau dynamique sur la cellule **A6**, juste en dessous de la plage source, en appelant `cells.get("A6").setDynamicArrayFormula("=TRANSPOSE(A1:D5)", null, true)`.
4. L'argument `null` passe les `FormulaParseOptions` par défaut, et le troisième argument `true` indique à Aspose.Cells de traiter la formule comme un tableau dynamique et de l'évaluer afin que les valeurs débordées soient écrites dans le classeur.
5. Enregistrez le classeur avec `workbook.save(outputFile)`.
La cellule **A6** contient la formule `=TRANSPOSE(A1:D5)` et Excel déverse automatiquement le résultat dans la région **A6:D10**, un bloc de 5 lignes par 4 colonnes égal aux données transposées.

{{% alert color="primary" %}}
Cette approche fonctionne **uniquement sur Excel 365 / 2021 ou version ultérieure**. Les anciennes versions d'Excel ne déverseront pas correctement les formules de tableau dynamique.
{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells");
const srcFile = "source.xlsx";
const outFile = "output_transpose_dynamic.xlsx";
const opts = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx);
const workbook = new AsposeCells.Workbook(srcFile, opts);
const worksheet = workbook.getWorksheets().get(0);
const cells = worksheet.getCells();
cells.get("A6").setDynamicArrayFormula("=TRANSPOSE(A1:D5)", new AsposeCells.FormulaParseOptions(), true);
workbook.save(outFile, AsposeCells.SaveFormat.Xlsx);
```

## **Approche 3 — Transposer avec une formule de tableau classique (CSE)**
Utilisez cette approche lorsque vous souhaitez qu'une formule `TRANSPOSE` soit conservée dans le classeur mais que le fichier Excel cible puisse être ouvert dans **des versions plus anciennes d'Excel (antérieures à 2021, y compris 2019, 2016, 2013, etc.)** où le débordement de tableau dynamique n'est pas pris en charge. La formule de tableau CSE classique (Ctrl+Shift+Entrée) est l'alternative compatible avec les versions antérieures que toutes les versions d'Excel peuvent évaluer.

### **API utilisée**
`cell.setArrayFormula(string arrayFormula, int nRows, int nColumns)` est une méthode de `Aspose.Cells.Cell` qui attribue une **formule de tableau classique (CSE)** à la cellule d'ancrage et déclare les dimensions du tableau résultant. Aspose.Cells écrit le marqueur de formule de tableau multi-cellules afin qu'Excel évalue la formule comme une expression de tableau unique qui remplit la plage déclarée.

### **Étapes**
1. Chargez le classeur source comme décrit dans les approches précédentes.
2. Récupérez la première feuille de calcul et accédez à sa collection `Cells`.
3. Appelez `cells.get("A6").setArrayFormula("=TRANSPOSE(A1:D5)", 4, 5)`. Le deuxième argument `4` est le nombre de lignes du tableau de destination et le troisième argument `5` est le nombre de colonnes.
4. Enregistrez le classeur avec `workbook.save(outputFile)`.
La cellule **A6** est l'ancre de la formule de tableau et le tableau évalué s'étend sur 4 lignes par 5 colonnes à partir de A6, correspondant aux dimensions transposées de la source A1:D5. Excel écrit un marqueur de formule de tableau unique sur toute la plage résultante afin que les anciennes versions d'Excel l'évaluent correctement.

{{% alert color="primary" %}}
Les formules de tableau CSE sont la méthode Excel classique pour évaluer une expression `TRANSPOSE` et cette approche est universellement compatible avec toutes les versions d'Excel.
{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells");
// Charger le classeur source avec les options de chargement xlsx
const srcFile = "source.xlsx";
const workbook = new AsposeCells.Workbook(srcFile, new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx));
// Accéder à la première feuille de calcul et à sa collection Cells
const worksheet = workbook.getWorksheets().get(0);
const cells = worksheet.getCells();
// Définir la formule matricielle CSE classique sur la cellule A6.
// La formule =TRANSPOSE(A1:D5) fait pivoter la plage source de 5 lignes x 4 colonnes
// en un tableau de 4 lignes x 5 colonnes. Le deuxième argument (4) est le nombre de lignes
// et le troisième argument (5) est le nombre de colonnes du tableau résultant.
// Aspose.Cells écrit le marqueur de formule matricielle CSE afin qu'Excel l'évalue comme
// une seule formule matricielle multi-cellules, compatible avec les anciennes versions d'Excel
// (2019, 2016, 2013, etc.) qui ne prennent pas en charge le déversement dynamique des tableaux.
cells.get("A6").setArrayFormula("=TRANSPOSE(A1:D5)", 4, 5);
// Enregistrer le classeur pour que le marqueur de formule matricielle soit persisté
workbook.save("output.xlsx");
```

## **Comparaison — Quand utiliser chaque approche**
| Approche | API / Méthode | Version Excel | Formule source conservée ? | Plage de sortie |
|----------|---------------|---------------|---------------------------|-----------------|
| Approche 1 — Transposition en place | `range.transpose()` | Toutes les versions Excel | Non (valeurs uniquement) | Plage d'ancrage initiale, 5×4 |
| Approche 2 — Formule de tableau dynamique | `cell.setDynamicArrayFormula` | Excel 365 / 2021+ | Oui (débordement dynamique) | Débordée à partir de l'ancre |
| Approche 3 — Formule de tableau classique (CSE) | `cell.setArrayFormula` | Toutes les versions Excel | Oui (formule de tableau multi-cellules) | Taille explicite, 4×5 |
Utilisez l'**Approche 1** lorsque vous avez besoin d'une transformation rapide, compatible entre versions, et que vous n'avez besoin que des valeurs transposées écrites dans le fichier. Utilisez l'**Approche 2** lorsqu'Excel moderne est garanti et que vous souhaitez que la formule reste active et se mette à jour si la source change. Utilisez l'**Approche 3** lorsque vous avez besoin de la plus large compatibilité avec une formule conservée dans toutes les versions d'Excel, y compris les anciennes versions qui ne prennent pas en charge les tableaux dynamiques.

## **Articles connexes**
- [Rendu de tableau à cellule unique SmartMarker](/cells/fr/nodejs-cpp/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)
- [Insertion d'une image dans une cellule](/cells/fr/nodejs-cpp/inserting-an-image-into-a-cell/)
- [Fractionnement de fichiers Excel en plusieurs fichiers](/cells/fr/nodejs-cpp/splitting-excel-files-into-multiple-files/)

{{< app/cells/assistant language="nodejs-cpp" >}}