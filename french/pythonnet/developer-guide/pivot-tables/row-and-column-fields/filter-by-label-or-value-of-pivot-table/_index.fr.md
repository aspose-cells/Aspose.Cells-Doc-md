---
title: Filtrer les tableaux croisés dynamiques par étiquette ou valeur
linktitle: Filtrer par étiquette ou valeur
description: Aspose.Cells for Python via .NET prend en charge des fonctions complètes de filtrage des tableaux croisés dynamiques. Cet article explique le filtrage par étiquette, date, valeur, top 10 et par masquage ou affichage des éléments.
keywords: Aspose.Cells, bibliothèque Python via .NET, feuille de calcul, tableau croisé dynamique, filtre, filtre d'étiquette, filtre de valeur, filtre de date, filtre top 10, élément de tableau croisé dynamique, masquer élément de tableau croisé dynamique
type: docs
weight: 10
url: /fr/python-net/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Aspose.Cells propose cinq stratégies pratiques pour filtrer les données affichées dans un tableau croisé dynamique. Vous pouvez appliquer des filtres d'étiquettes aux champs de ligne ou de colonne contenant du texte, utiliser des filtres de dates lorsque le champ ne contient que des cellules de type date-heure ou des cellules vides, appliquer des filtres de valeurs sur les nombres agrégés, utiliser des filtres top 10 pour classer les données selon un champ de valeur, ou masquer et afficher manuellement des éléments individuels à l'aide de la propriété `is_hidden`. Chaque stratégie est exposée via des API dédiées sur les classes `PivotField` et `PivotItem`.

{{% alert color="primary" %}}
{{% /alert %}}

## **Introduction**

Les tableaux croisés dynamiques sont des outils d'analyse puissants, mais les synthèses brutes contiennent souvent bien plus d'informations que ce dont vous avez besoin pour une présentation. Le filtrage est le principal mécanisme permettant de réduire un tableau croisé dynamique aux lignes, colonnes ou valeurs pertinentes pour un rapport spécifique. Aspose.Cells for Python via .NET reproduit les capacités de filtrage disponibles dans Microsoft Excel, en les exposant par programmation afin que la génération de rapports puisse être entièrement automatisée.

Les stratégies de filtrage suivantes sont présentées dans cet article :

1. **Filtre d'étiquette** — filtre les éléments des champs de ligne ou de colonne en fonction de leurs étiquettes textuelles.
2. **Filtre de date** — filtre les champs de ligne ou de colonne qui ne contiennent que des valeurs de date-heure (ou des cellules vides).
3. **Filtre de valeur** — filtre les éléments en fonction des valeurs agrégées d'un champ de données.
4. **Filtre top 10** — affiche uniquement les N premiers ou N derniers éléments classés selon un champ de valeur.
5. **Masquer / Afficher des éléments du tableau croisé dynamique** — contrôle manuellement la visibilité de chaque élément individuel d'un champ.

Chaque approche utilise une méthode différente de la classe `PivotField` ou une propriété de la classe `PivotItem`. Après l'application de tout filtre, vous devez appeler `refresh_data()` et `calculate_data()` sur le tableau croisé dynamique afin que les données mises en cache et les valeurs calculées reflètent le nouvel état du filtre.

## **Filtre d'étiquette**

Un filtre d'étiquette vous permet de filtrer les éléments d'un champ de ligne ou de colonne en comparant leurs libellés textuels à un motif. Cela est utile lorsque vous souhaitez afficher uniquement les produits dont les noms commencent par une lettre spécifique, contiennent un mot particulier, ou correspondent à un autre critère basé sur le libellé.

Aspose.Cells expose le filtrage par étiquette via la méthode `PivotField.filter_by_label(PivotFilterType, label_string)`. L'énumération `PivotFilterType` inclut des valeurs telles que `CaptionBeginsWith`, `CaptionContains`, `CaptionEndsWith`, `CaptionDoesNotContain`, `CaptionIsNotBlank`, `CaptionIsBlank`, etc. Le deuxième argument fournit la chaîne de libellé utilisée pour la comparaison.

L'exemple suivant charge un classeur contenant un tableau croisé dynamique existant, applique un filtre d'étiquette afin que seuls les éléments dont les libellés commencent par un préfixe spécifié restent visibles, actualise le tableau croisé dynamique et enregistre le résultat.

```python
import aspose.cells as ac

fileName = "sample.xlsx"
prefix = "B"

# Charger le classeur existant contenant un tableau croisé dynamique
workbook = ac.Workbook(fileName)

# Accéder à la feuille de calcul par index (première feuille de calcul)
worksheet = workbook.worksheets[0]

# Accéder au tableau croisé dynamique par index
pivot_table = worksheet.pivot_tables[0]

# Récupérer le premier PivotField de ligne
row_field = pivot_table.row_fields[0]

# Appliquer le filtre d'étiquette — afficher uniquement les éléments de ligne dont les étiquettes commencent par le préfixe fourni
row_field.filter_by_label(ac.PivotFilterType.CAPTION_BEGINS_WITH, prefix, "")

# Actualiser et recalculer les données du tableau croisé dynamique pour que le filtre prenne effet
pivot_table.pivot_cache.refresh()

# Enregistrer le classeur sur le disque
workbook.save(fileName)
```

## **Filtre de date**

Les filtres de date vous permettent de restreindre un tableau croisé dynamique selon des critères basés sur les dates, tels qu'aujourd'hui, la semaine dernière, ce mois-ci, le trimestre prochain, ou une plage de dates spécifique. Ce sont des filtres spécialisés qui fonctionnent uniquement sur les champs stockant des informations de date-heure.

{{% alert color="primary" %}}

Le filtre de date ne fonctionne que lorsque la zone de ligne ou de colonne contient uniquement des cellules de type date-heure ou des cellules vides. Si le champ sous-jacent contient d'autres types de données tels que des nombres ou du texte, le filtre de date ne produira pas le résultat escompté. Assurez-vous que le champ est formaté en tant que date et que toutes les valeurs sont des instances `DateTime` valides ou des cellules vides avant d'appliquer ce filtre.

{{% /alert %}}

Aspose.Cells expose le filtrage par date via la méthode `PivotField.filter_by_date(PivotFilterType, *date_times)`. L'énumération `PivotFilterType` contient des valeurs de date dédiées telles que `Today`, `Yesterday`, `LastWeek`, `ThisWeek`, `NextWeek`, `LastMonth`, `ThisMonth`, `NextMonth`, `LastQuarter`, `ThisQuarter`, `NextQuarter`, `LastYear`, `ThisYear`, `NextYear`, et `Between`. Selon le type de filtre choisi, vous transmettez une ou deux valeurs `DateTime` (pour `Between`, vous transmettez les dates de début et de fin).

L'exemple suivant charge un classeur contenant un tableau croisé dynamique dont la zone de ligne contient un champ de date, applique un filtre de date qui restreint les éléments visibles à une plage de dates particulière, actualise le tableau croisé dynamique et enregistre le classeur.

```python
import datetime

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
# (Le filtre de date fonctionne uniquement lorsque la zone ligne/colonne contient uniquement des cellules date-heure ou des vides)
date_field = pivot_table.row_fields[0]

# Définir le critère de date pour le filtre Between
start_date = datetime(2020, 1, 1)
end_date = datetime(2020, 12, 31)

# Appliquer le filtre de date sur le champ pivot
date_field.filter_by_date(ac.PivotFilterType.DATE_BETWEEN, start_date, end_date)

# Actualiser et recalculer le tableau croisé dynamique pour que le filtre prenne effet
pivot_table.pivot_cache.refresh()

# Persister le classeur
workbook.save(output_path)
```

## **Filtre de valeur**

Les filtres de valeur opèrent sur les valeurs agrégées qu'un tableau croisé dynamique calcule dans sa zone de données. Au lieu de faire correspondre des étiquettes textuelles, ils comparent les totaux numériques à un seuil. Les cas d'utilisation typiques incluent l'affichage uniquement des produits dont la somme des ventes dépasse un montant cible, ou uniquement des régions dont le nombre de transactions se situe dans une plage donnée.

Aspose.Cells expose le filtrage par valeur via la méthode `PivotField.filter_by_value(value_field, PivotFilterType, *thresholds)`. Le paramètre `PivotFilterType` utilise des valeurs telles que `ValueGreaterThan`, `ValueLessThan`, `ValueBetween`, `ValueEqual`, `ValueNotEqual`, `ValueGreaterThanOrEqual`, et `ValueLessThanOrEqual`. Le paramètre `value_field` spécifie quel champ de données doit être évalué, et le ou les derniers arguments fournissent la ou les valeurs seuils.

L'exemple suivant charge un classeur contenant un tableau croisé dynamique, applique un filtre de valeur qui ne conserve que les éléments dont les ventes agrégées dépassent un seuil numérique, actualise le tableau croisé dynamique et enregistre le classeur.

```python
import aspose.cells as ac

workbook = ac.Workbook("sample.xlsx")
worksheet = workbook.worksheets[0]
pivot_table = worksheet.pivot_tables[0]

row_field = pivot_table.row_fields[0]
data_field = pivot_table.data_fields[0]

# Trouver l'index du champ de données manuellement car PivotFieldCollection n'a pas IndexOf
data_field_index = -1
for i in range(pivot_table.data_fields.count):
    if pivot_table.data_fields[i] == data_field:
        data_field_index = i
        break

if data_field_index >= 0:
    row_field.filter_by_value(data_field_index, ac.PivotFilterType.VALUE_GREATER_THAN, 5000, float('inf'))

pivot_table.pivot_cache.refresh()

workbook.save("output.xlsx")
```

## **Filtre top 10**

Le filtre top 10 est une forme spécialisée de filtre de valeur qui ne conserve que les N éléments les plus élevés ou les plus bas en fonction d'un champ de valeur choisi. Il est couramment utilisé pour les rapports de classement tels que « top 10 des produits par chiffre d'affaires » ou « bottom 5 des régions par nombre de ventes ».

{{% alert color="primary" %}}

Le filtre top 10 n'est efficace que lorsque le tableau croisé dynamique possède un ou plusieurs champs de valeur dans la zone de données. Sans au moins un champ de valeur, il n'existe aucune mesure agrégée permettant de classer les éléments, et le filtre ne peut pas être appliqué.

{{% /alert %}}

Aspose.Cells expose le filtrage top 10 via la méthode `PivotField.filter_top_10(item_count, is_top, value_field, PivotFilterType)`. Le paramètre `item_count` définit le nombre d'éléments à conserver, `is_top` indique s'il faut conserver les éléments du haut (True) ou du bas (False), `value_field` fait référence au champ de données utilisé pour le classement, et `PivotFilterType` contrôle la manière dont la valeur est calculée (généralement `Sum`, mais aussi `Count` et `Percent`).

L'exemple suivant charge un classeur contenant un tableau croisé dynamique qui possède un champ de valeur, applique un filtre top 10 pour ne conserver que les 10 éléments les plus élevés selon la somme des ventes, actualise le tableau croisé dynamique et enregistre le classeur.

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

# Vérifier qu'il y a au moins un PivotField de valeur dans la zone de données
if pivotTable.data_fields.count == 0:
    raise Exception("Pivot table has no value (data) PivotField.")
valueField = pivotTable.data_fields[0]

# Récupérer le PivotField de ligne cible (le champ auquel appliquer Top 10)
rowField = pivotTable.row_fields[0]

# Le premier (et seul) champ de données est à l'index 0 ; Top 10 classe selon lui.
valueFieldIndex = 0

# Appliquer le filtre Top 10 sur le champ de ligne :
#   - itemCount   = 10
#   - filterType  = PivotFilterType.Sum
#   - isTop       = true (top N ; false signifierait bottom N)
#   - valueFieldIndex = l'index du champ de données utilisé pour classer les éléments
rowField.filter_top10(10, acp.PivotFilterType.Sum, True, valueFieldIndex)

# Actualiser les données du tableau croisé dynamique et recalculer pour que le filtre prenne effet
pivotTable.pivot_cache.refresh()

# Enregistrer le classeur
workbook.save(outputPath)
```

## **Filtrer en masquant ou en affichant des éléments du tableau croisé dynamique**

En plus des API de filtrage structurées, Aspose.Cells vous permet de contrôler directement la visibilité de chaque élément individuel du tableau croisé dynamique. En parcourant la collection `PivotItems` d'un `PivotField` et en basculant la propriété `is_hidden`, vous pouvez supprimer de manière sélective des éléments spécifiques sans appliquer un filtre basé sur une formule. Définir `is_hidden = True` masque l'élément dans le tableau croisé dynamique ; définir `is_hidden = False` l'affiche à nouveau.

Cette approche est utile lorsque la règle de filtrage est irrégulière ou propre à un élément, par exemple masquer un petit nombre de catégories nommées qui ne doivent pas apparaître dans un rapport particulier. L'exemple ci-dessous charge un tableau croisé dynamique, masque un élément spécifique par son nom, montre comment l'afficher à nouveau, actualise le tableau croisé dynamique et enregistre le classeur.

```python
import aspose.cells as ac

# Charger un classeur existant contenant un tableau croisé dynamique
workbook = ac.Workbook("pivot_table_sample.xlsx")

# Accéder à la première feuille de calcul qui contient le tableau croisé dynamique
sheet = workbook.worksheets[0]

# Accéder au tableau croisé dynamique par index (le premier tableau croisé dynamique de la feuille)
pivot_table = sheet.pivot_tables[0]

# Récupérer le PivotField cible (le premier champ d'étiquette de ligne dans lequel nous masquerons/afficherons des éléments)
pivot_field = pivot_table.row_fields[0]

# Parcourir la collection PivotItems du PivotField sélectionné
item_count = pivot_field.pivot_items.count
for i in range(item_count):
    item = pivot_field.pivot_items[i]

    # Masquer les éléments du tableau croisé dynamique qui correspondent à un nom/critère spécifique
    if item.name == "Item1" or item.name == "Item2":
        item.is_hidden = True

    # Démontrer l'affichage : réafficher un élément précédemment masqué du tableau croisé dynamique
    if item.name == "Item3":
        item.is_hidden = False

# Actualiser et recalculer le tableau croisé dynamique pour que les modifications prennent effet
pivot_table.pivot_cache.refresh()

# Enregistrer le classeur — les éléments masqués restent dans les données sous-jacentes
# mais sont exclus du résultat affiché du tableau croisé dynamique
workbook.save("output_pivot_filtered.xlsx")
```

## **Résumé**

Aspose.Cells for Python via .NET offre un ensemble complet de fonctionnalités de filtrage des tableaux croisés dynamiques qui correspondent à celles disponibles dans Microsoft Excel. Les filtres d'étiquettes, de dates et de valeurs couvrent les scénarios d'analyse les plus courants, tandis que le filtre top 10 gère les rapports de classement. Lorsque la règle de filtrage est irrégulière, la propriété `PivotItem.is_hidden` offre une solution flexible au niveau de l'élément. La combinaison de ces stratégies — par exemple, appliquer un filtre d'étiquette puis masquer des éléments spécifiques — vous permet de construire des rapports de tableaux croisés dynamiques précisément ciblés entièrement à partir du code.
{{< app/cells/assistant language="python-net" >}}