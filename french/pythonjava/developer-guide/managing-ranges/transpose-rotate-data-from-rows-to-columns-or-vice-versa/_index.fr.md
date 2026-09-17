---
title: Transposer une plage
linktitle: Transposer une plage
description: Cet article explique comment transposer ou faire pivoter des données de lignes vers des colonnes ou inversement dans des fichiers Excel à l'aide de Aspose.Cells for Python via Java selon trois approches différentes.
keywords: Aspose.Cells, bibliothèque Python via Java, feuille de calcul, transposer une plage, faire pivoter des données, fonction TRANSPOSE, formule de tableau dynamique, formule de tableau, TRANSPOSE Excel, lignes vers colonnes
type: docs
weight: 80
url: /fr/python-java/transpose-rotate-data-from-rows-to-columns-or-vice-versa/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells for Python via Java prend en charge la transposition (rotation) des données de sorte que les lignes deviennent des colonnes et les colonnes deviennent des lignes de trois manières différentes. La première approche utilise la méthode en place `Range.transpose()` et fonctionne sur toutes les versions d'Excel, tandis que la deuxième utilise `Cell.setDynamicArrayFormula()` pour écrire une formule de tableau dynamique moderne `=TRANSPOSE(...)` qui se déverse automatiquement sur Excel 365 ou Excel 2021. La troisième approche utilise `Cell.setArrayFormula()` pour écrire une formule de tableau classique Ctrl+Shift+Enter (CSE) compatible avec les anciennes versions d'Excel. Cet article passe en revue chaque approche avec des instructions étape par étape et des exemples de code complets.
{{% /alert %}}

## **Introduction**
Transposer une plage signifie la faire pivoter de sorte que ce qui était une ligne devienne une colonne et ce qui était une colonne devienne une ligne, ce qui revient à réfléchir les données par rapport à leur diagonale principale. Dans Microsoft Excel, la fonction de feuille de calcul `TRANSPOSE` effectue cette opération, et la référence conceptuelle est documentée à l'adresse [https://support.microsoft.com/en-us/excel/functions/transpose-function](https://support.microsoft.com/en-us/excel/functions/transpose-function). La même idée peut être appliquée par programmation à une plage de cellules, ce qui est utile dans de nombreux scénarios professionnels et de reporting.
Les scénarios courants dans lesquels la transposition est utile incluent les suivants.
- Réorienter les rapports de ventes trimestriels ou annuels où les trimestres s'étendent normalement horizontalement sur la page et les régions verticalement, ou inversement.
- Échanger l'orientation des axes dans les tableaux de bord ou les graphiques afin qu'une série temporelle s'étende verticalement plutôt qu'horizontalement.
- Remodeler les données importées depuis des systèmes externes afin qu'elles correspondent à la disposition attendue par les modèles d'analyse ou de reporting en aval.
Pour rendre le reste de l'article concret, chaque exemple utilise le petit tableau de ventes par région par trimestre suivant. Dans le classeur d'exemple, ce tableau occupe la plage **A1:D5**, avec **A1** laissé vide comme coin supérieur gauche, **B1:D1** contenant les en-têtes de région, et **A2:A5** contenant les en-têtes de trimestre.
| Region            | Europe    | Asia      | North America |
|-------------------|-----------|-----------|---------------|
| Qtr 1             | 21704714  | 8774099   | 12094215      |
| Qtr 2             | 17987034  | 12214447  | 10873099      |
| Qtr 3             | 19485029  | 14356879  | 15689543      |
| Qtr 4             | 22567894  | 15763492  | 17456723      |
L'article présente ensuite trois façons différentes de transposer ces données à l'aide de Aspose.Cells for Python via Java, chacune adaptée à une version et un cas d'usage différents d'Excel.

## **Approche 1 — Transposer une plage en place (Range.transpose)**
Utilisez cette approche lorsque vous souhaitez transposer des données sans faire appel à la fonction de feuille de calcul `TRANSPOSE`. Elle fonctionne sur **toutes les versions d'Excel** et n'a aucune dépendance aux tableaux dynamiques, ce qui en fait l'option la plus sûre et compatible entre versions. Elle est idéale lorsque vous n'avez besoin que du résultat transposé final et que vous n'avez pas besoin de conserver la formule `TRANSPOSE` d'origine dans le classeur.

### **API utilisée**
`Range.transpose()` est une méthode d'instance de la classe `com.aspose.cells.Range`. Son appel retourne la plage en place en échangeant ses lignes et colonnes, de sorte que ce qui était une ligne devient une colonne et ce qui était une colonne devient une ligne. La méthode modifie directement les cellules sous-jacentes sans écrire de formule.

### **Étapes**
1. Ouvrez le classeur source avec `LoadOptions` défini sur le format `.xlsx` en appelant `Workbook(srcFile, LoadOptions(LoadFormat.Xlsx))`.
2. Récupérez la première feuille de calcul du classeur à l'aide de `workbook.getWorksheets().get(0)`.
3. Accédez à la collection de cellules de la feuille de calcul via `worksheet.getCells()`.
4. Créez la plage source couvrant **A1:D5** en appelant `cells.createRange("A1:D5")`.
5. Appelez `source.transpose()` pour faire pivoter la plage en place, en échangeant lignes et colonnes.
6. Enregistrez le classeur avec `workbook.save(outputFile)`.
Après transposition, la même plage d'ancrage contient les données pivotées. La première ligne lit (vide, **Europe**, **Asia**, **North America**) et la première colonne lit (vide, **Qtr 1**, **Qtr 2**, **Qtr 3**, **Qtr 4**). Chaque colonne d'origine des ventes devient une ligne dans la plage transposée.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, LoadOptions, LoadFormat
srcFile = "source.xlsx"
outputFile = "transposed.xlsx"
loadOptions = LoadOptions(LoadFormat.Xlsx)
workbook = Workbook(srcFile, loadOptions)
worksheet = workbook.getWorksheets().get(0)
cells = worksheet.getCells()
source = cells.createRange("A1:D5")
source.transpose()
workbook.save(outputFile)
jpype.shutdownJVM()
```

## **Approche 2 — Transposer avec une formule de tableau dynamique (Excel 365 / 2021)**
Utilisez cette approche lorsque vous souhaitez conserver la formule `=TRANSPOSE(A1:D5)` comme formule active dans le classeur de sortie afin que le résultat se mette à jour automatiquement si les données source changent, et que le fichier Excel cible sera ouvert dans **Excel 365 / Excel 2021 ou version ultérieure** où les tableaux dynamiques et l'opérateur de déversement sont pris en charge.

### **API utilisée**
`Cell.setDynamicArrayFormula(String formula, FormulaParseOptions options, boolean calculateValue)` est une méthode de `com.aspose.cells.Cell` qui définit la formule de la cellule comme **formule de tableau dynamique**. Excel évalue la formule une fois et déverse automatiquement le résultat dans les cellules environnantes. Le troisième paramètre, lorsqu'il est défini sur `True`, indique à Aspose.Cells de calculer également les valeurs résultantes au moment de l'écriture.

### **Étapes**
1. Chargez le classeur source à l'aide de `Workbook(srcFile, LoadOptions(LoadFormat.Xlsx))`.
2. Récupérez la première feuille de calcul et accédez à sa collection `Cells`.
3. Placez la formule de tableau dynamique dans la cellule **A6**, juste en dessous de la plage source, en appelant `cells.get("A6").setDynamicArrayFormula("=TRANSPOSE(A1:D5)", None, True)`.
4. L'argument `None` passe les `FormulaParseOptions` par défaut, et le troisième argument `True` indique à Aspose.Cells de traiter la formule comme un tableau dynamique et de l'évaluer afin que les valeurs déversées soient écrites dans le classeur.
5. Enregistrez le classeur avec `workbook.save(outputFile)`.
La cellule **A6** contient la formule `=TRANSPOSE(A1:D5)` et Excel déverse automatiquement le résultat dans la région **A6:D10**, un bloc de 5 lignes par 4 colonnes égal aux données transposées.

{{% alert color="primary" %}}
Cette approche fonctionne **uniquement sur Excel 365 / 2021 ou version ultérieure**. Les anciennes versions d'Excel ne déverseront pas correctement les formules de tableau dynamique.
{{% /alert %}}

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, LoadOptions, LoadFormat, FormulaParseOptions, SaveFormat
# code porté ici
srcFile = "source.xlsx"
outFile = "output_transpose_dynamic.xlsx"
workbook = Workbook(srcFile, LoadOptions(LoadFormat.Xlsx))
worksheet = workbook.getWorksheets().get(0)
cells = worksheet.getCells()
cells.get("A6").setDynamicArrayFormula("=TRANSPOSE(A1:D5)", FormulaParseOptions(), True)
workbook.save(outFile, SaveFormat.Xlsx)
jpype.shutdownJVM()
```

## **Approche 3 — Transposer avec une formule de tableau classique (CSE)**
Utilisez cette approche lorsque vous souhaitez qu'une formule `TRANSPOSE` soit conservée dans le classeur mais que le fichier Excel cible puisse être ouvert dans **des versions plus anciennes d'Excel (avant 2021, y compris 2019, 2016, 2013, etc.)** où le déversement de tableau dynamique n'est pas pris en charge. La formule de tableau CSE classique (Ctrl+Shift+Enter) est l'alternative compatible héritée que toutes les versions d'Excel peuvent évaluer.

### **API utilisée**
`Cell.setArrayFormula(String arrayFormula, int nRows, int nColumns)` est une méthode de `com.aspose.cells.Cell` qui attribue une **formule de tableau classique (CSE)** à la cellule d'ancrage et déclare les dimensions du tableau résultant. Aspose.Cells écrit le marqueur de formule multi-cellules pour qu'Excel évalue la formule comme une expression de tableau unique qui remplit la plage déclarée.

### **Étapes**
1. Chargez le classeur source de la même manière que dans les approches précédentes.
2. Récupérez la première feuille de calcul et accédez à sa collection `Cells`.
3. Appelez `cells.get("A6").setArrayFormula("=TRANSPOSE(A1:D5)", 4, 5)`. Le deuxième argument `4` est le nombre de lignes du tableau de destination et le troisième argument `5` est le nombre de colonnes.
4. Enregistrez le classeur avec `workbook.save(outputFile)`.
La cellule **A6** est l'ancrage de la formule de tableau et le tableau évalué s'étend sur 4 lignes par 5 colonnes en partant de A6, correspondant aux dimensions transposées de la source A1:D5. Excel écrit un marqueur de formule de tableau unique sur la plage résultante afin que les anciennes versions d'Excel l'évaluent correctement.

{{% alert color="primary" %}}
Les formules de tableau CSE constituent la méthode classique d'Excel pour évaluer une expression `TRANSPOSE` et cette approche est universellement compatible avec toutes les versions d'Excel.
{{% /alert %}}

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, LoadOptions, LoadFormat, Worksheet, Cells
# Charger le classeur source avec les options de chargement xlsx
srcFile = "source.xlsx"
workbook = Workbook(srcFile, LoadOptions(LoadFormat.Xlsx))
# Accéder à la première feuille de calcul et à sa collection Cells
worksheet = workbook.getWorksheets().get(0)
cells = worksheet.getCells()
# Définir la formule matricielle CSE classique sur la cellule A6.
# La formule =TRANSPOSE(A1:D5) fait pivoter la plage source de 5 lignes x 4 colonnes
# en un tableau de 4 lignes x 5 colonnes. Le deuxième argument (4) est le nombre de lignes
# et le troisième argument (5) est le nombre de colonnes du tableau résultant.
# Aspose.Cells écrit le marqueur de formule matricielle CSE afin qu'Excel l'évalue comme
# une formule matricielle unique multi-cellules, compatible avec les anciennes versions d'Excel
# (2019, 2016, 2013, etc.) qui ne prennent pas en charge le déversement dynamique des tableaux.
cells.get("A6").setArrayFormula("=TRANSPOSE(A1:D5)", 4, 5)
# Enregistrer le classeur afin que le marqueur de formule matricielle soit persisté
workbook.save("output.xlsx")
jpype.shutdownJVM()
```

## **Comparaison — Quand utiliser chaque approche**
| Approche | API / Méthode | Version d'Excel | Formule source conservée ? | Plage de sortie |
|----------|--------------|-----------------|--------------------------|------------------|
| Approche 1 — Transposition en place | `Range.transpose()` | Toutes les versions d'Excel | Non (valeurs uniquement) | Même plage d'ancrage, 5×4 |
| Approche 2 — Formule de tableau dynamique | `Cell.setDynamicArrayFormula` | Excel 365 / 2021+ | Oui (déversement dynamique) | Déversée depuis l'ancrage |
| Approche 3 — Formule de tableau classique (CSE) | `Cell.setArrayFormula` | Toutes les versions d'Excel | Oui (formule multi-cellules) | Taille explicite, 4×5 |
Utilisez l'**Approche 1** lorsque vous avez besoin d'une transformation rapide et compatible entre versions et que vous n'avez besoin que des valeurs transposées écrites dans le fichier. Utilisez l'**Approche 2** lorsqu'Excel moderne est garanti et que vous souhaitez que la formule reste active et se mette à jour si la source change. Utilisez l'**Approche 3** lorsque vous avez besoin de la compatibilité la plus large avec une formule conservée à travers toutes les versions d'Excel, y compris les versions plus anciennes qui ne prennent pas en charge les tableaux dynamiques.

## **Articles connexes**
- [Rendu de tableau à cellule unique SmartMarker | Aspose.Cells for Python via Java](/cells/fr/python-java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)
- [Insertion d'une image dans une cellule](/cells/fr/python-java/inserting-an-image-into-a-cell/)
- [Fractionnement de fichiers Excel en plusieurs fichiers](/cells/fr/python-java/splitting-excel-files-into-multiple-files/)

{{< app/cells/assistant language="python" >}}| Region            | Europe    | Asia      | North America |