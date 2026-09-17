---
title: Actualiser les tableaux croisés dynamiques et leurs caches dans Aspose.Cells for Node.js via C++
description: Apprenez à actualiser les tableaux croisés dynamiques dans Aspose.Cells for Node.js via C++ à l'aide de l'API de rafraîchissement de tableaux croisés dynamiques de v26.7. Cet article couvre RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData et GetPivotTables avec des exemples de code pratiques.
linktitle: Actualiser les tableaux croisés dynamiques
keywords: Aspose.Cells, Node.js via C++, tableau croisé dynamique, actualiser, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /fr/nodejs-cpp/refresh-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells fournit une API d'actualisation en couches qui vous permet de recharger les données des tableaux croisés dynamiques à quatre niveaux différents — du classeur entier jusqu'à un seul tableau croisé dynamique. À partir d'**Aspose.Cells for Node.js via C++ v26.7**, la méthode héritée `PivotTable.RefreshData()` est marquée comme obsolète et doit être remplacée par les API plus efficaces, sensibles au cache, décrites dans cet article.
{{% /alert %}}

## Introduction
Actualiser un tableau croisé dynamique est rarement une opération unique. En arrière-plan, Aspose.Cells gère une chaîne de données en couches qui relie vos données source d'origine aux valeurs rendues visibles dans la feuille de calcul. Comprendre cette chaîne est essentiel pour choisir la bonne API d'actualisation dans chaque situation.
La chaîne de données à quatre niveaux est la suivante :
1. **Source de données** — les plages de feuilles de calcul d'origine, la requête de base de données ou la plage de consolidation où se trouvent les valeurs brutes.
2. **PivotCache** — l'instantané en mémoire des données source. Chaque tableau croisé dynamique est construit au-dessus d'un `PivotCache` ; c'est ici que toutes les données sont rassemblées et agrégées.
3. **PivotTable** — l'objet de vue qui définit les champs de ligne, de colonne, de valeur et de filtre. Un `PivotTable` lit *uniquement* depuis son `PivotCache`, jamais directement depuis la source de données.
4. **Cells** — les `Cells` de la feuille de calcul dans lesquelles le `PivotTable` rend ses valeurs calculées et ses styles.

{{% alert color="primary" %}}
`PivotCache.SourceType` (énumération `PivotTableSourceType`) indique d'où proviennent les données du cache. Depuis la v26.7, `PivotCache.Refresh()` prend uniquement en charge les types de source **`Sheet`** et **`Consolidation`** — c'est-à-dire les données résidant dans des plages de feuilles de calcul. Les sources externes (bases de données, connexions externes, etc.) ne peuvent pas encore être actualisées via l'API de cache.
{{% /alert %}}

En raison de cette chaîne, il existe deux chemins d'actualisation fondamentaux dans Aspose.Cells :
- **`PivotTable.CalculateData()`** — recalcule l'affichage d'un `PivotTable` à partir des données déjà mises en cache, sans aller-retour vers la source de données.
Tous les scénarios de cet article utilisent des données sources situées dans des cellules de feuille de calcul ; le type de source est donc `Sheet` et les opérations d'actualisation se comportent comme décrit.

## Démarrage rapide
Si vous avez simplement besoin du code le plus court possible qui actualise chaque tableau croisé dynamique du classeur, un seul appel suffit :

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
// Écrire la ligne d'en-tête dans les cellules A1:C1
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
// Écrire les lignes de données dans les cellules A2:C9 (8 lignes de données de fruits pour 2020 et 2021)
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
// Ajouter un tableau croisé dynamique : plage source "A1:C9", cellule de destination "E3", nom "Pivot1"
let pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);
// Assigner les champs du tableau croisé dynamique : Fruit aux Lignes, Year aux Colonnes, Amount aux Données
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
// Modifier plusieurs valeurs de Amount dans les données source pour simuler des changements
worksheet.getCells().get("C2").putValue(55);
worksheet.getCells().get("C5").putValue(85);
worksheet.getCells().get("C9").putValue(125);
// Actualiser tous les tableaux croisés dynamiques / cache de tableau croisé dynamique dans le classeur
workbook.refreshAll();
// Enregistrer le classeur
workbook.save("output.xlsx");
```

Tout le reste de cet article explique quand choisir une API plus restreinte à la place.

## Imports requis
Tous les exemples JavaScript de cet article supposent que le module Aspose.Cells for Node.js via C++ a été chargé et que les types de tableaux croisés dynamiques se trouvent dans le namespace `Aspose.Cells.Pivot`. Une configuration typique est la suivante :
- `const AsposeCells = require("aspose.cells.node");`
- `const { PivotFieldType } = AsposeCells;` (ou accès via `AsposeCells.Pivot.PivotFieldType`)

## Actualiser tous les tableaux croisés dynamiques du classeur
Lorsque vous devez vous assurer que chaque cache de tableau croisé dynamique et chaque tableau croisé dynamique du classeur reflète les dernières données source, l'API la plus simple et la plus complète est `Workbook.RefreshAll()`. Un seul appel parcourt tout le classeur — actualisant chaque `PivotCache` depuis sa source, puis recalculant chaque `PivotTable` dépendant. C'est l'approche recommandée pour les actualisations générales et complètes d'un document lorsque la performance n'est pas un critère critique.
L'exemple suivant construit un classeur avec une plage source Fruit/Année/Montant, crée un tableau croisé dynamique, modifie certaines valeurs source, puis utilise `RefreshAll()` pour tout mettre à jour en un seul appel.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
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
let pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
worksheet.getCells().get("C2").putValue(300);
worksheet.getCells().get("C5").putValue(250);
worksheet.getCells().get("C9").putValue(400);
worksheet.refreshPivotTables();
workbook.save("output.xlsx");
```

## Actualiser tous les tableaux croisés dynamiques d'une seule feuille de calcul
Parfois, vous n'avez besoin d'actualiser que les tableaux croisés dynamiques présents sur une feuille de calcul spécifique — par exemple, lorsque les tableaux croisés dynamiques d'autres feuilles de calcul sont sans rapport et ne doivent pas être touchés. Pour ce cas, Aspose.Cells propose `Worksheet.RefreshPivotTables()`, qui est limité à une instance unique de `Worksheet`.

```javascript
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);
// Écrire la ligne d'en-tête Fruit / Année / Montant
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
// Écrire 8 lignes de données (lignes 2-9, correspondant à la plage source A1:C9)
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
// Ajouter un tableau croisé dynamique nommé "Pivot1" placé à la cellule de destination E3, provenant de A1:C9
var pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
var pivotTable = worksheet.getPivotTables().get(pivotIndex);
// Assigner les champs : Fruit à Ligne, Année à Colonne, Montant à Données
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Data, "Amount");
// Modifier une propriété de vue/display — c'est un changement uniquement de présentation,
// donc il ne nécessite PAS de relire les données source via PivotCache.Refresh().
pivotTable.setRefreshDataOnOpeningFile(false);
// CalculateData() restitue l'affichage de CE tableau croisé dynamique (données + style) à partir des
// données déjà détenues dans le PivotCache. Comme les données source n'ont pas changé,
// aucun aller-retour vers la source n'est effectué — seules les valeurs mises en cache sont recalculées
// dans les cellules de la feuille de calcul.
pivotTable.calculateData();
// Enregistrer le classeur sur le disque
workbook.save("output.xlsx");
```

## Actualiser un seul tableau croisé dynamique
Lorsque vous souhaitez un contrôle fin sur un seul tableau croisé dynamique, l'API basée sur le cache vous offre deux options. Le choix entre elles dépend de ce qui a réellement changé : les données source sous-jacentes, ou simplement les paramètres de vue/mise en page du tableau croisé dynamique lui-même.

### Données source modifiées — Utilisez `PivotCache.Refresh()`
Si les données source sous-jacentes ont changé, le bon point d'entrée est `pivotTable.PivotCache.Refresh()`. Cet appel relit les données source dans le cache, puis recalcule chaque `PivotTable` qui dépend de ce cache.

### Seule la vue/mise en page a changé — Utilisez `CalculateData()`
Si les données source n'ont *pas* changé mais que seuls les paramètres de vue ou de mise en page du tableau croisé dynamique ont été modifiés (par exemple, un champ a été déplacé vers une autre zone, ou un paramètre d'actualisation à l'ouverture a été activé), il n'est pas nécessaire d'effectuer un aller-retour vers la source de données. Le cache contient déjà les bonnes données ; seul le `PivotTable` rendu doit être recalculé. Dans ce cas, `pivotTable.CalculateData()` est le bon choix.
L'exemple suivant modifie une propriété non-source du tableau croisé dynamique, puis appelle `CalculateData()` pour le rendre à nouveau à partir du cache existant.
Un classeur contient souvent de nombreux tableaux croisés dynamiques qui reposent tous sur un cache partagé. Pour les énumérer — par exemple, avant d'effectuer une actualisation par lot, ou pour diagnostiquer l'impact d'un cache partagé — utilisez `PivotCache.GetPivotTables()`. Cette méthode renvoie la collection de tous les `PivotTable` qui dépendent du cache donné.

## Migration depuis l'obsolète `PivotTable.RefreshData()`
Avant Aspose.Cells for Node.js via C++ v26.7, la méthode standard pour actualiser un tableau croisé dynamique consistait à appeler `PivotTable.RefreshData()` sur chaque tableau croisé dynamique individuellement. Depuis la v26.7, cette méthode est marquée comme **obsolète** et doit être remplacée par les API sensibles au cache décrites ci-dessus.
Il y a deux raisons pour lesquelles l'approche `RefreshData()` par table est problématique dans les classeurs réels :
- Elle récupère les données depuis la source *à chaque* appel, même lorsque la source n'a pas changé.
Les remplacements recommandés sont les suivants :
L'exemple suivant démontre le nouveau modèle efficace pour les classeurs comportant plusieurs tableaux croisés dynamiques partageant un seul cache.

## Quelle API d'actualisation dois-je utiliser ?
Le tableau ci-dessous résume les API d'actualisation disponibles et quand choisir chacune d'elles.
| Objectif | API recommandée | Notes |
|------|-----------------|-------|
| Actualiser tout le classeur | `Workbook.RefreshAll()` | Un seul appel ; couvre tous les caches et tables. |
| Actualiser uniquement les tableaux croisés dynamiques d'une seule feuille | `Worksheet.RefreshPivotTables()` | Limité à une feuille de calcul. |
| Données source modifiées pour un cache | `pivotTable.PivotCache.Refresh()` | Actualise TOUS les tableaux croisés dynamiques de ce cache partagé. |
| Seuls les paramètres de vue/mise en page ont changé | `pivotTable.CalculateData()` | Évite un aller-retour inutile vers la source. |
| Lister tous les tableaux croisés dynamiques d'un cache partagé | `pivotCache.GetPivotTables()` | À utiliser pour énumérer avant une actualisation en masse. |
En pratique, privilégiez les API basées sur le cache plutôt que l'obsolète `RefreshData()` par table. Elles sont conscientes des caches partagés, évitent les récupérations de source redondantes et vous permettent de choisir le plus petit périmètre qui satisfait votre besoin d'actualisation.

## Pièges courants
- **Oublier d'actualiser avant d'enregistrer.** Un tableau croisé dynamique n'écrit ses valeurs rendues dans la feuille de calcul que lorsque sa chaîne de données est actualisée. Si vous modifiez des cellules source, appelez `PivotCache.Refresh()` (ou `Workbook.RefreshAll()`) avant `Workbook.save()`, sinon le fichier enregistré contiendra toujours les anciennes valeurs agrégées.
- **Appeler l'obsolète `RefreshData()` par table.** Dans la v26.7, `PivotTable.RefreshData()` est marquée comme obsolète et récupère la source à chaque appel. Avec plusieurs tableaux croisés dynamiques partageant un cache, cela entraîne N récupérations de source redondantes. Remplacez par un seul `PivotCache.Refresh()` suivi de `CalculateData()` par table.
- **Actualiser alors que seule la mise en page a changé.** Si vous n'avez modifié que la vue d'un tableau croisé dynamique (ordre des colonnes, `ConsolidationFunction`, etc.) sans toucher aux données source, `PivotCache.Refresh()` est inutile et lent. Appelez `pivotTable.CalculateData()` pour rendre à nouveau à partir du cache existant.
- **Source externe non prise en charge par `PivotCache.Refresh()`.** Si la source du tableau croisé dynamique provient d'une connexion externe (base de données, cube OLAP, etc.), `PivotCache.Refresh()` ne peut pas l'actualiser dans la v26.7 — elle ne prend actuellement en charge que les types de source `Sheet` et `Consolidation`. Pour les sources externes, rouvrez le classeur ou reconstruisez le cache depuis la source.

```csharp
using Aspose.Cells;
Workbook workbook = new Workbook("input.xlsx");
workbook.RefreshAll();
workbook.Save("output.xlsx");
```

{{< app/cells/assistant language="nodejs-cpp" >}}