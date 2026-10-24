---
title: Actualiser les tableaux croisés dynamiques et les caches de pivot dans Aspose.Cells for .NET
description: Découvrez comment actualiser les tableaux croisés dynamiques dans Aspose.Cells for .NET à l’aide de l’API d’actualisation des pivots v26.7+. Cet article présente RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData et GetPivotTables avec des exemples de code pratiques.
linktitle: Actualiser les tableaux croisés dynamiques
keywords: Aspose.Cells, .NET, tableau croisé dynamique, actualisation, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /fr/net/refresh-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells fournit une API d’actualisation hiérarchisée qui permet de recharger les données des tableaux croisés dynamiques à quatre niveaux de granularité — de l’ensemble du classeur jusqu’au tableau croisé dynamique individuel. Avec **Aspose.Cells for .NET v26.7**, la méthode héritée `PivotTable.RefreshData()` est marquée comme obsolète et doit être remplacée par les API plus efficaces, qui tiennent compte du cache et sont décrites dans cet article.
{{% /alert %}}

## Introduction
L’actualisation d’un tableau croisé dynamique est rarement une opération unique. En arrière-plan, Aspose.Cells maintient une chaîne de données hiérarchisée qui relie les données source d’origine aux valeurs affichées dans la feuille de calcul. Comprendre cette chaîne est essentiel pour choisir l’API d’actualisation appropriée à chaque situation.
La chaîne de données à quatre niveaux est :
1. **Source de données** — les plages de la feuille de calcul d’origine, la requête de base de données ou la plage de consolidation dans lesquelles résident les valeurs brutes.
2. **`PivotCache`** — l’instantané en mémoire des données source. Chaque tableau croisé dynamique est construit sur un `PivotCache` ; c’est là que toutes les données sont regroupées et agrégées.
3. **`PivotTable`** — l’objet de vue qui définit les champs de ligne, de colonne, de valeur et de filtre. Un `PivotTable` lit *uniquement* les données de son `PivotCache`, jamais directement celles de la source de données.
4. **`Cells`** — la collection `Cells` de la feuille de calcul dans laquelle le `PivotTable` rend les valeurs qu’il calcule et les styles.

{{% alert color="primary" %}}
`PivotCache.SourceType` (l’énumération `PivotTableSourceType`) indique d’où viennent les données du cache. Depuis la version v26.7, `PivotCache.Refresh()` prend en charge uniquement les types de source **`Sheet`** et **`Consolidation`** — autrement dit, les données situées dans des plages de feuille de calcul. Les sources externes (bases de données, connexions externes, etc.) ne peuvent pas encore être actualisées via l’API du cache.
En raison de cette chaîne, il existe deux chemins d’actualisation fondamentaux dans Aspose.Cells :
- **`PivotTable.CalculateData()`** — recalcule l’affichage d’un `PivotTable` à partir de données déjà mises en cache, sans aller-retour vers la source de données.
Tous les scénarios de cet article utilisent des données sources composées de cellules de feuille de calcul. Le type de source est donc `Sheet` et les opérations d’actualisation se comportent comme décrit.
{{% /alert %}}

## Démarrage rapide
Si vous avez uniquement besoin du code le plus court possible pour actualiser tous les tableaux croisés dynamiques du classeur, un seul appel suffit :

```csharp
using Aspose.Cells;
Workbook workbook = new Workbook("input.xlsx");
workbook.RefreshAll();
workbook.Save("output.xlsx");
```

Le reste de cet article explique quand choisir une API plus restrictive.

## Directives `using` requises
Tous les exemples C# de cet article commencent par les trois directives `using` suivantes, car les types de pivot résident dans le namespace `Aspose.Cells.Pivot` :
- `using System;`
- `using Aspose.Cells;`
- `using Aspose.Cells.Pivot;`

## Actualiser tous les tableaux croisés dynamiques du classeur
Lorsque vous devez garantir que chaque cache de pivot et chaque tableau croisé dynamique du classeur reflète les dernières données source, l’API la plus simple et la plus complète est `Workbook.RefreshAll()`. Un seul appel parcourt l’ensemble du classeur — actualisant chaque `PivotCache` depuis sa source, puis recalculant chaque `PivotTable` dépendant. Il s’agit de l’approche recommandée pour les actualisations générales de l’ensemble du document lorsque les performances ne sont pas un facteur déterminant.
L’exemple suivant crée un classeur avec une plage source Fruit/Year/Amount, crée un tableau croisé dynamique, modifie certaines valeurs source, puis utilise `RefreshAll()` pour tout mettre à jour en un seul appel.

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
// Écrire les lignes de données dans les cellules A2:C9 (8 lignes de données de fruits sur 2020 et 2021)
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
// Affecter les champs du tableau croisé dynamique : Fruit aux lignes, Year aux colonnes, Amount aux données
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
// Modifier plusieurs valeurs de Amount dans les données source pour simuler des changements
worksheet.Cells["C2"].PutValue(55);
worksheet.Cells["C5"].PutValue(85);
worksheet.Cells["C9"].PutValue(125);
// Actualiser tous les tableaux croisés dynamiques / caches de tableau croisé dynamique du classeur
workbook.RefreshAll();
// Enregistrer le classeur
workbook.Save("output.xlsx");
```

## Actualiser tous les tableaux croisés dynamiques d’une seule feuille de calcul
Parfois, vous n’avez besoin d’actualiser que les tableaux croisés dynamiques présents sur une feuille de calcul précise — par exemple, lorsque ceux des autres feuilles de calcul ne sont pas concernés et ne doivent pas être modifiés. Dans ce cas, Aspose.Cells fournit `Worksheet.RefreshPivotTables()`, dont la portée se limite à une seule instance de `Worksheet`.

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
Pour exerter un contrôle précis sur un seul tableau croisé dynamique, l’API basée sur le cache vous propose deux options. Le choix dépend de ce qui a réellement changé : les données source sous-jacentes ou uniquement les paramètres d’affichage ou de disposition du tableau croisé dynamique lui-même.

### Les données source ont changé — Utilisez `PivotCache.Refresh()`
Si les données source sous-jacentes ont changé, le point d’entrée approprié est `pivotTable.PivotCache.Refresh()`. Cet appel relit les données source dans le cache, puis recalcule tous les `PivotTable` qui dépendent de ce cache.

### Seuls les paramètres d’affichage ou de disposition ont changé — Utilisez `CalculateData()`
Si les données source n’ont *pas* changé et que seuls les paramètres d’affichage ou de disposition du tableau croisé dynamique ont été modifiés (par exemple, si un champ a été déplacé vers une autre zone ou si un paramètre d’actualisation à l’ouverture a été activé ou désactivé), il n’est pas nécessaire de revenir à la source de données. Le cache contient déjà les données correctes ; seul le `PivotTable` rendu doit être recalculé. Dans ce cas, `pivotTable.CalculateData()` est le choix approprié.
L’exemple suivant modifie une propriété du tableau croisé dynamique qui n’est pas liée à la source, puis appelle `CalculateData()` pour effectuer à nouveau son rendu à partir du cache existant.

```csharp
using Aspose.Cells;
using Aspose.Cells.Pivot;
var workbook = new Workbook();
var worksheet = workbook.Worksheets[0];
// Écrire la ligne d’en-tête Fruit / Year / Amount
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
// Ajouter un tableau croisé dynamique nommé "Pivot1" placé dans la cellule de destination E3, avec A1:C9 comme source
int pivotIndex = worksheet.PivotTables.Add("A1:C9", "E3", "Pivot1");
var pivotTable = worksheet.PivotTables[pivotIndex];
// Affecter les champs : Fruit à Ligne, Year à Colonne, Amount à Données
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
// Modifier une propriété d’affichage/de disposition — il s’agit uniquement d’un changement de présentation,
// donc il ne nécessite PAS de relire les données source via PivotCache.Refresh().
pivotTable.RefreshDataOnOpeningFile = false;
// CalculateData() redessine l’affichage de CE tableau croisé dynamique (données + style) à partir des
// données déjà conservées dans le PivotCache. Comme les données source n’ont pas changé,
// aucun aller-retour vers la source n’est effectué — seules les valeurs mises en cache sont recalculées
// dans les cellules de la feuille de calcul.
pivotTable.CalculateData();
// Enregistrer le classeur sur le disque
workbook.Save("output.xlsx");
```

Un classeur contient souvent de nombreux tableaux croisés dynamiques qui reposent tous sur un cache partagé. Pour les énumérer — par exemple, avant d’effectuer une actualisation par lot ou de diagnostiquer l’impact d’un cache partagé — utilisez `PivotCache.GetPivotTables()`. Cette méthode retourne la collection de tous les `PivotTable` qui dépendent du cache donné.

## Migration depuis la méthode obsolète `PivotTable.RefreshData()`
Avant Aspose.Cells for .NET v26.7, la méthode standard pour actualiser un tableau croisé dynamique consistait à appeler `PivotTable.RefreshData()` sur chaque tableau croisé dynamique individuellement. Depuis la version v26.7, cette méthode est marquée comme **obsolète** et doit être remplacée par les API tenant compte du cache décrites ci-dessus.
Dans les classeurs réels, l’approche consistant à appeler `RefreshData()` pour chaque table présente deux problèmes :
- Elle récupère à nouveau les données depuis la source *à chaque appel*, même si la source n’a pas changé.
Les remplacements recommandés sont :
L’exemple suivant présente le nouveau modèle efficace pour les classeurs contenant plusieurs tableaux croisés dynamiques qui partagent un seul cache.

## Quelle API d’actualisation dois-je utiliser ?
Le tableau ci-dessous résume les API d’actualisation disponibles et le moment où choisir chacune d’elles.
| Objectif | API recommandée | Remarques |
|------|-----------------|-------|
| Actualiser l’ensemble du classeur | `Workbook.RefreshAll()` | Un seul appel ; couvre tous les caches et tableaux croisés dynamiques. |
| Actualiser uniquement les tableaux croisés dynamiques d’une seule feuille | `Worksheet.RefreshPivotTables()` | Portée limitée à une feuille de calcul. |
| Les données source d’un cache ont changé | `pivotTable.PivotCache.Refresh()` | Actualise TOUS les tableaux croisés dynamiques qui utilisent ce cache partagé. |
| Seuls les paramètres d’affichage ou de disposition ont changé | `pivotTable.CalculateData()` | Évite tout aller-retour inutile vers la source. |
| Répertorier tous les tableaux croisés dynamiques d’un cache partagé | `pivotCache.GetPivotTables()` | À utiliser pour les énumérer avant une actualisation groupée. |
En pratique, privilégiez les API basées sur le cache à la méthode obsolète `RefreshData()` par table. Elles tiennent compte des caches partagés, évitent les récupérations de données source redondantes et permettent de choisir la portée la plus restrictive qui satisfait vos besoins d’actualisation.

## Pièges courants
- **Oublier d’actualiser avant l’enregistrement.** Un tableau croisé dynamique n’écrit ses valeurs affichées dans la feuille de calcul que lorsque sa chaîne de données est actualisée. Si vous modifiez des cellules source, appelez `PivotCache.Refresh()` (ou `Workbook.RefreshAll()`) avant `Workbook.Save()`, sinon le fichier enregistré contiendra toujours les anciennes valeurs agrégées.
- **Appeler la méthode obsolète `RefreshData()` pour chaque table.** Depuis la version v26.7, `PivotTable.RefreshData()` est marquée obsolète et récupère à nouveau la source à chaque appel. Avec plusieurs tableaux croisés dynamiques partageant un cache, cela entraîne N récupérations redondantes de la source. Remplacez-la par un seul appel à `PivotCache.Refresh()`, suivi de `CalculateData()` pour chaque table.
- **Actualiser lorsque seule la disposition a changé.** Si vous avez uniquement modifié l’affichage d’un tableau croisé dynamique (ordre des colonnes, `ConsolidationFunction`, etc.) sans toucher aux données source, `PivotCache.Refresh()` est inutile et lent. Appelez `pivotTable.CalculateData()` pour effectuer le rendu à partir du cache existant.
- **Source externe non prise en charge par `PivotCache.Refresh()`.** Si la source du tableau croisé dynamique provient d’une connexion externe (base de données, cube OLAP, etc.), `PivotCache.Refresh()` ne peut pas l’actualiser dans la version v26.7 — elle prend actuellement en charge uniquement les types de source `Sheet` et `Consolidation`. Pour les sources externes, rouvrez le classeur ou reconstruisez le cache à partir de la source.

{{< app/cells/assistant language="csharp" >}}