---
title: Actualiser les Tableaux Croisés Dynamiques et leurs caches avec Aspose.Cells for Python via Java
linktitle: Actualiser les Tableaux Croisés Dynamiques et leurs caches avec Aspose.Cells for Python via Java
description: Découvrez comment actualiser les Tableaux Croisés Dynamiques dans Aspose.Cells for Python via Java à l’aide de l’API d’actualisation v26.7+. Cet article présente refreshAll, refreshPivotTables, PivotCache.refresh, calculateData et getPivotTables, avec des exemples de code pratiques.
keywords: Aspose.Cells, Python via Java, Tableau Croisé Dynamique, actualisation, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /fr/python-java/refresh-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells fournit une API d’actualisation hiérarchisée qui vous permet de recharger les données des Tableaux Croisés Dynamiques à quatre portées différentes — de l’ensemble du classeur jusqu’à un seul Tableau Croisé Dynamique. À partir de la version **Aspose.Cells for Python via Java v26.7**, la méthode héritée `PivotTable.refreshData()` est marquée comme obsolète et doit être remplacée par les API plus efficaces tenant compte du cache décrites dans cet article.
{{% /alert %}}

## Introduction
L’actualisation d’un Tableau Croisé Dynamique est rarement une seule opération. En arrière-plan, Aspose.Cells maintient une chaîne de données hiérarchisée qui relie les données source d’origine aux valeurs affichées dans la feuille de calcul. Comprendre cette chaîne est essentiel pour choisir l’API d’actualisation adaptée à chaque situation.
La chaîne de données à quatre niveaux est la suivante :
1. **Source de données** — les plages de la feuille de calcul d’origine, la requête de base de données ou la plage de consolidation où résident les valeurs brutes.
2. **PivotCache** — l’instantané en mémoire des données source. Chaque Tableau Croisé Dynamique est construit sur un `PivotCache` ; c’est là que toutes les données sont rassemblées et agrégées.
3. **PivotTable** — l’objet d’affichage qui définit les champs de ligne, de colonne, de valeur et de filtre. Un `PivotTable` ne lit ses données *uniquement* que depuis son `PivotCache`, jamais directement depuis la source de données.
4. **Cells** — la collection `Cells` de la feuille de calcul dans laquelle le `PivotTable` rend les valeurs calculées et les styles.

{{% alert color="primary" %}}
`PivotCache.getSourceType()` (enum `PivotTableSourceType`) indique d’où proviennent les données du cache. À partir de v26.7, `PivotCache.refresh()` ne prend en charge que les types de source **`SHEET`** et **`CONSOLIDATION`** — c’est-à-dire les données résidant dans des plages d’une feuille de calcul. Les sources externes (bases de données, connexions externes, etc.) ne peuvent pas encore être actualisées au moyen de l’API de cache.
En raison de cette chaîne, Aspose.Cells propose deux voies d’actualisation fondamentales :
- **`PivotTable.calculateData()`** — recalcule l’affichage d’un `PivotTable` à partir de données déjà mises en cache, sans aller-retour vers la source de données.
Tous les scénarios de cet article utilisent des données source situées dans des cellules d’une feuille de calcul. Le type de source est donc `SHEET` et les opérations d’actualisation se comportent comme décrit.
{{% /alert %}}

## Quick Start
Si vous avez seulement besoin du code le plus court possible pour actualiser tous les Tableaux Croisés Dynamiques du classeur, un seul appel suffit :

```python
import jpype
from asposecells.api import Workbook

workbook = Workbook("input.xlsx")
workbook.refreshAll()
workbook.save("output.xlsx")
```

Tout le reste de cet article explique quand choisir une API plus ciblée.

## Required Imports
Tous les exemples Python de cet article reposent sur les imports suivants, car les types de Tableau Croisé Dynamique se trouvent dans le `namespace` `aspose.cells.pivot` :
- `import jpype`
- `import aspose.cells as cells`
Le module `jpype` sert à démarrer la JVM, tandis que `aspose.cells` expose les types liés aux classeurs, aux feuilles de calcul, aux cellules et aux Tableaux Croisés Dynamiques utilisés dans cet article.

## Refresh All Pivot Tables in the Workbook
Lorsque vous devez garantir que chaque cache et chaque Tableau Croisé Dynamique du classeur reflète les dernières données source, l’API la plus simple et la plus complète est `Workbook.refreshAll()`. Un seul appel parcourt l’ensemble du classeur — actualisant chaque `PivotCache` à partir de sa source, puis recalculant chaque `PivotTable` qui en dépend. C’est l’approche recommandée pour les actualisations générales de l’ensemble du document sans contrainte de performance.
L’exemple suivant crée un classeur avec une plage source Fruit/Year/Amount, crée un Tableau Croisé Dynamique, modifie certaines valeurs source, puis utilise `refreshAll()` pour tout mettre à jour en un seul appel.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType
# Create a new workbook
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# Write header row into cells A1:C1
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")
# Write data rows into cells A2:C9 (8 rows of fruit data across 2020 and 2021)
worksheet.getCells().get("A2").putValue("grape")
worksheet.getCells().get("B2").putValue(2020)
worksheet.getCells().get("C2").putValue(50)
worksheet.getCells().get("A3").putValue("blueberry")
worksheet.getCells().get("B3").putValue(2020)
worksheet.getCells().get("C3").putValue(60)
worksheet.getCells().get("A4").putValue("kiwi")
worksheet.getCells().get("B4").putValue(2020)
worksheet.getCells().get("C4").putValue(70)
worksheet.getCells().get("A5").putValue("cherry")
worksheet.getCells().get("B5").putValue(2020)
worksheet.getCells().get("C5").putValue(80)
worksheet.getCells().get("A6").putValue("grape")
worksheet.getCells().get("B6").putValue(2021)
worksheet.getCells().get("C6").putValue(90)
worksheet.getCells().get("A7").putValue("blueberry")
worksheet.getCells().get("B7").putValue(2021)
worksheet.getCells().get("C7").putValue(100)
worksheet.getCells().get("A8").putValue("kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(110)
worksheet.getCells().get("A9").putValue("cherry")
worksheet.getCells().get("B9").putValue(2021)
worksheet.getCells().get("C9").putValue(120)
# Add a pivot table: source range "A1:C9", destination cell "E3"
pivotTable = worksheet.getPivotTables().add("A1:C9", 2, 4)
# Assign pivot fields: Fruit to Rows, Year to Columns, Amount to Data
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
# Modify several Amount values in the source data to simulate changes
worksheet.getCells().get("C2").putValue(55)
worksheet.getCells().get("C5").putValue(85)
worksheet.getCells().get("C9").putValue(125)
# Refresh every pivot table / pivot cache in the workbook
workbook.refreshAll()
# Save the workbook
workbook.save("output.xlsx")
jpype.shutdownJVM()
```

## Refresh All Pivot Tables on a Single Worksheet
Parfois, vous avez seulement besoin d’actualiser les Tableaux Croisés Dynamiques qui se trouvent sur une feuille de calcul spécifique — par exemple, lorsque vous savez que ceux des autres feuilles de calcul ne sont pas apparentés et ne doivent pas être affectés. Pour ce cas, Aspose.Cells fournit `Worksheet.refreshPivotTables()`, dont la portée est limitée à une seule instance de `Worksheet`.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")
worksheet.getCells().get("A2").putValue("grape")
worksheet.getCells().get("B2").putValue(2020)
worksheet.getCells().get("C2").putValue(100)
worksheet.getCells().get("A3").putValue("blueberry")
worksheet.getCells().get("B3").putValue(2021)
worksheet.getCells().get("C3").putValue(150)
worksheet.getCells().get("A4").putValue("kiwi")
worksheet.getCells().get("B4").putValue(2020)
worksheet.getCells().get("C4").putValue(200)
worksheet.getCells().get("A5").putValue("cherry")
worksheet.getCells().get("B5").putValue(2021)
worksheet.getCells().get("C5").putValue(120)
worksheet.getCells().get("A6").putValue("grape")
worksheet.getCells().get("B6").putValue(2021)
worksheet.getCells().get("C6").putValue(180)
worksheet.getCells().get("A7").putValue("blueberry")
worksheet.getCells().get("B7").putValue(2020)
worksheet.getCells().get("C7").putValue(130)
worksheet.getCells().get("A8").putValue("kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(220)
worksheet.getCells().get("A9").putValue("cherry")
worksheet.getCells().get("B9").putValue(2020)
worksheet.getCells().get("C9").putValue(140)
pivotTable = worksheet.getPivotTables().add("A1:C9", 2, 4)
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
worksheet.getCells().get("C2").putValue(300)
worksheet.getCells().get("C5").putValue(250)
worksheet.getCells().get("C9").putValue(400)
worksheet.refreshPivotTables()
workbook.save("output.xlsx")
jpype.shutdownJVM()
```

## Refresh a Single Pivot Table
Lorsque vous souhaitez contrôler précisément un seul Tableau Croisé Dynamique, l’API basée sur le cache vous propose deux options. Le choix dépend de ce qui a réellement changé : les données source sous-jacentes, ou uniquement les paramètres d’affichage ou de disposition du Tableau Croisé Dynamique lui-même.

### Source Data Changed — Use `PivotCache.refresh()`
Si les données source sous-jacentes ont changé, le point d’entrée approprié est `pivotTable.getPivotCache().refresh()`. Cet appel relit les données source dans le cache, puis recalcule chaque `PivotTable` qui dépend de ce cache.

### Only View/Layout Changed — Use `calculateData()`
Si les données source n’ont *pas* changé et que seuls les paramètres d’affichage ou de disposition du Tableau Croisé Dynamique ont été modifiés, par exemple si un champ a été déplacé vers une autre zone ou si un paramètre d’actualisation à l’ouverture a été basculé, il est inutile de faire un aller-retour vers la source de données. Le cache contient déjà les données appropriées ; seul le `PivotTable` affiché doit être recalculé. Dans ce cas, `pivotTable.calculateData()` est le choix approprié.
L’exemple suivant modifie une propriété du Tableau Croisé Dynamique qui n’est pas liée à la source, puis appelle `calculateData()` pour le régénérer à partir du cache existant.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# Write Fruit / Year / Amount header row
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")
# Write 8 data rows (rows 2-9, fitting the source range A1:C9)
worksheet.getCells().get("A2").putValue("Grape")
worksheet.getCells().get("B2").putValue(2020)
worksheet.getCells().get("C2").putValue(100)
worksheet.getCells().get("A3").putValue("Blueberry")
worksheet.getCells().get("B3").putValue(2020)
worksheet.getCells().get("C3").putValue(200)
worksheet.getCells().get("A4").putValue("Kiwi")
worksheet.getCells().get("B4").putValue(2020)
worksheet.getCells().get("C4").putValue(300)
worksheet.getCells().get("A5").putValue("Cherry")
worksheet.getCells().get("B5").putValue(2020)
worksheet.getCells().get("C5").putValue(400)
worksheet.getCells().get("A6").putValue("Grape")
worksheet.getCells().get("B6").putValue(2021)
worksheet.getCells().get("C6").putValue(150)
worksheet.getCells().get("A7").putValue("Blueberry")
worksheet.getCells().get("B7").putValue(2021)
worksheet.getCells().get("C7").putValue(250)
worksheet.getCells().get("A8").putValue("Kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(350)
worksheet.getCells().get("A9").putValue("Cherry")
worksheet.getCells().get("B9").putValue(2021)
worksheet.getCells().get("C9").putValue(450)
# Add a pivot table placed at destination cell E3, sourcing from A1:C9
pivotTable = worksheet.getPivotTables().add("A1:C9", 2, 4)
# Assign fields: Fruit to Row, Year to Column, Amount to Data
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
# Modify a view/layout property — this is a presentation-only change,
# so it does NOT require re-reading the source data through PivotCache.refresh().
pivotTable.setRefreshDataOnOpeningFile(False)
# calculateData() re-renders THIS pivot table's display (data + style) from the
# data already held in the PivotCache. Because the source data did not change,
# no round-trip to the source is performed — only the cached values are recalculated
# into worksheet cells.
pivotTable.calculateData()
# Save the workbook to disk
workbook.save("output.xlsx")
jpype.shutdownJVM()
```

Un classeur contient souvent de nombreux Tableaux Croisés Dynamiques qui reposent tous sur un même cache partagé. Pour les énumérer — par exemple avant d’effectuer une actualisation par lot ou afin de diagnostiquer l’impact d’un cache partagé — utilisez `PivotCache.getPivotTables()`. Cette méthode retourne la collection de tous les `PivotTable` qui dépendent du cache indiqué.

## Migrating from the Obsolete `PivotTable.refreshData()`
Avant la version Aspose.Cells for Python via Java v26.7, la méthode standard pour actualiser un Tableau Croisé Dynamique consistait à appeler `PivotTable.refreshData()` sur chaque Tableau Croisé Dynamique individuellement. À partir de v26.7, cette méthode est marquée **comme obsolète** et doit être remplacée par les API tenant compte du cache décrites ci-dessus.
L’approche par table avec `refreshData()` pose problème dans les classeurs du monde réel pour deux raisons :
- Elle récupère à nouveau les données depuis la source *à chaque* appel, même si la source n’a pas changé.
Les remplacements recommandés sont les suivants :
L’exemple suivant présente le nouveau modèle efficace pour les classeurs contenant plusieurs Tableaux Croisés Dynamiques qui partagent un même cache.

## Which Refresh API Should I Use?
Le tableau ci-dessous résume les API d’actualisation disponibles et le moment de choisir chacune d’elles.
| Objectif | API recommandée | Remarques |
|------|-----------------|-------|
| Actualiser tout le classeur | `Workbook.refreshAll()` | Un seul appel ; couvre tous les caches et tous les tableaux. |
| Actualiser uniquement les Tableaux Croisés Dynamiques d’une feuille | `Worksheet.refreshPivotTables()` | Limitée à une feuille de calcul. |
| Les données source d’un cache ont changé | `pivotTable.getPivotCache().refresh()` | Actualise TOUS les Tableaux Croisés Dynamiques qui utilisent ce cache partagé. |
| Seuls les paramètres d’affichage ou de disposition ont changé | `pivotTable.calculateData()` | Évite un aller-retour inutile vers la source. |
| Répertorier tous les Tableaux Croisés Dynamiques d’un cache partagé | `pivotCache.getPivotTables()` | À utiliser pour les énumérer avant une actualisation en masse. |
En pratique, privilégiez les API fondées sur le cache plutôt que la méthode obsolète `refreshData()` par table. Elles tiennent compte des caches partagés, évitent les récupérations de données source redondantes et permettent de choisir la plus petite portée qui répond à votre besoin d’actualisation.

## Common Pitfalls
- **Oublier d’actualiser avant d’enregistrer.** Un Tableau Croisé Dynamique n’écrit ses valeurs affichées dans la feuille de calcul que lorsque sa chaîne de données est actualisée. Si vous modifiez des cellules source, appelez `PivotCache.refresh()` (ou `Workbook.refreshAll()`) avant `Workbook.save()`, sinon le fichier enregistré contiendra encore les anciennes valeurs agrégées.
- **Appeler la méthode obsolète `RefreshData()` pour chaque table.** Dans v26.7, `PivotTable.RefreshData()` est marquée comme obsolète et récupère à nouveau les données source à chaque appel. Lorsque plusieurs Tableaux Croisés Dynamiques partagent un cache, cela entraîne N récupérations redondantes des données source. Remplacez-la par un seul appel à `PivotCache.refresh()`, suivi de `calculateData()` pour chaque table.
- **Actualiser alors que seule la disposition a changé.** Si vous avez modifié uniquement l’affichage d’un Tableau Croisé Dynamique (ordre des colonnes, `ConsolidationFunction`, etc.) sans toucher aux données source, `PivotCache.refresh()` est inutile et lent. Appelez `pivotTable.calculateData()` pour régénérer l’affichage à partir du cache existant.
- **Source externe non prise en charge par `PivotCache.refresh()`.** Si la source du Tableau Croisé Dynamique provient d’une connexion externe (base de données, cube OLAP, etc.), `PivotCache.refresh()` ne peut pas l’actualiser dans v26.7 — il prend actuellement en charge uniquement les types de source `Sheet` et `Consolidation`. Pour les sources externes, rouvrez le classeur ou reconstruisez le cache à partir de la source.

{{< app/cells/assistant language="python" >}}