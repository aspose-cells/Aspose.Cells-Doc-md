---
title: Filtrage des tableaux croisés dynamiques par étiquette ou valeur
description: Aspose.Cells for Python via Java offre des capacités complètes de filtrage des tableaux croisés dynamiques. Cet article explique comment filtrer les données d'un tableau croisé dynamique à l'aide de filtres d'étiquettes, de filtres de dates, de filtres de valeurs, des filtres des 10 premiers, et en masquant ou affichant des éléments du tableau croisé dynamique.
linktitle: Filtrage des tableaux croisés dynamiques par étiquette ou valeur
keywords: Aspose.Cells, bibliothèque Python via Java, tableur, tableau croisé dynamique, filtre, filtre d'étiquette, filtre de valeur, filtre de date, filtre des 10 premiers, élément de tableau croisé dynamique, masquer un élément de tableau croisé dynamique
type: docs
weight: 10
url: /fr/python-java/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells propose cinq stratégies pratiques pour filtrer les données affichées dans un tableau croisé dynamique. Vous pouvez appliquer des filtres d'étiquettes aux champs de ligne ou de colonne textuels, utiliser des filtres de date lorsque le champ contient uniquement des cellules de date et d'heure ou des cellules vides, appliquer des filtres de valeur sur des nombres agrégés, utiliser les filtres des 10 premiers pour classer selon un champ de valeur, ou masquer et afficher manuellement des éléments individuels du tableau croisé dynamique à l'aide de la propriété `is_hidden`. Chaque stratégie est exposée via des API dédiées sur les classes `PivotField` et `PivotItem`.
{{% /alert %}}

## **Introduction**
Les tableaux croisés dynamiques sont des outils analytiques puissants, mais les résumés bruts contiennent souvent bien plus d'informations que vous n'avez besoin de présenter. Le filtrage est le principal mécanisme permettant de restreindre un tableau croisé dynamique aux lignes, colonnes ou valeurs pertinentes pour un rapport spécifique. Aspose.Cells for Python via Java reproduit les capacités de filtrage disponibles dans Microsoft Excel, en les exposant par programmation afin que la génération de rapports puisse être entièrement automatisée.
Les stratégies de filtrage suivantes sont abordées dans cet article :
1. **Filtre d'étiquette** — filtre les éléments des champs de ligne ou de colonne en fonction de leurs étiquettes textuelles.
2. **Filtre de date** — filtre les champs de ligne ou de colonne qui contiennent uniquement des valeurs de date et d'heure (ou des valeurs vides).
3. **Filtre de valeur** — filtre les éléments en fonction des valeurs agrégées d'un champ de données.
4. **Filtre des 10 premiers** — n'affiche que les N premiers ou N derniers éléments classés selon un champ de valeur.
5. **Masquer / Afficher les éléments du tableau croisé dynamique** — contrôle manuellement la visibilité de chaque élément individuel dans un champ.
Chaque approche utilise une méthode différente de la classe `PivotField` ou une propriété de la classe `PivotItem`. Après avoir appliqué un filtre, vous devez appeler `refresh_data()` et `calculate_data()` sur le tableau croisé dynamique afin que les données mises en cache et les valeurs calculées reflètent le nouvel état du filtre.

## **Filtre d'étiquette**
Un filtre d'étiquette vous permet de filtrer les éléments d'un champ de ligne ou de colonne en comparant leurs légendes textuelles à un modèle. Cela est utile lorsque vous souhaitez afficher uniquement les produits dont les noms commencent par une lettre spécifique, contiennent un mot particulier ou correspondent à tout autre critère basé sur les légendes.
Aspose.Cells expose le filtrage par étiquette via la méthode `PivotField.filter_by_label(PivotFilterType, str)`. L'énumération `PivotFilterType` inclut des valeurs telles que `CaptionBeginsWith`, `CaptionContains`, `CaptionEndsWith`, `CaptionDoesNotContain`, `CaptionIsNotBlank`, `CaptionIsBlank`, et ainsi de suite. Le deuxième argument fournit la chaîne d'étiquette utilisée pour la comparaison.
L'exemple suivant charge un classeur contenant un tableau croisé dynamique existant, applique un filtre d'étiquette de sorte que seuls les éléments dont les légendes commencent par un préfixe spécifié restent visibles, actualise le tableau croisé dynamique et enregistre le résultat.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, PivotFilterType
fileName = "sample.xlsx"
prefix = "B"
# Load the existing workbook containing a pivot table
workbook = Workbook(fileName)
# Access the worksheet by index (first worksheet)
worksheet = workbook.getWorksheets().get(0)
# Access the pivot table by index
pivotTable = worksheet.getPivotTables().get(0)
# Retrieve the first row PivotField
rowField = pivotTable.getRowFields().get(0)
# Apply the label filter — show only row items whose labels begin with the supplied prefix
rowField.filterByLabel(PivotFilterType.CAPTION_BEGINS_WITH, prefix, "")
# Refresh and recalculate the pivot table data so the filter takes effect
pivotTable.getPivotCache().refresh()
# Save the workbook back to disk
workbook.save(fileName)
jpype.shutdownJVM()
```

## **Filtre de date**
Les filtres de date vous permettent de restreindre un tableau croisé dynamique selon des critères basés sur la date, tels qu'aujourd'hui, la semaine dernière, ce mois-ci, le trimestre suivant ou une plage de dates spécifique. Ce sont des filtres spécialisés qui fonctionnent uniquement contre les champs stockant des informations de date et d'heure.

{{% alert color="primary" %}}
Le filtre de date ne fonctionne que lorsque la zone de ligne ou de colonne contient uniquement des cellules de date et d'heure ou des valeurs vides. Si le champ sous-jacent contient d'autres types de données tels que des nombres ou du texte, le filtre de date ne produira pas le résultat attendu. Assurez-vous que le champ est formaté en tant que date et que toutes les valeurs sont des instances valides de `DateTime` ou des cellules vides avant d'appliquer ce filtre.
Aspose.Cells expose le filtrage par date via la méthode `PivotField.filter_by_date(PivotFilterType, values)`. L'énumération `PivotFilterType` contient des valeurs de date dédiées telles que `Today`, `Yesterday`, `LastWeek`, `ThisWeek`, `NextWeek`, `LastMonth`, `ThisMonth`, `NextMonth`, `LastQuarter`, `ThisQuarter`, `NextQuarter`, `LastYear`, `ThisYear`, `NextYear` et `Between`. Selon le type de filtre choisi, vous passez une ou deux valeurs `DateTime` (pour `Between`, vous passez les dates de début et de fin).
L'exemple suivant charge un classeur contenant un tableau croisé dynamique dont la zone de ligne contient un champ de date, applique un filtre de date qui restreint les éléments visibles à une plage de dates particulière, actualise le tableau croisé dynamique et enregistre le classeur.
{{% /alert %}}

```python
import jpype
import os
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, PivotFilterType
inputPath = "sample.xlsx"
outputPath = "output_filtered.xlsx"
if not os.path.exists(inputPath):
    raise FileNotFoundError(f"Source workbook not found: {inputPath}")
# Load the existing workbook that contains the pivot table
workbook = Workbook(inputPath)
# Access the worksheet that holds the pivot table (by index)
worksheet = workbook.getWorksheets().get(0)
# Access the pivot table by index
pivotTable = worksheet.getPivotTables().get(0)
# Retrieve the date PivotField from the row area
# (Date filter only works when the row/column area contains only date-time cells or blanks)
dateField = pivotTable.getRowFields().get(0)
# Define the date criterion for the Between filter
Date = jpype.JClass("java.util.Date")
startDate = Date(2020 - 1900, 0, 1)
endDate = Date(2020 - 1900, 11, 31)
# Apply the date filter on the pivot field
dateField.filterByDate(PivotFilterType.DATE_BETWEEN, startDate, endDate)
# Refresh and recalculate the pivot table so the filter takes effect
pivotTable.getPivotCache().refresh()
# Persist the workbook
workbook.save(outputPath)
jpype.shutdownJVM()
```

## **Filtre de valeur**
Les filtres de valeur opèrent sur les valeurs agrégées qu'un tableau croisé dynamique calcule dans sa zone de données. Au lieu de faire correspondre des étiquettes textuelles, ils comparent des totaux numériques à un seuil. Les cas d'utilisation typiques incluent l'affichage uniquement des produits dont la somme des ventes dépasse un montant cible ou uniquement des régions dont le nombre de transactions se situe dans une plage.
Aspose.Cells expose le filtrage par valeur via la méthode `PivotField.filter_by_value(value_field, filter_type, values)`. Le paramètre `filter_type` utilise des valeurs telles que `ValueGreaterThan`, `ValueLessThan`, `ValueBetween`, `ValueEqual`, `ValueNotEqual`, `ValueGreaterThanOrEqual` et `ValueLessThanOrEqual`. Le paramètre `value_field` spécifie quel champ de données doit être évalué, et le ou les derniers arguments fournissent la ou les valeurs seuils.
L'exemple suivant charge un classeur contenant un tableau croisé dynamique, applique un filtre de valeur qui ne conserve que les éléments dont les ventes agrégées dépassent un seuil numérique, actualise le tableau croisé dynamique et enregistre le classeur.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, PivotFilterType
workbook = Workbook("sample.xlsx")
worksheet = workbook.getWorksheets().get(0)
pivotTable = worksheet.getPivotTables().get(0)
rowField = pivotTable.getRowFields().get(0)
dataField = pivotTable.getDataFields().get(0)
# Find the data field index manually since PivotFieldCollection doesn't have IndexOf
dataFieldIndex = -1
for i in range(pivotTable.getDataFields().getCount()):
    if pivotTable.getDataFields().get(i) == dataField:
        dataFieldIndex = i
        break
if dataFieldIndex >= 0:
    rowField.filterByValue(dataFieldIndex, PivotFilterType.VALUE_GREATER_THAN, 5000, float('inf'))
pivotTable.getPivotCache().refresh()
workbook.save("output.xlsx")
jpype.shutdownJVM()
```

## **Filtre des 10 premiers**
Le filtre des 10 premiers est une forme spécialisée de filtre de valeur qui ne conserve que les N premiers ou N derniers éléments en fonction d'un champ de valeur choisi. Il est couramment utilisé pour les rapports de classement tels que « les 10 meilleurs produits par chiffre d'affaires » ou « les 5 régions les plus faibles par nombre de ventes ».

{{% alert color="primary" %}}
Le filtre des 10 premiers n'est efficace que lorsque le tableau croisé dynamique possède un ou plusieurs champs de valeur dans la zone de données. Sans au moins un champ de valeur, il n'y a aucune mesure agrégée permettant de classer les éléments, et le filtre ne peut pas être appliqué.
Aspose.Cells expose le filtrage Top 10 via la méthode `PivotField.filterTop10(valueFieldIndex, filterType, isTop, itemCount)`. Le paramètre `valueFieldIndex` est l'index du champ de données dont les valeurs agrégées classent les éléments, `filterType` sélectionne l'unité de `itemCount` (`PivotFilterType.COUNT` conserve un nombre fixe d'éléments, `PivotFilterType.PERCENT` conserve un pourcentage des éléments, de sorte que `itemCount` est le pourcentage lui-même), `isTop` indique s'il faut conserver les premiers éléments (true) ou les derniers (false), et `itemCount` définit combien d'éléments, ou quel pourcentage, conserver.
L'exemple suivant charge un classeur contenant un tableau croisé dynamique qui contient un champ de valeur, applique un filtre des 10 premiers pour ne conserver que les 10 éléments les plus élevés par somme des ventes, actualise le tableau croisé dynamique et enregistre le classeur.
{{% /alert %}}

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, PivotTable, PivotField, PivotFilterType
# Load the existing workbook that contains the pivot table
inputPath = "input.xlsx"
outputPath = "output.xlsx"
workbook = Workbook(inputPath)
# Access the worksheet that holds the pivot table (index 0)
worksheet = workbook.getWorksheets().get(0)
# Access the pivot table by index
pivotTable = worksheet.getPivotTables().get(0)
# Confirm there is at least one value PivotField in the data area
if pivotTable.getDataFields().getCount() == 0:
    raise Exception("Pivot table has no value (data) PivotField.")
valueField = pivotTable.getDataFields().get(0)
# Retrieve the target row PivotField (the field we want to apply Top 10 on)
rowField = pivotTable.getRowFields().get(0)
# The first (and only) data field is at index 0; Top 10 ranks by it.
valueFieldIndex = 0
# Apply the Top 10 filter on the row field:
#   - itemCount   = 10
#   - filterType  = PivotFilterType.SUM
#   - isTop       = true (top N; false would mean bottom N)
#   - valueFieldIndex = the index of the data field used to rank items
rowField.filterTop10(valueFieldIndex, PivotFilterType.COUNT, True, 10)
# Refresh the pivot table data and recalculate it so the filter takes effect
pivotTable.getPivotCache().refresh()
# Save the workbook
workbook.save(outputPath)
jpype.shutdownJVM()
```

## **Filtrage par masquage ou affichage des éléments du tableau croisé dynamique**
En plus des API de filtrage structurées, Aspose.Cells vous permet de contrôler directement la visibilité de chaque élément individuel du tableau croisé dynamique. En parcourant la collection `PivotItems` d'un `PivotField` et en basculant la propriété `is_hidden`, vous pouvez supprimer sélectivement des éléments spécifiques sans appliquer un filtre basé sur une formule. Définir `is_hidden = True` masque l'élément du tableau croisé dynamique ; définir `is_hidden = False` l'affiche à nouveau et le rend visible.
Cette approche est utile lorsque la règle de filtrage est irrégulière ou spécifique à un élément, par exemple masquer un petit nombre de catégories nommées qui ne doivent pas apparaître dans un rapport particulier. L'exemple ci-dessous charge un tableau croisé dynamique, masque un élément spécifique par son nom, montre comment l'afficher à nouveau, actualise le tableau croisé dynamique et enregistre le classeur.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotTable, PivotField, PivotItem
# Load an existing workbook containing a pivot table
workbook = Workbook("pivot_table_sample.xlsx")
# Access the first worksheet which contains the pivot table
sheet = workbook.getWorksheets().get(0)
# Access the pivot table by index (the first pivot table on the sheet)
pivotTable = sheet.getPivotTables().get(0)
# Retrieve the target PivotField (the first row label field that we'll hide/unhide items in)
pivotField = pivotTable.getRowFields().get(0)
# Iterate through the PivotItems collection of the selected PivotField
itemCount = pivotField.getPivotItems().getCount()
for i in range(itemCount):
    item = pivotField.getPivotItems().get(i)
    # Hide pivot items that match a specific name/criterion
    if item.getName() == "Item1" or item.getName() == "Item2":
        item.setHidden(True)
    # Demonstrate unhiding: re-show a previously hidden pivot item
    if item.getName() == "Item3":
        item.setHidden(False)
# Refresh and recalculate the pivot table so changes take effect
pivotTable.getPivotCache().refresh()
# Save the workbook — hidden items stay in the underlying data
# but are excluded from the displayed pivot table output
workbook.save("output_pivot_filtered.xlsx")
jpype.shutdownJVM()
```

## **Résumé**
Aspose.Cells for Python via Java fournit un ensemble complet de capacités de filtrage des tableaux croisés dynamiques qui correspondent à celles que l'on trouve dans Microsoft Excel. Les filtres d'étiquette, de date et de valeur couvrent les scénarios analytiques les plus courants, tandis que le filtre des 10 premiers gère les rapports de classement. Lorsque la règle de filtrage est irrégulière, la propriété `PivotItem.is_hidden` offre une solution de secours flexible au niveau des éléments. La combinaison de ces stratégies — par exemple, appliquer un filtre d'étiquette puis masquer des éléments spécifiques — vous permet de créer des rapports de tableau croisé dynamique précisément ciblés entièrement à partir du code.

{{< app/cells/assistant language="python" >}}