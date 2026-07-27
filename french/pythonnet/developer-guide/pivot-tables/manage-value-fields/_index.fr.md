---
title: Gérer les champs de valeur d'un tableau croisé dynamique dans Aspose.Cells pour .NET
linktitle: Champs de valeur
description: Apprenez à ajouter des champs de base à la zone de données d'un tableau croisé dynamique, à modifier la fonction de synthèse avec PivotField.function, et à tracer le champ de valeur sur l'axe Ligne ou Colonne dans Aspose.Cells for Python via .NET.
keywords: Aspose.Cells, Python via .NET, tableau croisé dynamique, champ de valeur, PivotField, PivotField.function, champ de données, PivotTable.values_field, Somme, Moyenne
type: docs
weight: 230
url: /fr/python-net/pivot-table-manage-value-fields/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## Ajout d'un champ à la zone de données
L'ajout d'un champ de base à la zone de données (valeur) est la première étape pour façonner la manière dont un tableau croisé dynamique agrège vos données sources. Aspose.Cells expose `PivotTable.add_field_to_area(PivotFieldType, str)`, une surcharge qui accepte la constante `PivotFieldType.DATA` et le nom de la colonne source. Une fois qu'un champ est ajouté à la zone de données, l'API l'expose via la collection `PivotTable.data_fields`, dans l'ordre dans lequel les champs ont été ajoutés. Par défaut, une colonne source numérique est résumée avec `ConsolidationFunction.SUM`, tandis qu'une colonne non numérique utilise `Count` par défaut.
## Modification de la fonction de synthèse
Chaque champ placé dans la zone de données est encapsulé en interne sous forme d'instance `PivotField`, et sa propriété `function` renvoie une valeur de l'énumération `ConsolidationFunction`. Le même setter `function` vous permet de basculer entre les agrégats disponibles, notamment `Sum`, `Count`, `Average`, `Max`, `Min`, `Product`, `StdDev`, `StdDevp`, `Var` et `Varp`.
{{% alert color="primary" %}}
La modification de `function` affecte uniquement l'agrégat, la colonne source ne change pas.
{{% /alert %}}
Vous pouvez donc laisser un champ de données en `Sum` tout en ajoutant un second champ de données ciblant la même colonne source mais utilisant `Count` ou `Average`, le tout dans un seul tableau croisé dynamique.
## Tracer les champs de valeur sur l'axe Ligne ou Colonne
Lorsqu'un tableau croisé dynamique contient au moins deux champs de données, Aspose.Cells expose un champ virtuel supplémentaire appelé `PivotTable.values_field`. Ce champ virtuel représente l'agrégat de chaque champ de données présent dans la zone de données. Vous pouvez le faire glisser dans la zone Ligne ou Colonne en tant que champ pivot de base, ce qui est utile pour disposer plusieurs mesures côte à côte.
{{% alert color="primary" %}}
`PivotTable.values_field` ne fonctionne pas s'il n'y a aucun ou un seul champ de valeur.
{{% /alert %}}
Les scénarios ci-dessous présentent trois exemples de bout en bout qui illustrent chaque fonctionnalité décrite ci-dessus sur la même structure de tableau croisé dynamique.
## Scénario 1 — Glisser un champ de base dans la zone Valeur
Ce scénario montre comment placer un seul champ de base (`Amount`) dans la zone de données d'un tableau croisé dynamique existant. La structure de tableau croisé dynamique partagée place `Category` et `Item` sur l'axe Ligne et `Year` sur l'axe Colonne. Après l'opération, `Amount` apparaît dans la zone de données et est calculé comme la `Sum` de `Amount` par défaut.
```python
from aspose.cells.pivot import PivotFieldType

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"

# En-têtes dans A1:D1
worksheet.cells[0, 0].put_value("Category")
worksheet.cells[0, 1].put_value("Item")
worksheet.cells[0, 2].put_value("Year")
worksheet.cells[0, 3].put_value("Amount")

# Lignes de données A2:D9 utilisant des boucles imbriquées avec branchement sur j
for i in range(1, 9):
    for j in range(4):
        if j == 0:
            worksheet.cells[i, j].put_value("Fruit" if i <= 4 else "Vegetable")
        elif j == 1:
            if i == 1 or i == 2:
                worksheet.cells[i, j].put_value("Apple")
            elif i == 3 or i == 4:
                worksheet.cells[i, j].put_value("Banana")
            elif i == 5 or i == 6:
                worksheet.cells[i, j].put_value("Carrot")
            else:
                worksheet.cells[i, j].put_value("Daikon")
        elif j == 2:
            worksheet.cells[i, j].put_value(2020 + ((i - 1) % 2))
        elif j == 3:
            if i == 1:
                worksheet.cells[i, j].put_value(100)
            elif i == 2:
                worksheet.cells[i, j].put_value(150)
            elif i == 3:
                worksheet.cells[i, j].put_value(80)
            elif i == 4:
                worksheet.cells[i, j].put_value(90)
            elif i == 5:
                worksheet.cells[i, j].put_value(50)
            elif i == 6:
                worksheet.cells[i, j].put_value(60)
            elif i == 7:
                worksheet.cells[i, j].put_value(40)
            else:
                worksheet.cells[i, j].put_value(45)

# Ajouter un tableau croisé dynamique à F3 avec le nom PivotTable1
pivot_index = worksheet.pivot_tables.add("A1:D9", "F3", "PivotTable1")
pivot_table = worksheet.pivot_tables[pivot_index]

# Disposition du tableau croisé : Category et Item en Ligne, Year en Colonne, Amount comme champ de données
pivot_table.add_field_to_area(PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")

pivot_table.calculate_data()
workbook.save("output_drag.xlsx")
```
## Scénario 2 — Modification de la fonction de synthèse
Ce scénario démarre à partir de la même structure de tableau croisé dynamique que le Scénario 1, mais ajoute le champ `Amount` deux fois à la zone de données. Les deux champs de données font référence à la même colonne source, toutefois le second champ est remplacé à l'aide du setter `PivotField.function` afin qu'il devienne `Count` au lieu du `Sum` par défaut.
```python
import aspose.cells as ac

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"

headers = ["Category", "Item", "Year", "Amount"]
for j in range(len(headers)):
    worksheet.cells[0, j].put_value(headers[j])

data = [
    ["Fruit",     "Apple",  2020, 100],
    ["Fruit",     "Apple",  2021, 150],
    ["Fruit",     "Banana", 2020,  80],
    ["Fruit",     "Banana", 2021,  90],
    ["Vegetable", "Carrot", 2020,  50],
    ["Vegetable", "Carrot", 2021,  60],
    ["Vegetable", "Daikon", 2020,  40],
    ["Vegetable", "Daikon", 2021,  45]
]

for i in range(len(data)):
    for j in range(len(data[i])):
        worksheet.cells[i + 1, j].put_value(data[i][j])

pivot_index = worksheet.pivot_tables.add("A1:D9", "F3", "PivotTable1")
pivot_table = worksheet.pivot_tables[pivot_index]

pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")

pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

count_field = pivot_table.data_fields[1]
count_field.function = ac.ConsolidationFunction.COUNT

pivot_table.calculate_data()

workbook.save("output_function.xlsx")
```
## Scénario 3 — Tracer les champs de valeur sur l'axe Ligne ou Colonne
Avec deux champs de données en place, `PivotTable.values_field` devient utilisable. Ce scénario fait glisser ce champ virtuel agrégé sur la zone Colonne afin que chaque mesure de la zone de données apparaisse comme son propre bloc de colonnes à côté de `Year`.
```python
import aspose.cells as ac

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"

headers = ["Category", "Item", "Year", "Amount"]
for j in range(len(headers)):
    worksheet.cells[0, j].put_value(headers[j])

data = [
    ["Fruit",     "Apple",  2020, 100],
    ["Fruit",     "Apple",  2021, 150],
    ["Fruit",     "Banana", 2020,  80],
    ["Fruit",     "Banana", 2021,  90],
    ["Vegetable", "Carrot", 2020,  50],
    ["Vegetable", "Carrot", 2021,  60],
    ["Vegetable", "Daikon", 2020,  40],
    ["Vegetable", "Daikon", 2021,  45]
]

for i in range(len(data)):
    for j in range(len(data[i])):
        worksheet.cells[i + 1, j].put_value(data[i][j])

pivot_index = worksheet.pivot_tables.add("A1:D9", "F3", "PivotTable1")
pivot_table = worksheet.pivot_tables[pivot_index]

pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")
pivot_table.data_fields[1].function = ac.ConsolidationFunction.COUNT

# Tracer les champs de valeurs sur l'axe des colonnes.
pivot_table.add_field_to_area(ac.PivotFieldType.COLUMN, pivot_table.values_field.name)

pivot_table.calculate_data()

workbook.save("output_plot.xlsx")
```
Ensemble, ces trois scénarios couvrent chaque aspect de la manipulation des champs de valeur dans Aspose.Cells for Python via .NET, d'un seul champ de données avec le `Sum` par défaut à un tableau croisé dynamique multi-mesures dans lequel le `ValuesField` virtuel contrôle la disposition sur l'axe Ligne ou Colonne.

{{< app/cells/assistant language="python" >}}
