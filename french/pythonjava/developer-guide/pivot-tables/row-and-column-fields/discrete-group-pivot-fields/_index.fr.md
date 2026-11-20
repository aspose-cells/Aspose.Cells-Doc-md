---
title: Regroupement discret des éléments d’un champ de tableau croisé dynamique
linktitle: Regroupement discret
description: Découvrez comment regrouper les éléments d’un champ de tableau croisé dynamique dans des groupes personnalisés nommés, tels que fruits et légumes, à l’aide de `DiscreteGroupItem` et `PivotFieldGroupOptions.getDiscreteGroupItems` avec Aspose.Cells for Python via Java.
keywords: Aspose.Cells, tableau croisé dynamique, regroupement discret, DiscreteGroupItem, PivotFieldGroupOptions, regrouper les éléments d’un champ de tableau croisé dynamique, groupes personnalisés, PivotField.group, Python via Java, tableau croisé dynamique Excel
type: docs
weight: 90
url: /fr/python-java/discrete-group-pivot-fields/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Scénarios d’utilisation possibles**
- Le regroupement automatique collecte les éléments en fonction de leur type de données, par exemple en regroupant les dates par mois et par trimestre ou les nombres par plages. Le regroupement discret résout le problème inverse en regroupant des éléments spécifiques et sans lien entre eux dans des groupes personnalisés nommés, par exemple des produits en groupes de fruits et de légumes, des magasins par région ou des comptes par zone. Aspose.Cells fournit le regroupement discret au moyen de la classe `DiscreteGroupItem` et de la méthode `PivotFieldGroupOptions.getDiscreteGroupItems()`.
- Un `DiscreteGroupItem` est constitué d’un nom de groupe et des éléments qui lui appartiennent. Les éléments peuvent être identifiés de deux manières : par leur nom (`DiscreteGroupItem("fruit", ["grape", "cherry"])`) ou par leurs positions dans les données source, indexées à partir de zéro (`DiscreteGroupItem("fruit", [0, 3])`). Les deux formes produisent le même résultat.
- Le regroupement discret s’applique à un champ situé dans la zone des lignes ou dans la zone des colonnes du tableau croisé dynamique en transmettant les options à `PivotField.group(PivotFieldGroupOptions)`.

## **Regroupement des éléments d’un champ de tableau croisé dynamique par noms d’élément**
L’exemple suivant construit une petite liste de ventes (produit, date et montant), crée un tableau croisé dynamique à partir de celle-ci avec `product` dans la zone des lignes, `date` dans la zone des colonnes et `amount` dans la zone des données, puis définit deux groupes personnalisés d’après les noms des éléments : `fruit` (`grape`, `cherry`) et `vegetables` (`carrot`, `potato`). Le résultat présente une structure à deux niveaux dans la zone des lignes : le nom du groupe occupe le niveau extérieur et les éléments d’origine sont imbriqués au-dessous. Cette structure facilite la lecture des tendances par groupe personnalisé et par élément.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import (
    Workbook,
    Worksheet,
    Cells,
    Range,
    SaveFormat,
    DiscreteGroupItem,
    PivotFieldGroupOptions,
    PivotFieldType,
    PivotTableStyleType,
)
GregorianCalendar = jpype.JPackage("java.util").GregorianCalendar
def create_date(year, month, day):
    calendar = GregorianCalendar(year, month - 1, day)
    return calendar.getTime()
wb = Workbook()
sheet = wb.getWorksheets().get(0)
cells = sheet.getCells()
cells.get(0, 0).putValue("product")
cells.get(1, 0).putValue("grape")
cells.get(2, 0).putValue("carrot")
cells.get(3, 0).putValue("potato")
cells.get(4, 0).putValue("cherry")
date_style = wb.createStyle()
date_style.setCustom("m/d/yyyy")
cells.get(0, 1).putValue("date")
cells.get(1, 1).putValue(create_date(2021, 2, 5))
cells.get(2, 1).putValue(create_date(2022, 3, 8))
cells.get(3, 1).putValue(create_date(2023, 4, 10))
cells.get(4, 1).putValue(create_date(2024, 5, 16))
for r in range(1, 5):
    cells.get(r, 1).setStyle(date_style)
cells.get(0, 2).putValue("amount")
cells.get(1, 2).putValue(50.0)
cells.get(2, 2).putValue(60.0)
cells.get(3, 2).putValue(70.0)
cells.get(4, 2).putValue(80.0)
# Add a pivot table with the destination cell A12 (row 11, column 0)
pivot_table = sheet.getPivotTables().add("=Sheet1!A1:C5", 11, 0)
pivot_table.addFieldToArea(PivotFieldType.ROW, "product")
pivot_table.addFieldToArea(PivotFieldType.COLUMN, "date")
pivot_table.addFieldToArea(PivotFieldType.DATA, "amount")
pivot_table.setPivotTableStyleType(
    PivotTableStyleType.PIVOT_TABLE_STYLE_MEDIUM_10
)
# Group specific items into custom groups by item names
fruit = DiscreteGroupItem("fruit", ["grape", "cherry"])
vegetable = DiscreteGroupItem("vegetable", ["carrot", "potato"])
group_options = PivotFieldGroupOptions()
group_options.setDiscreteGroupItems([fruit, vegetable])
pivot_table.calculateData()
pivot_table.getRowFields().get(0).group(group_options)
wb.save("outputDiscreteGroupPivotField.xlsx")
jpype.shutdownJVM()
```

Après l’appel à `calculateData()`, la zone des lignes du tableau croisé dynamique affiche `fruit` (`grape` 50, `cherry` 80) et `vegetable` (`carrot` 60, `potato` 70), avec un total général de 260, tandis que les étiquettes de colonne conservent les quatre dates (2/5/2021, 3/8/2022, 4/10/2023, 5/16/2024).

## **Regroupement des éléments d’un champ de tableau croisé dynamique par indices d’élément**
Lorsque les noms des éléments sont longs ou localisés, le deuxième constructeur de `DiscreteGroupItem` identifie les éléments par leur indice. Les indices correspondent à des positions indexées à partir de zéro, selon l’ordre d’apparition des éléments dans les données source, et non selon l’ordre alphabétique. Dans les données d’exemple ci-dessus, `grape` est l’élément 0, `carrot` l’élément 1, `potato` l’élément 2 et `cherry` l’élément 3 ; `fruit` correspond donc à `{ 0, 3 }` et `vegetable` à `{ 1, 2 }`. Le résultat est identique à celui de l’exemple fondé sur les noms.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import (
    Workbook,
    PivotFieldType,
    PivotTableStyleType,
)
Date = jpype.JClass("java.util.Date")
DiscreteGroupItem = jpype.JClass("com.aspose.cells.DiscreteGroupItem")
PivotFieldGroupOptions = jpype.JClass("com.aspose.cells.PivotFieldGroupOptions")
wb = Workbook()
sheet = wb.getWorksheets().get(0)
cells = sheet.getCells()
cells.get(0, 0).putValue("product")
cells.get(1, 0).putValue("grape")
cells.get(2, 0).putValue("carrot")
cells.get(3, 0).putValue("potato")
cells.get(4, 0).putValue("cherry")
date_style = wb.createStyle()
date_style.setCustom("m/d/yyyy")
cells.get(0, 1).putValue("date")
cells.get(1, 1).putValue(Date(2021 - 1900, 2 - 1, 5))
cells.get(2, 1).putValue(Date(2022 - 1900, 3 - 1, 8))
cells.get(3, 1).putValue(Date(2023 - 1900, 4 - 1, 10))
cells.get(4, 1).putValue(Date(2024 - 1900, 5 - 1, 16))
for r in range(1, 5):
    cells.get(r, 1).setStyle(date_style)
cells.get(0, 2).putValue("amount")
cells.get(1, 2).putValue(50.0)
cells.get(2, 2).putValue(60.0)
cells.get(3, 2).putValue(70.0)
cells.get(4, 2).putValue(80.0)
pivot_table = sheet.getPivotTables().add("=Sheet1!A1:C5", 11, 0)
pivot_table.addFieldToArea(PivotFieldType.ROW, "product")
pivot_table.addFieldToArea(PivotFieldType.COLUMN, "date")
pivot_table.addFieldToArea(PivotFieldType.DATA, "amount")
pivot_table.setPivotTableStyleType(
    PivotTableStyleType.PIVOT_TABLE_STYLE_MEDIUM_10
)
pivot_table.calculateData()
fruit = DiscreteGroupItem("fruit", [0, 3])
vegetable = DiscreteGroupItem("vegetable", [1, 2])
group_options = PivotFieldGroupOptions()
group_options.setDiscreteGroupItems([fruit, vegetable])
pivot_table.getRowFields().get(0).group(group_options)
pivot_table.calculateData()
wb.save("outputDiscreteGroupPivotFieldByIndex.xlsx")
jpype.shutdownJVM()
```

## **Remarque**

{{% alert color="primary" %}}
- Les éléments qui ne sont affectés à aucun groupe personnalisé ne sont pas perdus. Ils restent dans le tableau croisé dynamique au même niveau que les groupes personnalisés, chacune sous forme d’entrée autonome à un seul élément. Dans l’exemple ci-dessus, la définition du seul groupe `fruit` laisse `carrot` et `potato` dans la zone des lignes comme entrées autonomes à côté du groupe `fruit`.
- Les méthodes `PivotFieldGroupOptions.getNewPivotField()` et `setNewPivotField()` contrôlent la disposition du regroupement discret. `getNewPivotField()` retourne `true` par défaut, ce qui ajoute le champ regroupé en tant que nouveau champ extérieur à côté du champ d’origine et produit la disposition à deux niveaux présentée ci-dessus (`getRowFields()` passe à 2). Utilisez `setNewPivotField(false)` pour remplacer le champ d’origine ; la zone des lignes affiche alors un seul niveau contenant uniquement les noms des groupes et leurs valeurs agrégées, à savoir `fruit` 130 (50 + 80) et `vegetable` 130 (60 + 70).
- Les constructeurs de `DiscreteGroupItem` fondés sur les noms et sur les indices peuvent être utilisés conjointement au sein de la même collection `getDiscreteGroupItems()`.
{{% /alert %}}

## **Articles connexes**
- [Regrouper les champs dans un tableau croisé dynamique](/cells/fr/python-java/group-pivot-fields-in-the-pivot-table/)
- [Ajouter des champs de ligne et de colonne à un tableau croisé dynamique](/cells/fr/python-java/pivot-table-add-row-and-column-fields/)
- [Filtrer les tableaux croisés dynamiques par libellé ou par valeur](/cells/fr/python-java/filter-by-label-or-value-of-pivot-table/)
- [Appliquer un style à un tableau croisé dynamique](/cells/fr/python-java/apply-style-to-pivot-table/)
- [Actualiser un tableau croisé dynamique](/cells/fr/python-java/refresh-pivot-table/)

{{< app/cells/assistant language="python" >}}