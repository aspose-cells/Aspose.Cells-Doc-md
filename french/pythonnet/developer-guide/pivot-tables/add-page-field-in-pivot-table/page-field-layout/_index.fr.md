---
title: Modifier la disposition des champs de page dans un Tableau Croisé Dynamique
description: Découvrez comment contrôler la disposition de la zone des champs de page dans un Tableau Croisé Dynamique à l’aide d’Aspose.Cells for Python via .NET, notamment en définissant l’ordre d’affichage, le nombre de champs de page avant retour à la ligne et l’ordre des champs de page situés en haut du Tableau Croisé Dynamique.
linktitle: Modifier la disposition des champs de page dans un Tableau Croisé Dynamique
keywords: Aspose.Cells, bibliothèque Python via .NET, tableur, Tableau Croisé Dynamique, champ de page, ordre des champs de page, nombre de champs de page avant retour à la ligne, déplacement d’un champ de page
type: docs
weight: 191
url: /fr/python-net/change-page-field-layout/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Cet article fait suite au sujet **Ajouter un champ de page dans un Tableau Croisé Dynamique**. Il montre comment contrôler la disposition de la zone des champs de page — la bande de contrôles de filtre située en haut d’un Tableau Croisé Dynamique — notamment l’ordre d’affichage, le nombre de champs de page avant retour à la ligne et le réordonnancement des champs.
{{% /alert %}}

## **Introduction**
Un Tableau Croisé Dynamique dans Microsoft Excel expose une **zone dédiée aux champs de page**, située au-dessus du corps des lignes, des colonnes et des données du tableau. Cette zone est affichée sous forme d’une bande de contrôles de filtre déroulants, avec un contrôle par champ de page. Les utilisateurs finaux cliquent sur ces contrôles pour segmenter le Tableau Croisé Dynamique selon des critères tels que l’année ou la région. Aspose.Cells for Python via .NET modélise cette zone par le biais de la collection `pivot_table.page_fields` et expose trois propriétés qui contrôlent sa disposition visuelle :
- `pivot_table.page_field_order` (une valeur `PrintOrderType`) détermine si les champs de page supplémentaires sont placés *à côté* des champs existants ou *en dessous*.
- `pivot_table.page_field_wrap_count` définit le nombre de champs de page placés dans chaque ligne ou colonne avant le retour à la ligne.
- `pivot_table.page_fields.move(curr_index, dest_index)` réordonne les champs de page sans modifier le mode d’ordre.
Cet article présente trois exemples de code qui illustrent chacune de ces opérations sur un jeu de données commun, afin de comparer les dispositions obtenues côte à côte.

## **Données source**
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
Les huit lignes sont renseignées dans chaque exemple de code, dans le même ordre, de sorte que les données source ne varient jamais entre les scénarios ; seules les propriétés de disposition des champs de page diffèrent.

## **Exemple 1 : Côte à côte, puis en dessous**
Dans le premier scénario, nous configurons les deux champs de page (`Year`, `Region`) afin qu’ils apparaissent **côte à côte sur une seule ligne** en haut du Tableau Croisé Dynamique. Nous attribuons `Fruit` à l’axe des lignes, plaçons `Year` en premier et `Region` en second sur l’axe des pages (l’ordre des appels `add_field_to_area` détermine l’index initial), ajoutons `Amount` (`Sum`) comme champ de données, puis définissons `page_field_order` sur `PrintOrderType.OVER_THEN_DOWN` et `page_field_wrap_count = 2`. Avec `OverThenDown` et un nombre de champs de page avant retour à la ligne de 2, les deux champs de page sont disposés horizontalement, côte à côte sur une seule ligne en haut du Tableau Croisé Dynamique. La bande occupe donc une ligne d’une largeur de deux cellules.

```python
import os
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
data_dir = "output"
if not os.path.exists(data_dir):
    os.makedirs(data_dir, exist_ok=True)
workbook = ac.Workbook()
worksheets = workbook.worksheets
pivot_data_sheet = worksheets.add("PivotData")
pivot_data_cells = pivot_data_sheet.cells
# Headers (row 0)
pivot_data_cells.get(0, 0).put_value("Fruit")
pivot_data_cells.get(0, 1).put_value("Year")
pivot_data_cells.get(0, 2).put_value("Region")
pivot_data_cells.get(0, 3).put_value("Amount")
# Row 1: Apple, 2022, North, 150
pivot_data_cells.get(1, 0).put_value("Apple")
pivot_data_cells.get(1, 1).put_value(2022)
pivot_data_cells.get(1, 2).put_value("North")
pivot_data_cells.get(1, 3).put_value(150)
# Row 2: Apple, 2023, North, 180
pivot_data_cells.get(2, 0).put_value("Apple")
pivot_data_cells.get(2, 1).put_value(2023)
pivot_data_cells.get(2, 2).put_value("North")
pivot_data_cells.get(2, 3).put_value(180)
# Row 3: Banana, 2022, South, 120
pivot_data_cells.get(3, 0).put_value("Banana")
pivot_data_cells.get(3, 1).put_value(2022)
pivot_data_cells.get(3, 2).put_value("South")
pivot_data_cells.get(3, 3).put_value(120)
# Row 4: Banana, 2023, South, 140
pivot_data_cells.get(4, 0).put_value("Banana")
pivot_data_cells.get(4, 1).put_value(2023)
pivot_data_cells.get(4, 2).put_value("South")
pivot_data_cells.get(4, 3).put_value(140)
# Row 5: Cherry, 2022, East, 200
pivot_data_cells.get(5, 0).put_value("Cherry")
pivot_data_cells.get(5, 1).put_value(2022)
pivot_data_cells.get(5, 2).put_value("East")
pivot_data_cells.get(5, 3).put_value(200)
# Row 6: Cherry, 2023, East, 220
pivot_data_cells.get(6, 0).put_value("Cherry")
pivot_data_cells.get(6, 1).put_value(2023)
pivot_data_cells.get(6, 2).put_value("East")
pivot_data_cells.get(6, 3).put_value(220)
# Row 7: Grape, 2022, West, 90
pivot_data_cells.get(7, 0).put_value("Grape")
pivot_data_cells.get(7, 1).put_value(2022)
pivot_data_cells.get(7, 2).put_value("West")
pivot_data_cells.get(7, 3).put_value(90)
# Row 8: Grape, 2023, West, 110
pivot_data_cells.get(8, 0).put_value("Grape")
pivot_data_cells.get(8, 1).put_value(2023)
pivot_data_cells.get(8, 2).put_value("West")
pivot_data_cells.get(8, 3).put_value(110)
# Add PivotTableReport sheet
pivot_table_sheet = worksheets.add("PivotTableReport")
pivot_tables = pivot_table_sheet.pivot_tables
# Create pivot table sourced from PivotData!A1:D9 placed at A1 on PivotTableReport
pivot_table = pivot_tables.add("PivotData!A1:D9", 0, 0)
# Add fields
pivot_table.add_field_to_area(PivotFieldType.ROW, 0)   # Fruit
pivot_table.add_field_to_area(PivotFieldType.PAGE, 1)  # Year
pivot_table.add_field_to_area(PivotFieldType.PAGE, 2)  # Region
pivot_table.add_field_to_area(PivotFieldType.DATA, 3)  # Amount
pivot_table.data_fields[0].function = ac.ConsolidationFunction.SUM
# Configure page field area layout: place page fields across first, wrap after every 2
pivot_table.page_field_order = ac.PrintOrderType.OVER_THEN_DOWN
pivot_table.page_field_wrap_count = 2
# Refresh and calculate
pivot_table.calculate_data()
# Save
workbook.save(os.path.join(data_dir, "pageFieldLayout_overThenDown.xlsx"))
```

## **Exemple 2 : En dessous, puis à côté**
Dans cet exemple, nous plaçons `Fruit` sur l’axe des lignes, `Year` et `Region` sur l’axe des pages (avec `Year` en premier), et `Amount` (`Sum`) comme champ de données — exactement comme dans l’exemple 1. Nous définissons ensuite `page_field_order` sur `PrintOrderType.DOWN_THEN_OVER` et `page_field_wrap_count` sur `2`. Avec `DownThenOver` et un nombre de champs de page avant retour à la ligne de 2, les deux champs de page sont empilés verticalement — `Year` en haut et `Region` juste en dessous — afin de former une seule colonne en haut du Tableau Croisé Dynamique. La bande occupe donc deux lignes d’une largeur d’une cellule, contrairement à l’exemple 1.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
workbook = ac.Workbook()
pivot_data = workbook.worksheets[0]
pivot_data.name = "PivotData"
pivot_report = workbook.worksheets.add("PivotTableReport")
headers = ["Fruit", "Year", "Region", "Amount"]
for c in range(len(headers)):
    pivot_data.cells.get(0, c).put_value(headers[c])
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
        pivot_data.cells.get(r + 1, c).put_value(data[r][c])
pivot_table = pivot_report.pivot_tables.add("PivotData!A1:D9", 0, 0)
pivot_table.add_field_to_area(PivotFieldType.ROW, 0)
pivot_table.add_field_to_area(PivotFieldType.PAGE, 1)
pivot_table.add_field_to_area(PivotFieldType.PAGE, 2)
pivot_table.add_field_to_area(PivotFieldType.DATA, 3)
pivot_table.page_field_order = ac.PrintOrderType.DOWN_THEN_OVER
pivot_table.page_field_wrap_count = 2
pivot_table.calculate_data()
workbook.save("pageFieldLayout_downThenOver.xlsx")
```

## **Exemple 3 : Déplacer un champ de page**
Dans le troisième scénario, nous conservons ce jeu de données et cette répartition des champs, définissons une disposition neutre (`OverThenDown` avec un nombre de champs de page avant retour à la ligne de `2`), puis démontrons l’opération `page_fields.move`. L’appel `move(0, 1)` déplace le champ de page situé à l’index 0 (`Year`) vers la position 1, et le champ de page qui se trouvait à la position 1 (`Region`) passe à la position 0. Après cet appel, `Region` est le premier champ de page et `Year` le second. Le mode de retour à la ligne et d’ordre reste inchangé ; la bande est donc toujours affichée horizontalement, côte à côte, et seul l’ordre des deux listes déroulantes a été inversé.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
workbook = ac.Workbook()
data_sheet = workbook.worksheets[0]
data_sheet.name = "PivotData"
data_sheet.cells.get("A1").put_value("Fruit")
data_sheet.cells.get("B1").put_value("Year")
data_sheet.cells.get("C1").put_value("Region")
data_sheet.cells.get("D1").put_value("Amount")
data_sheet.cells.get("A2").put_value("Apple")
data_sheet.cells.get("B2").put_value(2022)
data_sheet.cells.get("C2").put_value("North")
data_sheet.cells.get("D2").put_value(150)
data_sheet.cells.get("A3").put_value("Apple")
data_sheet.cells.get("B3").put_value(2023)
data_sheet.cells.get("C3").put_value("North")
data_sheet.cells.get("D3").put_value(180)
data_sheet.cells.get("A4").put_value("Banana")
data_sheet.cells.get("B4").put_value(2022)
data_sheet.cells.get("C4").put_value("South")
data_sheet.cells.get("D4").put_value(120)
data_sheet.cells.get("A5").put_value("Banana")
data_sheet.cells.get("B5").put_value(2023)
data_sheet.cells.get("C5").put_value("South")
data_sheet.cells.get("D5").put_value(140)
data_sheet.cells.get("A6").put_value("Cherry")
data_sheet.cells.get("B6").put_value(2022)
data_sheet.cells.get("C6").put_value("East")
data_sheet.cells.get("D6").put_value(200)
data_sheet.cells.get("A7").put_value("Cherry")
data_sheet.cells.get("B7").put_value(2023)
data_sheet.cells.get("C7").put_value("East")
data_sheet.cells.get("D7").put_value(220)
data_sheet.cells.get("A8").put_value("Grape")
data_sheet.cells.get("B8").put_value(2022)
data_sheet.cells.get("C8").put_value("West")
data_sheet.cells.get("D8").put_value(90)
data_sheet.cells.get("A9").put_value("Grape")
data_sheet.cells.get("B9").put_value(2023)
data_sheet.cells.get("C9").put_value("West")
data_sheet.cells.get("D9").put_value(110)
pivot_sheet = workbook.worksheets.add("PivotTableReport")
pivot_table = pivot_sheet.pivot_tables.add("PivotData!A1:D9", 2, 0)
pivot_table.add_field_to_area(PivotFieldType.ROW, 0)
pivot_table.add_field_to_area(PivotFieldType.PAGE, 1)
pivot_table.add_field_to_area(PivotFieldType.PAGE, 2)
pivot_table.add_field_to_area(PivotFieldType.DATA, 3)
pivot_table.page_field_order = ac.PrintOrderType.OVER_THEN_DOWN
pivot_table.page_field_wrap_count = 2
pivot_table.page_fields.move(0, 1)
pivot_table.calculate_data()
workbook.save("pageFieldLayout_move.xlsx")
```

## **Articles associés**
- [Ajouter un champ de page dans un Tableau Croisé Dynamique](/cells/fr/python-net/add-page-field-in-pivot-table/) — la page parente qui présente l’ajout de champs de page à un Tableau Croisé Dynamique.
- [Champs de ligne et de colonne dans un Tableau Croisé Dynamique](/cells/fr/python-net/row-and-column-fields/) — explique l’attribution de champs aux axes des lignes et des colonnes en complément du travail sur l’axe des pages présenté ici.
- [Gérer les champs de valeur dans un Tableau Croisé Dynamique](/cells/fr/python-net/manage-value-fields/) — décrit comment configurer la zone de données ou des valeurs, notamment l’agrégation `Sum` utilisée dans cet article.
- [Actualiser un Tableau Croisé Dynamique](/cells/fr/python-net/refresh-pivot-table/) — explique `refresh_data` et `calculate_data`, qui sont nécessaires après le réordonnancement des champs de page.
- [Appliquer un style à un Tableau Croisé Dynamique](/cells/fr/python-net/apply-style-to-pivot-table/) — montre comment mettre en forme le Tableau Croisé Dynamique après la disposition de la bande des champs de page.

{{< app/cells/assistant language="python-net" >}}