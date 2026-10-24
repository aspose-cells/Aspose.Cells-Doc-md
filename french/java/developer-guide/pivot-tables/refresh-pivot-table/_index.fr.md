---
title: Actualiser les Tableaux Croisés Dynamiques et les caches de Tableau Croisé Dynamique dans Aspose.Cells for Java
linktitle: Actualiser les Tableaux Croisés Dynamiques et les caches de Tableau Croisé Dynamique dans Aspose.Cells for Java
description: Apprenez à actualiser les Tableaux Croisés Dynamiques dans Aspose.Cells for Java à l’aide de l’API d’actualisation des Tableaux Croisés Dynamiques v26.7+. Cet article présente RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData et GetPivotTables avec des exemples de code pratiques.
keywords: Aspose.Cells, Java, Tableau Croisé Dynamique, actualisation, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /fr/java/refresh-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells fournit une API d’actualisation à plusieurs niveaux qui vous permet de recharger les données de Tableau Croisé Dynamique à quatre échelles différentes, de l’ensemble du classeur jusqu’à un seul Tableau Croisé Dynamique. À partir de la version **Aspose.Cells for Java v26.7**, l’ancienne méthode `PivotTable.refreshData()` est marquée comme obsolète et doit être remplacée par les API plus efficaces qui tiennent compte du cache, décrites dans cet article.
{{% /alert %}}

## Introduction
L’actualisation d’un Tableau Croisé Dynamique constitue rarement une opération unique. En arrière-plan, Aspose.Cells maintient une chaîne de données à plusieurs niveaux qui relie les données source d’origine aux valeurs affichées dans la feuille de calcul. Comprendre cette chaîne est essentiel pour choisir l’API d’actualisation adaptée à chaque situation.
La chaîne de données à quatre niveaux est la suivante :
1. **Source de données** — les plages de la feuille de calcul d’origine, la requête de base de données ou la plage de consolidation où se trouvent les valeurs brutes.
2. **PivotCache** — l’instantané en mémoire des données source. Chaque Tableau Croisé Dynamique est construit sur un `PivotCache` ; toutes les données sont regroupées et agrégées à cet endroit.
3. **PivotTable** — l’objet de visualisation qui définit les champs de ligne, de colonne, de valeur et de filtre. Un `PivotTable` lit *uniquement* à partir de son `PivotCache`, jamais directement à partir de la source de données.
4. **Cells** — la collection `Cells` de la feuille de calcul dans laquelle le `PivotTable` restitue ses valeurs calculées et ses styles.

{{% alert color="primary" %}}
`PivotCache.getSourceType()` (énumération `PivotTableSourceType`) indique l’origine des données du cache. À partir de v26.7, `PivotCache.refresh()` prend en charge uniquement les types de source **`Sheet`** et **`Consolidation`**, c’est-à-dire les données qui résident dans les plages de feuilles de calcul. Les sources externes (bases de données, connexions externes, etc.) ne peuvent pas encore être actualisées via l’API de cache.
En raison de cette chaîne, Aspose.Cells propose deux voies d’actualisation fondamentales :
- **`PivotTable.calculateData()`** — recalcule l’affichage d’un `PivotTable` à partir de données déjà mises en cache, sans aller-retour vers la source de données.
Tous les scénarios de cet article utilisent des données sources situées dans les cellules d’une feuille de calcul. Le type de source est donc `Sheet` et les opérations d’actualisation se comportent comme décrit.
{{% /alert %}}

## Quick Start
Si vous souhaitez uniquement le code le plus court permettant d’actualiser tous les tableaux croisés dynamiques du classeur, un seul appel suffit :

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook("input.xlsx");
workbook.refreshAll();
workbook.save("output.xlsx");
```

Le reste de cet article explique quand choisir une API plus ciblée.

## Required Import Statements
Tous les exemples Java de cet article commencent par les instructions d’import suivantes, car les types de Tableau Croisé Dynamique se trouvent dans le package `com.aspose.cells.pivot` :
- `import java.lang.System;`
- `import com.aspose.cells.Workbook;`
- `import com.aspose.cells.pivot.*;`

## Refresh All Pivot Tables in the Workbook
Lorsque vous devez vous assurer que chaque cache et chaque Tableau Croisé Dynamique du classeur reflète les dernières données sources, l’API la plus simple et la plus complète est `Workbook.refreshAll()`. Un seul appel parcourt l’ensemble du classeur, actualise chaque `PivotCache` depuis sa source, puis recalcule chaque `PivotTable` dépendant. Cette approche est recommandée pour les actualisations générales de l’ensemble du document lorsque le temps d’exécution n’est pas un facteur déterminant.
L’exemple suivant crée un classeur avec une plage source Fruit/Year/Amount, crée un Tableau Croisé Dynamique, modifie certaines valeurs sources, puis utilise `refreshAll()` pour tout mettre à jour en un seul appel.

```java
import com.aspose.cells.*;
// Create a new workbook
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
// Write header row into cells A1:C1
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
// Write data rows into cells A2:C9 (8 rows of fruit data across 2020 and 2021)
worksheet.getCells().get("A2").putValue("grape");
worksheet.getCells().get("B2").putValue(2020);
worksheet.getCells().get("C2").putValue(50);
worksheet.getCells().get("A3").putValue("blueberry");
worksheet.getCells().get("B3").putValue(2020);
worksheet.getCells().get("C3").putValue(60);
worksheet.getCells().get("A4").putValue("kiwi");
worksheet.getCells().get("B4").putValue(2020);
worksheet.getCells().get("C4").putValue(70);
worksheet.getCells().get("A5").putValue("cherry");
worksheet.getCells().get("B5").putValue(2020);
worksheet.getCells().get("C5").putValue(80);
worksheet.getCells().get("A6").putValue("grape");
worksheet.getCells().get("B6").putValue(2021);
worksheet.getCells().get("C6").putValue(90);
worksheet.getCells().get("A7").putValue("blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(100);
worksheet.getCells().get("A8").putValue("kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(110);
worksheet.getCells().get("A9").putValue("cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(120);
// Add a pivot table: source range "A1:C9", destination cell "E3", name "Pivot1"
int pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);
// Assign pivot fields: Fruit to Rows, Year to Columns, Amount to Data
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
// Modify several Amount values in the source data to simulate changes
worksheet.getCells().get("C2").putValue(55);
worksheet.getCells().get("C5").putValue(85);
worksheet.getCells().get("C9").putValue(125);
// Refresh every pivot table / pivot cache in the workbook
workbook.refreshAll();
// Save the workbook
workbook.save("output.xlsx");
```

## Refresh All Pivot Tables on a Single Worksheet
Parfois, vous ne souhaitez actualiser que les tableaux croisés dynamiques d’une feuille de calcul spécifique, par exemple lorsque vous savez que ceux des autres feuilles de calcul ne sont pas apparentés et ne doivent pas être modifiés. Pour ce cas, Aspose.Cells fournit `Worksheet.refreshPivotTables()`, une API limitée à une seule instance de `Worksheet`.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
worksheet.getCells().get("A2").putValue("grape");
worksheet.getCells().get("B2").putValue(2020);
worksheet.getCells().get("C2").putValue(100);
worksheet.getCells().get("A3").putValue("blueberry");
worksheet.getCells().get("B3").putValue(2021);
worksheet.getCells().get("C3").putValue(150);
worksheet.getCells().get("A4").putValue("kiwi");
worksheet.getCells().get("B4").putValue(2020);
worksheet.getCells().get("C4").putValue(200);
worksheet.getCells().get("A5").putValue("cherry");
worksheet.getCells().get("B5").putValue(2021);
worksheet.getCells().get("C5").putValue(120);
worksheet.getCells().get("A6").putValue("grape");
worksheet.getCells().get("B6").putValue(2021);
worksheet.getCells().get("C6").putValue(180);
worksheet.getCells().get("A7").putValue("blueberry");
worksheet.getCells().get("B7").putValue(2020);
worksheet.getCells().get("C7").putValue(130);
worksheet.getCells().get("A8").putValue("kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(220);
worksheet.getCells().get("A9").putValue("cherry");
worksheet.getCells().get("B9").putValue(2020);
worksheet.getCells().get("C9").putValue(140);
int pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
worksheet.getCells().get("C2").putValue(300);
worksheet.getCells().get("C5").putValue(250);
worksheet.getCells().get("C9").putValue(400);
worksheet.refreshPivotTables();
workbook.save("output.xlsx");
```

## Refresh a Single Pivot Table
Lorsque vous souhaitez exercer un contrôle précis sur un seul Tableau Croisé Dynamique, l’API basée sur le cache vous offre deux options. Le choix dépend de ce qui a réellement changé : les données source sous-jacentes ou uniquement les paramètres d’affichage ou de mise en page du Tableau Croisé Dynamique lui-même.

### Source Data Changed — Use `PivotCache.refresh()`
Si les données source sous-jacentes ont changé, le point d’entrée approprié est `pivotTable.getPivotCache().refresh()`. Cet appel relit les données source dans le cache, puis recalcule chaque `PivotTable` qui dépend de ce cache.

### Only View/Layout Changed — Use `calculateData()`
Si les données source n’ont *pas* changé et que seuls les paramètres d’affichage ou de mise en page du Tableau Croisé Dynamique ont été modifiés, par exemple si un champ a été déplacé vers une autre zone ou si un paramètre d’actualisation à l’ouverture a été activé ou désactivé, il est inutile de revenir à la source. Le cache contient déjà les données correctes ; seul le `PivotTable` affiché doit être recalculé. Dans ce cas, `pivotTable.calculateData()` est le choix approprié.
L’exemple suivant modifie une propriété du Tableau Croisé Dynamique qui ne fait pas partie de la source, puis appelle `calculateData()` pour le restituer à partir du cache existant.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
// Write Fruit / Year / Amount header row
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
// Write 8 data rows (rows 2-9, fitting the source range A1:C9)
worksheet.getCells().get("A2").putValue("Grape");
worksheet.getCells().get("B2").putValue(2020);
worksheet.getCells().get("C2").putValue(100);
worksheet.getCells().get("A3").putValue("Blueberry");
worksheet.getCells().get("B3").putValue(2020);
worksheet.getCells().get("C3").putValue(200);
worksheet.getCells().get("A4").putValue("Kiwi");
worksheet.getCells().get("B4").putValue(2020);
worksheet.getCells().get("C4").putValue(300);
worksheet.getCells().get("A5").putValue("Cherry");
worksheet.getCells().get("B5").putValue(2020);
worksheet.getCells().get("C5").putValue(400);
worksheet.getCells().get("A6").putValue("Grape");
worksheet.getCells().get("B6").putValue(2021);
worksheet.getCells().get("C6").putValue(150);
worksheet.getCells().get("A7").putValue("Blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(250);
worksheet.getCells().get("A8").putValue("Kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(350);
worksheet.getCells().get("A9").putValue("Cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(450);
// Add a pivot table named "Pivot1" placed at destination cell E3, sourcing from A1:C9
int pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);
// Assign fields: Fruit to Row, Year to Column, Amount to Data
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
// Modify a view/layout property -- this is a presentation-only change,
// so it does NOT require re-reading the source data through PivotCache.refresh().
pivotTable.setRefreshDataOnOpeningFile(false);
// calculateData() re-renders THIS pivot table's display (data + style) from the
// data already held in the PivotCache. Because the source data did not change,
// no round-trip to the source is performed -- only the cached values are recalculated
// into worksheet cells.
pivotTable.calculateData();
// Save the workbook to disk
workbook.save("output.xlsx");
```

Un classeur contient souvent de nombreux tableaux croisés dynamiques construits sur un même cache partagé. Pour les énumérer, par exemple avant d’effectuer une actualisation par lot ou pour diagnostiquer l’impact d’un cache partagé, utilisez `PivotCache.getPivotTables()`. Cette méthode retourne la collection de tous les `PivotTable` qui dépendent du cache spécifié.

## Migrating from the Obsolete `PivotTable.refreshData()`
Avant Aspose.Cells for Java v26.7, la manière standard d’actualiser un tableau croisé dynamique consistait à appeler `PivotTable.refreshData()` sur chaque tableau croisé dynamique individuellement. À partir de v26.7, cette méthode est marquée **obsolète** et doit être remplacée par les API basées sur le cache décrites ci-dessus.
L’approche `refreshData()` par table présente deux problèmes dans les classeurs du monde réel :
- Elle récupère à nouveau les données depuis la source *à chaque* appel, même si la source n’a pas changé.
Les remplacements recommandés sont :
L’exemple suivant présente le nouveau modèle efficace pour les classeurs contenant plusieurs tableaux croisés dynamiques qui partagent un seul cache.

## Which Refresh API Should I Use?
Le tableau suivant récapitule les API d’actualisation disponibles et les cas auxquels chacune convient.
| Objectif | API recommandée | Remarques |
|------|-----------------|-------|
| Actualiser tout le classeur | `Workbook.refreshAll()` | Un seul appel couvre tous les caches et tous les tableaux. |
| Actualiser uniquement les tableaux croisés dynamiques d’une feuille | `Worksheet.refreshPivotTables()` | Limitée à une feuille de calcul. |
| Les données source d’un cache ont changé | `pivotTable.getPivotCache().refresh()` | Actualise TOUS les tableaux croisés dynamiques qui partagent ce cache. |
| Seuls les paramètres d’affichage ou de mise en page ont changé | `pivotTable.calculateData()` | Évite un aller-retour inutile vers la source. |
| Répertorier tous les tableaux croisés dynamiques d’un cache partagé | `pivotCache.getPivotTables()` | À utiliser pour les énumérer avant une actualisation en masse. |
En pratique, préférez les API basées sur le cache à la méthode obsolète `refreshData()` par table. Elles tiennent compte des caches partagés, évitent les récupérations redondantes de la source et vous permettent de choisir la portée la plus limitée qui répond à votre besoin d’actualisation.

## Common Pitfalls
- **Oublier d’actualiser avant d’enregistrer.** Un Tableau Croisé Dynamique n’écrit ses valeurs affichées dans la feuille de calcul que lorsque sa chaîne de données est actualisée. Si vous modifiez des cellules source, appelez `PivotCache.refresh()` (ou `Workbook.refreshAll()`) avant `Workbook.save()`, sinon le fichier enregistré contient toujours les anciennes valeurs agrégées.
- **Appeler la méthode obsolète `refreshData()` pour chaque table.** En v26.7, `PivotTable.refreshData()` est marquée comme obsolète et récupère à nouveau la source à chaque appel. Avec plusieurs tableaux croisés dynamiques partageant un cache, cela entraîne N récupérations redondantes de la source. Remplacez cet appel par un seul `PivotCache.refresh()`, suivi de `calculateData()` pour chaque table.
- **Actualiser alors que seule la mise en page a changé.** Si vous ne modifiez que l’affichage d’un Tableau Croisé Dynamique (ordre des colonnes, `ConsolidationFunction`, etc.) sans toucher aux données source, `PivotCache.refresh()` est inutile et lent. Appelez `pivotTable.calculateData()` pour effectuer le rendu à partir du cache existant.
- **Source externe non prise en charge par `PivotCache.refresh()`.** Si la source du Tableau Croisé Dynamique provient d’une connexion externe (base de données, cube OLAP, etc.), `PivotCache.refresh()` ne peut pas l’actualiser dans v26.7. Cette API prend en charge uniquement les types de source `Sheet` et `Consolidation`. Pour les sources externes, rouvrez le classeur ou reconstruisez le cache à partir de la source.

{{< app/cells/assistant language="java" >}}