---
title: Affichage ou filtrage du Top 10 dans le Tableau Croisé Dynamique
linktitle: Affichage ou filtrage du Top 10 dans le Tableau Croisé Dynamique
description: Apprenez comment n’afficher que les éléments les mieux ou les moins classés d’un champ de tableau croisé dynamique dans Aspose.Cells for Python via Java. Cet article couvre la méthode top10AutoShow d’Excel 97‑2003, la lecture des options avec Top10AutoShowSettings, et le filtre Top 10 d’Excel 2007‑365 via filterTop10.
keywords: Aspose.Cells for Python via Java, tableau croisé dynamique, top 10, affichage automatique, top10AutoShow, Top10AutoShowSettings, PivotFieldTop10AutoShowSettings, filterTop10, PivotFilterType, PivotField, Python
type: docs
weight: 20
url: /fr/python-java/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Scénarios d’utilisation possibles**
Un tableau croisé dynamique qui répertorie chaque élément d’un champ de ligne peut être difficile à lire lorsque le champ comporte des dizaines de membres. Un rapport Top 10 ne conserve que les éléments les mieux ou les moins classés, ce qui correspond exactement aux besoins des rapports de classement — « top 5 produits par chiffre d’affaires » ou « bottom 3 régions par nombre de ventes ». Aspose.Cells prend en charge deux mécanismes à cet effet, qui correspondent à deux générations de Microsoft Excel.
- **Excel 97-2003 AutoShow** — la méthode `PivotField.top10AutoShow()`. Il s’agit du réglage classique « Afficher les N meilleurs ou les N moins bons éléments » stocké directement sur le champ du tableau croisé dynamique. Il fonctionne dans chaque version d’Excel, ancienne ou récente, car il fait partie du format original du tableau croisé dynamique.
- **Excel 2007-365 Top 10 Filter** — la méthode `PivotField.filterTop10()`. Il s’agit du filtre de valeur Top 10 moderne trouvé dans le menu du champ sous « Filtres de valeurs ». Il est stocké sous forme d’un objet `PivotFilter` attaché au champ et offre un classement basé sur le nombre d’éléments ou le pourcentage.

## **Affichage du Top 10 dans Excel 97‑2003 (top10AutoShow)**
L’AutoShow classique est configuré avec un appel unique à `PivotField.top10AutoShow(boolean isAutoShow, boolean isTop, int count, int rankBy)` :
- `isAutoShow` — active ou désactive le paramètre AutoShow sur le champ.
- `isTop` — `True` conserve les éléments les mieux classés (Top), `False` conserve les éléments les moins bien classés (Bottom).
- `count` — nombre d’éléments à conserver, par exemple 10 pour un rapport Top 10 classique.
- `rankBy` — l’index zéro‑basé du **champ de données** dont les valeurs classent les éléments. Passez -1 pour classer les éléments par le champ lui‑même.
Le classement peut être basé sur un champ de valeur ou sur le champ lui‑même. Deux variantes naturelles existent, présentées ci‑dessous.

### **Classer par un champ de valeur**
Classez les éléments du champ de ligne par un champ de valeur ordinaire tel que Somme des Ventes. L’exemple suivant crée un tableau croisé dynamique avec un champ de ligne (`Sport`) et un champ de données (`Sales`), puis affiche les 2 sports les mieux vendus. `rankBy` vaut 0 car « Sum of Sales » est le champ de données à l’index 0.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, PivotFieldType
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.getCells().get("A1").putValue("Sport")
worksheet.getCells().get("B1").putValue("Quarter")
worksheet.getCells().get("C1").putValue("Sales")
sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"]
row = 2
for sport in sports:
    for quarter in range(1, 4):
        worksheet.getCells().get(row, 0).putValue(sport)
        worksheet.getCells().get(row, 1).putValue("Qtr" + str(quarter))
        worksheet.getCells().get(row, 2).putValue(1000 + 777 * row)
        row += 1
pivot_table = worksheet.getPivotTables().add("A1:C16", 2, 5)
pivot_table.addFieldToArea(PivotFieldType.ROW, "Sport")
pivot_table.addFieldToArea(PivotFieldType.DATA, "Sales")
pivot_table.calculateData()
sport_field = pivot_table.getRowFields().get(0)
sport_field.top10AutoShow(True, True, 2, 0)
pivot_table.calculateData()
workbook.save("output-top10-by-value-field.xlsx")
jpype.shutdownJVM()
```

### **Classer par le champ lui‑même**
Un champ peut également être classé par lui‑même — passez -1 comme `rankBy`. Aucun champ de données supplémentaire n’est nécessaire pour cette variante ; le champ doit simplement se situer dans la zone ligne (ou colonne). L’exemple suivant montre les 3 sports les moins performants classés par le champ lui‑même. Lorsque ce réglage est enregistré, l’attribut `rankBy` est omis du XML du tableau croisé dynamique car -1 est la valeur par défaut du format, et `Top10AutoShowSettings.getRankBy()` renvoie -1.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.getCells().get("A1").putValue("Sport")
worksheet.getCells().get("B1").putValue("Quarter")
worksheet.getCells().get("C1").putValue("Sales")
sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"]
row = 2
for sport in sports:
    for quarter in range(1, 4):
        worksheet.getCells().get(row, 0).putValue(sport)
        worksheet.getCells().get(row, 1).putValue("Qtr" + str(quarter))
        worksheet.getCells().get(row, 2).putValue(1000 + 777 * row)
        row += 1
pivot_table = worksheet.getPivotTables().add("A1:C16", 2, 5)
pivot_table.addFieldToArea(PivotFieldType.ROW, "Sport")
pivot_table.addFieldToArea(PivotFieldType.DATA, "Sales")
pivot_table.calculateData()
sport_field = pivot_table.getRowFields().get(0)
# Show the bottom 3 items ranked by the field itself (rankBy = -1)
sport_field.top10AutoShow(True, False, 3, -1)
pivot_table.calculateData()
workbook.save("output-top10-by-field-itself.xlsx")
jpype.shutdownJVM()
```

## **Lecture des options actuelles (Top10AutoShowSettings)**
La méthode `PivotField.getTop10AutoShowSettings()` renvoie un objet `PivotFieldTop10AutoShowSettings` qui expose les options AutoShow actuellement stockées sur le champ. Utilisez‑le pour inspecter la façon dont un classeur existant, ou un tableau croisé dynamique que vous venez de configurer, présentera ses éléments — y compris les classeurs chargés depuis un fichier.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat
workbook = Workbook("output-top10-by-value-field.xlsx")
pivot_table = workbook.getWorksheets().get(0).getPivotTables().get(0)
sport_field = pivot_table.getRowFields()[0]
settings = sport_field.getTop10AutoShowSettings()
print("AutoShow enabled: " + str(settings.isAutoShow()))
print("Direction: " + ("Top" if settings.isTop() else "Bottom"))
print("Item count: " + str(settings.getAutoShowCount()))
print("Ranking data field index: " + str(settings.getRankBy()))
jpype.shutdownJVM()
```

Les quatre propriétés correspondent aux attributs AutoShow classiques écrits dans le XML du tableau croisé dynamique (`autoShow`, `topAutoShow`, `itemPageCount`, `rankBy`), de sorte que les valeurs lues sont celles que chaque version d’Excel respectera.

## **Remarque**

{{% alert color="primary" %}}
- Les accesseurs directs de `PivotField` `isAutoShow()`, `isAscendShow()`, `getAutoShowCount()` et `getAutoShowField()` sont marqués comme obsolètes. Utilisez l’objet `Top10AutoShowSettings` à la place : `PivotField.isAutoShow()` devient `Top10AutoShowSettings.isAutoShow()`, `PivotField.isAscendShow()` devient `Top10AutoShowSettings.isTop()`, `PivotField.getAutoShowCount()` devient `Top10AutoShowSettings.getAutoShowCount()`, et `PivotField.getAutoShowField()` devient `Top10AutoShowSettings.getRankBy()`. La méthode `top10AutoShow()` elle‑même est la façon prise en charge pour modifier les paramètres.
- `top10AutoShow` fonctionne avec les champs de ligne et de colonne. Un champ présent uniquement dans la zone de page (filtre) ne peut pas être classé de cette manière, car ses éléments ne sont pas disposés dans le corps du tableau croisé dynamique.
{{% /alert %}}

## **Excel 2007‑365 : filtre Top 10 (filterTop10)**
Les versions modernes d’Excel exposent le Top 10 comme un filtre de valeur dans le menu du champ (Filtres de valeurs, Top 10…). Aspose.Cells le modélise avec la méthode `PivotField.filterTop10(int valueFieldIndex, PivotFilterType type, boolean isTop, int itemCount)`, qui renvoie le `PivotFilter` créé :
- `valueFieldIndex` — l’index zéro‑basé du champ de données dont les valeurs agrégées classent les éléments.
- `type` — ce que signifie `itemCount`. `PivotFilterType.COUNT` conserve un nombre fixe d’éléments (l’option Items de la boîte de dialogue). `PivotFilterType.PERCENT` conserve un pourcentage des éléments, ainsi `itemCount` représente le pourcentage lui‑même — 30 conserve les 30 % meilleurs. `PivotFilterType.SUM` classe selon la couverture de valeur cumulative.
- `isTop` — `True` pour Top, `False` pour Bottom.
- `itemCount` — le N dans Top N ; son unité dépend de `type`.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType, PivotFilterType
try:
    workbook = Workbook()
    worksheet = workbook.getWorksheets().get(0)
    worksheet.getCells().get("A1").putValue("Sport")
    worksheet.getCells().get("B1").putValue("Quarter")
    worksheet.getCells().get("C1").putValue("Sales")
    sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"]
    row = 2
    for sport in sports:
        for quarter in range(1, 4):
            worksheet.getCells().get(row, 0).putValue(sport)
            worksheet.getCells().get(row, 1).putValue("Qtr" + str(quarter))
            worksheet.getCells().get(row, 2).putValue(1000 + 777 * row)
            row += 1
    pivot_table = worksheet.getPivotTables().add("A1:C16", 2, 5)
    pivot_table.addFieldToArea(PivotFieldType.ROW, "Sport")
    pivot_table.addFieldToArea(PivotFieldType.DATA, "Sales")
    pivot_table.calculateData()
    sport_field = pivot_table.getRowFields().get(0)
    # Top 10 Filter — keep the top 2 items by "Sum of Sales" (data field index 0)
    filter = sport_field.filterTop10(0, PivotFilterType.COUNT, True, 2)
    # For a percentage-based filter instead, keep the top 30 percent of the items:
    # sport_field.filterTop10(0, PivotFilterType.PERCENT, True, 30)
    pivot_table.getPivotCache().refresh()
    pivot_table.calculateData()
    workbook.save("output-top10-filter.xlsx")
finally:
    jpype.shutdownJVM()
```

{{% alert color="primary" %}}
`top10AutoShow` et `filterTop10` sont deux fonctionnalités distinctes. AutoShow écrit l’attribut classique `autoShow` défini sur le champ du tableau croisé dynamique et est pris en compte par toutes les versions d’Excel depuis Excel 97. `filterTop10` écrit une entrée moderne `PivotFilter`, qui nécessite Excel 2007 ou ultérieur. Lorsqu’un classeur est ouvert dans une version plus ancienne d’Excel, un tableau croisé dynamique utilisant le filtre moderne revient à afficher tous les éléments. Pour les documents qui doivent circuler dans des outils hérités, privilégiez `top10AutoShow` ; pour les classeurs modernes, privilégiez `filterTop10` car il se combine avec les autres filtres de valeur.
{{% /alert %}}

## **Articles associés**
- [Filtrer les tableaux croisés dynamiques par libellé ou valeur](/cells/fr/python-java/filter-by-label-or-value-of-pivot-table/)
- [Ajouter des champs de ligne et de colonne au tableau croisé dynamique](/cells/fr/python-java/pivot-table-add-row-and-column-fields/)
- [Regrouper les champs de tableau croisé dynamique](/cells/fr/python-java/group-pivot-fields-in-the-pivot-table/)
- [Actualiser le tableau croisé dynamique](/cells/fr/python-java/refresh-pivot-table/)
- [Ajouter un champ de page dans le tableau croisé dynamique](/cells/fr/python-java/add-page-field-in-pivot-table/)

{{< app/cells/assistant language="python" >}}