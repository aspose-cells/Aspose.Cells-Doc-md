---
title: Transpose Range
description: This article explains how to transpose or rotate data from rows to columns or vice versa in Excel files using Aspose.Cells for Python via .NET, with three different approaches.
linktitle: Transposer une plage
url: /fr/python-net/transpose-rotate-data-from-rows-to-columns-or-vice-versa/
keywords: Aspose.Cells for Python via .NET, tableur, transposer une plage, faire pivoter les données, fonction TRANSPOSE, formule de tableau dynamique, formule matricielle, Excel TRANSPOSE, Lignes en Colonnes
type: docs
weight: 80
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

keywords: Aspose.Cells for Python via .NET, tableur, transposer une plage, faire pivoter les données, fonction TRANSPOSE, formule de tableau dynamique, formule matricielle, Excel TRANSPOSE, Lignes en Colonnes
type: docs
weight: 80

{{% alert color="primary" %}}
Aspose.Cells for Python via .NET prend en charge la transposition (rotation) des données de sorte que les lignes deviennent des colonnes et les colonnes deviennent des lignes de trois manières différentes. La première approche utilise la méthode in-place `range.transpose()` et fonctionne sur toutes les versions d'Excel, tandis que la seconde utilise `cell.set_dynamic_array_formula()` pour écrire une formule moderne de tableau dynamique `=TRANSPOSE(...)` qui se déverse automatiquement dans Excel 365 ou Excel 2021. La troisième approche utilise `cell.set_array_formula()` pour écrire une formule matricielle classique Ctrl+Shift+Enter (CSE) compatible avec les anciennes versions d'Excel. Cet article présente chaque approche avec des instructions étape par étape et des exemples de code complets.
{{% /alert %}}

## **Introduction**
Transposer une plage signifie la faire pivoter de sorte que ce qui était une ligne devienne une colonne et ce qui était une colonne devienne une ligne, reflétant ainsi les données à travers sa diagonale principale. Dans Microsoft Excel, la fonction de feuille de calcul `TRANSPOSE` effectue cette opération, et la référence conceptuelle est documentée à [https://support.microsoft.com/en-us/excel/functions/transpose-function](https://support.microsoft.com/en-us/excel/functions/transpose-function). La même idée peut être appliquée par programmation à une plage de cellules, ce qui est utile dans de nombreux scénarios métier et de reporting.
Les scénarios courants dans lesquels la transposition est utile incluent les suivants.
- Réorienter les rapports de ventes trimestriels ou annuels où les trimestres s'étendent normalement sur la page et les régions descendent le long de la page, ou inversement.
- Inverser l'orientation des axes dans les tableaux de bord ou les graphiques afin qu'une série temporelle descende le long de la page au lieu de s'étendre horizontalement.
- Remodeler les données importées de systèmes externes afin qu'elles correspondent à la disposition attendue par les modèles d'analyse ou de reporting en aval.
Pour rendre le reste de l'article concret, chaque exemple utilise le petit tableau suivant des ventes par région et par trimestre. Dans le classeur d'exemple, ce tableau occupe la plage **A1:D5**, avec **A1** laissé vide comme coin supérieur gauche, **B1:D1** contenant les en-têtes de région, et **A2:A5** contenant les en-têtes de trimestre.
| Région           | Europe    | Asie       | Amérique du Nord |
|------------------|-----------|-----------|------------------|
| Trim 1           | 21704714  | 8774099   | 12094215         |
| Trim 2           | 17987034  | 12214447  | 10873099         |
| Trim 3           | 19485029  | 14356879  | 15689543         |
| Trim 4           | 22567894  | 15763492  | 17456723         |
L'article présente ensuite trois approches différentes pour transposer ces données à l'aide d'Aspose.Cells for Python via .NET, chacune adaptée à une version d'Excel et un cas d'utilisation différents.

## **Approche 1 — Transposer une plage en place (range.transpose)**
Utilisez cette approche lorsque vous souhaitez transposer des données sans impliquer la fonction de feuille de calcul `TRANSPOSE`. Elle fonctionne sur **toutes les versions d'Excel** et ne dépend pas des tableaux dynamiques, ce qui en fait l'option compatible inter-versions la plus sûre. Elle est idéale lorsque vous n'avez besoin que du résultat final transposé et que vous n'avez pas besoin de conserver la formule `TRANSPOSE` d'origine dans le classeur.

### **API utilisée**
`range.transpose()` est une méthode d'instance de la classe `Aspose.Cells.Range`. Son appel retourne la plage en place en échangeant ses lignes et ses colonnes, de sorte que ce qui était une ligne devient une colonne et ce qui était une colonne devient une ligne. La méthode modifie directement les cellules sous-jacentes sans écrire de formule.

### **Étapes**
1. Ouvrez le classeur source avec `LoadOptions` défini sur le format `.xlsx` en appelant `Workbook(srcFile, LoadOptions(LoadFormat.Xlsx))`.
2. Récupérez la première feuille de calcul du classeur à l'aide de `workbook.worksheets[0]`.
3. Accédez à la collection de cellules de la feuille de calcul via `worksheet.cells`.
4. Créez la plage source couvrant **A1:D5** en appelant `cells.create_range("A1:D5")`.
5. Appelez `source.transpose()` pour faire pivoter la plage en place, en échangeant les lignes et les colonnes.
6. Enregistrez le classeur avec `workbook.save(outputFile)`.
Après la transposition, la même plage d'ancrage contient les données pivotées. La première ligne indique (vide, **Europe**, **Asie**, **Amérique du Nord**) et la première colonne indique (vide, **Trim 1**, **Trim 2**, **Trim 3**, **Trim 4**). Chaque colonne de ventes d'origine devient une ligne dans la plage transposée.

```python
import aspose.cells as ac
srcFile = "source.xlsx"
outputFile = "transposed.xlsx"
workbook = ac.Workbook(srcFile, ac.LoadOptions(ac.LoadFormat.XLSX))
worksheet = workbook.worksheets[0]
cells = worksheet.cells
source = cells.create_range("A1:D5")
source.transpose()
workbook.save(outputFile)
```

## **Approche 2 — Transposer avec une formule de tableau dynamique (Excel 365 / 2021)**
Utilisez cette approche lorsque vous souhaitez conserver la formule `=TRANSPOSE(A1:D5)` comme une formule active dans le classeur de sortie afin que le résultat se mette à jour automatiquement si les données sources changent, et que le fichier Excel cible sera ouvert dans **Excel 365 / Excel 2021 ou ultérieur** où les tableaux dynamiques et l'opérateur de débordement sont pris en charge.

### **API utilisée**
`cell.set_dynamic_array_formula(formula, options, calculate_value)` est une méthode de `Aspose.Cells.Cell` qui définit la formule de la cellule comme une **formule de tableau dynamique**. Excel évalue la formule une seule fois et déverse automatiquement le résultat dans les cellules environnantes. Le troisième paramètre, lorsqu'il est défini sur `True`, indique à Aspose.Cells de calculer également les valeurs résultantes au moment de l'écriture.

### **Étapes**
1. Chargez le classeur source à l'aide de `Workbook(srcFile, LoadOptions(LoadFormat.Xlsx))`.
2. Récupérez la première feuille de calcul et accédez à sa collection `cells`.
3. Placez la formule de tableau dynamique dans la cellule **A6**, juste sous la plage source, en appelant `cells["A6"].set_dynamic_array_formula("=TRANSPOSE(A1:D5)", None, True)`.
4. L'argument `None` passe les `FormulaParseOptions` par défaut, et le troisième argument `True` indique à Aspose.Cells de traiter la formule comme un tableau dynamique et de l'évaluer afin que les valeurs débordées soient écrites dans le classeur.
5. Enregistrez le classeur avec `workbook.save(outputFile)`.
La cellule **A6** contient la formule `=TRANSPOSE(A1:D5)` et Excel déverse automatiquement le résultat dans la région **A6:D10**, un bloc de 5 lignes par 4 colonnes correspondant aux données transposées.

{{% alert color="primary" %}}
Cette approche fonctionne **uniquement sur Excel 365 / 2021 ou ultérieur**. Les anciennes versions d'Excel ne déverseront pas correctement les formules de tableau dynamique.
{{% /alert %}}

```python
import aspose.cells as ac
srcFile = "source.xlsx"
outFile = "output_transpose_dynamic.xlsx"
workbook = ac.Workbook(srcFile, ac.LoadOptions(ac.LoadFormat.Xlsx))
worksheet = workbook.worksheets[0]
cells = worksheet.cells
cells["A6"].set_dynamic_array_formula("=TRANSPOSE(A1:D5)", ac.FormulaParseOptions(), True)
workbook.save(outFile, ac.SaveFormat.Xlsx)
```

## **Approche 3 — Transposer avec une formule matricielle classique (CSE)**
Utilisez cette approche lorsque vous souhaitez conserver une formule `TRANSPOSE` dans le classeur mais que le fichier Excel cible peut être ouvert dans **des versions plus anciennes d'Excel (antérieures à 2021, y compris 2019, 2016, 2013, etc.)** où le débordement des tableaux dynamiques n'est pas pris en charge. La formule matricielle CSE classique (Ctrl+Shift+Enter) est l'alternative compatible avec les versions antérieures que toutes les versions d'Excel peuvent évaluer.

### **API utilisée**
`cell.set_array_formula(array_formula, n_rows, n_columns)` est une méthode de `Aspose.Cells.Cell` qui attribue une **formule matricielle classique (CSE)** à la cellule d'ancrage et déclare les dimensions du tableau résultant. Aspose.Cells écrit le marqueur de formule matricielle multi-cellules afin qu'Excel évalue la formule comme une expression de tableau unique qui remplit la plage déclarée.

### **Étapes**
1. Chargez le classeur source de la même manière que dans les approches précédentes.
2. Récupérez la première feuille de calcul et accédez à sa collection `cells`.
3. Appelez `cells["A6"].set_array_formula("=TRANSPOSE(A1:D5)", 4, 5)`. Le deuxième argument `4` correspond au nombre de lignes du tableau de destination et le troisième argument `5` correspond au nombre de colonnes.
4. Enregistrez le classeur avec `workbook.save(outputFile)`.
La cellule **A6** est l'ancrage de la formule matricielle et le tableau évalué s'étend sur 4 lignes par 5 colonnes à partir de A6, correspondant aux dimensions transposées de la source A1:D5. Excel écrit un marqueur de formule matricielle unique sur la plage résultante afin que les anciennes versions d'Excel l'évaluent correctement.

{{% alert color="primary" %}}
Les formules matricielles CSE sont la méthode classique d'Excel pour évaluer une expression `TRANSPOSE` et cette approche est universellement compatible avec toutes les versions d'Excel.
{{% /alert %}}

```python
import aspose.cells as ac
# Charger le classeur source avec les LoadOptions xlsx
srcFile = "source.xlsx"
workbook = ac.Workbook(srcFile, ac.LoadOptions(ac.LoadFormat.Xlsx))
# Accéder à la première feuille de calcul et à sa collection Cells
worksheet = workbook.worksheets[0]
cells = worksheet.cells
# Définir la formule matricielle CSE classique sur la cellule A6.
# La formule =TRANSPOSE(A1:D5) transpose la plage source de 5 lignes x 4 colonnes
# en un tableau de 4 lignes x 5 colonnes. Le deuxième argument (4) est le nombre de lignes
# et le troisième argument (5) est le nombre de colonnes du tableau résultant.
# Aspose.Cells écrit le marqueur de formule matricielle CSE afin qu'Excel l'évalue comme
# une formule matricielle multi-cellules unique, compatible avec les anciennes versions d'Excel
# (2019, 2016, 2013, etc.) qui ne prennent pas en charge le déversement dynamique des tableaux.
cells["A6"].set_array_formula("=TRANSPOSE(A1:D5)", 4, 5)
# Enregistrer le classeur afin que le marqueur de formule matricielle soit conservé
workbook.save("output.xlsx")
```

## **Comparaison — Quand utiliser chaque approche**
| Approche | API / Méthode | Version d'Excel | Formule source conservée ? | Plage de sortie |
|----------|---------------|-----------------|---------------------------|-----------------|
| Approche 1 — Transposition en place | `range.transpose()` | Toutes les versions d'Excel | Non (valeurs uniquement) | Même plage d'ancrage, 5×4 |
| Approche 2 — Formule de tableau dynamique | `cell.set_dynamic_array_formula` | Excel 365 / 2021+ | Oui (déversement dynamique) | Déversée à partir de l'ancrage |
| Approche 3 — Formule matricielle classique (CSE) | `cell.set_array_formula` | Toutes les versions d'Excel | Oui (formule matricielle multi-cellules) | Taille explicite, 4×5 |
Utilisez **l'Approche 1** lorsque vous avez besoin d'une transformation rapide et inter-versions et que vous n'avez besoin que des valeurs transposées écrites dans le fichier. Utilisez **l'Approche 2** lorsqu'Excel moderne est garanti et que vous souhaitez que la formule reste active et se mette à jour si la source change. Utilisez **l'Approche 3** lorsque vous avez besoin de la plus large compatibilité avec une formule conservée à travers toutes les versions d'Excel, y compris les anciennes versions qui ne prennent pas en charge les tableaux dynamiques.

{{< app/cells/assistant language="python-net" >}}