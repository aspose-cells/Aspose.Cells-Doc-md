---
title: Actualisation des tableaux croisés dynamiques dans Aspose.Cells for .NET
linktitle: Actualisation des tableaux croisés dynamiques dans Aspose.Cells for .NET
description: Apprenez à actualiser les tableaux croisés dynamiques dans Aspose.Cells for .NET à l'aide de l'API d'actualisation des tableaux croisés dynamiques de la version 26.7+. Cet article couvre RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData et GetPivotTables avec des exemples de code pratiques.
keywords: Aspose.Cells, .NET, tableau croisé dynamique, actualisation, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /fr/net/refresh-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---


{{% alert color="primary" %}}

Aspose.Cells fournit une API d'actualisation en couches qui vous permet de recharger les données des tableaux croisés dynamiques à quatre niveaux différents — du classeur entier jusqu'à un seul tableau croisé dynamique. À partir de **Aspose.Cells for .NET v26.7**, la méthode héritée `PivotTable.RefreshData()` est marquée comme obsolète et doit être remplacée par les API plus efficaces, prenant en compte le cache, décrites dans cet article.

{{% /alert %}}

## Introduction

L'actualisation d'un tableau croisé dynamique est rarement une opération unique. En arrière-plan, Aspose.Cells maintient une chaîne de données en couches qui relie vos données source d'origine aux valeurs rendues que vous voyez dans la feuille de calcul. Comprendre cette chaîne est la clé pour choisir la bonne API d'actualisation pour chaque situation.

La chaîne de données à quatre couches est :

1. **Source de données** — les plages de cellules de la feuille de calcul d'origine, la requête de base de données ou la plage de consolidation où se trouvent les valeurs brutes.
2. **PivotCache** — l'instantané en mémoire des données source. Chaque tableau croisé dynamique est construit au-dessus d'un `PivotCache` ; c'est là que toutes les données sont collectées et agrégées.
3. **PivotTable** — l'objet de vue qui définit les champs de ligne, de colonne, de valeur et de filtre. Un `PivotTable` lit *uniquement* à partir de son `PivotCache`, jamais directement à partir de la source de données.
4. **Cells** — les `Cells` de la feuille de calcul dans lesquels le `PivotTable` rend ses valeurs calculées et ses styles.

Un concept particulièrement important est le **cache partagé**. Lorsque plusieurs tableaux croisés dynamiques d'un classeur référencent la même plage source, ils partagent *une seule* instance de `PivotCache`. Un seul `PivotCache` peut être référencé par de nombreux tableaux croisés dynamiques, et l'actualisation de ce cache actualise chaque `PivotTable` dépendant en une seule fois.

{{% alert color="primary" %}}

`PivotCache.SourceType` (énumération `PivotTableSourceType`) indique d'où proviennent les données du cache. Depuis la version 26.7, `PivotCache.Refresh()` ne prend en charge que les types de source **`Sheet`** et **`Consolidation`** — c'est-à-dire les données qui se trouvent dans des plages de feuilles de calcul. Les sources externes (bases de données, connexions externes, etc.) ne sont pas encore actualisables via l'API du cache.

{{% /alert %}}

En raison de cette chaîne, il existe deux chemins d'actualisation fondamentaux dans Aspose.Cells :

- **`PivotCache.Refresh()`** — recharge la source → cache ET recalcule tous les `PivotTable` dépendants en une seule opération.
- **`PivotTable.CalculateData()`** — recalcule l'affichage d'un seul `PivotTable` à partir des données déjà mises en cache, sans aller-retour vers la source de données.

Tous les scénarios de cet article utilisent des données source issues de cellules de feuille de calcul, donc le type de source est `Sheet` et les opérations d'actualisation se comportent comme décrit.

## Directives Using requises

Tous les exemples C# de cet article commencent par les trois directives using suivantes car les types de tableaux croisés dynamiques se trouvent dans le namespace `Aspose.Cells.Pivot` :

- `using System;`
- `using Aspose.Cells;`
- `using Aspose.Cells.Pivot;`

## Actualiser tous les tableaux croisés dynamiques du classeur

Lorsque vous devez vous assurer que chaque cache de tableau croisé dynamique et chaque tableau croisé dynamique du classeur reflètent les dernières données source, l'API la plus simple et la plus complète est `Workbook.RefreshAll()`. Un seul appel parcourt tout le classeur — actualisant chaque `PivotCache` à partir de sa source puis recalculant chaque `PivotTable` dépendant. C'est l'approche recommandée pour les actualisations générales de documents complets où la performance n'est pas un souci.

L'exemple suivant construit un classeur avec une plage source Fruit/Année/Montant, crée un tableau croisé dynamique, modifie certaines valeurs source, puis utilise `RefreshAll()` pour tout mettre à jour en un seul appel.

```csharp
using Aspose.Cells;

Workbook workbook = new Workbook("input.xlsx");
workbook.RefreshAll();
workbook.Save("output.xlsx");
```

## Actualiser tous les tableaux croisés dynamiques d'une seule feuille de calcul

Parfois, vous n'avez besoin d'actualiser que les tableaux croisés dynamiques qui se trouvent sur une feuille de calcul spécifique — par exemple, lorsque les tableaux croisés dynamiques d'autres feuilles de calcul sont connus pour être sans rapport et ne doivent pas être touchés. Pour ce cas, Aspose.Cells fournit `Worksheet.RefreshPivotTables()`, qui est limité à une seule instance de `Worksheet`.

C'est plus sélectif que `Workbook.RefreshAll()` : seuls les tableaux croisés dynamiques de la feuille de calcul ciblée sont actualisés, en laissant intacts les tableaux croisés dynamiques des autres feuilles.

L'exemple suivant remplit les mêmes données source Fruit/Année/Montant, ajoute un tableau croisé dynamique sur la première feuille de calcul, modifie certaines valeurs source, puis actualise uniquement les tableaux croisés dynamiques de cette feuille de calcul.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// Créer un nouveau classeur
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];

// Écrire la ligne d'en-tête dans les cellules A1:C1
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");

// Écrire les lignes de données dans les cellules A2:C9 (8 lignes de données sur les fruits pour 2020 et 2021)
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

// Ajouter un tableau croisé dynamique : plage source "A1:C9", cellule de destination "E3", nom "Pivot1"
int pivotIndex = worksheet.PivotTables.Add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];

// Assigner les champs du tableau croisé dynamique : Fruit aux Lignes, Year aux Colonnes, Amount aux Données
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

// Modifier plusieurs valeurs de Amount dans les données sources pour simuler des changements
worksheet.Cells["C2"].PutValue(55);
worksheet.Cells["C5"].PutValue(85);
worksheet.Cells["C9"].PutValue(125);

// Actualiser tous les tableaux croisés dynamiques / caches de tableaux croisés dynamiques dans le classeur
workbook.RefreshAll();

// Enregistrer le classeur
workbook.Save("output.xlsx");
```

## Actualiser un seul tableau croisé dynamique

Lorsque vous souhaitez un contrôle fin sur un seul tableau croisé dynamique, l'API basée sur le cache vous offre deux options. Le choix entre les deux dépend de ce qui a réellement changé : les données source sous-jacentes, ou simplement les paramètres d'affichage/de disposition du tableau croisé dynamique lui-même.

### Les données source ont changé — Utilisez `PivotCache.Refresh()`

Si les données source sous-jacentes ont changé, le bon point d'entrée est `pivotTable.PivotCache.Refresh()`. Cet appel relit les données source dans le cache, puis recalcule chaque `PivotTable` qui dépend de ce cache.

{{% alert color="primary" %}}

Parce que les tableaux croisés dynamiques partagent une seule instance de `PivotCache`, l'appel de `PivotCache.Refresh()` recalcule **tous** les tableaux croisés dynamiques construits sur ce même cache — pas seulement celui que vous référencez. Si deux tableaux croisés dynamiques partagent la même plage source, l'actualisation d'un cache actualise les deux.

{{% /alert %}}

L'exemple suivant crée deux tableaux croisés dynamiques sur la même plage source pour démontrer ce comportement de cache partagé, modifie certaines valeurs source, puis actualise via une seule référence au cache.

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

### Seule l'affichage/la disposition a changé — Utilisez `CalculateData()`

Si les données source n'ont *pas* changé mais que seuls les paramètres d'affichage ou de disposition du tableau croisé dynamique ont été modifiés (par exemple, un champ a été déplacé vers une autre zone, ou un paramètre d'actualisation à l'ouverture a été activé), il n'est pas nécessaire de faire un aller-retour vers la source de données. Le cache contient déjà les bonnes données ; seul le `PivotTable` rendu a besoin d'être recalculé. Dans ce cas, `pivotTable.CalculateData()` est le bon choix.

Cela évite la récupération source inutile et est nettement plus rapide lorsque de nombreux tableaux croisés dynamiques partagent le même cache.

L'exemple suivant modifie une propriété non source du tableau croisé dynamique, puis appelle `CalculateData()` pour le restituer à partir du cache existant.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// Créer un nouveau classeur et accéder à la première feuille de calcul
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];

// Écrire la ligne d'en-tête : Fruit / Année / Montant
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");

// Écrire environ 9 lignes de données (raisin / myrtille / kiwi / cerise sur 2020-2021)
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
worksheet.Cells["C6"].PutValue(500);

worksheet.Cells["A7"].PutValue("Blueberry");
worksheet.Cells["B7"].PutValue(2021);
worksheet.Cells["C7"].PutValue(600);

worksheet.Cells["A8"].PutValue("Kiwi");
worksheet.Cells["B8"].PutValue(2021);
worksheet.Cells["C8"].PutValue(700);

worksheet.Cells["A9"].PutValue("Cherry");
worksheet.Cells["B9"].PutValue(2021);
worksheet.Cells["C9"].PutValue(800);

// Ajouter le premier tableau croisé dynamique "Pivot1" ancré à la cellule E3, plage source A1:C9
int pivotIndex1 = worksheet.PivotTables.Add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable1 = worksheet.PivotTables[pivotIndex1];

// Assigner les champs pour Pivot1
pivotTable1.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable1.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable1.AddFieldToArea(PivotFieldType.Data, "Amount");

// Ajouter un SECOND tableau croisé dynamique "Pivot2" ancré à E15 en utilisant la MÊME plage source A1:C9
// Pivot1 et Pivot2 partagent un seul PivotCache car la plage source est identique.
int pivotIndex2 = worksheet.PivotTables.Add("A1:C9", "E15", "Pivot2");
PivotTable pivotTable2 = worksheet.PivotTables[pivotIndex2];

// Assigner les mêmes champs pour Pivot2
pivotTable2.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable2.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable2.AddFieldToArea(PivotFieldType.Data, "Amount");

// Modifier plusieurs valeurs de cellules Montant dans les données source pour simuler un changement de données
worksheet.Cells["C2"].PutValue(150);
worksheet.Cells["C4"].PutValue(350);
worksheet.Cells["C7"].PutValue(650);

// Actualiser le PivotCache partagé.
// Comme Pivot1 et Pivot2 partagent le même PivotCache, cet appel unique
// actualise LES DEUX tableaux croisés dynamiques (données + style) à partir de la source mise à jour.
pivotTable1.PivotCache.Refresh();

// Enregistrer le classeur
workbook.Save("output.xlsx");
```

## Obtenir tous les tableaux croisés dynamiques partageant le même PivotCache

Un classeur contient souvent de nombreux tableaux croisés dynamiques qui reposent tous sur un cache partagé. Pour les énumérer — par exemple, avant d'effectuer une actualisation par lot, ou pour diagnostiquer l'impact d'un cache partagé — utilisez `PivotCache.GetPivotTables()`. Cette méthode renvoie la collection de chaque `PivotTable` qui dépend du cache donné.

C'est aussi le moyen le plus direct de confirmer que deux tableaux croisés dynamiques partagent effectivement la même instance de `PivotCache` : vous pouvez comparer les références du cache, ou simplement parcourir la collection renvoyée par `GetPivotTables()` et observer quels tableaux croisés dynamiques y apparaissent.

L'exemple suivant crée deux tableaux croisés dynamiques sur la même plage source, vérifie qu'ils partagent la même instance de cache, puis énumère les tableaux croisés dynamiques du cache.

```csharp
using Aspose.Cells;
using Aspose.Cells.Pivot;

var workbook = new Workbook();
var worksheet = workbook.Worksheets[0];

// Écrire la ligne d'en-tête Fruit / Year / Amount
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

// Ajouter un tableau croisé dynamique nommé "Pivot1" placé à la cellule de destination E3, à partir de A1:C9
int pivotIndex = worksheet.PivotTables.Add("A1:C9", "E3", "Pivot1");
var pivotTable = worksheet.PivotTables[pivotIndex];

// Assigner les champs : Fruit à Ligne, Year à Colonne, Amount à Données
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

// Modifier une propriété d'affichage/de mise en page — il s'agit d'une modification purement présentationnelle,
// elle ne nécessite PAS de relire les données source via PivotCache.Refresh().
pivotTable.RefreshDataOnOpeningFile = false;

// CalculateData() restitue l'affichage de CE tableau croisé dynamique (données + style) à partir des
// données déjà détenues dans le PivotCache. Comme les données source n'ont pas changé,
// aucun aller-retour vers la source n'est effectué — seules les valeurs mises en cache sont recalculées
// dans les cellules de la feuille de calcul.
pivotTable.CalculateData();

// Enregistrer le classeur sur le disque
workbook.Save("output.xlsx");
```

## Migration depuis l'obsolète `PivotTable.RefreshData()`

Avant Aspose.Cells for .NET v26.7, la façon standard d'actualiser un tableau croisé dynamique était d'appeler `PivotTable.RefreshData()` sur chaque tableau croisé dynamique individuellement. Depuis la version 26.7, cette méthode est marquée comme **obsolète** et doit être remplacée par les API prenant en compte le cache décrites ci-dessus.

Il y a deux raisons pour lesquelles l'approche `RefreshData()` par tableau est problématique dans les classeurs du monde réel :

- Elle récupère à nouveau les données depuis la source *à chaque* appel, même lorsque la source n'a pas changé.
- Chaque appel actualise l'intégralité du cache partagé. Lorsque de nombreux tableaux croisés dynamiques partagent un cache, l'appel répété de `RefreshData()` par tableau croisé dynamique provoque la récupération à plusieurs reprises du même cache, ce qui est très lent.

Les remplacements recommandés sont :

- **Actualiser TOUS les tableaux croisés dynamiques du classeur** → utilisez `workbook.RefreshAll();`
- **Actualiser CERTAINS d'entre eux** → utilisez `pivotTable.PivotCache.Refresh();` pour un cache. Comme le cache est partagé, cet unique appel met à jour chaque tableau croisé dynamique construit au-dessus de ce cache. Les autres tableaux croisés dynamiques qui reposent sur un cache déjà actualisé peuvent être ignorés en toute sécurité.
- **Seule l'affichage/la disposition du tableau croisé a changé** → utilisez `pivotTable.CalculateData();` pour restituer à partir du cache existant sans aucun aller-retour vers la source.

L'exemple suivant démontre le nouveau modèle efficace pour les classeurs comportant plusieurs tableaux croisés dynamiques partageant un seul cache.


## Quelle API d'actualisation dois-je utiliser ?

Le tableau ci-dessous résume les API d'actualisation disponibles et quand choisir chacune d'elles.

| Objectif | API recommandée | Notes |
|------|-----------------|-------|
| Actualiser tout dans le classeur | `Workbook.RefreshAll()` | Un seul appel ; couvre tous les caches et tableaux. |
| Actualiser uniquement les tableaux croisés dynamiques d'une seule feuille | `Worksheet.RefreshPivotTables()` | Limité à une seule feuille de calcul. |
| Données source modifiées pour un cache | `pivotTable.PivotCache.Refresh()` | Actualise TOUS les tableaux croisés dynamiques de ce cache partagé. |
| Seuls les paramètres d'affichage/de disposition ont changé | `pivotTable.CalculateData()` | Évite un aller-retour inutile vers la source. |
| Lister tous les tableaux croisés dynamiques d'un cache partagé | `pivotCache.GetPivotTables()` | À utiliser pour énumérer avant une actualisation en masse. |

En pratique, privilégiez les API basées sur le cache par rapport à l'obsolète `RefreshData()` par tableau. Elles tiennent compte des caches partagés, évitent les récupérations redondantes de la source, et vous permettent de choisir la portée la plus petite qui satisfait votre besoin d'actualisation.

{{< app/cells/assistant language="csharp" >}}
