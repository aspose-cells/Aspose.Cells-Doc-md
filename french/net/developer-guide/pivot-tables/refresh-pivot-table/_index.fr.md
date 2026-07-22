---
title: Actualisation des tableaux croisés dynamiques dans Aspose.Cells for .NET
linktitle: Actualisation des tableaux croisés dynamiques
description: Apprenez à actualiser les tableaux croisés dynamiques dans Aspose.Cells for .NET à l'aide de l'API d'actualisation des tableaux croisés dynamiques v26.7+. Cet article couvre RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData et GetPivotTables avec des exemples de code pratiques.
keywords: Aspose.Cells, .NET, tableau croisé dynamique, actualisation, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /fr/net/refresh-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells fournit une API d'actualisation en couches qui vous permet de recharger les données des tableaux croisés dynamiques à quatre portées différentes — du classeur entier jusqu'à un seul tableau croisé dynamique. À partir d'**Aspose.Cells for .NET v26.7**, l'ancienne méthode `PivotTable.RefreshData()` est marquée comme obsolète et doit être remplacée par les API plus efficaces, sensibles au cache, décrites dans cet article.

{{% /alert %}}

## Introduction

L'actualisation d'un tableau croisé dynamique est rarement une opération isolée. En arrière-plan, Aspose.Cells maintient une chaîne de données en couches qui relie vos données sources d'origine aux valeurs rendues que vous voyez dans la feuille de calcul. Comprendre cette chaîne est la clé pour choisir la bonne API d'actualisation pour chaque situation.

La chaîne de données à quatre couches est :

1. **Source de données** — les plages de feuilles de calcul d'origine, la requête de base de données ou la plage de consolidation où se trouvent les valeurs brutes.
2. **PivotCache** — l'instantané en mémoire des données sources. Chaque tableau croisé dynamique est construit au-dessus d'un `PivotCache` ; c'est là que toutes les données sont collectées et agrégées.
3. **Tableau croisé dynamique** — l'objet de vue qui définit les champs de ligne, de colonne, de valeur et de filtre. Un `PivotTable` lit *uniquement* depuis son `PivotCache`, jamais directement depuis la source de données.
4. **Cellules** — les `Cells` de la feuille de calcul dans lesquelles le `PivotTable` rend ses valeurs calculées et ses styles.

Un concept particulièrement important est le **cache partagé**. Lorsque plusieurs tableaux croisés dynamiques d'un classeur référencent la même plage source, ils partagent *une seule* instance de `PivotCache`. Un seul `PivotCache` peut être référencé par de nombreux tableaux croisés dynamiques, et l'actualisation de ce cache actualise d'un coup chaque `PivotTable` dépendant.

{{% alert color="primary" %}}

`PivotCache.SourceType` (énumération `PivotTableSourceType`) indique d'où proviennent les données du cache. Depuis la v26.7, `PivotCache.Refresh()` prend uniquement en charge les types de sources **`Sheet`** et **`Consolidation`** — c'est-à-dire les données qui se trouvent dans des plages de feuilles de calcul. Les sources externes (bases de données, connexions externes, etc.) ne sont pas encore actualisables via l'API de cache.

{{% /alert %}}

En raison de cette chaîne, il existe deux chemins d'actualisation fondamentaux dans Aspose.Cells :

- **`PivotCache.Refresh()`** — recharge la source → cache ET recalcule tous les `PivotTable` dépendants en une seule opération.
- **`PivotTable.CalculateData()`** — recalcule l'affichage d'un seul `PivotTable` à partir des données déjà mises en cache, sans nouvel aller-retour vers la source de données.

Tous les scénarios de cet article utilisent des données sources provenant de cellules de feuille de calcul, donc le type de source est `Sheet` et les opérations d'actualisation se comportent comme décrits.

## Directives Using requises

Tous les exemples C# de cet article commencent par les trois directives using suivantes, car les types de tableaux croisés dynamiques se trouvent dans l'espace de noms `Aspose.Cells.Pivot` :

- `using System;`
- `using Aspose.Cells;`
- `using Aspose.Cells.Pivot;`

## Actualiser tous les tableaux croisés dynamiques du classeur

Lorsque vous devez vous assurer que chaque cache de tableau croisé dynamique et chaque tableau croisé dynamique du classeur reflètent les dernières données sources, l'API la plus simple et la plus complète est `Workbook.RefreshAll()`. Un seul appel parcourt le classeur entier — en actualisant chaque `PivotCache` à partir de sa source, puis en recalculant chaque `PivotTable` dépendant. C'est l'approche recommandée pour les actualisations générales et complètes de documents où la performance n'est pas un problème.

L'exemple suivant construit un classeur avec une plage source Fruit/Année/Montant, crée un tableau croisé dynamique, modifie certaines valeurs sources, puis utilise `RefreshAll()` pour tout mettre à jour en un seul appel.

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

// Attribuer les champs du tableau croisé dynamique : Fruit aux Lignes, Year aux Colonnes, Amount aux Données
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

// Modifier plusieurs valeurs de Amount dans les données source pour simuler des changements
worksheet.Cells["C2"].PutValue(55);
worksheet.Cells["C5"].PutValue(85);
worksheet.Cells["C9"].PutValue(125);

// Actualiser tous les tableaux croisés dynamiques / caches de tableaux croisés dynamiques dans le classeur
workbook.RefreshAll();

// Enregistrer le classeur
workbook.Save("output.xlsx");
```

## Actualiser tous les tableaux croisés dynamiques d'une seule feuille de calcul

Parfois, vous n'avez besoin d'actualiser que les tableaux croisés dynamiques qui se trouvent sur une feuille de calcul spécifique — par exemple, lorsque les tableaux croisés dynamiques d'autres feuilles de calcul ne sont pas liés et ne doivent pas être touchés. Pour ce cas, Aspose.Cells fournit `Worksheet.RefreshPivotTables()`, qui est limité à une seule instance de `Worksheet`.

C'est plus sélectif que `Workbook.RefreshAll()` : seuls les tableaux croisés dynamiques de la feuille de calcul ciblée sont actualisés, laissant intacts tous les tableaux croisés dynamiques des autres feuilles de calcul.

L'exemple suivant remplit les mêmes données sources Fruit/Année/Montant, ajoute un tableau croisé dynamique sur la première feuille de calcul, modifie certaines valeurs sources, puis actualise uniquement les tableaux croisés dynamiques de cette feuille de calcul.

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

Lorsque vous souhaitez un contrôle précis sur un seul tableau croisé dynamique, l'API basée sur le cache vous offre deux options. Le choix entre elles dépend de ce qui a réellement changé : les données sources sous-jacentes, ou simplement les paramètres d'affichage/disposition du tableau croisé dynamique lui-même.

### Les données sources ont changé — Utilisez `PivotCache.Refresh()`

Si les données sources sous-jacentes ont changé, le bon point d'entrée est `pivotTable.PivotCache.Refresh()`. Cet appel relit les données sources dans le cache, puis recalcule chaque `PivotTable` qui dépend de ce cache.

{{% alert color="primary" %}}

Étant donné que les tableaux croisés dynamiques partagent une seule instance de `PivotCache`, l'appel de `PivotCache.Refresh()` recalcule **tous** les tableaux croisés dynamiques construits sur ce même cache — pas seulement celui que vous référencez. Si deux tableaux croisés dynamiques partagent la même plage source, l'actualisation d'un cache actualise les deux.

{{% /alert %}}

L'exemple suivant crée deux tableaux croisés dynamiques sur la même plage source pour démontrer ce comportement de cache partagé, modifie certaines valeurs sources, puis actualise via une seule référence de cache.

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
// Parce que Pivot1 et Pivot2 partagent le même PivotCache, cet appel unique
// actualise LES DEUX tableaux croisés dynamiques (données + style) à partir de la source mise à jour.
pivotTable1.PivotCache.Refresh();

// Enregistrer le classeur
workbook.Save("output.xlsx");
```

### Seuls l'affichage/disposition ont changé — Utilisez `CalculateData()`

Si les données sources n'ont *pas* changé mais que seuls les paramètres d'affichage ou de disposition du tableau croisé dynamique ont été modifiés (par exemple, un champ a été déplacé vers une autre zone, ou un paramètre d'actualisation à l'ouverture a été activé), il n'est pas nécessaire de faire un nouvel aller-retour vers la source de données. Le cache contient déjà les bonnes données ; seul le `PivotTable` rendu doit être recalculé. Dans ce cas, `pivotTable.CalculateData()` est le bon choix.

Cela évite la récupération source inutile et est nettement plus rapide lorsque de nombreux tableaux croisés dynamiques partagent le même cache.

L'exemple suivant modifie une propriété non source du tableau croisé dynamique, puis appelle `CalculateData()` pour le rendre à nouveau à partir du cache existant.

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

// Ajouter un tableau croisé dynamique nommé "Pivot1" placé à la cellule de destination E3, avec comme source A1:C9
int pivotIndex = worksheet.PivotTables.Add("A1:C9", "E3", "Pivot1");
var pivotTable = worksheet.PivotTables[pivotIndex];

// Affecter les champs : Fruit à Ligne, Year à Colonne, Amount à Données
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

// Modifier une propriété d'affichage/de mise en page — il s'agit d'une modification de présentation uniquement,
// elle ne nécessite PAS de relire les données source via PivotCache.Refresh().
pivotTable.RefreshDataOnOpeningFile = false;

// CalculateData() réaffiche l'affichage de CE tableau croisé dynamique (données + style) à partir des
// données déjà détenues dans le PivotCache. Comme les données source n'ont pas changé,
// aucun aller-retour vers la source n'est effectué — seules les valeurs mises en cache sont recalculées
// dans les cellules de la feuille de calcul.
pivotTable.CalculateData();

// Enregistrer le classeur sur le disque
workbook.Save("output.xlsx");
```

## Obtenir tous les tableaux croisés dynamiques partageant le même PivotCache

Un classeur contient souvent de nombreux tableaux croisés dynamiques qui reposent tous sur un seul cache partagé. Pour les énumérer — par exemple, avant d'effectuer une actualisation par lot, ou pour diagnostiquer l'impact du cache partagé — utilisez `PivotCache.GetPivotTables()`. Cette méthode renvoie la collection de tous les `PivotTable` qui dépendent du cache donné.

C'est aussi le moyen le plus direct de confirmer que deux tableaux croisés dynamiques partagent bien la même instance de `PivotCache` : vous pouvez comparer les références de cache, ou simplement itérer la collection renvoyée par `GetPivotTables()` et observer quels tableaux croisés dynamiques y apparaissent.

L'exemple suivant crée deux tableaux croisés dynamiques sur la même plage source, vérifie qu'ils partagent la même instance de cache, puis énumère les tableaux croisés dynamiques du cache.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Name = "Sheet1";

worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");

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

worksheet.Cells["A10"].PutValue("Grape");
worksheet.Cells["B10"].PutValue(2021);
worksheet.Cells["C10"].PutValue(900);

int pivot1Index = worksheet.PivotTables.Add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable1 = worksheet.PivotTables[pivot1Index];
pivotTable1.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable1.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable1.AddFieldToArea(PivotFieldType.Data, "Amount");

int pivot2Index = worksheet.PivotTables.Add("A1:C9", "E15", "Pivot2");
PivotTable pivotTable2 = worksheet.PivotTables[pivot2Index];
pivotTable2.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable2.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable2.AddFieldToArea(PivotFieldType.Data, "Amount");

bool sameCache = object.ReferenceEquals(pivotTable1.PivotCache, pivotTable2.PivotCache);
Console.WriteLine("Pivot1 and Pivot2 share the same PivotCache: " + sameCache);

PivotTable[] sharedPivotTables = pivotTable1.PivotCache.GetPivotTables();
Console.WriteLine("Number of pivot tables sharing the cache: " + sharedPivotTables.Length);

foreach (PivotTable pt in sharedPivotTables)
{
    Console.WriteLine("Pivot table name: " + pt.Name);
}

workbook.Save("output.xlsx");
```

## Migration depuis l'obsolète `PivotTable.RefreshData()`

Avant Aspose.Cells for .NET v26.7, la méthode standard pour actualiser un tableau croisé dynamique consistait à appeler `PivotTable.RefreshData()` sur chaque tableau croisé dynamique individuellement. Depuis la v26.7, cette méthode est marquée comme **obsolète** et doit être remplacée par les API sensibles au cache décrites ci-dessus.

Il y a deux raisons pour lesquelles l'approche `RefreshData()` par tableau est problématique dans les classeurs réels :

- Elle récupère les données depuis la source *à chaque* appel, même lorsque la source n'a pas changé.
- Chaque appel actualise l'intégralité du cache partagé. Lorsque de nombreux tableaux croisés dynamiques partagent un seul cache, appeler `RefreshData()` à plusieurs reprises pour chaque tableau croisé dynamique entraîne une récupération répétée du même cache, ce qui est très lent.

Les remplacements recommandés sont :

- **Actualiser TOUS les tableaux croisés dynamiques du classeur** → utilisez `workbook.RefreshAll();`
- **Actualiser CERTAINS d'entre eux** → utilisez `pivotTable.PivotCache.Refresh();` pour un cache. Comme le cache est partagé, cet appel unique met à jour chaque tableau croisé dynamique construit au-dessus de ce cache. Les autres tableaux croisés dynamiques qui reposent sur un cache déjà actualisé peuvent être ignorés en toute sécurité.
- **Seuls l'affichage/la disposition du tableau croisé dynamique ont changé** → utilisez `pivotTable.CalculateData();` pour rendre à nouveau depuis le cache existant sans aucun aller-retour vers la source.

L'exemple suivant démontre le nouveau modèle efficace pour les classeurs comportant plusieurs tableaux croisés dynamiques partageant un seul cache.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// Créer un nouveau classeur et accéder à la première feuille de calcul
Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];

// --- Construire les données sources : Fruit / Année / Montant (en-tête + 9 lignes) ---
sheet.Cells["A1"].PutValue("Fruit");
sheet.Cells["B1"].PutValue("Year");
sheet.Cells["C1"].PutValue("Amount");

sheet.Cells["A2"].PutValue("Grape");      sheet.Cells["B2"].PutValue(2020); sheet.Cells["C2"].PutValue(1000);
sheet.Cells["A3"].PutValue("Blueberry");  sheet.Cells["B3"].PutValue(2020); sheet.Cells["C3"].PutValue(2000);
sheet.Cells["A4"].PutValue("Kiwi");       sheet.Cells["B4"].PutValue(2020); sheet.Cells["C4"].PutValue(1500);
sheet.Cells["A5"].PutValue("Cherry");     sheet.Cells["B5"].PutValue(2020); sheet.Cells["C5"].PutValue(2500);
sheet.Cells["A6"].PutValue("Grape");      sheet.Cells["B6"].PutValue(2021); sheet.Cells["C6"].PutValue(3000);
sheet.Cells["A7"].PutValue("Blueberry");  sheet.Cells["B7"].PutValue(2021); sheet.Cells["C7"].PutValue(1800);
sheet.Cells["A8"].PutValue("Kiwi");       sheet.Cells["B8"].PutValue(2021); sheet.Cells["C8"].PutValue(2200);
sheet.Cells["A9"].PutValue("Cherry");     sheet.Cells["B9"].PutValue(2021); sheet.Cells["C9"].PutValue(2700);

// --- Ajouter le premier tableau croisé dynamique (Pivot1) à la cellule de destination E3 ---
int idx1 = sheet.PivotTables.Add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable1 = sheet.PivotTables[idx1];
pivotTable1.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable1.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable1.AddFieldToArea(PivotFieldType.Data, "Amount");

// --- Ajouter le SECOND tableau croisé dynamique (Pivot2) sur la MÊME plage source ---
// Pivot1 et Pivot2 partagent UN PivotCache sous-jacent.
// C'est exactement le scénario où l'approche héritée RefreshData() par table
// devient inefficace : actualiser une table ré-extrait l'ensemble du
// cache partagé, donc actualiser N tables effectue la même extraction coûteuse N fois.
int idx2 = sheet.PivotTables.Add("A1:C9", "E15", "Pivot2");
PivotTable pivotTable2 = sheet.PivotTables[idx2];
pivotTable2.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable2.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable2.AddFieldToArea(PivotFieldType.Data, "Amount");

// --- Modifier plusieurs valeurs Montant dans les données sources ---
sheet.Cells["C2"].PutValue(5000);   // Raisin  2020
sheet.Cells["C5"].PutValue(7500);   // Cerise 2020
sheet.Cells["C9"].PutValue(9500);   // Cerise 2021

// --- Modèle OBSOLÈTE (avant 26.7) — PivotTable.RefreshData() ---
// pivotTable1.RefreshData();  // ré-extrait de la source, actualise tout le cache
// pivotTable2.RefreshData();  // ré-extrait ENCORE — le cache est déjà à jour !
// Chaque appel reconstruit le cache partagé, donc N tables = N extractions redondantes.

// --- NOUVEAU modèle v26.7+ : actualiser le cache UNE FOIS, puis ré-afficher au besoin ---
// Un appel à PivotCache.Refresh() récupère les valeurs modifiées dans le cache partagé
// ET recalcule l'affichage de CHAQUE tableau croisé dynamique qui le référence.
// Parce que Pivot1 et Pivot2 partagent un PivotCache, cet appel unique met à jour
// les deux tables — aucun second aller-retour vers la source n'est nécessaire.
pivotTable1.PivotCache.Refresh();

// CalculateData() ne ré-affiche que l'affichage d'un tableau croisé dynamique (données + style)
// à partir des données déjà détenues dans le cache — il ne touche PAS à la source.
// Nous l'appelons sur Pivot2 ici purement pour démontrer l'API : après que le cache
// a été actualisé une fois, toute table dépendante peut être ré-affichée sans
// revenir à la source. Utilisez CalculateData() seul quand seuls les
// paramètres d'affichage/de mise en page du tableau croisé ont changé et que le cache est à jour.
pivotTable2.CalculateData();

workbook.Save("output.xlsx");
```

## Quelle API d'actualisation dois-je utiliser ?

Le tableau ci-dessous résume les API d'actualisation disponibles et quand choisir chacune d'elles.

| Objectif | API recommandée | Notes |
|----------|-----------------|-------|
| Actualiser tout dans le classeur | `Workbook.RefreshAll()` | Un seul appel ; couvre tous les caches et tableaux. |
| Actualiser uniquement les tableaux croisés dynamiques d'une seule feuille | `Worksheet.RefreshPivotTables()` | Limité à une seule feuille de calcul. |
| Les données sources ont changé pour un cache | `pivotTable.PivotCache.Refresh()` | Actualise TOUS les tableaux croisés dynamiques de ce cache partagé. |
| Seuls les paramètres d'affichage/disposition ont changé | `pivotTable.CalculateData()` | Évite un aller-retour source inutile. |
| Lister tous les tableaux croisés dynamiques d'un cache partagé | `pivotCache.GetPivotTables()` | À utiliser pour énumérer avant une actualisation en masse. |

En pratique, privilégiez les API basées sur le cache par rapport à l'obsolète `RefreshData()` par tableau. Elles sont conscientes des caches partagés, elles évitent les récupérations redondantes de la source, et elles vous permettent de choisir la plus petite portée qui satisfait votre besoin d'actualisation.

{{< app/cells/assistant language="csharp" >}}