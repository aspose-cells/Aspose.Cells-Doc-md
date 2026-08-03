---
title: Filtrage des tableaux croisés dynamiques par étiquette ou valeur
linktitle: Filtrage des tableaux croisés dynamiques par étiquette ou valeur
description: Aspose.Cells for Python via Java offre des capacités complètes de filtrage des tableaux croisés dynamiques. Cet article explique comment filtrer les données d'un tableau croisé dynamique à l'aide de filtres d'étiquettes, de filtres de dates, de filtres de valeurs, des filtres des 10 premiers, et en masquant ou affichant des éléments du tableau croisé dynamique.
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
from asposecells.api import Workbook
from asposecells.api import Workbook, PivotFilterType

fileName = "sample.xlsx"
prefix = "B"

# Charger le classeur existant contenant un tableau croisé dynamique
workbook = Workbook(fileName)

# Accéder à la feuille de calcul par index (première feuille)
worksheet = workbook.getWorksheets().get(0)

# Accéder au tableau croisé dynamique par index
pivotTable = worksheet.getPivotTables().get(0)

# Récupérer le premier PivotField de ligne
rowField = pivotTable.getRowFields().get(0)

# Appliquer le filtre d'étiquette — afficher uniquement les éléments de ligne dont les étiquettes commencent par le préfixe fourni
rowField.filterByLabel(PivotFilterType.CaptionBeginsWith, prefix, "")

# Actualiser et recalculer les données du tableau croisé dynamique pour que le filtre prenne effet
pivotTable.getPivotCache().refresh()

# Enregistrer le classeur sur le disque
workbook.save(fileName)

jpype.shutdownJVM()
```
## **Filtre de date**
Les filtres de date vous permettent de restreindre un tableau croisé dynamique selon des critères basés sur la date, tels qu'aujourd'hui, la semaine dernière, ce mois-ci, le trimestre suivant ou une plage de dates spécifique. Ce sont des filtres spécialisés qui fonctionnent uniquement contre les champs stockant des informations de date et d'heure.
{{% alert color="primary" %}}
Le filtre de date ne fonctionne que lorsque la zone de ligne ou de colonne contient uniquement des cellules de date et d'heure ou des valeurs vides. Si le champ sous-jacent contient d'autres types de données tels que des nombres ou du texte, le filtre de date ne produira pas le résultat attendu. Assurez-vous que le champ est formaté en tant que date et que toutes les valeurs sont des instances valides de `DateTime` ou des cellules vides avant d'appliquer ce filtre.
{{% /alert %}}
Aspose.Cells expose le filtrage par date via la méthode `PivotField.filter_by_date(PivotFilterType, values)`. L'énumération `PivotFilterType` contient des valeurs de date dédiées telles que `Today`, `Yesterday`, `LastWeek`, `ThisWeek`, `NextWeek`, `LastMonth`, `ThisMonth`, `NextMonth`, `LastQuarter`, `ThisQuarter`, `NextQuarter`, `LastYear`, `ThisYear`, `NextYear` et `Between`. Selon le type de filtre choisi, vous passez une ou deux valeurs `DateTime` (pour `Between`, vous passez les dates de début et de fin).
L'exemple suivant charge un classeur contenant un tableau croisé dynamique dont la zone de ligne contient un champ de date, applique un filtre de date qui restreint les éléments visibles à une plage de dates particulière, actualise le tableau croisé dynamique et enregistre le classeur.
```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, PivotFilterType

inputPath = "sample.xlsx"
outputPath = "output_filtered.xlsx"

if not os.path.exists(inputPath):
    raise FileNotFoundError(f"Source workbook not found: {inputPath}")

# Charger le classeur existant qui contient le tableau croisé dynamique
workbook = Workbook(inputPath)

# Accéder à la feuille de calcul qui contient le tableau croisé dynamique (par index)
worksheet = workbook.getWorksheets().get(0)

# Accéder au tableau croisé dynamique par index
pivotTable = worksheet.getPivotTables().get(0)

# Récupérer le PivotField de date depuis la zone des lignes
# (Le filtre de date ne fonctionne que lorsque la zone de ligne/colonne ne contient que des cellules de date-heure ou des cellules vides)
dateField = pivotTable.getRowFields().get(0)

# Définir le critère de date pour le filtre Entre
Date = jpype.JClass("java.util.Date")
startDate = Date(2020 - 1900, 0, 1)
endDate = Date(2020 - 1900, 11, 31)

# Appliquer le filtre de date sur le champ croisé dynamique
dateField.filterByDate(PivotFilterType.DateBetween, startDate, endDate)

# Actualiser et recalculer le tableau croisé dynamique pour que le filtre prenne effet
pivotTable.getPivotCache().refresh()

# Enregistrer le classeur
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
from asposecells.api import Workbook
from asposecells.api import Workbook, PivotFilterType

workbook = Workbook("sample.xlsx")
worksheet = workbook.getWorksheets().get(0)
pivotTable = worksheet.getPivotTables().get(0)

rowField = pivotTable.getRowFields().get(0)
dataField = pivotTable.getDataFields().get(0)

# Trouver l'index du champ de données manuellement car PivotFieldCollection n'a pas de IndexOf
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
{{% /alert %}}
Aspose.Cells expose le filtrage des 10 premiers via la méthode `PivotField.filter_top10(item_count, is_top, value_field, filter_type)`. Le paramètre `item_count` définit combien d'éléments conserver, `is_top` indique s'il faut conserver les premiers éléments (true) ou les derniers éléments (false), `value_field` fait référence au champ de données utilisé pour le classement, et `filter_type` contrôle la manière dont la valeur est calculée (généralement `Sum`, mais aussi `Count` et `Percent`).
L'exemple suivant charge un classeur contenant un tableau croisé dynamique qui contient un champ de valeur, applique un filtre des 10 premiers pour ne conserver que les 10 éléments les plus élevés par somme des ventes, actualise le tableau croisé dynamique et enregistre le classeur.
```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, PivotTable, PivotField, PivotFilterType

# Charger le classeur existant qui contient le tableau croisé dynamique
inputPath = "input.xlsx"
outputPath = "output.xlsx"
workbook = Workbook(inputPath)

# Accéder à la feuille de calcul qui contient le tableau croisé dynamique (index 0)
worksheet = workbook.getWorksheets().get(0)

# Accéder au tableau croisé dynamique par index
pivotTable = worksheet.getPivotTables().get(0)

# Vérifier qu'il y a au moins un PivotField de valeur dans la zone de données
if pivotTable.getDataFields().getCount() == 0:
    raise Exception("Pivot table has no value (data) PivotField.")
valueField = pivotTable.getDataFields().get(0)

# Récupérer le PivotField de ligne cible (le champ auquel nous voulons appliquer Top 10)
rowField = pivotTable.getRowFields().get(0)

# Le premier (et seul) champ de données est à l'index 0 ; Top 10 classe par celui-ci.
valueFieldIndex = 0

# Appliquer le filtre Top 10 sur le champ de ligne :
#   - itemCount   = 10
#   - filterType  = PivotFilterType.Sum
#   - isTop       = true (N premiers ; false signifierait N derniers)
#   - valueFieldIndex = l'index du champ de données utilisé pour classer les éléments
rowField.filterTop10(10, PivotFilterType.Sum, True, valueFieldIndex)

# Actualiser les données du tableau croisé dynamique et le recalculer pour que le filtre prenne effet
pivotTable.getPivotCache().refresh()

# Enregistrer le classeur
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
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotTable, PivotField, PivotItem

# Charger un classeur existant contenant un tableau croisé dynamique
workbook = Workbook("pivot_table_sample.xlsx")

# Accéder à la première feuille de calcul qui contient le tableau croisé dynamique
sheet = workbook.getWorksheets().get(0)

# Accéder au tableau croisé dynamique par index (le premier tableau croisé dynamique de la feuille)
pivotTable = sheet.getPivotTables().get(0)

# Récupérer le PivotField cible (le premier champ d'étiquette de ligne dans lequel nous allons masquer/afficher des éléments)
pivotField = pivotTable.getRowFields().get(0)

# Parcourir la collection PivotItems du PivotField sélectionné
itemCount = pivotField.getPivotItems().getCount()
for i in range(itemCount):
    item = pivotField.getPivotItems().get(i)

    # Masquer les éléments du tableau croisé dynamique qui correspondent à un nom ou critère spécifique
    if item.getName() == "Item1" or item.getName() == "Item2":
        item.setIsHidden(True)

    # Démontrer l'affichage : réafficher un élément précédemment masqué du tableau croisé dynamique
    if item.getName() == "Item3":
        item.setIsHidden(False)

# Actualiser et recalculer le tableau croisé dynamique pour que les modifications prennent effet
pivotTable.getPivotCache().refresh()

# Enregistrer le classeur — les éléments masqués restent dans les données sous-jacentes
# mais sont exclus de l'affichage du tableau croisé dynamique
workbook.save("output_pivot_filtered.xlsx")

jpype.shutdownJVM()
```
## **Résumé**
Aspose.Cells for Python via Java fournit un ensemble complet de capacités de filtrage des tableaux croisés dynamiques qui correspondent à celles que l'on trouve dans Microsoft Excel. Les filtres d'étiquette, de date et de valeur couvrent les scénarios analytiques les plus courants, tandis que le filtre des 10 premiers gère les rapports de classement. Lorsque la règle de filtrage est irrégulière, la propriété `PivotItem.is_hidden` offre une solution de secours flexible au niveau des éléments. La combinaison de ces stratégies — par exemple, appliquer un filtre d'étiquette puis masquer des éléments spécifiques — vous permet de créer des rapports de tableau croisé dynamique précisément ciblés entièrement à partir du code.
{{< app/cells/assistant language="python" >}}