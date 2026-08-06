---
title: Modifier la disposition des champs de page dans un tableau croisé dynamique
linktitle: Modifier la disposition des champs de page dans un tableau croisé dynamique
description: Apprenez à contrôler la disposition de la zone des champs de page dans un tableau croisé dynamique à l'aide d'Aspose.Cells for Python via Java, y compris le réglage de l'ordre d'affichage, du nombre de retours à la ligne et de l'ordre des champs de page en haut du tableau croisé dynamique.
keywords: Aspose.Cells for Python via Java, bibliothèque Python Java, feuille de calcul, tableau croisé dynamique, champ de page, ordre des champs de page, nombre de retours des champs de page, déplacer le champ de page
type: docs
weight: 191
url: /fr/python-java/change-page-field-layout/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---
{{% alert color="primary" %}}
Cet article fait suite au sujet **Ajouter un champ de page dans un tableau croisé dynamique**. Il montre comment contrôler la disposition de la zone des champs de page — la barre de contrôles de filtre située en haut d'un tableau croisé dynamique — y compris l'ordre d'affichage, le nombre de retours à la ligne et le réordonnancement des champs.
{{% /alert %}}
## **Introduction**
Un tableau croisé dynamique dans Microsoft Excel expose une **zone de champs de page** dédiée qui se trouve au-dessus du corps ligne/colonne/données du tableau. Cette zone est rendue sous forme d'une barre de contrôles déroulants de filtres (un par champ de page) et c'est ce sur quoi les utilisateurs finaux cliquent pour découper le tableau croisé dynamique selon des critères tels que l'année ou la région. Aspose.Cells for Python via Java modélise cette zone via la collection `pivot_table.page_fields` et expose trois propriétés qui contrôlent la disposition visuelle de la barre :
- `pivot_table.page_field_order` (une valeur de type `Aspose.Cells.PrintOrderType`) décide si les champs de page supplémentaires sont placés *à côté* des champs existants ou *en dessous* de ceux-ci.
- `pivot_table.page_field_wrap_count` définit combien de champs de page sont placés par ligne ou colonne avant le retour à la ligne.
- `pivot_table.page_fields.move(curr_index, dest_index)` réordonne les champs de page sans modifier le mode d'ordre.
Cet article présente trois exemples de code qui illustrent chacune de ces opérations sur un jeu de données commun, afin que vous puissiez comparer les dispositions résultantes côte à côte.
## **Données source**
Les trois exemples ci-dessous chargent ces huit lignes de données de ventes dans une feuille de calcul nommée `PivotData`. Les données contiennent deux candidats aux champs de page (`Year`, `Region`), un candidat au champ de ligne (`Fruit`) et une mesure (`Amount`), ce qui rend la bande des champs de page significative à inspecter.
| Fruit  | Year | Region | Amount |
|--------|------|--------|--------|
| Apple  | 2022 | North  | 150    |
| Apple  | 2023 | North  | 180    |
| Banana | 2022 | South  | 120    |
| Banana | 2023 | South  | 140    |
| Cherry | 2022 | East   | 200    |
| Cherry | 2023 | East   | 220    |
| Grape  | 2022 | West   | 90     |
| Grape  | 2023 | West   | 110    |
Les huit lignes sont remplies dans chaque exemple de code, dans un ordre identique, de sorte que les données source ne diffèrent jamais entre les scénarios — seules les propriétés de disposition des champs de page changent.
## **Exemple 1 : De gauche à droite puis vers le bas**
Dans le premier scénario, nous configurons les deux champs de page (`Year`, `Region`) pour qu'ils apparaissent **côte à côte dans une seule ligne** en haut du tableau croisé dynamique. Nous assignons `Fruit` à l'axe des lignes, plaçons `Year` en premier et `Region` en second sur l'axe des pages (l'ordre des appels à `add_field_to_area` détermine l'indice de départ), ajoutons `Amount` (Somme) comme champ de données, puis définissons `page_field_order` sur `PrintOrderType.OVER_THEN_DOWN` avec `page_field_wrap_count = 2`. Avec `OVER_THEN_DOWN` et un nombre de retours à la ligne de 2, les deux champs de page sont disposés horizontalement côte à côte dans une seule ligne en haut du tableau croisé dynamique, de sorte que la bande occupe une ligne de largeur deux.
```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, WorksheetCollection, Worksheet, Cells, PivotTableCollection, PivotTable, PivotFieldType, ConsolidationFunction, PrintOrderType

dataDir = "output"
if not os.path.exists(dataDir):
    os.makedirs(dataDir, exist_ok=True)

workbook = Workbook()
worksheets = workbook.getWorksheets()

pivotDataIdx = worksheets.add("PivotData")
pivotDataSheet = worksheets.get(pivotDataIdx)
pivotDataCells = pivotDataSheet.getCells()

# En-têtes (ligne 0)
pivotDataCells.get(0, 0).putValue("Fruit")
pivotDataCells.get(0, 1).putValue("Year")
pivotDataCells.get(0, 2).putValue("Region")
pivotDataCells.get(0, 3).putValue("Amount")

# Ligne 1 : Apple, 2022, Nord, 150
pivotDataCells.get(1, 0).putValue("Apple")
pivotDataCells.get(1, 1).putValue(2022)
pivotDataCells.get(1, 2).putValue("North")
pivotDataCells.get(1, 3).putValue(150)

# Ligne 2 : Apple, 2023, Nord, 180
pivotDataCells.get(2, 0).putValue("Apple")
pivotDataCells.get(2, 1).putValue(2023)
pivotDataCells.get(2, 2).putValue("North")
pivotDataCells.get(2, 3).putValue(180)

# Ligne 3 : Banana, 2022, Sud, 120
pivotDataCells.get(3, 0).putValue("Banana")
pivotDataCells.get(3, 1).putValue(2022)
pivotDataCells.get(3, 2).putValue("South")
pivotDataCells.get(3, 3).putValue(120)

# Ligne 4 : Banana, 2023, Sud, 140
pivotDataCells.get(4, 0).putValue("Banana")
pivotDataCells.get(4, 1).putValue(2023)
pivotDataCells.get(4, 2).putValue("South")
pivotDataCells.get(4, 3).putValue(140)

# Ligne 5 : Cherry, 2022, Est, 200
pivotDataCells.get(5, 0).putValue("Cherry")
pivotDataCells.get(5, 1).putValue(2022)
pivotDataCells.get(5, 2).putValue("East")
pivotDataCells.get(5, 3).putValue(200)

# Ligne 6 : Cherry, 2023, Est, 220
pivotDataCells.get(6, 0).putValue("Cherry")
pivotDataCells.get(6, 1).putValue(2023)
pivotDataCells.get(6, 2).putValue("East")
pivotDataCells.get(6, 3).putValue(220)

# Ligne 7 : Grape, 2022, Ouest, 90
pivotDataCells.get(7, 0).putValue("Grape")
pivotDataCells.get(7, 1).putValue(2022)
pivotDataCells.get(7, 2).putValue("West")
pivotDataCells.get(7, 3).putValue(90)

# Ligne 8 : Grape, 2023, Ouest, 110
pivotDataCells.get(8, 0).putValue("Grape")
pivotDataCells.get(8, 1).putValue(2023)
pivotDataCells.get(8, 2).putValue("West")
pivotDataCells.get(8, 3).putValue(110)

# Ajouter la feuille PivotTableReport
pivotTableSheetIdx = worksheets.add("PivotTableReport")
pivotTableSheet = worksheets.get(pivotTableSheetIdx)
pivotTables = pivotTableSheet.getPivotTables()

# Créer un tableau croisé dynamique à partir de PivotData!A1:D9 placé en A1 sur PivotTableReport
pivotIndex = pivotTables.add("PivotData!A1:D9", "A1", "PivotTable1")
pivotTable = pivotTables.get(pivotIndex)

# Ajouter des champs
pivotTable.addFieldToArea(PivotFieldType.ROW, 0)   # Fruit
pivotTable.addFieldToArea(PivotFieldType.PAGE, 1)  # Année
pivotTable.addFieldToArea(PivotFieldType.PAGE, 2)  # Région
pivotTable.addFieldToArea(PivotFieldType.DATA, 3)  # Montant
pivotTable.getDataFields().get(0).setFunction(ConsolidationFunction.SUM)

# Configurer la disposition de la zone des champs de page : placer les champs de page horizontalement d'abord, revenir à la ligne après chaque 2
pivotTable.setPageFieldOrder(PrintOrderType.OVER_THEN_DOWN)
pivotTable.setPageFieldWrapCount(2)

# Actualiser et calculer
pivotTable.calculateData()

# Enregistrer
workbook.save(os.path.join(dataDir, "pageFieldLayout_overThenDown.xlsx"))

jpype.shutdownJVM()
```
## **Exemple 2 : De haut en bas puis vers la droite**
Dans cet exemple, nous plaçons `Fruit` sur l'axe des lignes, `Year` et `Region` sur l'axe des pages (avec `Year` en premier), et `Amount` (Somme) comme champ de données — exactement comme dans l'Exemple 1. Nous définissons ensuite `page_field_order` sur `PrintOrderType.DOWN_THEN_OVER` et `page_field_wrap_count` sur `2`. Avec `DOWN_THEN_OVER` et un nombre de retours à la ligne de 2, les deux champs de page sont empilés verticalement — `Year` en haut, `Region` directement en dessous — formant une seule colonne en haut du tableau croisé dynamique. La bande occupe donc deux lignes de largeur un, contrairement à l'Exemple 1.
```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, PivotFieldType, PrintOrderType

workbook = Workbook()
pivotData = workbook.getWorksheets().get(0)
pivotData.setName("PivotData")
pivotReportIdx = workbook.getWorksheets().add("PivotTableReport")
pivotReport = workbook.getWorksheets().get(pivotReportIdx)

headers = ["Fruit", "Year", "Region", "Amount"]
for c in range(len(headers)):
    pivotData.getCells().get(0, c).putValue(headers[c])

data = [
    ["Apple", 2022, "North", 150],
    ["Apple", 2023, "North", 180],
    ["Banana", 2022, "South", 120],
    ["Banana", 2023, "South", 140],
    ["Cherry", 2022, "East", 200],
    ["Cherry", 2023, "East", 220],
    ["Grape", 2022, "West", 90],
    ["Grape", 2023, "West", 110]
]

for r in range(len(data)):
    for c in range(len(data[r])):
        pivotData.getCells().get(r + 1, c).putValue(data[r][c])

idx = pivotReport.getPivotTables().add("PivotData!A1:D9", "A1", "PivotTable")
pivotTable = pivotReport.getPivotTables().get(idx)

pivotTable.addFieldToArea(PivotFieldType.ROW, 0)
pivotTable.addFieldToArea(PivotFieldType.PAGE, 1)
pivotTable.addFieldToArea(PivotFieldType.PAGE, 2)
pivotTable.addFieldToArea(PivotFieldType.DATA, 3)

pivotTable.setPageFieldOrder(PrintOrderType.DOWN_THEN_OVER)
pivotTable.setPageFieldWrapCount(2)

pivotTable.calculateData()

workbook.save("pageFieldLayout_downThenOver.xlsx")

jpype.shutdownJVM()
```
## **Exemple 3 : Déplacer un champ de page**
Dans le troisième scénario, nous conservons ce jeu de données et cette affectation de champs, définissons une disposition neutre (`OVER_THEN_DOWN` avec un nombre de retours à la ligne de `2`), puis démontrons l'opération `page_fields.move`. L'appel `move(0, 1)` déplace le champ de page à l'indice 0 (`Year`) vers la position 1, et le champ de page qui était à la position 1 (`Region`) passe à la position 0. Après cet appel, `Region` est le premier champ de page et `Year` est le second. Le mode de retour à la ligne et d'ordre reste inchangé, donc la bande est toujours rendue horizontalement côte à côte — seul l'ordre des deux listes déroulantes a été permuté.
```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType, PrintOrderType

workbook = Workbook()

dataSheet = workbook.getWorksheets().get(0)
dataSheet.setName("PivotData")

dataSheet.getCells().get("A1").putValue("Fruit")
dataSheet.getCells().get("B1").putValue("Year")
dataSheet.getCells().get("C1").putValue("Region")
dataSheet.getCells().get("D1").putValue("Amount")

dataSheet.getCells().get("A2").putValue("Apple")
dataSheet.getCells().get("B2").putValue(2022)
dataSheet.getCells().get("C2").putValue("North")
dataSheet.getCells().get("D2").putValue(150)

dataSheet.getCells().get("A3").putValue("Apple")
dataSheet.getCells().get("B3").putValue(2023)
dataSheet.getCells().get("C3").putValue("North")
dataSheet.getCells().get("D3").putValue(180)

dataSheet.getCells().get("A4").putValue("Banana")
dataSheet.getCells().get("B4").putValue(2022)
dataSheet.getCells().get("C4").putValue("South")
dataSheet.getCells().get("D4").putValue(120)

dataSheet.getCells().get("A5").putValue("Banana")
dataSheet.getCells().get("B5").putValue(2023)
dataSheet.getCells().get("C5").putValue("South")
dataSheet.getCells().get("D5").putValue(140)

dataSheet.getCells().get("A6").putValue("Cherry")
dataSheet.getCells().get("B6").putValue(2022)
dataSheet.getCells().get("C6").putValue("East")
dataSheet.getCells().get("D6").putValue(200)

dataSheet.getCells().get("A7").putValue("Cherry")
dataSheet.getCells().get("B7").putValue(2023)
dataSheet.getCells().get("C7").putValue("East")
dataSheet.getCells().get("D7").putValue(220)

dataSheet.getCells().get("A8").putValue("Grape")
dataSheet.getCells().get("B8").putValue(2022)
dataSheet.getCells().get("C8").putValue("West")
dataSheet.getCells().get("D8").putValue(90)

dataSheet.getCells().get("A9").putValue("Grape")
dataSheet.getCells().get("B9").putValue(2023)
dataSheet.getCells().get("C9").putValue("West")
dataSheet.getCells().get("D9").putValue(110)

pivotSheetIdx = workbook.getWorksheets().add("PivotTableReport")
pivotSheet = workbook.getWorksheets().get(pivotSheetIdx)

pivotIdx = pivotSheet.getPivotTables().add("PivotData!A1:D9", "A3", "PivotTable")
pivotTable = pivotSheet.getPivotTables().get(pivotIdx)

pivotTable.addFieldToArea(PivotFieldType.ROW, 0)
pivotTable.addFieldToArea(PivotFieldType.PAGE, 1)
pivotTable.addFieldToArea(PivotFieldType.PAGE, 2)
pivotTable.addFieldToArea(PivotFieldType.DATA, 3)

pivotTable.setPageFieldOrder(PrintOrderType.OVER_THEN_DOWN)
pivotTable.setPageFieldWrapCount(2)

pivotTable.getPageFields().move(0, 1)

pivotTable.calculateData()

workbook.save("pageFieldLayout_move.xlsx")

jpype.shutdownJVM()
```
## **Articles connexes**
- [Ajouter un champ de page dans un tableau croisé dynamique](/cells/fr/python-java/add-page-field-in-pivot-table/) — la page parente qui présente comment les champs de page sont ajoutés à un tableau croisé dynamique.
- [Champs de lignes et de colonnes dans un tableau croisé dynamique](/cells/fr/python-java/row-and-column-fields/) — couvre l'affectation des champs aux axes de lignes et de colonnes, complétant le travail sur l'axe des pages présenté ici.
- [Gérer les champs de valeur dans un tableau croisé dynamique](/cells/fr/python-java/manage-value-fields/) — décrit comment configurer la zone de données (valeurs), y compris l'agrégation `SUM` utilisée dans cet article.
- [Actualiser un tableau croisé dynamique](/cells/fr/python-java/refresh-pivot-table/) — explique `refresh_data` et `calculate_data`, qui sont nécessaires après le réordonnancement des champs de page.
- [Appliquer un style à un tableau croisé dynamique](/cells/fr/python-java/apply-style-to-pivot-table/) — montre comment formater le tableau croisé dynamique rendu une fois que la bande des champs de page a été disposée.
{{< app/cells/assistant language="python" >}}