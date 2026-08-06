---
title: Modifier la disposition des champs de page dans un tableau croisé dynamique
linktitle: Modifier la disposition des champs de page dans un tableau croisé dynamique
description: Apprenez à contrôler la disposition de la zone des champs de page dans un tableau croisé dynamique en utilisant Aspose.Cells for Python via .NET, y compris la définition de l'ordre d'affichage, du nombre de sauts et de l'ordre des champs de page en haut du tableau croisé dynamique.
keywords: Aspose.Cells, Python via .NET library, spreadsheet, pivot table, page field, page field order, page field wrap count, move page field
type: docs
weight: 191
url: /fr/python-net/change-page-field-layout/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---
{{% alert color="primary" %}}
Cet article fait suite au sujet **Ajouter un champ de page dans un tableau croisé dynamique**. Il montre comment contrôler la disposition de la zone des champs de page — la bande de contrôles de filtre située en haut d'un tableau croisé dynamique — y compris l'ordre d'affichage, le nombre de sauts et le réordonnancement des champs.
{{% /alert %}}
## **Introduction**
Un tableau croisé dynamique dans Microsoft Excel expose une **zone de champs de page** dédiée qui se trouve au-dessus du corps ligne/colonne/données du tableau. Cette zone est rendue sous forme de bande de contrôles de filtre déroulants (un par champ de page) et c'est ce sur quoi les utilisateurs finaux cliquent pour découper le tableau croisé dynamique selon des critères tels que l'année ou la région. Aspose.Cells for Python via .NET modélise cette zone via la collection `pivot_table.page_fields` et expose trois propriétés qui contrôlent la disposition visuelle de la bande :
- `pivot_table.page_field_order` (une valeur de type `PrintOrderType`) décide si les champs de page supplémentaires sont placés *à côté* de ceux existants ou *en dessous*.
- `pivot_table.page_field_wrap_count` définit combien de champs de page sont placés par ligne ou colonne avant le retour à la ligne.
- `pivot_table.page_fields.move(curr_index, dest_index)` réordonne les champs de page sans changer le mode d'ordre.
Cet article présente trois exemples de code qui illustrent chacune de ces opérations sur un jeu de données partagé, afin que vous puissiez comparer les dispositions résultantes côte à côte.
## **Données source**
Les trois exemples ci-dessous chargent ces huit lignes de données de ventes dans une feuille de calcul nommée `PivotData`. Les données contiennent deux candidats au champ de page (`Year`, `Region`), un candidat au champ de ligne (`Fruit`) et une mesure (`Amount`), ce qui rend la bande des champs de page significative à inspecter.
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
Les huit lignes sont remplies dans chaque exemple de code, dans un ordre identique, de sorte que les données source ne diffèrent jamais d'un scénario à l'autre — seules les propriétés de disposition des champs de page changent.
## **Exemple 1 : Horizontal puis vertical**
Dans le premier scénario, nous configurons les deux champs de page (`Year`, `Region`) pour qu'ils apparaissent **côte à côte sur une seule ligne** en haut du tableau croisé dynamique. Nous affectons `Fruit` à l'axe des lignes, plaçons `Year` en premier et `Region` en deuxième sur l'axe des pages (l'ordre des appels à `add_field_to_area` détermine l'index de départ), ajoutons `Amount` (Sum) comme champ de données, puis définissons `page_field_order` à `PrintOrderType.OverThenDown` avec `page_field_wrap_count = 2`. Avec `OverThenDown` et un nombre de sauts de 2, les deux champs de page sont disposés horizontalement côte à côte sur une seule ligne en haut du tableau croisé dynamique, de sorte que la bande occupe une ligne d'une largeur de deux.
```python
import os
import aspose.cells as ac

data_dir = "output"
if not os.path.exists(data_dir):
    os.makedirs(data_dir, exist_ok=True)

workbook = ac.Workbook()
worksheets = workbook.worksheets

pivot_data_idx = worksheets.add("PivotData")
pivot_data_sheet = worksheets[pivot_data_idx]
pivot_data_cells = pivot_data_sheet.cells

# En-têtes (ligne 0)
pivot_data_cells[0, 0].put_value("Fruit")
pivot_data_cells[0, 1].put_value("Year")
pivot_data_cells[0, 2].put_value("Region")
pivot_data_cells[0, 3].put_value("Amount")

# Ligne 1 : Pomme, 2022, Nord, 150
pivot_data_cells[1, 0].put_value("Apple")
pivot_data_cells[1, 1].put_value(2022)
pivot_data_cells[1, 2].put_value("North")
pivot_data_cells[1, 3].put_value(150)

# Ligne 2 : Pomme, 2023, Nord, 180
pivot_data_cells[2, 0].put_value("Apple")
pivot_data_cells[2, 1].put_value(2023)
pivot_data_cells[2, 2].put_value("North")
pivot_data_cells[2, 3].put_value(180)

# Ligne 3 : Banane, 2022, Sud, 120
pivot_data_cells[3, 0].put_value("Banana")
pivot_data_cells[3, 1].put_value(2022)
pivot_data_cells[3, 2].put_value("South")
pivot_data_cells[3, 3].put_value(120)

# Ligne 4 : Banane, 2023, Sud, 140
pivot_data_cells[4, 0].put_value("Banana")
pivot_data_cells[4, 1].put_value(2023)
pivot_data_cells[4, 2].put_value("South")
pivot_data_cells[4, 3].put_value(140)

# Ligne 5 : Cerise, 2022, Est, 200
pivot_data_cells[5, 0].put_value("Cherry")
pivot_data_cells[5, 1].put_value(2022)
pivot_data_cells[5, 2].put_value("East")
pivot_data_cells[5, 3].put_value(200)

# Ligne 6 : Cerise, 2023, Est, 220
pivot_data_cells[6, 0].put_value("Cherry")
pivot_data_cells[6, 1].put_value(2023)
pivot_data_cells[6, 2].put_value("East")
pivot_data_cells[6, 3].put_value(220)

# Ligne 7 : Raisin, 2022, Ouest, 90
pivot_data_cells[7, 0].put_value("Grape")
pivot_data_cells[7, 1].put_value(2022)
pivot_data_cells[7, 2].put_value("West")
pivot_data_cells[7, 3].put_value(90)

# Ligne 8 : Raisin, 2023, Ouest, 110
pivot_data_cells[8, 0].put_value("Grape")
pivot_data_cells[8, 1].put_value(2023)
pivot_data_cells[8, 2].put_value("West")
pivot_data_cells[8, 3].put_value(110)

# Ajouter la feuille PivotTableReport
pivot_table_sheet_idx = worksheets.add("PivotTableReport")
pivot_table_sheet = worksheets[pivot_table_sheet_idx]
pivot_tables = pivot_table_sheet.pivot_tables

# Créer un tableau croisé dynamique à partir de PivotData!A1:D9 placé à A1 sur PivotTableReport
pivot_index = pivot_tables.add("PivotData!A1:D9", "A1", "PivotTable1")
pivot_table = pivot_tables[pivot_index]

# Ajouter des champs
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, 0)   # Fruit
pivot_table.add_field_to_area(ac.PivotFieldType.PAGE, 1)  # Année
pivot_table.add_field_to_area(ac.PivotFieldType.PAGE, 2)  # Région
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, 3)  # Montant
pivot_table.data_fields[0].function = ac.ConsolidationFunction.SUM

# Configurer la disposition de la zone des champs de page : placer les champs de page horizontalement d'abord, avec un retour à la ligne après chaque 2
pivot_table.page_field_order = ac.PrintOrderType.OVER_THEN_DOWN
pivot_table.page_field_wrap_count = 2

# Actualiser et calculer
pivot_table.calculate_data()

# Enregistrer
workbook.save(os.path.join(data_dir, "pageFieldLayout_overThenDown.xlsx"))
```
## **Exemple 2 : Vertical puis horizontal**
Dans cet exemple, nous plaçons `Fruit` sur l'axe des lignes, `Year` et `Region` sur l'axe des pages (avec `Year` en premier), et `Amount` (Sum) comme champ de données — exactement comme dans l'Exemple 1. Nous définissons ensuite `page_field_order` à `PrintOrderType.DownThenOver` et `page_field_wrap_count` à `2`. Avec `DownThenOver` et un nombre de sauts de 2, les deux champs de page sont empilés verticalement — `Year` en haut, `Region` directement en dessous — formant une seule colonne en haut du tableau croisé dynamique. La bande occupe donc deux lignes d'une largeur de un, contrairement à l'Exemple 1.
```python
import aspose.cells as ac

workbook = ac.Workbook()
pivot_data = workbook.worksheets[0]
pivot_data.name = "PivotData"
pivot_report_idx = workbook.worksheets.add("PivotTableReport")
pivot_report = workbook.worksheets[pivot_report_idx]

headers = ["Fruit", "Year", "Region", "Amount"]
for c in range(len(headers)):
    pivot_data.cells[0, c].put_value(headers[c])

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
        pivot_data.cells[r + 1, c].put_value(data[r][c])

idx = pivot_report.pivot_tables.add("PivotData!A1:D9", "A1", "PivotTable")
pivot_table = pivot_report.pivot_tables[idx]

pivot_table.add_field_to_area(ac.PivotFieldType.ROW, 0)
pivot_table.add_field_to_area(ac.PivotFieldType.PAGE, 1)
pivot_table.add_field_to_area(ac.PivotFieldType.PAGE, 2)
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, 3)

pivot_table.page_field_order = ac.PrintOrderType.DOWN_THEN_OVER
pivot_table.page_field_wrap_count = 2

pivot_table.calculate_data()

workbook.save("pageFieldLayout_downThenOver.xlsx")
```
## **Exemple 3 : Déplacer un champ de page**
Dans le troisième scénario, nous conservons ce jeu de données et cette allocation des champs, définissons une disposition neutre (`OverThenDown` avec un nombre de sauts de `2`), puis démontrons l'opération `page_fields.move`. L'appel `move(0, 1)` déplace le champ de page à l'index 0 (`Year`) à la position 1, et le champ de page qui était à la position 1 (`Region`) passe à la position 0. Après cet appel, `Region` est le premier champ de page et `Year` est le deuxième. Le mode d'ordre et le nombre de sauts restent inchangés, de sorte que la bande est toujours rendue horizontalement côte à côte — seul l'ordre des deux listes déroulantes a été inversé.
```python
import aspose.cells as ac

workbook = ac.Workbook()

data_sheet = workbook.worksheets[0]
data_sheet.name = "PivotData"

data_sheet.cells["A1"].put_value("Fruit")
data_sheet.cells["B1"].put_value("Year")
data_sheet.cells["C1"].put_value("Region")
data_sheet.cells["D1"].put_value("Amount")

data_sheet.cells["A2"].put_value("Apple")
data_sheet.cells["B2"].put_value(2022)
data_sheet.cells["C2"].put_value("North")
data_sheet.cells["D2"].put_value(150)

data_sheet.cells["A3"].put_value("Apple")
data_sheet.cells["B3"].put_value(2023)
data_sheet.cells["C3"].put_value("North")
data_sheet.cells["D3"].put_value(180)

data_sheet.cells["A4"].put_value("Banana")
data_sheet.cells["B4"].put_value(2022)
data_sheet.cells["C4"].put_value("South")
data_sheet.cells["D4"].put_value(120)

data_sheet.cells["A5"].put_value("Banana")
data_sheet.cells["B5"].put_value(2023)
data_sheet.cells["C5"].put_value("South")
data_sheet.cells["D5"].put_value(140)

data_sheet.cells["A6"].put_value("Cherry")
data_sheet.cells["B6"].put_value(2022)
data_sheet.cells["C6"].put_value("East")
data_sheet.cells["D6"].put_value(200)

data_sheet.cells["A7"].put_value("Cherry")
data_sheet.cells["B7"].put_value(2023)
data_sheet.cells["C7"].put_value("East")
data_sheet.cells["D7"].put_value(220)

data_sheet.cells["A8"].put_value("Grape")
data_sheet.cells["B8"].put_value(2022)
data_sheet.cells["C8"].put_value("West")
data_sheet.cells["D8"].put_value(90)

data_sheet.cells["A9"].put_value("Grape")
data_sheet.cells["B9"].put_value(2023)
data_sheet.cells["C9"].put_value("West")
data_sheet.cells["D9"].put_value(110)

pivot_sheet_idx = workbook.worksheets.add("PivotTableReport")
pivot_sheet = workbook.worksheets[pivot_sheet_idx]

pivot_idx = pivot_sheet.pivot_tables.add("PivotData!A1:D9", "A3", "PivotTable")
pivot_table = pivot_sheet.pivot_tables[pivot_idx]

pivot_table.add_field_to_area(ac.PivotFieldType.ROW, 0)
pivot_table.add_field_to_area(ac.PivotFieldType.PAGE, 1)
pivot_table.add_field_to_area(ac.PivotFieldType.PAGE, 2)
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, 3)

pivot_table.page_field_order = ac.PrintOrderType.OVER_THEN_DOWN
pivot_table.page_field_wrap_count = 2

pivot_table.page_fields.move(0, 1)

pivot_table.calculate_data()

workbook.save("pageFieldLayout_move.xlsx")
```
## **Articles connexes**
- [Ajouter un champ de page dans un tableau croisé dynamique](/cells/fr/python-net/add-page-field-in-pivot-table/) — la page parente qui présente comment les champs de page sont ajoutés à un tableau croisé dynamique.
- [Champs de lignes et de colonnes dans un tableau croisé dynamique](/cells/fr/python-net/row-and-column-fields/) — couvre l'affectation des champs aux axes des lignes et des colonnes, complétant le travail sur l'axe des pages présenté ici.
- [Gérer les champs de valeurs dans un tableau croisé dynamique](/cells/fr/python-net/manage-value-fields/) — décrit comment configurer la zone des données (valeurs), y compris l'agrégation `Sum` utilisée dans cet article.
- [Actualiser le tableau croisé dynamique](/cells/fr/python-net/refresh-pivot-table/) — explique `refresh_data` et `calculate_data`, qui sont requis après le réordonnancement des champs de page.
- [Appliquer un style au tableau croisé dynamique](/cells/fr/python-net/apply-style-to-pivot-table/) — montre comment formater le tableau croisé dynamique rendu après la disposition de la bande des champs de page.
{{< app/cells/assistant language="python-net" >}}