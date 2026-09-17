---
title: Transposer une plage
linktitle: Transposer une plage
description: Cet article explique comment transposer ou faire pivoter des données de lignes vers des colonnes ou inversement dans des fichiers Excel à l'aide d'Aspose.Cells for Java, avec trois approches différentes.
keywords: Aspose.Cells, bibliothèque Java, tableur, transposer une plage, faire pivoter les données, fonction TRANSPOSE, formule de tableau dynamique, formule matricielle, TRANSPOSE Excel, Lignes vers Colonnes
type: docs
weight: 80
url: /fr/java/transpose-rotate-data-from-rows-to-columns-or-vice-versa/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells for Java prend en charge la transposition (rotation) des données afin que les lignes deviennent des colonnes et les colonnes deviennent des lignes de trois manières différentes. La première approche utilise la méthode `Range.transpose()` en place et fonctionne sur toutes les versions d'Excel, tandis que la seconde utilise `Cell.setDynamicArrayFormula()` pour écrire une formule moderne de tableau dynamique `=TRANSPOSE(...)` qui se déverse automatiquement dans Excel 365 ou Excel 2021. La troisième approche utilise `Cell.setArrayFormula()` pour écrire une formule matricielle classique Ctrl+Maj+Entrée (CSE) compatible avec les anciennes versions d'Excel. Cet article présente chaque approche avec des instructions pas à pas et des exemples de code complets.
{{% /alert %}}

## **Introduction**
Transposer une plage signifie la faire pivoter de sorte que ce qui était une ligne devienne une colonne et ce qui était une colonne devienne une ligne, ce qui revient à refléter les données par rapport à sa diagonale principale. Dans Microsoft Excel, la fonction de feuille de calcul `TRANSPOSE` effectue cette opération, et la référence conceptuelle est documentée à l'adresse [https://support.microsoft.com/en-us/excel/functions/transpose-function](https://support.microsoft.com/en-us/excel/functions/transpose-function). Ce concept peut être appliqué programmatiquement à une plage de cellules, ce qui est utile dans de nombreux scénarios métiers et de reporting.
- Réorienter des rapports de ventes trimestriels ou annuels où les trimestres s'étendent normalement sur la page et les régions descendent sur la page, ou inversement.
- Échanger l'orientation des axes dans des tableaux de bord ou des graphiques afin qu'une série temporelle descende sur la page au lieu de s'étendre horizontalement.
- Remodeler les données importées depuis des systèmes externes afin qu'elles correspondent à la disposition attendue par les modèles d'analyse ou de reporting en aval.
Pour rendre concret le reste de l'article, chaque exemple utilise le petit tableau de ventes par région et par trimestre suivant. Dans le classeur d'exemple, ce tableau occupe la plage **A1:D5**, avec **A1** laissé vide comme coin supérieur gauche, **B1:D1** contenant les en-têtes de régions et **A2:A5** contenant les en-têtes de trimestres.
| Region            | Europe    | Asia      | North America |
|-------------------|-----------|-----------|---------------|
| Qtr 1             | 21704714  | 8774099   | 12094215      |
| Qtr 2             | 17987034  | 12214447  | 10873099      |
| Qtr 3             | 19485029  | 14356879  | 15689543      |
| Qtr 4             | 22567894  | 15763492  | 17456723      |
L'article présente ensuite trois façons différentes de transposer ces données à l'aide d'Aspose.Cells for Java, chacune adaptée à une version d'Excel et à un cas d'utilisation différents.

## **Approche 1 — Transposer une plage en place (Range.transpose)**
Utilisez cette approche chaque fois que vous souhaitez transposer des données sans faire intervenir la fonction de feuille de calcul `TRANSPOSE`. Elle fonctionne sur **toutes les versions d'Excel** et ne dépend pas des tableaux dynamiques, ce qui en fait l'option la plus sûre et compatible entre versions. Elle est idéale lorsque vous n'avez besoin que du résultat final transposé et que vous n'avez pas besoin de conserver la formule `TRANSPOSE` d'origine dans le classeur.

### **API utilisée**
`Range.transpose()` est une méthode d'instance de la classe `com.aspose.cells.Range`. Son appel transpose la plage en place en échangeant ses lignes et ses colonnes, de sorte que ce qui était une ligne devient une colonne et ce qui était une colonne devient une ligne. La méthode modifie directement les cellules sous-jacentes sans écrire de formule.

### **Étapes**
1. Ouvrez le classeur source avec `LoadOptions` défini sur le format `.xlsx` en appelant `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))`.
2. Récupérez la première feuille de calcul du classeur à l'aide de `workbook.getWorksheets().get(0)`.
3. Accédez à la collection de cellules de la feuille de calcul via `worksheet.getCells()`.
4. Créez la plage source couvrant **A1:D5** en appelant `cells.createRange("A1:D5")`.
5. Appelez `source.transpose()` pour faire pivoter la plage en place, en échangeant lignes et colonnes.
6. Enregistrez le classeur avec `workbook.save(outputFile)`.
Après transposition, la plage d'ancrage initiale contient les données pivotées. La première ligne se lit (vide, **Europe**, **Asia**, **North America**) et la première colonne se lit (vide, **Qtr 1**, **Qtr 2**, **Qtr 3**, **Qtr 4**). Chaque colonne de ventes d'origine devient une ligne dans la plage transposée.

```java
import com.aspose.cells.*;
String srcFile = "source.xlsx";
String outputFile = "transposed.xlsx";
Workbook workbook = new Workbook(srcFile, new LoadOptions(LoadFormat.XLSX));
Worksheet worksheet = workbook.getWorksheets().get(0);
Cells cells = worksheet.getCells();
source.transpose();
workbook.save(outputFile);
```

## **Approche 2 — Transposer avec une formule de tableau dynamique (Excel 365 / 2021)**
Utilisez cette approche lorsque vous souhaitez conserver la formule `=TRANSPOSE(A1:D5)` comme formule active dans le classeur de sortie, afin que le résultat se mette à jour automatiquement si les données source changent, et que le fichier Excel cible soit ouvert dans **Excel 365 / Excel 2021 ou version ultérieure**, où les tableaux dynamiques et l'opérateur de déversement sont pris en charge.

### **API utilisée**
`Cell.setDynamicArrayFormula(String formula, FormulaParseOptions options, boolean calculateValue)` est une méthode de `com.aspose.cells.Cell` qui définit la formule de la cellule comme une **formule de tableau dynamique**. Excel évalue la formule une fois et déverse automatiquement le résultat dans les cellules environnantes. Le troisième paramètre, lorsqu'il est défini sur `true`, demande à Aspose.Cells de calculer également les valeurs résultantes au moment de l'écriture.

### **Étapes**
1. Chargez le classeur source à l'aide de `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))`.
2. Récupérez la première feuille de calcul et accédez à sa collection `Cells`.
3. Placez la formule de tableau dynamique sur la cellule **A6**, juste sous la plage source, en appelant `cells.get("A6").setDynamicArrayFormula("=TRANSPOSE(A1:D5)", null, true)`.
4. L'argument `null` passe les `FormulaParseOptions` par défaut, et le troisième argument `true` indique à Aspose.Cells de traiter la formule comme un tableau dynamique et de l'évaluer afin que les valeurs déversées soient écrites dans le classeur.
5. Enregistrez le classeur avec `workbook.save(outputFile)`.
La cellule **A6** contient la formule `=TRANSPOSE(A1:D5)` et Excel déverse automatiquement le résultat dans la zone **A6:D10**, un bloc de 5 lignes sur 4 colonnes correspondant aux données transposées.

{{% alert color="primary" %}}
Cette approche fonctionne **uniquement sur Excel 365 / 2021 ou version ultérieure**. Les anciennes versions d'Excel ne déverseront pas correctement les formules de tableau dynamique.
{{% /alert %}}

```java
import com.aspose.cells.*;
String srcFile = "source.xlsx";
String outFile = "output_transpose_dynamic.xlsx";
Workbook workbook = new Workbook(srcFile, new LoadOptions(LoadFormat.XLSX));
Worksheet worksheet = workbook.getWorksheets().get(0);
Cells cells = worksheet.getCells();
cells.get("A6").setDynamicArrayFormula("=TRANSPOSE(A1:D5)", new FormulaParseOptions(), true);
workbook.save(outFile, SaveFormat.XLSX);
```

## **Approche 3 — Transposer avec une formule matricielle classique (CSE)**
Utilisez cette approche lorsque vous souhaitez qu'une formule `TRANSPOSE` soit conservée dans le classeur, mais que le fichier Excel cible puisse être ouvert dans des **anciennes versions d'Excel (antérieures à 2021, y compris 2019, 2016, 2013, etc.)** où le déversement de tableau dynamique n'est pas pris en charge. La formule matricielle classique CSE (Ctrl+Maj+Entrée) est l'alternative compatible avec les versions antérieures, que toutes les versions d'Excel peuvent évaluer.

### **API utilisée**
`Cell.setArrayFormula(String arrayFormula, int nRows, int nColumns)` est une méthode de `com.aspose.cells.Cell` qui attribue une **formule matricielle classique (CSE)** à la cellule d'ancrage et déclare les dimensions du tableau résultant. Aspose.Cells écrit le marqueur de formule matricielle multi-cellules afin qu'Excel évalue la formule comme une expression de tableau unique remplissant la plage déclarée.

### **Étapes**
1. Chargez le classeur source comme décrit dans les approches précédentes.
2. Récupérez la première feuille de calcul et accédez à sa collection `Cells`.
3. Appelez `cells.get("A6").setArrayFormula("=TRANSPOSE(A1:D5)", 4, 5)`. Le deuxième argument `4` est le nombre de lignes du tableau de destination et le troisième argument `5` est le nombre de colonnes.
4. Enregistrez le classeur avec `workbook.save(outputFile)`.
La cellule **A6** est l'ancrage de la formule matricielle et le tableau évalué s'étend sur 4 lignes par 5 colonnes à partir de A6, correspondant aux dimensions transposées de la source A1:D5. Excel écrit un seul marqueur de formule matricielle sur la plage résultante afin que les anciennes versions d'Excel l'évaluent correctement.

{{% alert color="primary" %}}
Les formules matricielles CSE sont la méthode classique d'Excel pour évaluer une expression `TRANSPOSE` et cette approche est universellement compatible entre les versions d'Excel.
{{% /alert %}}

```java
import com.aspose.cells.*;
// Charger le classeur source avec les options de chargement xlsx
String srcFile = "source.xlsx";
Workbook workbook = new Workbook(srcFile, new LoadOptions(LoadFormat.XLSX));
// Accéder à la première feuille de calcul et à sa collection Cells
Worksheet worksheet = workbook.getWorksheets().get(0);
Cells cells = worksheet.getCells();
// Définir la formule matricielle CSE classique sur la cellule A6.
// La formule =TRANSPOSE(A1:D5) fait pivoter la plage source de 5 lignes x 4 colonnes
// en un tableau de 4 lignes x 5 colonnes. Le deuxième argument (4) est le nombre de lignes
// et le troisième argument (5) est le nombre de colonnes du tableau résultant.
// Aspose.Cells écrit le marqueur de formule matricielle CSE afin qu'Excel l'évalue comme
// une seule formule matricielle multi-cellules, compatible avec les anciennes versions d'Excel
// (2019, 2016, 2013, etc.) qui ne prennent pas en charge le déversement dynamique des tableaux.
cells.get("A6").setArrayFormula("=TRANSPOSE(A1:D5)", 4, 5);
// Enregistrer le classeur afin que le marqueur de formule matricielle soit conservé
workbook.save("output.xlsx");
```

## **Comparaison — Quand utiliser chaque approche**
| Approche | API / Méthode | Version d'Excel | Formule source conservée ? | Plage de sortie |
|----------|--------------|---------------|--------------------------|--------------|
| Approche 1 — Transposition en place | `Range.transpose()` | Toutes les versions d'Excel | Non (valeurs uniquement) | Plage d'ancrage initiale, 5×4 |
| Approche 2 — Formule de tableau dynamique | `Cell.setDynamicArrayFormula` | Excel 365 / 2021+ | Oui (se déverse dynamiquement) | Déversée depuis l'ancrage |
| Approche 3 — Formule matricielle classique (CSE) | `Cell.setArrayFormula` | Toutes les versions d'Excel | Oui (formule matricielle multi-cellules) | Taille explicite, 4×5 |
Utilisez **l'Approche 1** lorsque vous avez besoin d'une transformation rapide et compatible entre versions, et que seules les valeurs transposées doivent être écrites dans le fichier. Utilisez **l'Approche 2** lorsqu'Excel moderne est garanti et que vous souhaitez que la formule reste active et se mette à jour si la source change. Utilisez **l'Approche 3** lorsque vous avez besoin de la plus large compatibilité avec une formule conservée à travers toutes les versions d'Excel, y compris les anciennes versions qui ne prennent pas en charge les tableaux dynamiques.

## **Articles connexes**
- [Rendu de tableau à cellule unique SmartMarker | Aspose.Cells Java](/cells/fr/java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)
- [Insertion d'une image dans une cellule](/cells/fr/java/inserting-an-image-into-a-cell/)
- [Fractionnement de fichiers Excel en plusieurs fichiers](/cells/fr/java/splitting-excel-files-into-multiple-files/)

{{< app/cells/assistant language="java" >}}