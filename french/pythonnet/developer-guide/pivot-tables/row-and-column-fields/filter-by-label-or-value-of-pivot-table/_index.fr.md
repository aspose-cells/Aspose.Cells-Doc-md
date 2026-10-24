---
title: Filtrage des tableaux croisés dynamiques par étiquette ou par valeur
linktitle: Filtrage des tableaux croisés dynamiques par étiquette ou par valeur
description: Aspose.Cells for Python via .NET prend en charge des capacités complètes de filtrage des tableaux croisés dynamiques. Cet article explique comment filtrer les données d’un tableau croisé dynamique à l’aide de filtres d’étiquette, de date et de valeur, de filtres Top 10, ainsi que par le masquage ou l’affichage d’éléments du tableau croisé dynamique.
keywords: Aspose.Cells, bibliothèque Python via .NET, tableur, tableau croisé dynamique, filtre, filtre d’étiquette, filtre de valeur, filtre de date, filtre Top 10, élément de tableau croisé dynamique, masquer un élément de tableau croisé dynamique
type: docs
weight: 10
url: /fr/python-net/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells fournit cinq stratégies pratiques pour filtrer les données affichées dans un tableau croisé dynamique. Vous pouvez appliquer des filtres d’étiquette aux champs de ligne ou de colonne contenant du texte, utiliser des filtres de date lorsque le champ contient uniquement des cellules de date-heure ou des cellules vides, appliquer des filtres de valeur fondés sur les nombres agrégés, utiliser des filtres Top 10 pour classer les éléments selon un champ de valeur, ou masquer et réafficher manuellement des éléments individuels du tableau croisé dynamique à l’aide de la propriété `is_hidden`. Chaque stratégie est exposée par des API dédiées définies sur les classes `PivotField` et `PivotItem`.
{{% /alert %}}

## **Introduction**
Les tableaux croisés dynamiques sont de puissants outils d’analyse, mais les résumés bruts contiennent souvent beaucoup plus d’informations que vous n’avez besoin d’en présenter. Le filtrage est le principal mécanisme qui permet de restreindre un tableau croisé dynamique aux lignes, colonnes ou valeurs pertinentes pour un rapport donné. Aspose.Cells for Python via .NET reproduit les capacités de filtrage disponibles dans Microsoft Excel et les expose de manière programmatique, ce qui permet d’automatiser entièrement la génération des rapports.
Les stratégies de filtrage suivantes sont traitées dans cet article :
1. **Filtre d’étiquette** — filtre les éléments d’un champ de ligne ou de colonne en fonction de leurs libellés de texte.
2. **Filtre de date** — filtre les champs de ligne ou de colonne qui ne contiennent que des valeurs de date-heure ou des cellules vides.
3. **Filtre de valeur** — filtre les éléments en fonction des valeurs agrégées d’un champ de données.
4. **Filtre Top 10** — affiche uniquement les N éléments ayant les valeurs les plus élevées ou les plus faibles, classés selon un champ de valeur.
5. **Masquage et réaffichage des éléments du tableau croisé dynamique** — contrôle manuellement la visibilité de chaque élément dans un champ.
Chaque approche utilise une méthode différente de la classe `PivotField` ou une propriété de la classe `PivotItem`. Après l’application d’un filtre, vous devez appeler `refresh_data()` et `calculate_data()` sur le tableau croisé dynamique afin que les données mises en cache et les valeurs calculées reflètent le nouvel état du filtre.

## **Filtre d’étiquette**
Un filtre d’étiquette permet de filtrer les éléments d’un champ de ligne ou de colonne en comparant leurs libellés de texte à un motif. Cette fonction est utile lorsque vous souhaitez afficher uniquement les produits dont le nom commence par une lettre spécifique, contient un mot particulier ou correspond à un autre critère fondé sur le libellé.
Aspose.Cells expose le filtrage par étiquette au moyen de la méthode `PivotField.filter_by_label(PivotFilterType, label_string)`. L’énumération `PivotFilterType` comprend des valeurs telles que `CaptionBeginsWith`, `CaptionContains`, `CaptionEndsWith`, `CaptionDoesNotContain`, `CaptionIsNotBlank`, `CaptionIsBlank`, etc. Le deuxième argument fournit la chaîne d’étiquette utilisée pour la comparaison.
L’exemple suivant charge un classeur contenant un tableau croisé dynamique existant, applique un filtre d’étiquette afin que seuls les éléments dont les libellés commencent par un préfixe spécifié restent visibles, actualise le tableau croisé dynamique, puis enregistre le résultat.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFilterType
fileName = "sample.xlsx"
prefix = "B"
# Charger le classeur existant contenant un tableau croisé dynamique
workbook = ac.Workbook(fileName)
# Accéder à la feuille de calcul par indice (première feuille de calcul)
worksheet = workbook.worksheets[0]
# Accéder au tableau croisé dynamique par indice
pivot_table = worksheet.pivot_tables[0]
# Récupérer le premier champ PivotField de ligne
row_field = pivot_table.row_fields[0]
# Appliquer le filtre d’étiquette — afficher uniquement les éléments de ligne dont les étiquettes commencent par le préfixe fourni
row_field.filter_by_label(PivotFilterType.CAPTION_BEGINS_WITH, prefix, "")
# Actualiser et recalculer les données du tableau croisé dynamique afin que le filtre prenne effet
pivot_table.pivot_cache.refresh()
# Enregistrer le classeur sur le disque
workbook.save(fileName)
```

## **Filtre de date**
Les filtres de date permettent de réduire un tableau croisé dynamique à l’aide de critères fondés sur des dates, tels qu’aujourd’hui, la semaine dernière, ce mois-ci, le trimestre prochain ou une plage de dates spécifique. Ce sont des filtres spécialisés qui ne s’appliquent qu’aux champs contenant des informations de date-heure.

{{% alert color="primary" %}}
Le filtre de date ne fonctionne que si la zone des lignes ou des colonnes contient uniquement des cellules de date-heure ou des cellules vides. Si le champ sous-jacent contient d’autres types de données, tels que des nombres ou du texte, le filtre de date ne produira pas le résultat attendu. Avant d’appliquer ce filtre, vérifiez que le champ est mis en forme en tant que date et que toutes les valeurs correspondent à des instances `datetime` valides ou à des cellules vides.
Aspose.Cells expose le filtrage par date au moyen de la méthode `PivotField.filter_by_date(PivotFilterType, *date_times)`. L’énumération `PivotFilterType` contient des valeurs dédiées aux filtres de date, telles que `Today`, `Yesterday`, `LastWeek`, `ThisWeek`, `NextWeek`, `LastMonth`, `ThisMonth`, `NextMonth`, `LastQuarter`, `ThisQuarter`, `NextQuarter`, `LastYear`, `ThisYear`, `NextYear` et `Between`. Selon le type de filtre sélectionné, vous transmettez une ou deux valeurs `datetime` (pour `Between`, vous transmettez les dates de début et de fin).
L’exemple suivant charge un classeur contenant un tableau croisé dynamique dont la zone des lignes contient un champ de date, applique un filtre de date qui limite les éléments visibles à une plage de dates particulière, actualise le tableau croisé dynamique, puis enregistre le classeur.
{{% /alert %}}

```python
import os
import aspose.cells as ac
from datetime import datetime
from aspose.cells.pivot import PivotFilterType
input_path = "sample.xlsx"
output_path = "output_filtered.xlsx"
if not os.path.exists(input_path):
    raise FileNotFoundError("Source workbook not found.", input_path)
# Charger le classeur existant qui contient le tableau croisé dynamique
workbook = ac.Workbook(input_path)
# Accéder à la feuille de calcul qui contient le tableau croisé dynamique (par index)
worksheet = workbook.worksheets[0]
# Accéder au tableau croisé dynamique par index
pivot_table = worksheet.pivot_tables[0]
# Récupérer le PivotField de date depuis la zone des lignes
# (Le filtre de date ne fonctionne que lorsque la zone de ligne/colonne contient uniquement des cellules de date-heure ou des cellules vides)
date_field = pivot_table.row_fields[0]
# Définir le critère de date pour le filtre Entre
start_date = datetime(2020, 1, 1)
end_date = datetime(2020, 12, 31)
# Appliquer le filtre de date sur le champ pivot
date_field.filter_by_date(PivotFilterType.DATE_BETWEEN, start_date, end_date)
# Actualiser et recalculer le tableau croisé dynamique pour que le filtre prenne effet
pivot_table.pivot_cache.refresh()
# Enregistrer le classeur
workbook.save(output_path)
```

## **Filtre de valeur**
Les filtres de valeur portent sur les valeurs agrégées qu’un tableau croisé dynamique calcule dans sa zone de données. Au lieu de comparer des libellés de texte, ils comparent des totaux numériques à un seuil. Les cas d’utilisation typiques consistent à afficher soit uniquement les produits dont la somme des ventes dépasse un montant cible, soit uniquement les régions dont le nombre de transactions se situe dans une plage donnée.
Aspose.Cells expose le filtrage par valeur au moyen de la méthode `PivotField.filter_by_value(value_field, PivotFilterType, *thresholds)`. Le paramètre `PivotFilterType` accepte des valeurs telles que `ValueGreaterThan`, `ValueLessThan`, `ValueBetween`, `ValueEqual`, `ValueNotEqual`, `ValueGreaterThanOrEqual` et `ValueLessThanOrEqual`. Le paramètre `value_field` spécifie le champ de données à évaluer, et les arguments finaux fournissent le ou les seuils.
L’exemple suivant charge un classeur contenant un tableau croisé dynamique, applique un filtre de valeur qui conserve uniquement les éléments dont les ventes agrégées dépassent un seuil numérique, actualise le tableau croisé dynamique, puis enregistre le classeur.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFilterType
workbook = ac.Workbook("sample.xlsx")
worksheet = workbook.worksheets[0]
pivot_table = worksheet.pivot_tables[0]
row_field = pivot_table.row_fields[0]
data_field = pivot_table.data_fields[0]
# Rechercher manuellement l’index du champ de données, car PivotFieldCollection ne dispose pas de IndexOf
data_field_index = -1
for i in range(len(pivot_table.data_fields)):
    if pivot_table.data_fields[i] == data_field:
        data_field_index = i
        break
if data_field_index >= 0:
    row_field.filter_by_value(data_field_index, PivotFilterType.VALUE_GREATER_THAN, 5000.0, float('inf'))
pivot_table.pivot_cache.refresh()
workbook.save("output.xlsx")
```

## **Filtre Top 10**
Le filtre Top 10 est une forme spécialisée de filtre de valeur qui ne conserve que les N éléments ayant les valeurs les plus élevées ou les plus faibles, selon le champ de valeur choisi. Il est couramment utilisé pour créer des rapports de classement tels que « les 10 produits principaux en fonction du chiffre d’affaires » ou « les 5 régions les moins bien classées en fonction du nombre de ventes ».

{{% alert color="primary" %}}
Le filtre Top 10 n’est efficace que si le tableau croisé dynamique contient un ou plusieurs champs de valeur dans la zone de données. En l’absence d’au moins un champ de valeur, aucune mesure agrégée ne permet de classer les éléments et le filtre ne peut pas être appliqué.
Aspose.Cells expose le filtre Top 10 au moyen de la méthode `PivotField.filter_top_10(item_count, is_top, value_field, PivotFilterType)`. Le paramètre `item_count` définit le nombre d’éléments à conserver, `is_top` indique s’il faut conserver les éléments en tête (`True`) ou en fin de classement (`False`), `value_field` désigne le champ de données utilisé pour le classement et `PivotFilterType` contrôle le mode de calcul de la valeur (généralement `Sum`, mais aussi `Count` et `Percent`).
L’exemple suivant charge un classeur contenant un tableau croisé dynamique qui comporte un champ de valeur, applique un filtre Top 10 pour conserver uniquement les 10 éléments les plus élevés selon la somme des ventes, actualise le tableau croisé dynamique, puis enregistre le classeur.
{{% /alert %}}

```python
import aspose.cells as ac
import aspose.cells.pivot as acp
# Charger le classeur existant contenant le tableau croisé dynamique
inputPath = "input.xlsx"
outputPath = "output.xlsx"
workbook = ac.Workbook(inputPath)
# Accéder à la feuille de calcul qui contient le tableau croisé dynamique (index 0)
worksheet = workbook.worksheets[0]
# Accéder au tableau croisé dynamique par index
pivotTable = worksheet.pivot_tables[0]
# Confirmer qu’il existe au moins un PivotField de valeur dans la zone de données
if len(pivotTable.data_fields) == 0:
    raise Exception("Pivot table has no value (data) PivotField.")
valueField = pivotTable.data_fields[0]
# Récupérer le PivotField de ligne cible (le champ auquel nous voulons appliquer Top 10)
rowField = pivotTable.row_fields[0]
# Le premier (et unique) champ de données se trouve à l’index 0 ; Top 10 classe les éléments en fonction de celui-ci.
valueFieldIndex = 0
# Appliquer le filtre Top 10 sur le champ de ligne :
#   - itemCount   = 10
#   - filterType  = PivotFilterType.SUM
#   - isTop       = true (N premiers ; false signifierait N derniers)
#   - valueFieldIndex = index du champ de données utilisé pour classer les éléments
rowField.filter_top10(10, acp.PivotFilterType.SUM, True, valueFieldIndex)
# Actualiser les données du tableau croisé dynamique et le recalculer afin que le filtre prenne effet
pivotTable.pivot_cache.refresh()
# Enregistrer le classeur
workbook.save(outputPath)
```

## **Filtrage par masquage ou réaffichage des éléments du tableau croisé dynamique**
Outre les API de filtrage structuré, Aspose.Cells vous permet de contrôler directement la visibilité de chaque élément individuel du tableau croisé dynamique. En parcourant la collection `PivotItems` d’un `PivotField` et en basculant la propriété `is_hidden`, vous pouvez masquer sélectivement des éléments spécifiques sans appliquer de filtre fondé sur une formule. La définition de `is_hidden = True` masque l’élément du tableau croisé dynamique ; la définition de `is_hidden = False` le réaffiche.
Cette approche est utile lorsque la règle de filtrage est irrégulière ou spécifique à un élément, par exemple pour masquer quelques catégories désignées par leur nom qui ne doivent pas apparaître dans un rapport particulier. L’exemple ci-dessous charge un tableau croisé dynamique, masque un élément spécifique par son nom, montre comment le réafficher, actualise le tableau croisé dynamique, puis enregistre le classeur.

```python
import aspose.cells as ac
# Charger un classeur existant contenant un tableau croisé dynamique
workbook = ac.Workbook("pivot_table_sample.xlsx")
# Accéder à la première feuille de calcul qui contient le tableau croisé dynamique
sheet = workbook.worksheets[0]
# Accéder au tableau croisé dynamique par index (le premier tableau croisé dynamique de la feuille)
pivot_table = sheet.pivot_tables[0]
# Récupérer le champ PivotField cible (le premier champ d’étiquette de ligne dans lequel nous masquerons ou afficherons des éléments)
pivot_field = pivot_table.row_fields[0]
# Parcourir la collection PivotItems du PivotField sélectionné
item_count = pivot_field.pivot_items.count
for i in range(item_count):
    item = pivot_field.pivot_items[i]
    # Masquer les éléments du tableau croisé dynamique qui correspondent à un nom ou critère spécifique
    if item.name == "Item1" or item.name == "Item2":
        item.is_hidden = True
    # Démontrer comment afficher de nouveau un élément du tableau croisé dynamique précédemment masqué
    if item.name == "Item3":
        item.is_hidden = False
# Actualiser et recalculer le tableau croisé dynamique afin que les modifications prennent effet
pivot_table.pivot_cache.refresh()
# Enregistrer le classeur — les éléments masqués restent dans les données sous-jacentes
# mais sont exclus de la sortie du tableau croisé dynamique affiché
workbook.save("output_pivot_filtered.xlsx")
```

## **Résumé**
Aspose.Cells for Python via .NET fournit un ensemble complet de fonctionnalités de filtrage des tableaux croisés dynamiques, comparables à celles disponibles dans Microsoft Excel. Les filtres d’étiquette, de date et de valeur couvrent les scénarios analytiques les plus courants, tandis que le filtre Top 10 gère les rapports de classement. Lorsque la règle de filtrage est irrégulière, la propriété `PivotItem.is_hidden` offre une solution de repli flexible à l’échelle de l’élément. La combinaison de ces stratégies — par exemple, l’application d’un filtre d’étiquette suivie du masquage d’éléments spécifiques — vous permet de créer, entièrement à partir du code, des rapports de tableaux croisés dynamiques ciblés avec précision.

## Articles connexes
- [Insérer un tableau croisé dynamique](/cells/fr/python-net/create-pivot-table/)
- [Ajouter des champs de ligne et de colonne à un tableau croisé dynamique dans Aspose.Cells for Python via .NET](/cells/fr/python-net/pivot-table-add-row-and-column-fields/)
- [Ajouter des champs de filtre à un tableau croisé dynamique dans Aspose.Cells for Python via .NET](/cells/fr/python-net/add-page-field-in-pivot-table/)
- [Gérer les champs de valeur d’un tableau croisé dynamique dans Aspose.Cells for Python via .NET](/cells/fr/python-net/manage-value-fields/)
- [Actualiser les tableaux croisés dynamiques et les caches de tableaux croisés dynamiques dans Aspose.Cells for Python via .NET](/cells/fr/python-net/refresh-pivot-table/)

{{< app/cells/assistant language="python-net" >}}