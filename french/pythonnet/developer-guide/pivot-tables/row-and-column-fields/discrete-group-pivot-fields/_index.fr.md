---
title: Regroupement discret des éléments d’un champ de tableau croisé dynamique
linktitle: Regroupement discret
description: Apprendre à regrouper les éléments d’un champ de tableau croisé dynamique dans des groupes personnalisés portant un nom, tels que les fruits et les légumes, à l’aide de DiscreteGroupItem et de pivot_field_group_options.discrete_group_items dans Aspose.Cells for Python via .NET.
keywords: Aspose.Cells for Python via .NET, tableau croisé dynamique, regroupement discret, DiscreteGroupItem, PivotFieldGroupOptions, regroupement des éléments du tableau croisé dynamique, groupes personnalisés, PivotField.group, Python, tableau croisé dynamique Excel
type: docs
weight: 90
url: /fr/python-net/discrete-group-pivot-fields/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Scénarios d’utilisation possibles**
- Le regroupement automatique regroupe les éléments par type de données, par exemple en regroupant les dates par mois et par trimestre ou les nombres par plage. Le regroupement discret répond au problème inverse en rassemblant des éléments spécifiques et sans rapport dans des groupes personnalisés portant un nom, par exemple en regroupant des produits sous les catégories « fruits » et « légumes », des magasins par région ou des comptes par zone. Aspose.Cells fournit le regroupement discret au moyen de la classe `DiscreteGroupItem` et de la propriété `pivot_field_group_options.discrete_group_items`.
- Un `DiscreteGroupItem` associe un nom de groupe aux éléments qui lui appartiennent. Les éléments peuvent être identifiés de deux façons : par leur nom (`DiscreteGroupItem("fruit", ["grape", "cherry"])`) ou par leur position dans les données sources, à partir de zéro (`DiscreteGroupItem("fruit", [0, 3])`). Ces deux formes produisent le même résultat.
- Le regroupement discret s’applique à un champ situé dans la zone des lignes ou des colonnes d’un tableau croisé dynamique. Pour l’appliquer, transmettez les options à `pivot_field.group(PivotFieldGroupOptions)`.

## **Regrouper les éléments d’un champ de tableau croisé dynamique par nom d’élément**
L’exemple suivant construit une petite liste de ventes (`product`, `date` et `amount`), crée un tableau croisé dynamique à partir de celle-ci avec `product` dans la zone des lignes, `date` dans la zone des colonnes et `amount` dans la zone des données, puis définit deux groupes personnalisés en fonction des noms des éléments : `fruit` (`grape`, `cherry`) et `vegetables` (`carrot`, `potato`). Le résultat affiche une disposition des lignes à deux niveaux : le nom du groupe forme le niveau extérieur et les éléments d’origine sont imbriqués au-dessous. Cette structure permet d’analyser les tendances par groupe personnalisé et par élément.

```python
import aspose.cells as ac
from datetime import datetime
from aspose.cells.pivot import DiscreteGroupItem, PivotFieldGroupOptions, PivotFieldType, PivotTableStyleType
wb = ac.Workbook()
sheet = wb.worksheets[0]
cells = sheet.cells
cells.get(0, 0).value = "product"
cells.get(1, 0).value = "grape"
cells.get(2, 0).value = "carrot"
cells.get(3, 0).value = "potato"
cells.get(4, 0).value = "cherry"
date_style = wb.create_style()
date_style.custom = "m/d/yyyy"
cells.get(0, 1).value = "date"
cells.get(1, 1).value = datetime(2021, 2, 5)
cells.get(2, 1).value = datetime(2022, 3, 8)
cells.get(3, 1).value = datetime(2023, 4, 10)
cells.get(4, 1).value = datetime(2024, 5, 16)
for r in range(1, 5):
    cells.get(r, 1).set_style(date_style)
cells.get(0, 2).value = "amount"
cells.get(1, 2).value = 50
cells.get(2, 2).value = 60
cells.get(3, 2).value = 70
cells.get(4, 2).value = 80
# Add a pivot table with the destination cell A12 (row 11, column 0)
pivot_table = sheet.pivot_tables.add("=Sheet1!A1:C5", 11, 0)
pivot_table.add_field_to_area(PivotFieldType.ROW, "product")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "date")
pivot_table.add_field_to_area(PivotFieldType.DATA, "amount")
pivot_table.pivot_table_style_type = PivotTableStyleType.PIVOT_TABLE_STYLE_MEDIUM10
# Group specific items into custom groups using 0-based source-appearance indexes
fruit = DiscreteGroupItem("fruit", [0, 3])
vegetable = DiscreteGroupItem("vegetable", [1, 2])
group_options = PivotFieldGroupOptions()
group_options.discrete_group_items = [fruit, vegetable]
pivot_table.row_fields[0].group(group_options)
pivot_table.calculate_data()
wb.save("outputDiscreteGroupPivotField.xlsx")
```

Après l’appel à `calculate_data()`, la zone des lignes du tableau croisé dynamique affiche `fruit` (`grape` 50, `cherry` 80) et `vegetable` (`carrot` 60, `potato` 70), avec un total général de 260, tandis que les étiquettes de colonnes conservent les quatre dates (2/5/2021, 3/8/2022, 4/10/2023, 5/16/2024).

## **Regrouper les éléments d’un champ de tableau croisé dynamique par indice d’élément**
Lorsque les noms des éléments sont longs ou localisés, le second constructeur de `DiscreteGroupItem` identifie les éléments par leur indice. Les indices correspondent aux positions des éléments, à partir de zéro, dans l’ordre d’apparition dans les données sources, et non dans l’ordre alphabétique. Dans les données d’exemple ci-dessus, `grape` est l’élément 0, `carrot` l’élément 1, `potato` l’élément 2 et `cherry` l’élément 3. Le groupe `fruit` correspond donc à `{ 0, 3 }` et le groupe `vegetable` à `{ 1, 2 }`. Le résultat est identique à celui de l’exemple fondé sur les noms.

```python
import aspose.cells as ac
from aspose.cells.pivot import DiscreteGroupItem, PivotFieldGroupOptions, PivotFieldType, PivotTableStyleType
from datetime import datetime
wb = ac.Workbook()
sheet = wb.worksheets[0]
cells = sheet.cells
cells.get(0, 0).value = "product"
cells.get(1, 0).value = "grape"
cells.get(2, 0).value = "carrot"
cells.get(3, 0).value = "potato"
cells.get(4, 0).value = "cherry"
date_style = wb.create_style()
date_style.custom = "m/d/yyyy"
cells.get(0, 1).value = "date"
cells.get(1, 1).value = datetime(2021, 2, 5)
cells.get(2, 1).value = datetime(2022, 3, 8)
cells.get(3, 1).value = datetime(2023, 4, 10)
cells.get(4, 1).value = datetime(2024, 5, 16)
for r in range(1, 5):
    cells.get(r, 1).set_style(date_style)
cells.get(0, 2).value = "amount"
cells.get(1, 2).value = 50
cells.get(2, 2).value = 60
cells.get(3, 2).value = 70
cells.get(4, 2).value = 80
# Add a pivot table with the destination cell A12 (row 11, column 0)
pivot_table = sheet.pivot_tables.add("=Sheet1!A1:C5", 11, 0)
pivot_table.add_field_to_area(PivotFieldType.ROW, "product")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "date")
pivot_table.add_field_to_area(PivotFieldType.DATA, "amount")
pivot_table.pivot_table_style_type = PivotTableStyleType.PIVOT_TABLE_STYLE_MEDIUM10
# grape is item 0, carrot is item 1, potato is item 2, cherry is item 3
# (zero-based positions in the order the items appear in the source data)
fruit = DiscreteGroupItem("fruit", [0, 3])
vegetable = DiscreteGroupItem("vegetable", [1, 2])
group_options = PivotFieldGroupOptions()
group_options.discrete_group_items = [fruit, vegetable]
pivot_table.row_fields[0].group(group_options)
pivot_table.calculate_data()
wb.save("outputDiscreteGroupPivotFieldByIndex.xlsx")
```

## **Remarque**

{{% alert color="primary" %}}
- Les éléments qui ne sont affectés à aucun groupe personnalisé ne sont pas perdus. Ils restent dans le tableau croisé dynamique, au même niveau que les groupes personnalisés, chacun formant une entrée autonome contenant un seul élément. Dans l’exemple ci-dessus, la définition du seul groupe `fruit` laisse `carrot` et `potato` dans la zone des lignes, sous forme d’entrées autonomes à côté du groupe `fruit`.
- La propriété `pivot_field_group_options.new_pivot_field` contrôle la disposition du regroupement discret. Sa valeur par défaut est `True`, ce qui ajoute le champ regroupé sous forme de nouveau champ extérieur à côté du champ d’origine et produit la disposition à deux niveaux illustrée ci-dessus (`row_fields` passe à 2). Pour remplacer le champ d’origine, définissez cette propriété sur `False` : la zone des lignes affiche alors un seul niveau contenant uniquement les noms des groupes et leurs valeurs agrégées, à savoir `fruit` 130 (50 + 80) et `vegetable` 130 (60 + 70).
- Les constructeurs de `DiscreteGroupItem` fondés sur les noms et sur les indices peuvent être combinés dans une même liste `discrete_group_items`.
{{% /alert %}}

## **Articles connexes**
- [Regrouper les champs du tableau croisé dynamique](/cells/fr/python-net/group-pivot-fields-in-the-pivot-table/)
- [Ajouter des champs de ligne et de colonne à un tableau croisé dynamique](/cells/fr/python-net/pivot-table-add-row-and-column-fields/)
- [Filtrer les tableaux croisés dynamiques par libellé ou valeur](/cells/fr/python-net/filter-by-label-or-value-of-pivot-table/)
- [Appliquer un style à un tableau croisé dynamique](/cells/fr/python-net/apply-style-to-pivot-table/)
- [Actualiser un tableau croisé dynamique](/cells/fr/python-net/refresh-pivot-table/)

{{< app/cells/assistant language="python-net" >}}