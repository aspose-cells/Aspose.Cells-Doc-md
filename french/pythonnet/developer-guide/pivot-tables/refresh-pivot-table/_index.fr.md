---
title: Actualiser les Tableaux Croisés Dynamiques et leurs caches avec Aspose.Cells for Python via .NET
linktitle: Actualiser les Tableaux Croisés Dynamiques et leurs caches avec Aspose.Cells for Python via .NET
description: Apprenez à actualiser les Tableaux Croisés Dynamiques dans Aspose.Cells for Python via .NET à l’aide de l’API d’actualisation des Tableaux Croisés Dynamiques v26.7+. Cet article couvre refresh_all, _refresh_pivot_tables, PivotCache.refresh, _calculate_data et _get_pivot_tables avec des exemples de code pratiques.
keywords: Aspose.Cells, Python via .NET, Tableau Croisé Dynamique, actualisation, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /fr/python-net/refresh-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells fournit une API d’actualisation à plusieurs niveaux qui permet de recharger les données de Tableau Croisé Dynamique à quatre portées différentes, depuis le classeur entier jusqu’à un seul Tableau Croisé Dynamique. À partir d’**Aspose.Cells for Python via .NET v26.7**, la méthode héritée `PivotTable.refresh_data()` est marquée comme obsolète et doit être remplacée par les API plus efficaces tenant compte du cache décrites dans cet article.
{{% /alert %}}

## Introduction
Le fait d’actualiser un Tableau Croisé Dynamique relève rarement d’une seule opération. En arrière-plan, Aspose.Cells maintient une chaîne de données à plusieurs niveaux qui relie vos données sources d’origine aux valeurs affichées dans la feuille de calcul. Comprendre cette chaîne est la clé permettant de choisir l’API d’actualisation adaptée à chaque situation.
La chaîne de données à quatre niveaux est la suivante :
1. **Source de données** — les plages de la feuille de calcul d’origine, la requête de base de données ou la plage de consolidation dans lesquelles les valeurs brutes sont stockées.
2. **PivotCache** — l’instantané en mémoire des données sources. Chaque Tableau Croisé Dynamique est construit sur un `PivotCache` ; c’est là que toutes les données sont regroupées et agrégées.
3. **PivotTable** — l’objet de vue qui définit les champs de ligne, de colonne, de valeur et de filtre. Un `PivotTable` lit *uniquement* depuis son `PivotCache`, jamais directement depuis la source de données.
4. **Cells** — les `Cells` de la feuille de calcul dans lesquels le `PivotTable` restitue les valeurs calculées et les styles.

{{% alert color="primary" %}}
`PivotCache.source_type` (énumération `PivotTableSourceType`) indique l’origine des données du cache. Depuis v26.7, `PivotCache.refresh()` prend en charge uniquement les types de source **`Sheet`** et **`Consolidation`**, c’est-à-dire les données résidant dans les plages de feuille de calcul. Les sources externes (bases de données, connexions externes, etc.) ne peuvent pas encore être actualisées via l’API de cache.
En raison de cette chaîne, Aspose.Cells propose deux voies fondamentales d’actualisation :
- **`PivotTable.calculate_data()`** — recalcule l’affichage d’un `PivotTable` à partir de données déjà mises en cache, sans aller-retour vers la source de données.
Tous les scénarios de cet article utilisent des données sources situées dans des cellules d’une feuille de calcul. Le type de source est donc `Sheet` et les opérations d’actualisation se comportent comme décrit.
{{% /alert %}}

## Quick Start
Si vous avez uniquement besoin du plus court code possible pour actualiser tous les Tableaux Croisés Dynamiques du classeur, un seul appel suffit :

```python
import aspose.cells as ac

workbook = ac.Workbook("input.xlsx")
workbook.refresh_all()
workbook.save("output.xlsx")
```

Le reste de cet article explique quand choisir une API plus ciblée.

## Required Imports
Tous les exemples Python de cet article commencent par les trois instructions d’importation suivantes, car les types de Tableau Croisé Dynamique se trouvent dans le namespace `aspose.cells.pivot` :
- `import sys`
- `import aspose.cells`
- `import aspose.cells.pivot`

## Refresh All Pivot Tables in the Workbook
Lorsque vous devez garantir que chaque cache de Tableau Croisé Dynamique et chaque Tableau Croisé Dynamique du classeur reflète les dernières données sources, l’API la plus simple et la plus complète est `Workbook.refresh_all()`. Un seul appel parcourt tout le classeur, actualisant chaque `PivotCache` à partir de sa source, puis recalculant chaque `PivotTable` dépendant. Cette approche est recommandée pour les actualisations générales de l’ensemble du document lorsque les performances ne sont pas une contrainte.
L’exemple suivant construit un classeur avec une plage source Fruit/Year/Amount, crée un Tableau Croisé Dynamique, modifie certaines valeurs sources, puis utilise `refresh_all()` pour tout actualiser en un seul appel.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
# Create a new workbook
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# Write header row into cells A1:C1
worksheet.cells.get("A1").put_value("Fruit")
worksheet.cells.get("B1").put_value("Year")
worksheet.cells.get("C1").put_value("Amount")
# Write data rows into cells A2:C9 (8 rows of fruit data across 2020 and 2021)
worksheet.cells.get("A2").put_value("grape")
worksheet.cells.get("B2").put_value(2020)
worksheet.cells.get("C2").put_value(50)
worksheet.cells.get("A3").put_value("blueberry")
worksheet.cells.get("B3").put_value(2020)
worksheet.cells.get("C3").put_value(60)
worksheet.cells.get("A4").put_value("kiwi")
worksheet.cells.get("B4").put_value(2020)
worksheet.cells.get("C4").put_value(70)
worksheet.cells.get("A5").put_value("cherry")
worksheet.cells.get("B5").put_value(2020)
worksheet.cells.get("C5").put_value(80)
worksheet.cells.get("A6").put_value("grape")
worksheet.cells.get("B6").put_value(2021)
worksheet.cells.get("C6").put_value(90)
worksheet.cells.get("A7").put_value("blueberry")
worksheet.cells.get("B7").put_value(2021)
worksheet.cells.get("C7").put_value(100)
worksheet.cells.get("A8").put_value("kiwi")
worksheet.cells.get("B8").put_value(2021)
worksheet.cells.get("C8").put_value(110)
worksheet.cells.get("A9").put_value("cherry")
worksheet.cells.get("B9").put_value(2021)
worksheet.cells.get("C9").put_value(120)
# Add a pivot table: source range "A1:C9", destination cell "E3"
pivot_table = worksheet.pivot_tables.add("A1:C9", 2, 4)
# Assign pivot fields: Fruit to Rows, Year to Columns, Amount to Data
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
# Modify several Amount values in the source data to simulate changes
worksheet.cells.get("C2").put_value(55)
worksheet.cells.get("C5").put_value(85)
worksheet.cells.get("C9").put_value(125)
# Refresh every pivot table / pivot cache in the workbook
workbook.refresh_all()
# Save the workbook
workbook.save("output.xlsx")
```

## Refresh All Pivot Tables on a Single Worksheet
Parfois, vous n’avez besoin d’actualiser que les Tableaux Croisés Dynamiques qui se trouvent sur une feuille de calcul précise, par exemple lorsque ceux des autres feuilles de calcul sont connus comme n’étant pas liés et ne doivent pas être modifiés. Dans ce cas, Aspose.Cells fournit `Worksheet.refresh_pivot_tables()`, une méthode limitée à une seule instance de `Worksheet`.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.cells.get("A1").put_value("Fruit")
worksheet.cells.get("B1").put_value("Year")
worksheet.cells.get("C1").put_value("Amount")
worksheet.cells.get("A2").put_value("grape")
worksheet.cells.get("B2").put_value(2020)
worksheet.cells.get("C2").put_value(100)
worksheet.cells.get("A3").put_value("blueberry")
worksheet.cells.get("B3").put_value(2021)
worksheet.cells.get("C3").put_value(150)
worksheet.cells.get("A4").put_value("kiwi")
worksheet.cells.get("B4").put_value(2020)
worksheet.cells.get("C4").put_value(200)
worksheet.cells.get("A5").put_value("cherry")
worksheet.cells.get("B5").put_value(2021)
worksheet.cells.get("C5").put_value(120)
worksheet.cells.get("A6").put_value("grape")
worksheet.cells.get("B6").put_value(2021)
worksheet.cells.get("C6").put_value(180)
worksheet.cells.get("A7").put_value("blueberry")
worksheet.cells.get("B7").put_value(2020)
worksheet.cells.get("C7").put_value(130)
worksheet.cells.get("A8").put_value("kiwi")
worksheet.cells.get("B8").put_value(2021)
worksheet.cells.get("C8").put_value(220)
worksheet.cells.get("A9").put_value("cherry")
worksheet.cells.get("B9").put_value(2020)
worksheet.cells.get("C9").put_value(140)
pivot_table = worksheet.pivot_tables.add("A1:C9", 2, 4)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
worksheet.cells.get("C2").put_value(300)
worksheet.cells.get("C5").put_value(250)
worksheet.cells.get("C9").put_value(400)
worksheet.refresh_pivot_tables()
workbook.save("output.xlsx")
```

## Refresh a Single Pivot Table
Lorsque vous souhaitez disposer d’un contrôle précis sur un seul Tableau Croisé Dynamique, l’API fondée sur le cache vous propose deux options. Le choix dépend de ce qui a réellement changé : les données sources sous-jacentes ou uniquement les paramètres d’affichage ou de disposition du Tableau Croisé Dynamique lui-même.

### Source Data Changed — Use `PivotCache.refresh()`
Si les données sources sous-jacentes ont changé, le point d’entrée approprié est `pivot_table.pivot_cache.refresh()`. Cet appel relit les données sources dans le cache, puis recalcule chaque `PivotTable` qui dépend de ce cache.

### Only View/Layout Changed — Use `calculate_data()`
Si les données sources n’ont *pas* changé et que seuls les paramètres d’affichage ou de disposition du Tableau Croisé Dynamique ont été modifiés (par exemple, si un champ a été déplacé vers une autre zone ou si un paramètre d’actualisation à l’ouverture a été activé), il n’est pas nécessaire de faire un aller-retour vers la source de données. Le cache contient déjà les données correctes ; seul le `PivotTable` affiché doit être recalculé. Dans ce cas, `pivot_table.calculate_data()` est le bon choix.
L’exemple suivant modifie une propriété qui n’est pas liée à la source du Tableau Croisé Dynamique, puis appelle `calculate_data()` pour le restituer à partir du cache existant.

```python
import aspose.cells as ac
import aspose.cells.pivot as acp
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# Write Fruit / Year / Amount header row
worksheet.cells.get("A1").put_value("Fruit")
worksheet.cells.get("B1").put_value("Year")
worksheet.cells.get("C1").put_value("Amount")
# Write 8 data rows (rows 2-9, fitting the source range A1:C9)
worksheet.cells.get("A2").put_value("Grape")
worksheet.cells.get("B2").put_value(2020)
worksheet.cells.get("C2").put_value(100)
worksheet.cells.get("A3").put_value("Blueberry")
worksheet.cells.get("B3").put_value(2020)
worksheet.cells.get("C3").put_value(200)
worksheet.cells.get("A4").put_value("Kiwi")
worksheet.cells.get("B4").put_value(2020)
worksheet.cells.get("C4").put_value(300)
worksheet.cells.get("A5").put_value("Cherry")
worksheet.cells.get("B5").put_value(2020)
worksheet.cells.get("C5").put_value(400)
worksheet.cells.get("A6").put_value("Grape")
worksheet.cells.get("B6").put_value(2021)
worksheet.cells.get("C6").put_value(150)
worksheet.cells.get("A7").put_value("Blueberry")
worksheet.cells.get("B7").put_value(2021)
worksheet.cells.get("C7").put_value(250)
worksheet.cells.get("A8").put_value("Kiwi")
worksheet.cells.get("B8").put_value(2021)
worksheet.cells.get("C8").put_value(350)
worksheet.cells.get("A9").put_value("Cherry")
worksheet.cells.get("B9").put_value(2021)
worksheet.cells.get("C9").put_value(450)
# Add a pivot table placed at destination cell E3, sourcing from A1:C9
pivot_table = worksheet.pivot_tables.add("A1:C9", 2, 4)
# Assign fields: Fruit to Row, Year to Column, Amount to Data
pivot_table.add_field_to_area(acp.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(acp.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(acp.PivotFieldType.DATA, "Amount")
# Modify a view/layout property — this is a presentation-only change,
# so it does NOT require re-reading the source data through PivotCache.refresh().
pivot_table.refresh_data_on_opening_file = False
# calculate_data() re-renders THIS pivot table's display (data + style) from the
# data already held in the PivotCache. Because the source data did not change,
# no round-trip to the source is performed — only the cached values are recalculated
# into worksheet cells.
pivot_table.calculate_data()
# Save the workbook to disk
workbook.save("output.xlsx")
```

Un classeur contient souvent de nombreux Tableaux Croisés Dynamiques qui reposent tous sur un même cache partagé. Pour les énumérer, par exemple avant d’effectuer une actualisation par lot ou afin de diagnostiquer l’impact d’un cache partagé, utilisez `PivotCache.get_pivot_tables()`. Cette méthode retourne la collection de tous les `PivotTable` qui dépendent du cache spécifié.

## Migrating from the Obsolete `PivotTable.refresh_data()`
Avant Aspose.Cells for Python via .NET v26.7, la méthode standard pour actualiser un Tableau Croisé Dynamique consistait à appeler `PivotTable.refresh_data()` sur chaque Tableau Croisé Dynamique individuellement. Depuis v26.7, cette méthode est marquée **obsolète** et doit être remplacée par les API fondées sur le cache décrites ci-dessus.
Il existe deux raisons qui rendent l’approche `refresh_data()` par table problématique dans les classeurs du monde réel :
- Elle récupère les données depuis la source *à chaque fois* qu’elle est appelée, même lorsque la source n’a pas changé.
Les remplacements recommandés sont :
L’exemple suivant présente le nouveau modèle efficace pour les classeurs contenant plusieurs Tableaux Croisés Dynamiques qui partagent un même cache.

## Which Refresh API Should I Use?
Le tableau ci-dessous récapitule les API d’actualisation disponibles et les situations dans lesquelles choisir chacune d’elles.
| Objectif | API recommandée | Remarques |
|------|-----------------|-------|
| Actualiser tout le classeur | `Workbook.refresh_all()` | Un seul appel ; couvre tous les caches et tous les tableaux croisés dynamiques. |
| Actualiser uniquement les tableaux croisés dynamiques d’une seule feuille | `Worksheet.refresh_pivot_tables()` | Limitée à une seule feuille de calcul. |
| Les données sources ont changé pour un cache | `pivot_table.pivot_cache.refresh()` | Actualise TOUS les tableaux croisés dynamiques de ce cache partagé. |
| Seuls les paramètres d’affichage ou de disposition ont changé | `pivot_table.calculate_data()` | Évite l’aller-retour inutile vers la source. |
| Lister tous les tableaux croisés dynamiques d’un cache partagé | `pivot_cache.get_pivot_tables()` | À utiliser pour les énumérer avant une actualisation groupée. |
En pratique, privilégiez les API fondées sur le cache plutôt que la méthode obsolète `refresh_data()` par table. Elles tiennent compte des caches partagés, évitent les récupérations redondantes de la source et vous permettent de choisir la plus petite portée qui répond à votre besoin d’actualisation.

## Common Pitfalls
- **Oublier d’actualiser avant d’enregistrer.** Un Tableau Croisé Dynamique n’écrit ses valeurs affichées dans la feuille de calcul que lorsque sa chaîne de données est actualisée. Si vous modifiez des cellules sources, appelez `PivotCache.refresh()` (ou `Workbook.refresh_all()`) avant `Workbook.save()`, sinon le fichier enregistré contient encore les anciennes valeurs agrégées.
- **Appeler la méthode obsolète `refresh_data()` par table.** Depuis v26.7, `PivotTable.refresh_data()` est marquée obsolète et recharge les données sources à chaque appel. Avec plusieurs Tableaux Croisés Dynamiques partageant un cache, cela entraîne N récupérations redondantes des données sources. Remplacez-la par un seul `PivotCache.refresh()`, suivi de `calculate_data()` pour chaque table.
- **Actualiser lorsque seule la disposition a changé.** Si vous n’avez modifié que la vue d’un Tableau Croisé Dynamique (ordre des colonnes, `ConsolidationFunction`, etc.) sans toucher aux données sources, l’appel à `PivotCache.refresh()` est inutile et lent. Appelez `pivotTable.calculate_data()` pour le restituer à partir du cache existant.
- **Source externe non prise en charge par `PivotCache.refresh()`.** Si la source du Tableau Croisé Dynamique provient d’une connexion externe (base de données, cube OLAP, etc.), `PivotCache.refresh()` ne peut pas l’actualiser dans la version v26.7 ; il prend actuellement en charge uniquement les types de source `Sheet` et `Consolidation`. Pour les sources externes, rouvrez le classeur ou reconstruisez le cache à partir de la source.

{{< app/cells/assistant language="python-net" >}}