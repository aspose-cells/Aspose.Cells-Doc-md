---
title: Ajouter des champs de ligne et de colonne à un tableau croisé dynamique dans Aspose.Cells pour .NET
linktitle: Champs de ligne et de colonne
description: Apprenez à ajouter des champs de base aux zones de ligne et de colonne d'un tableau croisé dynamique et à contrôler les sous-totaux des champs croisés à l'aide de PivotField.set_subtotals dans Aspose.Cells for Python via .NET.
keywords: Aspose.Cells, Python via .NET, tableau croisé dynamique, champ de ligne, champ de colonne, PivotField, set_subtotals, PivotFieldSubtotalType, sous-totaux
type: docs
weight: 220
url: /fr/python-net/pivot-table-add-row-column-fields/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Ajout d'un champ à la zone de ligne ou de colonne**

La méthode `PivotTable.add_field_to_area(PivotFieldType field_type, string field_name)` déplace un champ de base depuis les données sources vers l'une des quatre zones du tableau croisé dynamique. L'argument `field_type` accepte l'une des valeurs `PivotFieldType` suivantes.

- `ROW` — champs placés verticalement à gauche
- `COLUMN` — champs placés horizontalement en haut
- `DATA` — champs dont les valeurs sont agrégées
- `PAGE` — champs utilisés comme filtres de rapport

Une fois les champs ajoutés, vous pouvez y accéder via les propriétés `PivotTable.row_fields` et `PivotTable.column_fields`. Chaque propriété renvoie une `PivotFieldCollection`. Le champ à l'index 0 de `row_fields` est le champ de ligne le plus externe, et les indices suivants représentent les champs imbriqués à l'intérieur. La même convention d'indexation s'applique à `column_fields`.

L'ordre d'imbrication des champs est important. Ajouter `Category` à la zone de ligne en premier, puis `Item`, produit un tableau croisé dont le regroupement externe est `Category` et le regroupement interne est `Item`. Inverser l'ordre inverse la hiérarchie.

## **Sous-totaux des champs croisés**

La méthode `PivotField.set_subtotals(PivotFieldSubtotalType subtotal_type, bool shown)` contrôle quelles lignes de sous-totaux apparaissent pour un champ croisé. Chaque appel active ou désactive un seul type de sous-total indépendamment. Passer `shown = True` affiche le sous-total, tandis que `shown = False` le masque. Comme chaque appel n'affecte qu'un seul type, appeler la méthode plusieurs fois avec différentes valeurs de `subtotal_type` permet de construire un sous-ensemble personnalisé de sous-totaux.

L'énumération `PivotFieldSubtotalType` définit les types de sous-totaux disponibles.

- `AUTOMATIC` — Aspose.Cells choisit la sélection par défaut (généralement `SUM` pour les champs numériques)
- `NONE` — supprimer toutes les lignes de sous-total
- `SUM`
- `COUNT`
- `AVERAGE`
- `MAX`
- `MIN`
- `PRODUCT`
- `STDDEV`
- `STDDEVP`
- `VAR`
- `VARP`

{{% alert color="primary" %}}
Les sous-totaux ne s'affichent que lorsqu'il y a deux champs croisés ou plus dans la zone de ligne (ou dans la zone de colonne). Un seul champ n'a rien de significatif à sous-totaliser entre les groupes, donc les appels à `set_subtotals` n'ont aucun effet visible dans ce cas. Par conséquent, cet article place deux champs de ligne (`Category` externe, `Item` interne) dans chaque exemple afin que la limite de sous-total entre chaque groupe `Category` soit visible.
{{% /alert %}}

## **Scénario 1 — Sous-totaux automatiques (par défaut)**

Lorsque vous n'appelez pas du tout `set_subtotals`, Aspose.Cells applique la sélection `AUTOMATIC` aux champs numériques. L'exemple suivant confirme explicitement ce comportement en appelant `set_subtotals(PivotFieldSubtotalType.AUTOMATIC, True)` sur le champ de ligne externe `Category`.

```python
import aspose.cells as ac

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"

worksheet.cells[0, 0].put_value("Category")
worksheet.cells[0, 1].put_value("Item")
worksheet.cells[0, 2].put_value("Year")
worksheet.cells[0, 3].put_value("Amount")

worksheet.cells[1, 0].put_value("Fruit")
worksheet.cells[1, 1].put_value("Apple")
worksheet.cells[1, 2].put_value(2020)
worksheet.cells[1, 3].put_value(100)

worksheet.cells[2, 0].put_value("Fruit")
worksheet.cells[2, 1].put_value("Apple")
worksheet.cells[2, 2].put_value(2021)
worksheet.cells[2, 3].put_value(150)

worksheet.cells[3, 0].put_value("Fruit")
worksheet.cells[3, 1].put_value("Banana")
worksheet.cells[3, 2].put_value(2020)
worksheet.cells[3, 3].put_value(80)

worksheet.cells[4, 0].put_value("Fruit")
worksheet.cells[4, 1].put_value("Banana")
worksheet.cells[4, 2].put_value(2021)
worksheet.cells[4, 3].put_value(90)

worksheet.cells[5, 0].put_value("Vegetable")
worksheet.cells[5, 1].put_value("Carrot")
worksheet.cells[5, 2].put_value(2020)
worksheet.cells[5, 3].put_value(50)

worksheet.cells[6, 0].put_value("Vegetable")
worksheet.cells[6, 1].put_value("Carrot")
worksheet.cells[6, 2].put_value(2021)
worksheet.cells[6, 3].put_value(60)

worksheet.cells[7, 0].put_value("Vegetable")
worksheet.cells[7, 1].put_value("Daikon")
worksheet.cells[7, 2].put_value(2020)
worksheet.cells[7, 3].put_value(40)

worksheet.cells[8, 0].put_value("Vegetable")
worksheet.cells[8, 1].put_value("Daikon")
worksheet.cells[8, 2].put_value(2021)
worksheet.cells[8, 3].put_value(45)

pivot_index = worksheet.pivot_tables.add("A1:D9", "F3", "PivotTable1")
pivot_table = worksheet.pivot_tables[pivot_index]

pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

category_field = pivot_table.row_fields[0]
category_field.set_subtotals(ac.PivotFieldSubtotalType.AUTOMATIC, True)

pivot_table.calculate_data()

workbook.save("output_automatic.xlsx")
```

## **Scénario 2 — Suppression de tous les sous-totaux (None)**

Appeler `set_subtotals(PivotFieldSubtotalType.NONE, True)` supprime chaque ligne de sous-total du tableau croisé, ne laissant que les lignes de champ et le total général en bas. Cela est utile lorsque vous souhaitez les données regroupées brutes sans aucune ligne de synthèse.

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
    ["Fruit",     "Banana", 2020, 80],
    ["Fruit",     "Banana", 2021, 90],
    ["Vegetable", "Carrot", 2020, 50],
    ["Vegetable", "Carrot", 2021, 60],
    ["Vegetable", "Daikon", 2020, 40],
    ["Vegetable", "Daikon", 2021, 45],
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

category_field = pivot_table.row_fields[0]
for st in [ac.PivotFieldSubtotalType.SUM, ac.PivotFieldSubtotalType.COUNT, ac.PivotFieldSubtotalType.AVERAGE, ac.PivotFieldSubtotalType.MAX, ac.PivotFieldSubtotalType.MIN, ac.PivotFieldSubtotalType.PRODUCT]:
    category_field.set_subtotals(st, True)
pivot_table.calculate_data()

workbook.save("output_none.xlsx")
```

## **Scénario 3 — Sous-ensemble personnalisé de sous-totaux (Sum + Average)**

Vous n'êtes pas limité à un seul type de sous-total. Chaque appel à `set_subtotals` opère indépendamment sur un seul type, donc appeler la méthode deux fois — une fois avec `SUM` et une fois avec `AVERAGE` — produit un sous-ensemble personnalisé de deux lignes de sous-total pour chaque groupe `Category`.

```python
import aspose.cells as ac

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"

worksheet.cells["A1"].put_value("Category")
worksheet.cells["B1"].put_value("Item")
worksheet.cells["C1"].put_value("Year")
worksheet.cells["D1"].put_value("Amount")

worksheet.cells[1, 0].put_value("Fruit")
worksheet.cells[1, 1].put_value("Apple")
worksheet.cells[1, 2].put_value(2020)
worksheet.cells[1, 3].put_value(100)

worksheet.cells[2, 0].put_value("Fruit")
worksheet.cells[2, 1].put_value("Apple")
worksheet.cells[2, 2].put_value(2021)
worksheet.cells[2, 3].put_value(150)

worksheet.cells[3, 0].put_value("Fruit")
worksheet.cells[3, 1].put_value("Banana")
worksheet.cells[3, 2].put_value(2020)
worksheet.cells[3, 3].put_value(80)

worksheet.cells[4, 0].put_value("Fruit")
worksheet.cells[4, 1].put_value("Banana")
worksheet.cells[4, 2].put_value(2021)
worksheet.cells[4, 3].put_value(90)

worksheet.cells[5, 0].put_value("Vegetable")
worksheet.cells[5, 1].put_value("Carrot")
worksheet.cells[5, 2].put_value(2020)
worksheet.cells[5, 3].put_value(50)

worksheet.cells[6, 0].put_value("Vegetable")
worksheet.cells[6, 1].put_value("Carrot")
worksheet.cells[6, 2].put_value(2021)
worksheet.cells[6, 3].put_value(60)

worksheet.cells[7, 0].put_value("Vegetable")
worksheet.cells[7, 1].put_value("Daikon")
worksheet.cells[7, 2].put_value(2020)
worksheet.cells[7, 3].put_value(40)

worksheet.cells[8, 0].put_value("Vegetable")
worksheet.cells[8, 1].put_value("Daikon")
worksheet.cells[8, 2].put_value(2021)
worksheet.cells[8, 3].put_value(45)

pivot_tables = worksheet.pivot_tables
pivot_index = pivot_tables.add("A1:D9", "F3", "PivotTable1")
pivot_table = pivot_tables[pivot_index]

pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

category_field = pivot_table.row_fields[0]
category_field.set_subtotals(ac.PivotFieldSubtotalType.SUM, True)
category_field.set_subtotals(ac.PivotFieldSubtotalType.AVERAGE, True)

pivot_table.calculate_data()

workbook.save("output_custom.xlsx")
```

## **Récapitulatif**

Les trois scénarios ci-dessus partagent le même jeu de données et la même structure de tableau croisé dynamique. La seule différence entre eux est l'appel à `set_subtotals` appliqué au champ de ligne externe `Category`. Rappelez-vous la règle des deux champs : un seul champ dans une zone n'a rien à sous-totaliser, donc placez toujours au moins deux champs dans la zone de ligne ou de colonne lorsque vous souhaitez que `set_subtotals` ait un effet visible.

## **Articles connexes**

- [Champs de page dans les tableaux croisés dynamiques](/cells/fr/python-net/add-page-field-in-pivot-table/)
- [Actualisation des tableaux croisés dynamiques dans Aspose.Cells for Python via .NET](/cells/fr/python-net/refresh-pivot-table/)
- [Application de styles aux tableaux croisés dynamiques](/cells/fr/python-net/apply-style-to-pivot-table/)

{{< app/cells/assistant language="csharp" >}}
