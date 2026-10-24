---
title: Ajouter des champs de ligne et de colonne aux tableaux croisés dynamiques avec Aspose.Cells for Python via Java
description: Découvrez comment ajouter des champs de base aux régions de ligne et de colonne d’un Tableau Croisé Dynamique et contrôler les sous-totaux des champs de pivot à l’aide de PivotField.setSubtotals dans Aspose.Cells for Python via Java.
linktitle: Champs de ligne et de colonne
keywords: Aspose.Cells, Python via Java, Tableau Croisé Dynamique, champ de ligne, champ de colonne, PivotField, setSubtotals, PivotFieldSubtotalType, sous-totaux
type: docs
weight: 220
url: /fr/python-java/pivot-table-add-row-and-column-fields/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Ajouter un champ à la région de ligne ou de colonne**
La méthode `PivotTable.addFieldToArea(PivotFieldType fieldType, String fieldName)` déplace un champ de base des données source vers l’une des quatre régions du Tableau Croisé Dynamique. L’argument `fieldType` accepte l’une des valeurs `PivotFieldType` suivantes.
- `ROW` — champs placés verticalement à gauche
- `COLUMN` — champs placés horizontalement en haut
- `DATA` — champs dont les valeurs sont agrégées
- `PAGE` — champs utilisés comme filtres de rapport
L’ordre d’imbrication des champs est important. L’ajout de `Category` à la région de ligne, puis de `Item`, produit un Tableau Croisé Dynamique dont le groupement externe est `Category` et le groupement interne est `Item`. L’inversion de l’ordre inverse la hiérarchie.

## **Sous-totaux des champs de pivot**
La méthode `PivotField.setSubtotals(PivotFieldSubtotalType subtotalType, boolean shown)` contrôle les lignes de sous-total qui apparaissent pour un champ de pivot. Chaque appel active ou désactive indépendamment un seul type de sous-total. Le passage de `shown = true` affiche le sous-total, tandis que `shown = false` le masque. Comme chaque appel n’affecte qu’un seul type, l’appel de la méthode plusieurs fois avec différentes valeurs `subtotalType` permet de créer un sous-ensemble personnalisé de sous-totaux.
L’énumération `PivotFieldSubtotalType` définit les types de sous-total disponibles.
- `AUTOMATIC` — Aspose.Cells choisit la sélection par défaut (généralement `SUM` pour les champs numériques)
- `NONE` — supprime toutes les lignes de sous-total
- `SUM`
- `COUNT`
- `AVERAGE`
- `MAX`
- `MIN`
- `PRODUCT`
- `STD_DEV`
- `STD_DEVP`
- `VAR`
- `VARP`

{{% alert color="primary" %}}
Les sous-totaux ne s’affichent que lorsque la région de ligne (ou la région de colonne) contient au moins deux champs de pivot. Un champ unique ne dispose d’aucun intervalle significatif pour lequel calculer un sous-total ; les appels à `setSubtotals` n’ont donc aucun effet visible dans ce cas. Cet article place par conséquent deux champs de ligne (`Category` externe, `Item` interne) dans chaque exemple afin que la délimitation des sous-totaux entre chaque groupe `Category` soit visible.
{{% /alert %}}

## **Scénario 1 — Sous-totaux automatiques (par défaut)**
Lorsque vous n’appelez pas du tout `setSubtotals`, Aspose.Cells applique la sélection `AUTOMATIC` aux champs numériques. L’exemple suivant confirme explicitement ce comportement en appelant `setSubtotals(PivotFieldSubtotalType.AUTOMATIC, true)` sur le champ de ligne externe `Category`.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, PivotTable, PivotField, PivotFieldType, PivotFieldSubtotalType
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("Data")
worksheet.getCells().get(0, 0).putValue("Category")
worksheet.getCells().get(0, 1).putValue("Item")
worksheet.getCells().get(0, 2).putValue("Year")
worksheet.getCells().get(0, 3).putValue("Amount")
worksheet.getCells().get(1, 0).putValue("Fruit")
worksheet.getCells().get(1, 1).putValue("Apple")
worksheet.getCells().get(1, 2).putValue(2020)
worksheet.getCells().get(1, 3).putValue(100)
worksheet.getCells().get(2, 0).putValue("Fruit")
worksheet.getCells().get(2, 1).putValue("Apple")
worksheet.getCells().get(2, 2).putValue(2021)
worksheet.getCells().get(2, 3).putValue(150)
worksheet.getCells().get(3, 0).putValue("Fruit")
worksheet.getCells().get(3, 1).putValue("Banana")
worksheet.getCells().get(3, 2).putValue(2020)
worksheet.getCells().get(3, 3).putValue(80)
worksheet.getCells().get(4, 0).putValue("Fruit")
worksheet.getCells().get(4, 1).putValue("Banana")
worksheet.getCells().get(4, 2).putValue(2021)
worksheet.getCells().get(4, 3).putValue(90)
worksheet.getCells().get(5, 0).putValue("Vegetable")
worksheet.getCells().get(5, 1).putValue("Carrot")
worksheet.getCells().get(5, 2).putValue(2020)
worksheet.getCells().get(5, 3).putValue(50)
worksheet.getCells().get(6, 0).putValue("Vegetable")
worksheet.getCells().get(6, 1).putValue("Carrot")
worksheet.getCells().get(6, 2).putValue(2021)
worksheet.getCells().get(6, 3).putValue(60)
worksheet.getCells().get(7, 0).putValue("Vegetable")
worksheet.getCells().get(7, 1).putValue("Daikon")
worksheet.getCells().get(7, 2).putValue(2020)
worksheet.getCells().get(7, 3).putValue(40)
worksheet.getCells().get(8, 0).putValue("Vegetable")
worksheet.getCells().get(8, 1).putValue("Daikon")
worksheet.getCells().get(8, 2).putValue(2021)
worksheet.getCells().get(8, 3).putValue(45)
pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)
pivotTable.addFieldToArea(PivotFieldType.ROW, "Category")
pivotTable.addFieldToArea(PivotFieldType.ROW, "Item")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
categoryField = pivotTable.getRowFields().get(0)
categoryField.setSubtotals(PivotFieldSubtotalType.AUTOMATIC, True)
pivotTable.calculateData()
workbook.save("output_automatic.xlsx")
jpype.shutdownJVM()
```

## **Scénario 2 — Suppression de tous les sous-totaux (`NONE`)**
L’appel de `setSubtotals(PivotFieldSubtotalType.NONE, true)` supprime toutes les lignes de sous-total du Tableau Croisé Dynamique, ne laissant que les lignes de champ et le total général en bas. Cette approche est utile lorsque vous souhaitez afficher les données groupées brutes sans aucune ligne de résumé.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType, PivotFieldSubtotalType
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("Data")
headers = ["Category", "Item", "Year", "Amount"]
for j in range(len(headers)):
    worksheet.getCells().get(0, j).putValue(headers[j])
data = [
    ["Fruit",     "Apple",  2020, 100],
    ["Fruit",     "Apple",  2021, 150],
    ["Fruit",     "Banana", 2020, 80 ],
    ["Fruit",     "Banana", 2021, 90 ],
    ["Vegetable", "Carrot", 2020, 50 ],
    ["Vegetable", "Carrot", 2021, 60 ],
    ["Vegetable", "Daikon", 2020, 40 ],
    ["Vegetable", "Daikon", 2021, 45 ]
]
for i in range(len(data)):
    for j in range(len(data[0])):
        worksheet.getCells().get(i + 1, j).putValue(data[i][j])
pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)
pivotTable.addFieldToArea(PivotFieldType.ROW, "Category")
pivotTable.addFieldToArea(PivotFieldType.ROW, "Item")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
categoryField = pivotTable.getRowFields().get(0)
categoryField.setSubtotals(PivotFieldSubtotalType.NONE, True)
pivotTable.calculateData()
workbook.save("output_none.xlsx")
jpype.shutdownJVM()
```

## **Scénario 3 — Sous-ensemble personnalisé de sous-totaux (`SUM` + `AVERAGE`)**
Vous ne êtes pas limité à un seul type de sous-total. Chaque appel à `setSubtotals` agit indépendamment sur un type ; l’appeler deux fois — une fois avec `SUM` et une fois avec `AVERAGE` — produit un sous-ensemble personnalisé de deux lignes de sous-total pour chaque groupe `Category`.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotTableCollection, PivotTable, PivotFieldType, PivotField, PivotFieldSubtotalType
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("Data")
worksheet.getCells().get("A1").putValue("Category")
worksheet.getCells().get("B1").putValue("Item")
worksheet.getCells().get("C1").putValue("Year")
worksheet.getCells().get("D1").putValue("Amount")
worksheet.getCells().get(1, 0).putValue("Fruit")
worksheet.getCells().get(1, 1).putValue("Apple")
worksheet.getCells().get(1, 2).putValue(2020)
worksheet.getCells().get(1, 3).putValue(100)
worksheet.getCells().get(2, 0).putValue("Fruit")
worksheet.getCells().get(2, 1).putValue("Apple")
worksheet.getCells().get(2, 2).putValue(2021)
worksheet.getCells().get(2, 3).putValue(150)
worksheet.getCells().get(3, 0).putValue("Fruit")
worksheet.getCells().get(3, 1).putValue("Banana")
worksheet.getCells().get(3, 2).putValue(2020)
worksheet.getCells().get(3, 3).putValue(80)
worksheet.getCells().get(4, 0).putValue("Fruit")
worksheet.getCells().get(4, 1).putValue("Banana")
worksheet.getCells().get(4, 2).putValue(2021)
worksheet.getCells().get(4, 3).putValue(90)
worksheet.getCells().get(5, 0).putValue("Vegetable")
worksheet.getCells().get(5, 1).putValue("Carrot")
worksheet.getCells().get(5, 2).putValue(2020)
worksheet.getCells().get(5, 3).putValue(50)
worksheet.getCells().get(6, 0).putValue("Vegetable")
worksheet.getCells().get(6, 1).putValue("Carrot")
worksheet.getCells().get(6, 2).putValue(2021)
worksheet.getCells().get(6, 3).putValue(60)
worksheet.getCells().get(7, 0).putValue("Vegetable")
worksheet.getCells().get(7, 1).putValue("Daikon")
worksheet.getCells().get(7, 2).putValue(2020)
worksheet.getCells().get(7, 3).putValue(40)
worksheet.getCells().get(8, 0).putValue("Vegetable")
worksheet.getCells().get(8, 1).putValue("Daikon")
worksheet.getCells().get(8, 2).putValue(2021)
worksheet.getCells().get(8, 3).putValue(45)
pivotTables = worksheet.getPivotTables()
pivotIndex = pivotTables.add("A1:D9", "F3", "PivotTable1")
pivotTable = pivotTables.get(pivotIndex)
pivotTable.addFieldToArea(PivotFieldType.ROW, "Category")
pivotTable.addFieldToArea(PivotFieldType.ROW, "Item")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
categoryField = pivotTable.getRowFields().get(0)
categoryField.setSubtotals(PivotFieldSubtotalType.SUM, True)
categoryField.setSubtotals(PivotFieldSubtotalType.AVERAGE, True)
pivotTable.calculateData()
workbook.save("output_custom.xlsx")
jpype.shutdownJVM()
```

## **Récapitulatif**

Les trois scénarios ne diffèrent que par un seul point : les appels à `setSubtotals`. Tout le reste — l’ensemble de données, les champs et les zones auxquelles ils sont assignés — est identique, ce qui rend les dispositions directement comparables.
- **Placement des champs.** `PivotTable.addFieldToArea(PivotFieldType.ROW, fieldName)` déplace une colonne source vers une région. À l’intérieur d’une même région, l’ordre des appels détermine l’ordre d’affichage, de sorte que le premier appel correspond au groupe le plus externe. Les sous-totaux nécessitent au moins deux champs dans la même région : avec un seul champ, il n’y a rien entre les groupes sur lequel calculer un sous-total.
- **Scénario 1 — sous-totaux automatiques.** L’absence d’appel à `setSubtotals` laisse le choix à Excel, qui applique son sous-total par défaut aux champs numériques. L’appel à `setSubtotals` avec `PivotFieldSubtotalType.AUTOMATIC` enregistre explicitement ce choix au lieu de le laisser implicite.
- **Scénario 2 — absence de sous-totaux.** `setSubtotals` avec `PivotFieldSubtotalType.NONE` désactive le sous-total par défaut, de sorte que le tableau croisé conserve les lignes de champ et le total général, mais supprime les lignes de sous-total qu’Excel insérerait autrement entre elles.
- **Scénario 3 — sous-ensemble choisi.** Chaque appel active ou désactive exactement un type de sous-total, et les appels s’accumulent plutôt que de s’annuler mutuellement. Ainsi, un premier appel avec `PivotFieldSubtotalType.SUM` suivi d’un second avec `PivotFieldSubtotalType.AVERAGE` laisse les deux activés, et le tableau croisé affiche un sous-total « Somme », un sous-total « Moyenne » et un total général.

{{% alert color="primary" %}}
Rien dans la gestion des sous-totaux n’est spécifique à la région des lignes. Les mêmes appels à `setSubtotals` sur un champ provenant de `PivotTable.ColumnFields` produisent les mêmes trois dispositions sur l’axe des colonnes, car le paramètre appartient au champ croisé et non à l’axe sur lequel il est placé.
{{% /alert %}}
## **Articles associés**
- [Champs de page dans les tableaux croisés dynamiques](/cells/fr/python-java/add-page-field-in-pivot-table/)
- [Actualisation des tableaux croisés dynamiques avec Aspose.Cells for Python via Java](/cells/fr/python-java/refresh-pivot-table/)
- [Application de styles aux tableaux croisés dynamiques](/cells/fr/python-java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="python" >}}