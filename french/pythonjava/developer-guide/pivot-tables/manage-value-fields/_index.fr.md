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

pivot_index = worksheet.pivot_tables.add("A1:D9", "F3", "PivotTable1", True, False)
pivot_table = worksheet.pivot_tables[pivot_index]
pivot_table.add_field_to_area(PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")

pivot_table.calculate_data()
workbook.save("output_drag.xlsx")
```

## Modifier la fonction de synthèse
Chaque champ placé dans la zone des données est encapsulé en interne en tant qu'instance de `PivotField`, et sa propriété `Function` renvoie une valeur de l'énumération `ConsolidationFunction`. Le même setter `Function` vous permet de basculer entre les agrégats disponibles, notamment `SUM`, `COUNT`, `AVERAGE`, `MAX`, `MIN`, `PRODUCT`, `STDDEV`, `STDDEVP`, `VAR` et `VARP`.
{{% alert color="primary" %}}
La modification de `Function` n'affecte que l'agrégat, la colonne source ne change pas.
{{% /alert %}}
Vous pouvez donc laisser un champ de données en tant que `SUM` tout en ajoutant un second champ de données qui cible la même colonne source mais utilise `COUNT` ou `AVERAGE`, le tout dans un seul tableau croisé dynamique.

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

pivot_index = worksheet.pivot_tables.add("A1:D9", "F3", "PivotTable1", True, False)
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

## Placer les champs de valeurs sur l'axe Ligne ou Colonne
Lorsqu'un tableau croisé dynamique contient deux champs de données ou plus, Aspose.Cells expose un champ virtuel supplémentaire appelé `PivotTable.ValuesField`. Ce champ virtuel représente l'agrégat de chaque champ de données présent dans la zone des données. Vous pouvez le faire glisser dans la zone Ligne ou Colonne en tant que champ de base du tableau croisé dynamique, ce qui est utile pour disposer plusieurs mesures côte à côte.
{{% alert color="primary" %}}
`PivotTable.ValuesField` ne fonctionne pas s'il n'y a aucun champ de valeur ou seulement un.
{{% /alert %}}
Les scénarios ci-dessous présentent trois exemples de bout en bout qui démontrent chaque capacité décrite ci-dessus sur la même structure de tableau croisé dynamique.

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

pivot_index = worksheet.pivot_tables.add("A1:D9", "F3", "PivotTable1", True, False)
pivot_table = worksheet.pivot_tables[pivot_index]
pivot_table.add_field_to_area(PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.data_fields[1].function = ConsolidationFunction.COUNT
pivot_table.add_field_to_area(PivotFieldType.COLUMN, pivot_table.values_field)

pivot_table.calculate_data()
workbook.save("output_plot.xlsx")
```

{{< app/cells/assistant language="python" >}}