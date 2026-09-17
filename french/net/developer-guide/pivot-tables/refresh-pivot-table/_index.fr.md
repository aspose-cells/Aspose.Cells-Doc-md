---
title: Actualiser les tableaux croisés dynamiques et les caches de tableaux croisés dynamiques dans Aspose.Cells for .NET
description: Apprenez à actualiser les tableaux croisés dynamiques dans Aspose.Cells for .NET à l'aide de l'API d'actualisation des tableaux croisés dynamiques v26.7+. Cet article couvre RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData et GetPivotTables avec des exemples de code pratiques.
linktitle: Actualiser les tableaux croisés dynamiques
keywords: Aspose.Cells, .NET, tableau croisé dynamique, actualiser, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /fr/net/refresh-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells fournit une API d'actualisation en couches qui vous permet de recharger les données des tableaux croisés dynamiques à quatre niveaux de portée différents, du classeur entier jusqu'à un seul tableau croisé dynamique. À partir d'**Aspose.Cells for .NET v26.7**, l'ancienne méthode `PivotTable.RefreshData()` est marquée comme obsolète et doit être remplacée par les API plus efficaces, conscientes du cache, décrites dans cet article.
{{% /alert %}}

## Introduction
L'actualisation d'un tableau croisé dynamique est rarement une opération unique. En arrière-plan, Aspose.Cells maintient une chaîne de données en couches qui relie vos données sources d'origine aux valeurs rendues que vous voyez dans la feuille de calcul. Comprendre cette chaîne est la clé pour choisir la bonne API d'actualisation dans chaque situation.
La chaîne de données à quatre couches est la suivante :
1. **Source de données** — les plages de feuilles de calcul d'origine, la requête de base de données ou la plage de consolidation où résident les valeurs brutes.
2. **PivotCache** — l'instantané en mémoire des données sources. Chaque tableau croisé dynamique est construit au-dessus d'un `PivotCache` ; c'est là que toutes les données sont rassemblées et agrégées.
3. **PivotTable** — l'objet de vue qui définit les champs de ligne, colonne, valeur et filtre. Un `PivotTable` lit *uniquement* à partir de son `PivotCache`, jamais directement à partir de la source de données.
4. **Cells** — la collection `Cells` de la feuille de calcul dans laquelle le `PivotTable` rend ses valeurs calculées et ses styles.

{{% alert color="primary" %}}
`PivotCache.SourceType` (énumération `PivotTableSourceType`) indique d'où proviennent les données du cache. Depuis la v26.7, `PivotCache.Refresh()` ne prend en charge que les types de source **`Sheet`** et **`Consolidation`** — c'est-à-dire les données qui résident dans des plages de feuilles de calcul. Les sources externes (bases de données, connexions externes, etc.) ne sont pas encore actualisables via l'API du cache.
{{% /alert %}}

En raison de cette chaîne, il existe deux chemins d'actualisation fondamentaux dans Aspose.Cells :
- **`PivotTable.CalculateData()`** — recalcule l'affichage d'un `PivotTable` à partir des données déjà mises en cache, sans aller-retour vers la source de données.
Tous les scénarios de cet article utilisent des données sources provenant de cellules de feuilles de calcul, donc le type de source est `Sheet` et les opérations d'actualisation se comportent comme décrit.

## Démarrage rapide
Si vous avez seulement besoin du code le plus court possible qui actualise chaque tableau croisé dynamique du classeur, un seul appel suffit :

```csharp
using Aspose.Cells;
Workbook workbook = new Workbook("input.xlsx");
workbook.RefreshAll();
workbook.Save("output.xlsx");
```

Tout le reste de cet article explique quand choisir une API plus restreinte à la place.

## Directives Using requises
Tous les exemples C# de cet article commencent par les trois directives using suivantes car les types liés aux tableaux croisés dynamiques se trouvent dans l'espace de noms `Aspose.Cells.Pivot` :
- `using System;`
- `using Aspose.Cells;`
- `using Aspose.Cells.Pivot;`

## Actualiser tous les tableaux croisés dynamiques du classeur
Lorsque vous devez vous assurer que chaque cache de tableau croisé dynamique et chaque tableau croisé dynamique du classeur reflète les dernières données sources, l'API la plus simple et la plus complète est `Workbook.RefreshAll()`. Un seul appel traverse l'ensemble du classeur — actualisant chaque `PivotCache` à partir de sa source, puis recalculant chaque `PivotTable` dépendant. C'est l'approche recommandée pour les actualisations complètes et générales de documents où la performance n'est pas un souci.
L'exemple suivant construit un classeur avec une plage source Fruit/Année/Montant, crée un tableau croisé dynamique, modifie certaines valeurs sources, puis utilise `RefreshAll()` pour tout mettre à jour en un seul appel.

## Actualiser tous les tableaux croisés dynamiques d'une seule feuille de calcul
Parfois, vous n'avez besoin d'actualiser que les tableaux croisés dynamiques qui se trouvent sur une feuille de calcul spécifique — par exemple, lorsque les tableaux croisés dynamiques des autres feuilles de calcul sont connus pour ne pas être liés et ne doivent pas être touchés. Pour ce cas, Aspose.Cells fournit `Worksheet.RefreshPivotTables()`, qui est limité à une seule instance de `Worksheet`.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");
worksheet.Cells["A2"].PutValue("grape");
worksheet.Cells["B2"].PutValue(2020);
worksheet.Cells["C2"].PutValue(100);
worksheet.Cells["A3"].PutValue("blueberry");
worksheet.Cells["B3"].PutValue(2021);
worksheet.Cells["C3"].PutValue(150);
worksheet.Cells["A4"].PutValue("kiwi");
worksheet.Cells["B4"].PutValue(2020);
worksheet.Cells["C4"].PutValue(200);
worksheet.Cells["A5"].PutValue("cherry");
worksheet.Cells["B5"].PutValue(2021);
worksheet.Cells["C5"].PutValue(120);
worksheet.Cells["A6"].PutValue("grape");
worksheet.Cells["B6"].PutValue(2021);
worksheet.Cells["C6"].PutValue(180);
worksheet.Cells["A7"].PutValue("blueberry");
worksheet.Cells["B7"].PutValue(2020);
worksheet.Cells["C7"].PutValue(130);
worksheet.Cells["A8"].PutValue("kiwi");
worksheet.Cells["B8"].PutValue(2021);
worksheet.Cells["C8"].PutValue(220);
worksheet.Cells["A9"].PutValue("cherry");
worksheet.Cells["B9"].PutValue(2020);
worksheet.Cells["C9"].PutValue(140);
int pivotIndex = worksheet.PivotTables.Add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
worksheet.Cells["C2"].PutValue(300);
worksheet.Cells["C5"].PutValue(250);
worksheet.Cells["C9"].PutValue(400);
worksheet.RefreshPivotTables();
workbook.Save("output.xlsx");
```

## Actualiser un seul tableau croisé dynamique
Lorsque vous souhaitez un contrôle granulaire sur un seul tableau croisé dynamique, l'API basée sur le cache vous offre deux options. Le choix entre elles dépend de ce qui a réellement changé : les données sources sous-jacentes, ou seulement les paramètres de vue/mise en page du tableau croisé dynamique lui-même.

### Données sources modifiées — Utilisez `PivotCache.Refresh()`
Si les données sources sous-jacentes ont changé, le bon point d'entrée est `pivotTable.PivotCache.Refresh()`. Cet appel relit les données sources dans le cache puis recalcule chaque `PivotTable` qui dépend de ce cache.

### Seule la vue/mise en page modifiée — Utilisez `CalculateData()`
Si les données sources n'ont *pas* changé mais que seuls les paramètres de vue ou de mise en page du tableau croisé dynamique ont été modifiés (par exemple, un champ a été déplacé vers une autre zone, ou un paramètre d'actualisation à l'ouverture a été activé), il n'est pas nécessaire de faire un aller-retour vers la source de données. Le cache contient déjà les bonnes données ; seul le `PivotTable` rendu doit être recalculé. Dans ce cas, `pivotTable.CalculateData()` est le bon choix.
L'exemple suivant modifie une propriété non liée à la source du tableau croisé dynamique, puis appelle `CalculateData()` pour le restituer à partir du cache existant.

```csharp
using Aspose.Cells;
using Aspose.Cells.Pivot;
var workbook = new Workbook();
var worksheet = workbook.Worksheets[0];
// Écrire la ligne d'en-tête Fruit / Année / Montant
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");
// Écrire 8 lignes de données (lignes 2-9, correspondant à la plage source A1:C9)
worksheet.Cells["A2"].PutValue("Grape");
worksheet.Cells["B2"].PutValue(2020);
worksheet.Cells["C2"].PutValue(100);
worksheet.Cells["A3"].PutValue("Blueberry");
worksheet.Cells["B3"].PutValue(2020);
worksheet.Cells["C3"].PutValue(200);
worksheet.Cells["A4"].PutValue("Kiwi");
worksheet.Cells["B4"].PutValue(2020);
worksheet.Cells["C4"].PutValue(300);
worksheet.Cells["A5"].PutValue("Cherry");
worksheet.Cells["B5"].PutValue(2020);
worksheet.Cells["C5"].PutValue(400);
worksheet.Cells["A6"].PutValue("Grape");
worksheet.Cells["B6"].PutValue(2021);
worksheet.Cells["C6"].PutValue(150);
worksheet.Cells["A7"].PutValue("Blueberry");
worksheet.Cells["B7"].PutValue(2021);
worksheet.Cells["C7"].PutValue(250);
worksheet.Cells["A8"].PutValue("Kiwi");
worksheet.Cells["B8"].PutValue(2021);
worksheet.Cells["C8"].PutValue(350);
worksheet.Cells["A9"].PutValue("Cherry");
worksheet.Cells["B9"].PutValue(2021);
worksheet.Cells["C9"].PutValue(450);
// Ajouter un tableau croisé dynamique nommé "Pivot1" placé dans la cellule de destination E3, à partir de la plage A1:C9
int pivotIndex = worksheet.PivotTables.Add("A1:C9", "E3", "Pivot1");
var pivotTable = worksheet.PivotTables[pivotIndex];
// Assigner les champs : Fruit à Ligne, Année à Colonne, Montant à Données
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
// Modifier une propriété d'affichage/de disposition — c'est un changement de présentation uniquement,
// cela ne nécessite PAS de relire les données source via PivotCache.Refresh().
pivotTable.RefreshDataOnOpeningFile = false;
// CalculateData() restitue l'affichage de CE tableau croisé dynamique (données + style) à partir du
// données déjà détenues dans le PivotCache. Comme les données source n'ont pas changé,
// aucun aller-retour vers la source n'est effectué — seules les valeurs mises en cache sont recalculées
// dans les cellules de la feuille de calcul.
pivotTable.CalculateData();
// Enregistrer le classeur sur le disque
workbook.Save("output.xlsx");
```

Un classeur contient souvent de nombreux tableaux croisés dynamiques qui reposent tous sur un cache partagé. Pour les énumérer — par exemple, avant d'effectuer une actualisation en masse, ou pour diagnostiquer l'impact d'un cache partagé — utilisez `PivotCache.GetPivotTables()`. Cette méthode renvoie la collection de tous les `PivotTable` qui dépendent du cache donné.

## Migration depuis l'obsolète `PivotTable.RefreshData()`
Avant Aspose.Cells for .NET v26.7, la méthode standard pour actualiser un tableau croisé dynamique consistait à appeler `PivotTable.RefreshData()` sur chaque tableau croisé dynamique individuellement. À partir de la v26.7, cette méthode est marquée comme **obsolète** et doit être remplacée par les API conscientes du cache décrites ci-dessus.
Il y a deux raisons pour lesquelles l'approche `RefreshData()` par tableau est problématique dans les classeurs réels :
- Elle récupère à nouveau les données depuis la source *à chaque* appel, même lorsque la source n'a pas changé.
Les remplacements recommandés sont les suivants :
L'exemple suivant illustre le nouveau modèle efficace pour les classeurs comportant plusieurs tableaux croisés dynamiques partageant un seul cache.

## Quelle API d'actualisation dois-je utiliser ?
Le tableau ci-dessous résume les API d'actualisation disponibles et quand choisir chacune d'elles.
| Objectif | API recommandée | Notes |
|----------|-----------------|-------|
| Actualiser tout dans le classeur | `Workbook.RefreshAll()` | Un appel ; couvre tous les caches et tableaux. |
| Actualiser uniquement les tableaux croisés dynamiques d'une seule feuille | `Worksheet.RefreshPivotTables()` | Limité à une seule feuille de calcul. |
| Données sources modifiées pour un cache | `pivotTable.PivotCache.Refresh()` | Actualise TOUS les tableaux croisés dynamiques de ce cache partagé. |
| Seuls les paramètres de vue/mise en page ont changé | `pivotTable.CalculateData()` | Évite l'aller-retour inutile vers la source. |
| Lister tous les tableaux croisés dynamiques d'un cache partagé | `pivotCache.GetPivotTables()` | À utiliser pour énumérer avant une actualisation en masse. |
En pratique, préférez les API basées sur le cache à l'obsolète `RefreshData()` par tableau. Elles sont conscientes des caches partagés, évitent les récupérations redondantes de la source et vous permettent de choisir la portée la plus petite qui satisfait votre besoin d'actualisation.

## Pièges courants
- **Oublier d'actualiser avant d'enregistrer.** Un tableau croisé dynamique n'écrit ses valeurs rendues dans la feuille de calcul que lorsque sa chaîne de données est actualisée. Si vous modifiez des cellules sources, appelez `PivotCache.Refresh()` (ou `Workbook.RefreshAll()`) avant `Workbook.Save()`, sinon le fichier enregistré contiendra toujours les anciennes valeurs agrégées.
- **Appeler l'obsolète `RefreshData()` par tableau.** Dans la v26.7, `PivotTable.RefreshData()` est marqué comme obsolète et récupère à nouveau la source à chaque appel. Avec plusieurs tableaux croisés dynamiques partageant un cache, cela signifie N récupérations redondantes de la source. Remplacez par un seul `PivotCache.Refresh()` suivi de `CalculateData()` par tableau.
- **Actualiser alors que seule la mise en page a changé.** Si vous n'avez modifié que la vue d'un tableau croisé dynamique (ordre des colonnes, `ConsolidationFunction`, etc.) sans toucher aux données sources, `PivotCache.Refresh()` est inutile et lent. Appelez `pivotTable.CalculateData()` pour restituer à partir du cache existant.
- **Source externe non prise en charge par `PivotCache.Refresh()`.** Si la source du tableau croisé dynamique provient d'une connexion externe (base de données, cube OLAP, etc.), `PivotCache.Refresh()` ne peut pas l'actualiser dans la v26.7 — elle ne prend actuellement en charge que les types de source `Sheet` et `Consolidation`. Pour les sources externes, rouvrez le classeur ou reconstruisez le cache à partir de la source.linktitle: Actualiser les tableaux croisés dynamiquescsharp
Un classeur contient souvent de nombreux tableaux croisés dynamiques qui reposent tous sur un cache partagé. Pour les énumérer — par exemple, avant d'effectuer une actualisation en masse, ou pour diagnostiquer l'impact d'un cache partagé — utilisez `PivotCache.GetPivotTables()`. Cette méthode renvoie la collection de tous les `PivotTable` qui dépendent du cache donné.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
// Create a new workbook
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
// Write header row into cells A1:C1
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");
// Write data rows into cells A2:C9 (8 rows of fruit data across 2020 and 2021)
worksheet.Cells["A2"].PutValue("grape");
worksheet.Cells["B2"].PutValue(2020);
worksheet.Cells["C2"].PutValue(50);
worksheet.Cells["A3"].PutValue("blueberry");
worksheet.Cells["B3"].PutValue(2020);
worksheet.Cells["C3"].PutValue(60);
worksheet.Cells["A4"].PutValue("kiwi");
worksheet.Cells["B4"].PutValue(2020);
worksheet.Cells["C4"].PutValue(70);
worksheet.Cells["A5"].PutValue("cherry");
worksheet.Cells["B5"].PutValue(2020);
worksheet.Cells["C5"].PutValue(80);
worksheet.Cells["A6"].PutValue("grape");
worksheet.Cells["B6"].PutValue(2021);
worksheet.Cells["C6"].PutValue(90);
worksheet.Cells["A7"].PutValue("blueberry");
worksheet.Cells["B7"].PutValue(2021);
worksheet.Cells["C7"].PutValue(100);
worksheet.Cells["A8"].PutValue("kiwi");
worksheet.Cells["B8"].PutValue(2021);
worksheet.Cells["C8"].PutValue(110);
worksheet.Cells["A9"].PutValue("cherry");
worksheet.Cells["B9"].PutValue(2021);
worksheet.Cells["C9"].PutValue(120);
// Add a pivot table: source range "A1:C9", destination cell "E3", name "Pivot1"
int pivotIndex = worksheet.PivotTables.Add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];
// Assign pivot fields: Fruit to Rows, Year to Columns, Amount to Data
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
// Modify several Amount values in the source data to simulate changes
worksheet.Cells["C2"].PutValue(55);
worksheet.Cells["C5"].PutValue(85);
worksheet.Cells["C9"].PutValue(125);
// Refresh every pivot table / pivot cache in the workbook
workbook.RefreshAll();
// Save the workbook
workbook.Save("output.xlsx");
```

{{< app/cells/assistant language="csharp" >}}