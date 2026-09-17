---
title: Transpose Range
description: This article explains how to transpose or rotate data from rows to columns or vice versa in Excel files using Aspose.Cells for Node.js via Java, with three different approaches.
linktitle: Transposition de plage
url: /fr/nodejs-java/transpose-rotate-data-from-rows-to-columns-or-vice-versa/
keywords: Aspose.Cells, Bibliothèque Node.js via Java, feuille de calcul, transposition de plage, faire pivoter des données, fonction TRANSPOSE, formule de tableau dynamique, formule matricielle, TRANSPOSE Excel, Lignes vers Colonnes
type: docs
weight: 80
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells for Node.js via Java prend en charge la transposition (rotation) des données de sorte que les lignes deviennent des colonnes et que les colonnes deviennent des lignes de trois manières différentes. La première approche utilise la méthode in-place `Range.transpose()` et fonctionne sur toutes les versions d'Excel, tandis que la seconde utilise `Cell.setDynamicArrayFormula()` pour écrire une formule moderne de tableau dynamique `=TRANSPOSE(...)` qui se déverse automatiquement sur Excel 365 ou Excel 2021. La troisième approche utilise `Cell.setArrayFormula()` pour écrire une formule matricielle classique de type Ctrl+Shift+Entrée (CSE) compatible avec les anciennes versions d'Excel. Cet article passe en revue chaque approche avec des instructions étape par étape et des exemples de code complets.
{{% /alert %}}

## **Introduction**
Transposer une plage signifie la faire pivoter de sorte que ce qui était une ligne devient une colonne et ce qui était une colonne devient une ligne, ce qui revient à refléter les données le long de sa diagonale principale. Dans Microsoft Excel, la fonction de feuille de calcul `TRANSPOSE` effectue cette opération, et la référence conceptuelle est documentée à l'adresse [https://support.microsoft.com/en-us/excel/functions/transpose-function](https://support.microsoft.com/en-us/excel/functions/transpose-function). La même idée peut être appliquée par programmation à une plage de cellules, ce qui est utile dans de nombreux scénarios métier et de reporting.
Voici les scénarios courants dans lesquels la transposition est utile :
- Réorienter les rapports de ventes trimestriels ou annuels où les trimestres s'exécutent normalement en travers de la page et les régions le long de la page, ou inversement.
- Inverser l'orientation des axes dans des tableaux de bord ou des graphiques afin qu'une série temporelle s'exécute le long de la page au lieu d'en travers.
- Remodeler les données importées depuis des systèmes externes afin qu'elles correspondent à la disposition attendue par les modèles d'analyse ou de reporting en aval.
Pour rendre concret le reste de l'article, chaque exemple utilise le petit tableau de ventes par région et par trimestre suivant. Dans le classeur d'exemple, ce tableau occupe la plage **A1:D5**, avec **A1** laissé vide en tant que coin supérieur gauche, **B1:D1** contenant les en-têtes de région et **A2:A5** contenant les en-têtes de trimestre.
| Region            | Europe    | Asia      | North America |
|-------------------|-----------|-----------|---------------|
| Qtr 1             | 21704714  | 8774099   | 12094215      |
| Qtr 2             | 17987034  | 12214447  | 10873099      |
| Qtr 3             | 19485029  | 14356879  | 15689543      |
| Qtr 4             | 22567894  | 15763492  | 17456723      |
L'article présente ensuite trois façons différentes de transposer ces données à l'aide d'Aspose.Cells for Node.js via Java, chacune adaptée à une version d'Excel et à un cas d'utilisation différents.

## **Approche 1 — Transposer une plage en place (Range.transpose)**
Utilisez cette approche chaque fois que vous souhaitez transposer des données sans faire intervenir la fonction de feuille de calcul `TRANSPOSE`. Elle fonctionne sur **toutes les versions d'Excel** et ne dépend pas des tableaux dynamiques, ce qui en fait l'option la plus sûre en termes de compatibilité entre versions. Elle est idéale lorsque vous n'avez besoin que du résultat final transposé et que vous n'avez pas besoin de conserver la formule `TRANSPOSE` d'origine dans le classeur.

### **API utilisée**
`Range.transpose()` est une méthode d'instance de la classe `com.aspose.cells.Range`. Son appel transpose la plage en place en échangeant ses lignes et ses colonnes, de sorte que ce qui était une ligne devient une colonne et ce qui était une colonne devient une ligne. La méthode modifie directement les cellules sous-jacentes sans écrire de formule.

### **Étapes**
1. Ouvrez le classeur source avec `LoadOptions` défini sur le format `.xlsx` en appelant `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))`.
2. Récupérez la première feuille de calcul du classeur à l'aide de `workbook.getWorksheets().get(0)`.
3. Accédez à la collection de cellules de la feuille de calcul via `worksheet.getCells()`.
4. Créez la plage source couvrant **A1:D5** en appelant `cells.createRange("A1:D5")`.
5. Appelez `source.transpose()` pour faire pivoter la plage en place, en échangeant lignes et colonnes.
6. Enregistrez le classeur avec `workbook.save(outputFile)`.
Après la transposition, la même plage d'ancrage contient les données pivotées. La première ligne se lit (vide, **Europe**, **Asia**, **North America**) et la première colonne se lit (vide, **Qtr 1**, **Qtr 2**, **Qtr 3**, **Qtr 4**). Chaque colonne d'origine des ventes devient une ligne dans la plage transposée.

```javascript
const AsposeCells = require("aspose.cells");
const srcFile = "source.xlsx";
const outputFile = "transposed.xlsx";
const loadOptions = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx);
const workbook = new AsposeCells.Workbook(srcFile, loadOptions);
const worksheet = workbook.getWorksheets().get(0);
const cells = worksheet.getCells();
const source = cells.createRange("A1:D5");
source.transpose();
workbook.save(outputFile);
```

## **Approche 2 — Transposer avec une formule de tableau dynamique (Excel 365 / 2021)**
Utilisez cette approche lorsque vous souhaitez conserver la formule `=TRANSPOSE(A1:D5)` en tant que formule active dans le classeur de sortie afin que le résultat se mette à jour automatiquement si les données source changent, et que le fichier Excel cible sera ouvert dans **Excel 365 / Excel 2021 ou version ultérieure** où les tableaux dynamiques et l'opérateur de déversement sont pris en charge.

### **API utilisée**
`Cell.setDynamicArrayFormula(String formula, FormulaParseOptions options, boolean calculateValue)` est une méthode de `com.aspose.cells.Cell` qui définit la formule de la cellule en tant que **formule de tableau dynamique**. Excel évalue la formule une seule fois et déverse automatiquement le résultat dans les cellules environnantes. Le troisième paramètre, lorsqu'il est défini sur `true`, indique à Aspose.Cells de calculer également les valeurs résultantes au moment de l'écriture.

### **Étapes**
1. Chargez le classeur source à l'aide de `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))`.
2. Récupérez la première feuille de calcul et accédez à sa collection `Cells`.
3. Placez la formule de tableau dynamique dans la cellule **A6**, juste en dessous de la plage source, en appelant `cells.get("A6").setDynamicArrayFormula("=TRANSPOSE(A1:D5)", null, true)`.
4. L'argument `null` passe les `FormulaParseOptions` par défaut, et le troisième argument `true` indique à Aspose.Cells de traiter la formule comme un tableau dynamique et de l'évaluer afin que les valeurs déversées soient écrites dans le classeur.
5. Enregistrez le classeur avec `workbook.save(outputFile)`.
La cellule **A6** contient la formule `=TRANSPOSE(A1:D5)` et Excel déverse automatiquement le résultat dans la région **A6:D10**, un bloc de 5 lignes par 4 colonnes égal aux données transposées.

{{% alert color="primary" %}}
Cette approche fonctionne **uniquement sur Excel 365 / 2021 ou version ultérieure**. Les anciennes versions d'Excel ne déversent pas correctement les formules de tableau dynamique.
{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells");
const srcFile = "source.xlsx";
const outFile = "output_transpose_dynamic.xlsx";
const workbook = new AsposeCells.Workbook(srcFile, new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx));
const worksheet = workbook.getWorksheets().get(0);
const cells = worksheet.getCells();
cells.get("A6").setDynamicArrayFormula("=TRANSPOSE(A1:D5)", new AsposeCells.FormulaParseOptions(), true);
workbook.save(outFile, AsposeCells.SaveFormat.Xlsx);
```

## **Approche 3 — Transposer avec une formule matricielle classique (CSE)**
Utilisez cette approche lorsque vous souhaitez qu'une formule `TRANSPOSE` soit conservée dans le classeur mais que le fichier Excel cible puisse être ouvert dans **d'anciennes versions d'Excel (antérieures à 2021, notamment 2019, 2016, 2013, etc.)** où le déversement de tableau dynamique n'est pas pris en charge. La formule matricielle classique CSE (Ctrl+Shift+Entrée) est l'alternative compatible avec les versions antérieures, que toutes les versions d'Excel peuvent évaluer.

### **API utilisée**
`Cell.setArrayFormula(String arrayFormula, int nRows, int nColumns)` est une méthode de `com.aspose.cells.Cell` qui attribue une **formule matricielle classique (CSE)** à la cellule d'ancrage et déclare les dimensions du tableau résultant. Aspose.Cells écrit le marqueur de formule matricielle multi-cellules afin qu'Excel évalue la formule comme une expression de tableau unique remplissant la plage déclarée.

### **Étapes**
1. Chargez le classeur source de la même manière que dans les approches précédentes.
2. Récupérez la première feuille de calcul et accédez à sa collection `Cells`.
3. Appelez `cells.get("A6").setArrayFormula("=TRANSPOSE(A1:D5)", 4, 5)`. Le deuxième argument `4` correspond au nombre de lignes du tableau de destination et le troisième argument `5` au nombre de colonnes.
4. Enregistrez le classeur avec `workbook.save(outputFile)`.
La cellule **A6** est l'ancrage de la formule matricielle et le tableau évalué s'étend sur 4 lignes par 5 colonnes à partir de A6, ce qui correspond aux dimensions transposées de la source A1:D5. Excel écrit un seul marqueur de formule matricielle sur la plage résultante afin que les anciennes versions d'Excel l'évaluent correctement.

{{% alert color="primary" %}}
Les formules matricielles CSE représentent la méthode classique d'évaluation d'une expression `TRANSPOSE` dans Excel. Cette approche est compatible avec toutes les versions d'Excel.
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
// en un tableau de 4 lignes x 5 colonnes. Le deuxième argument (4) correspond au nombre de lignes
// et le troisième argument (5) au nombre de colonnes du tableau résultant.
// Aspose.Cells écrit le marqueur de formule matricielle CSE afin qu'Excel l'évalue
// comme une formule matricielle unique multi-cellules, compatible avec les anciennes versions d'Excel
// (2019, 2016, 2013, etc.) qui ne prennent pas en charge le déversement dynamique des tableaux.
cells.get("A6").setArrayFormula("=TRANSPOSE(A1:D5)", 4, 5);
// Enregistrer le classeur pour que le marqueur de formule matricielle soit conservé
workbook.save("output.xlsx");
```

## **Comparaison — Quand utiliser chaque approche**
| Approche | API / Méthode | Version d'Excel | Formule source conservée ? | Plage de sortie |
|----------|--------------|---------------|--------------------------|--------------|
| Approche 1 — Transposition en place | `Range.transpose()` | Toutes les versions d'Excel | Non (valeurs uniquement) | Même plage d'ancrage, 5×4 |
| Approche 2 — Formule de tableau dynamique | `Cell.setDynamicArrayFormula` | Excel 365 / 2021+ | Oui (déversement dynamique) | Déversée depuis l'ancrage |
| Approche 3 — Formule matricielle classique (CSE) | `Cell.setArrayFormula` | Toutes les versions d'Excel | Oui (formule matricielle multi-cellules) | Taille explicite, 4×5 |
Utilisez l'**Approche 1** lorsque vous avez besoin d'une transformation rapide et compatible avec toutes les versions d'Excel, et que seules les valeurs transposées doivent être écrites dans le fichier. Utilisez l'**Approche 2** lorsque vous utilisez une version moderne d'Excel et que vous souhaitez que la formule reste active et se mette à jour si la source change. Utilisez l'**Approche 3** lorsque vous avez besoin de la plus large compatibilité avec une formule conservée dans toutes les versions d'Excel, y compris les anciennes versions qui ne prennent pas en charge les tableaux dynamiques.

## **Articles connexes**
- [Rendu matriciel d'une cellule unique SmartMarker | Aspose.Cells for Node.js via Java](/cells/fr/nodejs-java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)
- [Insertion d'une image dans une cellule](/cells/fr/nodejs-java/inserting-an-image-into-a-cell/)
- [Fractionnement de fichiers Excel en plusieurs fichiers](/cells/fr/nodejs-java/splitting-excel-files-into-multiple-files/)

{{< app/cells/assistant language="nodejs-java" >}}