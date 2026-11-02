---
title: Afficher ou filtrer les 10 premiers éléments dans un tableau croisé dynamique
linktitle: Afficher ou filtrer les 10 premiers éléments dans un tableau croisé dynamique
description: Apprenez à afficher uniquement les éléments les mieux classés ou les moins bien classés d’un champ de tableau croisé dynamique dans Aspose.Cells for Python via Java. Cet article présente la méthode top10AutoShow d’Excel 97-2003, la lecture des options avec Top10AutoShowSettings et le filtre des 10 premiers éléments d’Excel 2007-365 via filterTop10.
keywords: Aspose.Cells for Python via Java, tableau croisé dynamique, 10 premiers éléments, affichage automatique, top10AutoShow, Top10AutoShowSettings, PivotFieldTop10AutoShowSettings, filterTop10, PivotFilterType, PivotField, Python
type: docs
weight: 20
url: /fr/python-java/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Scénarios d’utilisation possibles**
Un tableau croisé dynamique qui répertorie tous les éléments d’un champ de ligne peut être difficile à lire lorsque le champ comporte des dizaines de membres. Un rapport de type « 10 premiers éléments » conserve uniquement les éléments les mieux classés ou les moins bien classés, ce qui répond précisément aux besoins des rapports de classement, par exemple « 5 meilleurs produits par chiffre d’affaires » ou « 3 régions les moins bien classées en fonction du nombre de ventes ». Aspose.Cells prend en charge deux mécanismes à cet effet, qui correspondent à deux générations de Microsoft Excel.
- **AutoShow pour Excel 97-2003** — la méthode `PivotField.top10AutoShow()`. Il s’agit du paramètre classique « Afficher les N premiers/derniers éléments », stocké directement sur le champ de tableau croisé dynamique. Il fonctionne avec toutes les versions d’Excel, anciennes comme récentes, car il fait partie du format d’origine des tableaux croisés dynamiques.
- **Filtre des 10 premiers éléments pour Excel 2007-365** — la méthode `PivotField.filterTop10()`. Il s’agit du filtre moderne des 10 premiers éléments, disponible dans le menu du champ, sous « Filtres de valeurs ». Il est stocké sous forme d’objet `PivotFilter` associé au champ et permet le classement selon le nombre d’éléments ou selon un pourcentage.

## **Afficher les 10 premiers éléments dans Excel 97-2003 (top10AutoShow)**
Le paramètre classique AutoShow se configure par un appel unique à `PivotField.top10AutoShow(boolean isAutoShow, boolean isTop, int count, int rankBy)` :
- `isAutoShow` — active ou désactive le paramètre AutoShow sur le champ.
- `isTop` — `True` conserve les éléments les mieux classés (« Haut »), `False` conserve les moins bien classés (« Bas »).
- `count` — indique le nombre d’éléments à conserver, par exemple 10 pour un rapport classique des 10 premiers éléments.
- `rankBy` — l’index (numéroté à partir de zéro) du **champ de données** dont les valeurs servent à classer les éléments. Transmettez la valeur -1 pour classer les éléments selon le champ lui-même.
Le classement peut être effectué à partir d’un champ de valeurs ou du champ lui-même. Deux variantes possibles sont présentées ci-dessous.

### **Classer selon un champ de valeurs**
Classez les éléments du champ de ligne en fonction d’un champ de valeurs ordinaire, tel que « Somme des ventes ». L’exemple suivant crée un tableau croisé dynamique avec un champ de ligne (`Sport`) et un champ de données (`Sales`), puis affiche les 2 sports les mieux classés en fonction des ventes. `rankBy` vaut 0, car « Somme des ventes » est le champ de données situé à l’index 0.

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
sport_field.setAutoShow(True)
sport_field.setAutoShowCount(2)
sport_field.setAutoShowField(2)
pivot_table.calculateData()
workbook.save("output-top10-by-value-field.xlsx")
jpype.shutdownJVM()
```

### **Classer selon le champ lui-même**
Un champ peut également être classé par lui-même : transmettez la valeur -1 comme `rankBy`. Cette variante ne nécessite aucun champ de données supplémentaire ; le champ doit simplement se trouver dans la zone de ligne (ou de colonne). L’exemple suivant affiche les 3 sports les moins bien classés selon le champ lui-même. Lors de l’enregistrement de ce paramètre, l’attribut `rankBy` est omis du XML du tableau croisé dynamique, car -1 est la valeur par défaut de ce format. La méthode `Top10AutoShowSettings.getRankBy()` restitue ensuite la valeur -1.

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
# Afficher les 3 derniers éléments classés selon le champ lui-même (rankBy = -1)
sport_field.top10AutoShow(True, False, 3, -1)
pivot_table.calculateData()
workbook.save("output-top10-by-field-itself.xlsx")
jpype.shutdownJVM()
```

## **Lire les options actuelles (Top10AutoShowSettings)**
La méthode `PivotField.getTop10AutoShowSettings()` renvoie un objet `PivotFieldTop10AutoShowSettings` qui expose les options AutoShow actuellement stockées dans le champ. Utilisez-la pour examiner la manière dont un classeur existant ou un tableau croisé dynamique que vous venez de configurer affichera ses éléments. Cette méthode permet également d’inspecter les classeurs chargés à partir d’un fichier.

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

Les quatre propriétés correspondent aux attributs AutoShow classiques écrits dans le XML du tableau croisé dynamique (`autoShow`, `topAutoShow`, `itemPageCount`, `rankBy`). Les valeurs relues sont donc celles que toutes les versions d’Excel prennent en compte.

## **Remarque**

{{% alert color="primary" %}}
- Les méthodes d’accès directes de `PivotField`, à savoir `isAutoShow()`, `isAscendShow()`, `getAutoShowCount()` et `getAutoShowField()`, sont marquées comme obsolètes. Utilisez plutôt l’objet `Top10AutoShowSettings` : `PivotField.isAutoShow()` devient `Top10AutoShowSettings.isAutoShow()`, `PivotField.isAscendShow()` devient `Top10AutoShowSettings.isTop()`, `PivotField.getAutoShowCount()` devient `Top10AutoShowSettings.getAutoShowCount()` et `PivotField.getAutoShowField()` devient `Top10AutoShowSettings.getRankBy()`. La méthode `top10AutoShow()` est la méthode prise en charge pour modifier ces paramètres.
- `top10AutoShow` fonctionne avec les champs de ligne et de colonne. Un champ situé uniquement dans la zone de page (filtre) ne peut pas être classé de cette manière, car ses éléments ne sont pas présentés dans le corps du tableau croisé dynamique.
{{% /alert %}}

## **Excel 2007-365 : filtre des 10 premiers éléments (filterTop10)**
Les versions récentes d’Excel proposent les 10 premiers éléments sous forme de filtre de valeurs dans le menu du champ (« Filtres de valeurs », « 10 premiers éléments... »). Aspose.Cells modélise cette fonctionnalité au moyen de la méthode `PivotField.filterTop10(int valueFieldIndex, PivotFilterType type, boolean isTop, int itemCount)`, qui renvoie l’objet `PivotFilter` créé :
- `valueFieldIndex` — l’index (numéroté à partir de zéro) du champ de données dont les valeurs agrégées servent à classer les éléments.
- `type` — détermine la signification de `itemCount`. `PivotFilterType.COUNT` conserve un nombre fixe d’éléments (l’option « Éléments » de la boîte de dialogue). `PivotFilterType.PERCENT` conserve un pourcentage des éléments ; `itemCount` correspond donc directement au pourcentage — la valeur 30 conserve les 30 % d’éléments les mieux classés. `PivotFilterType.SUM` effectue le classement selon le cumul des valeurs.
- `isTop` — `True` pour « Haut », `False` pour « Bas ».
- `itemCount` — le nombre N dans l’expression « N premiers éléments » ; son unité dépend de `type`.

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
    # Filtre Top 10 — conserver les 2 premiers éléments par « Sum of Sales » (index du champ de données 0)
    filter = sport_field.filterTop10(0, PivotFilterType.COUNT, True, 2)
    # Pour un filtre basé sur un pourcentage, conserver plutôt les 30 % premiers éléments :
    # sport_field.filterTop10(0, PivotFilterType.PERCENT, True, 30)
    pivot_table.getPivotCache().refresh()
    pivot_table.calculateData()
    workbook.save("output-top10-filter.xlsx")
finally:
    jpype.shutdownJVM()
```

{{% alert color="primary" %}}
`top10AutoShow` et `filterTop10` sont deux fonctionnalités distinctes. AutoShow écrit l’attribut classique `autoShow` dans le champ de tableau croisé dynamique et est pris en compte par toutes les versions d’Excel, depuis Excel 97. `filterTop10` écrit une entrée `PivotFilter` moderne, qui nécessite Excel 2007 ou une version ultérieure. Lorsqu’un classeur est ouvert dans une version plus ancienne d’Excel, un tableau croisé dynamique qui utilise le filtre moderne affiche tous les éléments. Pour les documents qui doivent faire l’objet d’un aller-retour au moyen d’outils hérités, préférez `top10AutoShow` ; pour les classeurs modernes, préférez `filterTop10`, car cette méthode se combine avec les autres filtres de valeurs.
{{% /alert %}}

## **Articles connexes**
- [Filtrer les tableaux croisés dynamiques par libellé ou par valeur](/cells/fr/python-java/filter-by-label-or-value-of-pivot-table/)
- [Ajouter des champs de ligne et de colonne à un tableau croisé dynamique](/cells/fr/python-java/pivot-table-add-row-and-column-fields/)
- [Grouper les champs dans le tableau croisé dynamique](/cells/fr/python-java/group-pivot-fields-in-the-pivot-table/)
- [Actualiser le tableau croisé dynamique](/cells/fr/python-java/refresh-pivot-table/)
- [Ajouter un champ de page à un tableau croisé dynamique](/cells/fr/python-java/add-page-field-in-pivot-table/)

{{< app/cells/assistant language="python" >}}