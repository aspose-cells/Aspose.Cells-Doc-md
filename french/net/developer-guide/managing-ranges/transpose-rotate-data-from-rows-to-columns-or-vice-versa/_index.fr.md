---
title: Transposer une plage
description: Cet article explique comment transposer ou faire pivoter les données de lignes vers des colonnes, ou inversement, dans des fichiers Excel à l'aide de Aspose.Cells for .NET selon trois approches différentes.
linktitle: Transposer une plage
url: /fr/net/transpose-rotate-data-from-rows-to-columns-or-vice-versa/
keywords: Aspose.Cells, .NET library, spreadsheet, transpose range, rotate data, transpose function, dynamic array formula, array formula, Excel TRANSPOSE, Rows to Columns
type: docs
weight: 80
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells for .NET prend en charge la transposition (rotation) des données afin que les lignes deviennent des colonnes et les colonnes deviennent des lignes selon trois méthodes différentes. La première approche utilise la méthode en place `Range.Transpose()` et fonctionne sur toutes les versions d'Excel, tandis que la seconde utilise `Cell.SetDynamicArrayFormula()` pour écrire une formule moderne de tableau dynamique `=TRANSPOSE(...)` qui se propage automatiquement sur Excel 365 ou Excel 2021. La troisième approche utilise `Cell.SetArrayFormula()` pour écrire une formule matricielle classique de type Ctrl+Shift+Entrée (CSE) compatible avec les versions antérieures d'Excel. Cet article détaille chaque approche à l'aide d'instructions pas à pas et d'exemples de code complets.
{{% /alert %}}

## **Introduction**
Transposer une plage signifie la faire pivoter de sorte que ce qui était une ligne devienne une colonne et ce qui était une colonne devienne une ligne, reflétant ainsi les données à travers sa diagonale principale. Dans Microsoft Excel, la fonction de feuille de calcul `TRANSPOSE` effectue cette opération, et la référence conceptuelle est documentée à l'adresse [https://support.microsoft.com/en-us/excel/functions/transpose-function](https://support.microsoft.com/en-us/excel/functions/transpose-function). Ce concept peut être appliqué par programmation à une plage de cellules, ce qui est utile dans de nombreux scénarios métier et de reporting.
- Réorienter les rapports de ventes trimestriels ou annuels où les trimestres s'étendent normalement horizontalement et les régions verticalement, ou inversement.
- Inverser l'orientation des axes dans des tableaux de bord ou des graphiques afin qu'une série temporelle s'affiche verticalement plutôt qu'horizontalement.
- Remodeler les données importées à partir de systèmes externes afin qu'elles correspondent à la disposition attendue par les modèles d'analyse ou de reporting en aval.
Pour rendre concret le reste de cet article, chaque exemple utilise le petit tableau suivant des ventes par région et par trimestre. Dans le classeur d'exemple, ce tableau occupe la plage **A1:D5**, où **A1** est laissée vide en tant que coin supérieur gauche, **B1:D1** contient les en-têtes de région et **A2:A5** contient les en-têtes de trimestre.
| Région            | Europe    | Asie      | Amérique du Nord |
|-------------------|-----------|-----------|------------------|
| Qtr 1             | 21704714  | 8774099   | 12094215         |
| Qtr 2             | 17987034  | 12214447  | 10873099         |
| Qtr 3             | 19485029  | 14356879  | 15689543         |
| Qtr 4             | 22567894  | 15763492  | 17456723         |
L'article présente ensuite trois méthodes différentes pour transposer ces données à l'aide de Aspose.Cells for .NET, chacune adaptée à une version et un cas d'usage d'Excel différents.

## **Approche 1 — Transposer une plage en place (Range.Transpose)**
Utilisez cette approche lorsque vous souhaitez transposer des données sans faire intervenir la fonction de feuille de calcul `TRANSPOSE`. Elle fonctionne sur **toutes les versions d'Excel** et ne dépend pas des tableaux dynamiques, ce qui en fait l'option compatible inter-versions la plus sûre. Elle est idéale lorsque vous avez uniquement besoin du résultat transposé final et que vous n'avez pas besoin de conserver la formule `TRANSPOSE` d'origine dans le classeur.

### **API utilisée**
`Range.Transpose()` est une méthode d'instance de la classe `Aspose.Cells.Range`. L'appeler retourne la plage en place en échangeant ses lignes et ses colonnes, de sorte que ce qui était une ligne devient une colonne et ce qui était une colonne devient une ligne. La méthode modifie directement les cellules sous-jacentes sans écrire de formule.

### **Étapes**
1. Ouvrez le classeur source avec `LoadOptions` paramétré sur le format `.xlsx` en appelant `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))`.
2. Récupérez la première feuille de calcul du classeur à l'aide de `workbook.Worksheets[0]`.
3. Accédez à la collection de cellules de la feuille de calcul via `worksheet.Cells`.
4. Créez la plage source couvrant **A1:D5** en appelant `cells.CreateRange("A1:D5")`.
5. Appelez `source.Transpose()` pour faire pivoter la plage en place, en échangeant les lignes et les colonnes.
6. Enregistrez le classeur avec `workbook.Save(outputFile)`.
Après la transposition, cette plage d'ancrage contient les données pivotées. La première ligne se lit (vide, **Europe**, **Asie**, **Amérique du Nord**) et la première colonne se lit (vide, **Qtr 1**, **Qtr 2**, **Qtr 3**, **Qtr 4**). Chaque colonne de ventes d'origine devient une ligne dans la plage transposée.

```csharp
using System;
using System.IO;
using Aspose.Cells;
string srcFile = "source.xlsx";
string outputFile = "transposed.xlsx";
Workbook workbook = new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx));
Worksheet worksheet = workbook.Worksheets[0];
Cells cells = worksheet.Cells;
var source = cells.CreateRange("A1:D5");
source.Transpose();
workbook.Save(outputFile);
```

## **Approche 2 — Transposer avec une formule de tableau dynamique (Excel 365 / 2021)**
Utilisez cette approche lorsque vous souhaitez conserver la formule `=TRANSPOSE(A1:D5)` sous forme de formule active dans le classeur de sortie afin que le résultat se mette à jour automatiquement si les données sources changent, et que le fichier Excel cible sera ouvert dans **Excel 365 / Excel 2021 ou version ultérieure**, où les tableaux dynamiques et l'opérateur de propagation sont pris en charge.

### **API utilisée**
`Cell.SetDynamicArrayFormula(string formula, FormulaParseOptions options, bool calculateValue)` est une méthode de `Aspose.Cells.Cell` qui définit la formule de la cellule en tant que **formule de tableau dynamique**. Excel évalue la formule une seule fois et propage automatiquement le résultat dans les cellules environnantes. Le troisième paramètre, lorsqu'il est défini sur `true`, indique à Aspose.Cells de calculer également les valeurs résultantes au moment de l'écriture.

### **Étapes**
1. Chargez le classeur source à l'aide de `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))`.
2. Récupérez la première feuille de calcul et accédez à sa collection `Cells`.
3. Placez la formule de tableau dynamique dans la cellule **A6**, juste en dessous de la plage source, en appelant `cells["A6"].SetDynamicArrayFormula("=TRANSPOSE(A1:D5)", new FormulaParseOptions(), true)`.
4. L'argument `new FormulaParseOptions()` utilise les paramètres `FormulaParseOptions` par défaut, et le troisième argument `true` indique à Aspose.Cells de traiter la formule comme un tableau dynamique et de l'évaluer afin que les valeurs propagées soient écrites dans le classeur.
5. Enregistrez le classeur avec `workbook.Save(outputFile)`.
La cellule **A6** contient la formule `=TRANSPOSE(A1:D5)` et Excel propage automatiquement le résultat dans la région **A6:E9**, un bloc de 4 lignes sur 5 colonnes correspondant aux données transposées.

{{% alert color="primary" %}}
Cette approche fonctionne **uniquement sur Excel 365 / 2021 ou version ultérieure**. Les versions antérieures d'Excel ne propagent pas correctement les formules de tableau dynamique.
{{% /alert %}}

```csharp
using System;
using System.IO;
using Aspose.Cells;
string srcFile = "source.xlsx";
string outFile = "output_transpose_dynamic.xlsx";
Workbook workbook = new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx));
Worksheet worksheet = workbook.Worksheets[0];
Cells cells = worksheet.Cells;
cells["A6"].SetDynamicArrayFormula("=TRANSPOSE(A1:D5)", new FormulaParseOptions(), true);
workbook.Save(outFile, SaveFormat.Xlsx);
```

## **Approche 3 — Transposer avec une formule matricielle classique (CSE)**
Utilisez cette approche lorsque vous souhaitez qu'une formule `TRANSPOSE` soit conservée dans le classeur, mais que le fichier Excel cible puisse être ouvert dans **des versions antérieures d'Excel (antérieures à 2021, y compris 2019, 2016, 2013, etc.)** où la propagation des tableaux dynamiques n'est pas prise en charge. La formule matricielle classique de type CSE (Ctrl+Shift+Entrée) est l'alternative rétrocompatible que toutes les versions d'Excel peuvent évaluer.

### **API utilisée**
`Cell.SetArrayFormula(string arrayFormula, int nRows, int nColumns)` est une méthode de `Aspose.Cells.Cell` qui attribue une **formule matricielle classique (CSE)** à la cellule d'ancrage et déclare les dimensions du tableau résultant. Aspose.Cells écrit le marqueur de formule matricielle multi-cellules afin qu'Excel évalue la formule comme une expression de tableau unique qui remplit la plage déclarée.

### **Étapes**
1. Chargez le classeur source comme décrit dans les approches précédentes.
2. Récupérez la première feuille de calcul et accédez à sa collection `Cells`.
3. Appelez `cells["A6"].SetArrayFormula("=TRANSPOSE(A1:D5)", 4, 5)`. Le deuxième argument `4` correspond au nombre de lignes du tableau de destination et le troisième argument `5` correspond au nombre de colonnes.
4. Enregistrez le classeur avec `workbook.Save(outputFile)`.
La cellule **A6** est l'ancrage de la formule matricielle et le tableau évalué s'étend sur 4 lignes et 5 colonnes en partant de A6, correspondant aux dimensions transposées de la source A1:D5. Excel écrit un marqueur de formule matricielle unique sur la plage résultante afin que les versions antérieures d'Excel l'évaluent correctement.

{{% alert color="primary" %}}
Les formules matricielles CSE constituent la manière classique, dans Excel, d'évaluer une expression `TRANSPOSE` et cette approche est universellement compatible avec toutes les versions d'Excel.
{{% /alert %}}

```csharp
using System;
using System.IO;
using Aspose.Cells;
// Charger le classeur source avec LoadOptions xlsx
string srcFile = "source.xlsx";
Workbook workbook = new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx));
// Accéder à la première feuille de calcul et à sa collection Cells
Worksheet worksheet = workbook.Worksheets[0];
Cells cells = worksheet.Cells;
// Définir la formule matricielle CSE classique sur la cellule A6.
// La formule =TRANSPOSE(A1:D5) transpose la plage source de 5 lignes x 4 colonnes
// en un tableau de 4 lignes x 5 colonnes. Le deuxième argument (4) est le nombre de lignes
// et le troisième argument (5) est le nombre de colonnes du tableau résultant.
// Aspose.Cells écrit le marqueur de formule matricielle CSE pour qu'Excel l'évalue comme
// une formule matricielle multi-cellules unique, compatible avec les anciennes versions d'Excel
// (2019, 2016, 2013, etc.) qui ne prennent pas en charge le déversement dynamique des tableaux.
cells["A6"].SetArrayFormula("=TRANSPOSE(A1:D5)", 4, 5);
// Enregistrer le classeur pour que le marqueur de formule matricielle soit persisté
workbook.Save("output.xlsx");
```

## **Comparaison — Quand utiliser chaque approche**
| Approche | API / Méthode | Version d'Excel | Formule source conservée ? | Plage de sortie |
|----------|--------------|-----------------|---------------------------|-----------------|
| Approche 1 — Transposition en place | `Range.Transpose()` | Toutes les versions d'Excel | Non (valeurs uniquement) | Plage d'ancrage initiale, 5×4 |
| Approche 2 — Formule de tableau dynamique | `Cell.SetDynamicArrayFormula` | Excel 365 / 2021+ | Oui (propagation dynamique) | Propagée à partir de l'ancrage |
| Approche 3 — Formule matricielle classique (CSE) | `Cell.SetArrayFormula` | Toutes les versions d'Excel | Oui (formule matricielle multi-cellules) | Taille explicite, 4×5 |
Utilisez l'**Approche 1** lorsque vous avez besoin d'une transformation rapide, inter-versions, et que seules les valeurs transposées doivent être écrites dans le fichier. Utilisez l'**Approche 2** lorsqu'Excel moderne est garanti et que vous souhaitez que la formule reste active et se mette à jour si la source change. Utilisez l'**Approche 3** lorsque vous avez besoin de la compatibilité la plus large, avec une formule conservée, sur toutes les versions d'Excel, y compris les versions antérieures qui ne prennent pas en charge les tableaux dynamiques.

{{< app/cells/assistant language="csharp" >}}