---
title: Transposer une plage
linktitle: Transposer une plage
description: Cet article explique comment transposer ou faire pivoter des données de lignes vers des colonnes et inversement dans des fichiers Excel à l'aide de Aspose.Cells for .NET, selon trois approches différentes.
keywords: Aspose.Cells, bibliothèque .NET, tableur, transposition de plage, rotation des données, fonction TRANSPOSE, formule de tableau dynamique, formule matricielle, TRANSPOSE Excel, lignes vers colonnes
type: docs
weight: 80
url: /fr/net/transpose-rotate-data-from-rows-to-columns-or-vice-versa/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells for .NET permet de transposer (faire pivoter) des données afin que les lignes deviennent des colonnes et les colonnes deviennent des lignes, selon trois approches différentes. La première approche utilise la méthode sur place `Range.Transpose()` et fonctionne avec toutes les versions d'Excel, tandis que la deuxième utilise `Cell.SetDynamicArrayFormula()` pour écrire une formule moderne de tableau dynamique `=TRANSPOSE(...)` qui se déverse automatiquement sous Excel 365 ou Excel 2021. La troisième approche utilise `Cell.SetArrayFormula()` pour écrire une formule matricielle classique Ctrl+Shift+Enter (CSE) compatible avec les anciennes versions d'Excel. Cet article présente chaque approche au moyen d'instructions détaillées et d'exemples de code complets.
{{% /alert %}}

## **Introduction**
Transposer une plage consiste à la faire pivoter de sorte que ce qui était une ligne devienne une colonne et ce qui était une colonne devienne une ligne, en effectuant ainsi une symétrie par rapport à sa diagonale principale. Dans Microsoft Excel, la fonction de feuille de calcul `TRANSPOSE` effectue cette opération. La documentation de référence associée est disponible à l'adresse [https://support.microsoft.com/en-us/excel/functions/transpose-function](https://support.microsoft.com/en-us/excel/functions/transpose-function). Ce principe peut être appliqué par programme à une plage de cellules, ce qui est utile dans de nombreux scénarios métier et de production de rapports.
- Réorienter des rapports de ventes trimestriels ou annuels dans lesquels les trimestres s'étendent en largeur sur la page et les régions en hauteur, ou inversement.
- Inverser l'orientation des axes dans des tableaux de bord ou des graphiques afin qu'une série chronologique s'étende en hauteur plutôt qu'en largeur.
- Restructurer des données importées de systèmes externes afin de les adapter à la disposition attendue par les modèles d'analyse ou de génération de rapports en aval.
Pour illustrer concrètement l'article, chaque exemple utilise le petit tableau suivant des ventes par région et par trimestre. Dans le classeur d'exemple, ce tableau occupe la plage **A1:D5** : la cellule **A1** est laissée vide et correspond au coin supérieur gauche, **B1:D1** contient les en-têtes de région et **A2:A5** contient les en-têtes de trimestre.
| Region            | Europe    | Asia      | North America |
|-------------------|-----------|-----------|---------------|
| Qtr 1             | 21704714  | 8774099   | 12094215      |
| Qtr 2             | 17987034  | 12214447  | 10873099      |
| Qtr 3             | 19485029  | 14356879  | 15689543      |
| Qtr 4             | 22567894  | 15763492  | 17456723      |
L'article présente ensuite trois approches différentes pour transposer ces données avec Aspose.Cells for .NET, chacune adaptée à une version différente d'Excel et à un cas d'usage distinct.

## **Approche 1 — Transposer une plage sur place (Range.Transpose)**
Utilisez cette approche lorsque vous souhaitez transposer des données sans recourir à la fonction de feuille de calcul `TRANSPOSE`. Elle fonctionne avec **toutes les versions d'Excel** et est indépendante des tableaux dynamiques, ce qui en fait l'option la plus sûre en termes de compatibilité entre les versions. Elle convient lorsque vous n'avez besoin que du résultat final transposé et que vous ne souhaitez pas conserver la formule `TRANSPOSE` d'origine dans le classeur.

### **API utilisée**
`Range.Transpose()` est une méthode d'instance de la classe `Aspose.Cells.Range`. L'appel à cette méthode inverse la plage sur place en échangeant ses lignes et ses colonnes, de sorte que ce qui était une ligne devient une colonne et ce qui était une colonne devient une ligne. La méthode modifie directement les cellules sous-jacentes sans écrire de formule.

### **Étapes**
1. Ouvrez le classeur source avec l'objet `LoadOptions` configuré pour le format `.xlsx`, en appelant `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))`.
2. Récupérez la première feuille de calcul du classeur à l'aide de `workbook.Worksheets[0]`.
3. Accédez à la collection de cellules de la feuille de calcul à l'aide de `worksheet.Cells`.
4. Créez la plage source qui couvre **A1:D5** en appelant `cells.CreateRange("A1:D5")`.
5. Appelez `source.Transpose()` pour transposer la plage sur place en échangeant les lignes et les colonnes.
6. Enregistrez le classeur à l'aide de `workbook.Save(outputFile)`.
Après la transposition, cette plage d'ancrage contient les données transposées. La première ligne présente les valeurs (vide, **Europe**, **Asia**, **North America**) et la première colonne présente les valeurs (vide, **Qtr 1**, **Qtr 2**, **Qtr 3**, **Qtr 4**). Chaque colonne de ventes d'origine devient une ligne dans la plage transposée.

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
Utilisez cette approche lorsque vous souhaitez conserver la formule `=TRANSPOSE(A1:D5)` dans le classeur de sortie afin que le résultat se mette à jour automatiquement lorsque les données source changent, à condition que le fichier Excel cible soit ouvert dans **Excel 365 / Excel 2021 ou version ultérieure**, où les tableaux dynamiques et l'opérateur de débordement sont pris en charge.

### **API utilisée**
`Cell.SetDynamicArrayFormula(string formula, FormulaParseOptions options, bool calculateValue)` est une méthode de la classe `Aspose.Cells.Cell` qui définit la formule de la cellule comme une **formule de tableau dynamique**. Excel évalue la formule une seule fois et déverse automatiquement le résultat dans les cellules environnantes. Le troisième paramètre, lorsqu'il est défini sur `true`, indique à Aspose.Cells de calculer également les valeurs qui en résultent au moment de l'écriture.

### **Étapes**
1. Chargez le classeur source à l'aide de `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))`.
2. Récupérez la première feuille de calcul, puis accédez à sa collection `Cells`.
3. Placez la formule de tableau dynamique dans la cellule **A6**, juste sous la plage source, en appelant `cells["A6"].SetDynamicArrayFormula("=TRANSPOSE(A1:D5)", new FormulaParseOptions(), true)`.
4. L'argument `new FormulaParseOptions()` utilise les paramètres par défaut de `FormulaParseOptions`, tandis que le troisième argument, `true`, indique à Aspose.Cells de traiter la formule comme un tableau dynamique et de l'évaluer afin que les valeurs déversées soient écrites dans le classeur.
5. Enregistrez le classeur à l'aide de `workbook.Save(outputFile)`.
La cellule **A6** contient la formule `=TRANSPOSE(A1:D5)` et Excel déverse automatiquement le résultat dans la plage **A6:E9**, qui forme un bloc de 4 lignes sur 5 colonnes correspondant aux données transposées.

{{% alert color="primary" %}}
Cette approche fonctionne **uniquement sur Excel 365 / 2021 ou version ultérieure**. Les versions d'Excel antérieures ne déversent pas correctement les formules de tableau dynamique.
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
Utilisez cette approche lorsque vous souhaitez conserver une formule `TRANSPOSE` dans le classeur et que le fichier Excel cible doit pouvoir être ouvert dans **des versions d'Excel plus anciennes (antérieures à 2021, notamment 2019, 2016, 2013, etc.)**, qui ne prennent pas en charge le débordement de tableau dynamique. La formule matricielle classique CSE (Ctrl+Shift+Enter) constitue l'alternative rétrocompatible que toutes les versions d'Excel peuvent évaluer.

### **API utilisée**
`Cell.SetArrayFormula(string arrayFormula, int nRows, int nColumns)` est une méthode de la classe `Aspose.Cells.Cell` qui affecte une **formule matricielle (CSE) classique** à la cellule d'ancrage et déclare les dimensions du tableau qui en résulte. Aspose.Cells écrit le marqueur de formule matricielle couvrant plusieurs cellules afin qu'Excel évalue la formule comme une expression matricielle unique qui remplit la plage déclarée.

### **Étapes**
1. Chargez le classeur source comme décrit dans les approches précédentes.
2. Récupérez la première feuille de calcul, puis accédez à sa collection `Cells`.
3. Appelez `cells["A6"].SetArrayFormula("=TRANSPOSE(A1:D5)", 4, 5)`. Le deuxième argument, `4`, correspond au nombre de lignes du tableau de destination et le troisième, `5`, au nombre de colonnes.
4. Enregistrez le classeur à l'aide de `workbook.Save(outputFile)`.
La cellule **A6** est la cellule d'ancrage de la formule matricielle et le tableau calculé s'étend sur 4 lignes sur 5 colonnes à partir de A6, ce qui correspond aux dimensions obtenues par transposition de la plage source A1:D5. Excel écrit un seul marqueur de formule matricielle sur toute la plage résultante afin que les versions d'Excel les plus anciennes l'évaluent correctement.

{{% alert color="primary" %}}
Les formules matricielles CSE sont la manière classique d'évaluer une expression `TRANSPOSE` dans Excel. Cette approche est compatible avec toutes les versions d'Excel.
{{% /alert %}}

```csharp
using System;
using System.IO;
using Aspose.Cells;
// Charger le classeur source avec les LoadOptions xlsx
string srcFile = "source.xlsx";
Workbook workbook = new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx));
// Accéder à la première feuille de calcul et à sa collection Cells
Worksheet worksheet = workbook.Worksheets[0];
Cells cells = worksheet.Cells;
// Définir la formule de tableau CSE classique sur la cellule A6.
// La formule =TRANSPOSE(A1:D5) fait pivoter la plage source de 5 lignes et 4 colonnes
// en un tableau de 4 lignes et 5 colonnes. Le deuxième argument (4) correspond au nombre de lignes
// et le troisième argument (5) au nombre de colonnes du tableau résultant.
// Aspose.Cells écrit le marqueur de formule de tableau CSE afin qu'Excel l'évalue comme
// une seule formule de tableau sur plusieurs cellules, compatible avec les anciennes versions d'Excel
// (2019, 2016, 2013, etc.) qui ne prennent pas en charge le débordement de tableaux dynamiques.
cells["A6"].SetArrayFormula("=TRANSPOSE(A1:D5)", 4, 5);
// Enregistrer le classeur afin que le marqueur de formule de tableau soit conservé
workbook.Save("output.xlsx");
```

## **Comparaison — Quand utiliser chaque approche**
| Approche | API / méthode | Version d'Excel | Formule source conservée ? | Plage de sortie |
|----------|--------------|---------------|--------------------------|--------------|
| Approche 1 — Transposition sur place | `Range.Transpose()` | Toutes les versions d'Excel | Non (valeurs uniquement) | Plage d'ancrage initiale, 5×4 |
| Approche 2 — Formule de tableau dynamique | `Cell.SetDynamicArrayFormula` | Excel 365 / 2021+ | Oui (déversement dynamique) | Plage déversée depuis la cellule d'ancrage |
| Approche 3 — Formule matricielle classique (CSE) | `Cell.SetArrayFormula` | Toutes les versions d'Excel | Oui (formule matricielle sur plusieurs cellules) | Taille explicite, 4×5 |
Utilisez l'**Approche 1** lorsque vous avez besoin d'une transformation rapide compatible entre les versions et que vous ne souhaitez écrire que les valeurs transposées dans le fichier. Utilisez l'**Approche 2** lorsque l'utilisation d'une version moderne d'Excel est garantie et que vous souhaitez conserver la formule dans le classeur, avec une mise à jour automatique lorsque les données source changent. Utilisez l'**Approche 3** lorsque vous avez besoin de la plus large compatibilité et souhaitez conserver une formule dans toutes les versions d'Excel, y compris les versions plus anciennes qui ne prennent pas en charge les tableaux dynamiques.

{{< app/cells/assistant language="csharp" >}}