---
title: Champs de valeurs dans Aspose.Cells for Python via Java
linktitle: Champs de valeurs dans Aspose.Cells for Python via Java
description: Apprenez à ajouter des champs de base à la zone des données d'un tableau croisé dynamique, à modifier la fonction de synthèse avec PivotField.Function, et à placer le champ de valeur sur l'axe Ligne ou Colonne dans Aspose.Cells for Python via Java.
keywords: Aspose.Cells, Python via Java, tableau croisé dynamique, champ de valeur, PivotField, PivotField.Function, champ de données, PivotTable.ValuesField, Sum, Average
type: docs
weight: 230
url: /fr/python-java/manage-value-fields/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## Ajouter un champ à la zone des données
L'ajout d'un champ de base à la zone des données (valeurs) est la première étape pour façonner la manière dont un tableau croisé dynamique agrège vos données sources. Aspose.Cells expose `PivotTable.addFieldToArea(PivotFieldType, string)`, une surcharge qui accepte la constante `PivotFieldType.DATA` et le nom de la colonne source. Une fois qu'un champ est ajouté à la zone des données, l'API l'expose via la collection `PivotTable.DataFields`, dans l'ordre dans lequel les champs ont été ajoutés. Par défaut, une colonne source numérique est synthétisée avec `ConsolidationFunction.SUM`, tandis qu'une colonne non numérique est définie par défaut sur `COUNT`.
## Modifier la fonction de synthèse
Chaque champ placé dans la zone des données est encapsulé en interne en tant qu'instance de `PivotField`, et sa propriété `Function` renvoie une valeur de l'énumération `ConsolidationFunction`. Le même setter `Function` vous permet de basculer entre les agrégats disponibles, notamment `SUM`, `COUNT`, `AVERAGE`, `MAX`, `MIN`, `PRODUCT`, `STDDEV`, `STDDEVP`, `VAR` et `VARP`.
{{% alert color="primary" %}}
La modification de `Function` n'affecte que l'agrégat, la colonne source ne change pas.
{{% /alert %}}
Vous pouvez donc laisser un champ de données en tant que `SUM` tout en ajoutant un second champ de données qui cible la même colonne source mais utilise `COUNT` ou `AVERAGE`, le tout dans un seul tableau croisé dynamique.
## Placer les champs de valeurs sur l'axe Ligne ou Colonne
Lorsqu'un tableau croisé dynamique contient deux champs de données ou plus, Aspose.Cells expose un champ virtuel supplémentaire appelé `PivotTable.ValuesField`. Ce champ virtuel représente l'agrégat de chaque champ de données présent dans la zone des données. Vous pouvez le faire glisser dans la zone Ligne ou Colonne en tant que champ de base du tableau croisé dynamique, ce qui est utile pour disposer plusieurs mesures côte à côte.
{{% alert color="primary" %}}
`PivotTable.ValuesField` ne fonctionne pas s'il n'y a aucun champ de valeur ou seulement un.
{{% /alert %}}
Les scénarios ci-dessous présentent trois exemples de bout en bout qui démontrent chaque capacité décrite ci-dessus sur la même structure de tableau croisé dynamique.
## Scénario 1 — Glisser un champ de base dans la zone des valeurs
Ce scénario montre comment placer un seul champ de base (`Amount`) dans la zone des données d'un tableau croisé dynamique existant. La structure partagée du tableau croisé dynamique place `Category` et `Item` sur l'axe Ligne et `Year` sur l'axe Colonne. Après l'opération, `Amount` apparaît dans la zone des données et est calculé comme la `Sum` de `Amount` par défaut.
```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"

headers = ["Category", "Item", "Year", "Amount"]
for j, h in enumerate(headers):
    worksheet.cells.get(0, j).put_value(h)

data = [
    ["Fruit",     "Apple",  2020, 100],
    ["Fruit",     "Apple",  2021, 150],
    ["Fruit",     "Banana", 2020,  80],
    ["Fruit",     "Banana", 2021,  90],
    ["Vegetable", "Carrot", 2020,  50],
    ["Vegetable", "Carrot", 2021,  60],
    ["Vegetable", "Daikon", 2020,  40],
    ["Vegetable", "Daikon", 2021,  45],
]
for i, row in enumerate(data):
    for j, val in enumerate(row):
        worksheet.cells.get(i + 1, j).put_value(val)

pivot_index = worksheet.pivot_tables.add("A1:D9", "F3", "PivotTable1")
pivot_table = worksheet.pivot_tables[pivot_index]
pivot_table.add_field_to_area(PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")

pivot_table.calculate_data()
workbook.save("output_drag.xlsx")
```
## Scénario 2 — Modifier la fonction de synthèse
Ce scénario part de la même structure de tableau croisé dynamique que le scénario 1 mais ajoute le champ `Amount` à la zone des données deux fois. Les deux champs de données référencent la même colonne source, mais le second champ est écrasé à l'aide du setter `PivotField.Function` pour qu'il devienne `Count` au lieu de la `Sum` par défaut.
```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType, ConsolidationFunction

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"

headers = ["Category", "Item", "Year", "Amount"]
for j, h in enumerate(headers):
    worksheet.cells.get(0, j).put_value(h)

data = [
    ["Fruit",     "Apple",  2020, 100],
    ["Fruit",     "Apple",  2021, 150],
    ["Fruit",     "Banana", 2020,  80],
    ["Fruit",     "Banana", 2021,  90],
    ["Vegetable", "Carrot", 2020,  50],
    ["Vegetable", "Carrot", 2021,  60],
    ["Vegetable", "Daikon", 2020,  40],
    ["Vegetable", "Daikon", 2021,  45],
]
for i, row in enumerate(data):
    for j, val in enumerate(row):
        worksheet.cells.get(i + 1, j).put_value(val)

pivot_index = worksheet.pivot_tables.add("A1:D9", "F3", "PivotTable1")
pivot_table = worksheet.pivot_tables[pivot_index]
pivot_table.add_field_to_area(PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.data_fields[1].function = ConsolidationFunction.COUNT

pivot_table.calculate_data()
workbook.save("output_function.xlsx")
```
## Scénario 3 — Placer les champs de valeurs sur l'axe Ligne ou Colonne
Avec deux champs de données en place, `PivotTable.ValuesField` devient utilisable. Ce scénario fait glisser ce champ virtuel d'agrégat sur la zone Colonne afin que chaque mesure dans la zone des données apparaisse comme son propre bloc de colonnes à côté de `Year`.
```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType, ConsolidationFunction

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"

headers = ["Category", "Item", "Year", "Amount"]
for j, h in enumerate(headers):
    worksheet.cells.get(0, j).put_value(h)

data = [
    ["Fruit",     "Apple",  2020, 100],
    ["Fruit",     "Apple",  2021, 150],
    ["Fruit",     "Banana", 2020,  80],
    ["Fruit",     "Banana", 2021,  90],
    ["Vegetable", "Carrot", 2020,  50],
    ["Vegetable", "Carrot", 2021,  60],
    ["Vegetable", "Daikon", 2020,  40],
    ["Vegetable", "Daikon", 2021,  45],
]
for i, row in enumerate(data):
    for j, val in enumerate(row):
        worksheet.cells.get(i + 1, j).put_value(val)

pivot_index = worksheet.pivot_tables.add("A1:D9", "F3", "PivotTable1")
pivot_table = worksheet.pivot_tables[pivot_index]
pivot_table.add_field_to_area(PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.data_fields[1].function = ConsolidationFunction.COUNT
pivot_table.add_field_to_area(PivotFieldType.COLUMN, pivot_table.values_field.name)

pivot_table.calculate_data()
workbook.save("output_plot.xlsx")
```
Ensemble, ces trois scénarios couvrent tous les aspects de la manipulation des champs de valeurs dans Aspose.Cells for Python via Java, d'un seul champ de données avec la `Sum` par défaut à un tableau croisé dynamique multi-mesures dans lequel le `ValuesField` virtuel contrôle la disposition sur l'axe Ligne ou Colonne.
## Articles connexes
- [Champs de ligne et de colonne de tableau croisé dynamique dans Aspose.Cells for Python via Java](/cells/fr/python-java/row-and-column-fields/)
- [Champs de page dans les tableaux croisés dynamiques](/cells/fr/python-java/add-page-field-in-pivot-table/)
- [Actualisation des tableaux croisés dynamiques dans Aspose.Cells for Python via Java](/cells/fr/python-java/refresh-pivot-table/)
- [Application de styles aux tableaux croisés dynamiques](/cells/fr/python-java/apply-style-to-pivot-table/)
{{< app/cells/assistant language="python" >}}
