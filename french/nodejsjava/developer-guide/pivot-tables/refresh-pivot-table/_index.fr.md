---
title: Actualisation des tableaux croisés dynamiques dans Aspose.Cells for Node.js via Java
linktitle: Actualisation des tableaux croisés dynamiques dans Aspose.Cells for Node.js via Java
description: Apprenez à actualiser les tableaux croisés dynamiques dans Aspose.Cells for Node.js via Java à l'aide de l'API d'actualisation des tableaux croisés dynamiques v26.7+. Cet article couvre RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData et GetPivotTables avec des exemples de code pratiques.
keywords: Aspose.Cells, Node.js, Java, tableau croisé dynamique, actualisation, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /fr/nodejs-java/refresh-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells fournit une API d'actualisation en couches qui vous permet de recharger les données des tableaux croisés dynamiques à quatre niveaux différents — du classeur entier jusqu'à un seul tableau croisé dynamique. À partir d'**Aspose.Cells for Aspose.Cells for Node.js via Java v26.7**, l'ancienne méthode `PivotTable.RefreshData()` est marquée comme obsolète et doit être remplacée par les API plus efficaces, tenant compte du cache, décrites dans cet article.

{{% /alert %}}

## Introduction

L'actualisation d'un tableau croisé dynamique est rarement une opération unique. En arrière-plan, Aspose.Cells maintient une chaîne de données en couches qui connecte vos données source d'origine aux valeurs rendues que vous voyez dans la feuille de calcul. Comprendre cette chaîne est la clé pour choisir la bonne API d'actualisation pour toute situation.

La chaîne de données à quatre couches est :

1. **Source de données** — les plages de la feuille de calcul d'origine, la requête de base de données ou la plage de consolidation où se trouvent les valeurs brutes.
2. **PivotCache** — l'instantané en mémoire des données source. Chaque tableau croisé dynamique est construit au-dessus d'un `PivotCache` ; c'est là que toutes les données sont collectées et agrégées.
3. **PivotTable** — l'objet de vue qui définit les champs de ligne, de colonne, de valeur et de filtre. Un `PivotTable` lit *uniquement* depuis son `PivotCache`, jamais directement depuis la source de données.
4. **Cells** — les `Cells` de la feuille de calcul dans lesquelles le `PivotTable` restitue ses valeurs calculées et ses styles.

Un concept particulièrement important est le **cache partagé**. Lorsque plusieurs tableaux croisés dynamiques dans un classeur référencent la même plage source, ils partagent *une seule* instance de `PivotCache`. Un seul `PivotCache` peut être référencé par de nombreux tableaux croisés dynamiques, et l'actualisation de ce cache actualise tous les `PivotTable` dépendants en une seule fois.

{{% alert color="primary" %}}

`PivotCache.SourceType` (énumération `PivotTableSourceType`) indique d'où proviennent les données du cache. Depuis la v26.7, `PivotCache.Refresh()` ne prend en charge que les types de source **`Sheet`** et **`Consolidation`** — c'est-à-dire les données qui se trouvent dans les plages de la feuille de calcul. Les sources externes (bases de données, connexions externes, etc.) ne sont pas encore actualisables via l'API du cache.

{{% /alert %}}

En raison de cette chaîne, il existe deux chemins d'actualisation fondamentaux dans Aspose.Cells :

- **`PivotCache.Refresh()`** — recharge les données source → cache ET recalcule tous les `PivotTable` dépendants en une seule opération.
- **`PivotTable.CalculateData()`** — recalcule l'affichage d'un seul `PivotTable` à partir des données déjà mises en cache, sans aller-retour vers la source de données.

Tous les scénarios de cet article utilisent des données source de cellules de feuille de calcul, donc le type de source est `Sheet` et les opérations d'actualisation se comportent comme décrit.

## Imports requis

Tous les exemples JavaScript de cet article nécessitent le module Aspose.Cells for Node.js via Java. Les types de tableaux croisés dynamiques se trouvent dans le namespace `Aspose.Cells.Pivot`, qui fait partie du même module :

- `const aspose = require('aspose.cells');`
- Ou pour des imports spécifiques : `const { Workbook, Cells, PivotTableSourceType } = require('aspose.cells');`

## Actualiser tous les tableaux croisés dynamiques du classeur

Lorsque vous devez vous assurer que chaque cache de tableau croisé dynamique et chaque tableau croisé dynamique du classeur reflètent les dernières données source, l'API la plus simple et la plus complète est `Workbook.RefreshAll()`. Un seul appel parcourt le classeur entier — actualisant chaque `PivotCache` depuis sa source puis recalculant chaque `PivotTable` dépendant. C'est l'approche recommandée pour les actualisations générales et complètes du document où la performance n'est pas un souci.

L'exemple suivant construit un classeur avec une plage source Fruit/Année/Montant, crée un tableau croisé dynamique, modifie certaines valeurs source, puis utilise `RefreshAll()` pour tout mettre à jour en un seul appel.

```javascript
const AsposeCells = require("aspose.cells");

// Créer un nouveau classeur
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);

// Écrire la ligne d'en-tête dans les cellules A1:C1
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// Écrire les lignes de données dans les cellules A2:C9 (8 lignes de données sur les fruits pour 2020 et 2021)
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
const pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
const pivotTable = worksheet.getPivotTables().get(pivotIndex);

// Affecter les champs du tableau croisé dynamique : Fruit aux Lignes, Year aux Colonnes, Amount aux Données
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// Modifier plusieurs valeurs de Amount dans les données sources pour simuler des changements
worksheet.getCells().get("C2").putValue(55);
worksheet.getCells().get("C5").putValue(85);
worksheet.getCells().get("C9").putValue(125);

// Actualiser tous les tableaux croisés dynamiques / caches de tableaux croisés dynamiques dans le classeur
workbook.refreshAll();

// Enregistrer le classeur
workbook.save("output.xlsx");
```

## Actualiser tous les tableaux croisés dynamiques sur une seule feuille de calcul

Parfois, vous n'avez besoin d'actualiser que les tableaux croisés dynamiques qui se trouvent sur une feuille de calcul spécifique — par exemple, lorsque les tableaux croisés dynamiques sur d'autres feuilles de calcul sont connus comme non liés et ne doivent pas être touchés. Pour ce cas, Aspose.Cells fournit `Worksheet.RefreshPivotTables()`, qui est limité à une seule instance de `Worksheet`.

C'est plus sélectif que `Workbook.RefreshAll()` : seuls les tableaux croisés dynamiques de la feuille de calcul ciblée sont actualisés, laissant intacts les tableaux croisés dynamiques sur les autres feuilles de calcul.

L'exemple suivant remplit les mêmes données source Fruit/Année/Montant, ajoute un tableau croisé dynamique sur la première feuille de calcul, modifie certaines valeurs source, puis actualise uniquement les tableaux croisés dynamiques de cette feuille de calcul.

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

## Actualiser un seul tableau croisé dynamique

Lorsque vous souhaitez un contrôle précis sur un seul tableau croisé dynamique, l'API basée sur le cache vous offre deux options. Le choix entre elles dépend de ce qui a réellement changé : les données source sous-jacentes, ou simplement les paramètres de vue/disposition du tableau croisé dynamique lui-même.

### Les données source ont changé — Utilisez `PivotCache.Refresh()`

Si les données source sous-jacentes ont changé, le bon point d'entrée est `pivotTable.PivotCache.Refresh()`. Cet appel relit les données source dans le cache puis recalcule chaque `PivotTable` qui dépend de ce cache.

{{% alert color="primary" %}}

Parce que les tableaux croisés dynamiques partagent une seule instance de `PivotCache`, l'appel de `PivotCache.Refresh()` recalcule **tous** les tableaux croisés dynamiques construits sur ce même cache — pas seulement celui que vous référencez. Si deux tableaux croisés dynamiques partagent la même plage source, l'actualisation d'un cache actualise les deux.

{{% /alert %}}

L'exemple suivant crée deux tableaux croisés dynamiques sur la même plage source pour démontrer ce comportement de cache partagé, modifie certaines valeurs source, puis actualise via une référence de cache.

```javascript
const AsposeCells = require("aspose.cells");

// Créer un nouveau classeur et accéder à la première feuille de calcul
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);

// Écrire la ligne d'en-tête : Fruit / Année / Montant
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// Écrire environ 9 lignes de données (raisin / myrtille / kiwi / cerise pour 2020-2021)
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
worksheet.getCells().get("C6").putValue(500);

worksheet.getCells().get("A7").putValue("Blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(600);

worksheet.getCells().get("A8").putValue("Kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(700);

worksheet.getCells().get("A9").putValue("Cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(800);

// Ajouter le premier tableau croisé dynamique "Pivot1" ancré à la cellule E3, plage source A1:C9
const pivotIndex1 = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
const pivotTable1 = worksheet.getPivotTables().get(pivotIndex1);

// Assigner les champs pour Pivot1
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// Ajouter un SECOND tableau croisé dynamique "Pivot2" ancré à E15 en utilisant la MÊME plage source A1:C9
// Pivot1 et Pivot2 partagent un seul PivotCache car la plage source est identique.
const pivotIndex2 = worksheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
const pivotTable2 = worksheet.getPivotTables().get(pivotIndex2);

// Assigner les mêmes champs pour Pivot2
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// Modifier plusieurs valeurs de cellules de Montant dans les données source pour simuler un changement de données
worksheet.getCells().get("C2").putValue(150);
worksheet.getCells().get("C4").putValue(350);
worksheet.getCells().get("C7").putValue(650);

// Actualiser le PivotCache partagé.
// Comme Pivot1 et Pivot2 partagent le même PivotCache, cet appel unique
// actualise les DEUX tableaux croisés dynamiques (données + style) à partir de la source mise à jour.
pivotTable1.getPivotCache().refresh();

// Enregistrer le classeur
workbook.save("output.xlsx");
```

### Seule la vue/disposition a changé — Utilisez `CalculateData()`

Si les données source n'ont *pas* changé mais que seuls les paramètres de vue ou de disposition du tableau croisé dynamique ont été modifiés (par exemple, un champ a été déplacé vers une zone différente, ou un paramètre d'actualisation à l'ouverture a été basculé), il n'est pas nécessaire de faire un aller-retour vers la source de données. Le cache contient déjà les bonnes données ; seul le `PivotTable` rendu a besoin d'être recalculé. Dans ce cas, `pivotTable.CalculateData()` est le bon choix.

Cela évite la récupération inutile depuis la source et est nettement plus rapide lorsque plusieurs tableaux croisés dynamiques partagent le même cache.

L'exemple suivant modifie une propriété non liée à la source du tableau croisé dynamique, puis appelle `CalculateData()` pour le restituer depuis le cache existant.

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

// Ajouter un tableau croisé dynamique nommé "Pivot1" placé à la cellule de destination E3, à partir de A1:C9
var pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
var pivotTable = worksheet.getPivotTables().get(pivotIndex);

// Assigner les champs : Fruit à Ligne, Année à Colonne, Montant à Données
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// Modifier une propriété de vue/mise en page — ceci est une modification uniquement de présentation,
// donc elle ne nécessite PAS de relire les données source via PivotCache.Refresh().
pivotTable.setRefreshDataOnOpeningFile(false);

// CalculateData() réaffiche le rendu visuel (données + style) de CE tableau croisé dynamique à partir des
// données déjà détenues dans le PivotCache. Parce que les données source n'ont pas changé,
// aucun aller-retour vers la source n'est effectué — seules les valeurs mises en cache sont recalculées
// dans les cellules de la feuille de calcul.
pivotTable.calculateData();

// Enregistrer le classeur sur le disque
workbook.save("output.xlsx");
```

## Obtenir tous les tableaux croisés dynamiques partageant le même PivotCache

Un classeur contient souvent de nombreux tableaux croisés dynamiques qui reposent tous sur un cache partagé. Pour les énumérer — par exemple, avant d'effectuer une actualisation par lot, ou pour diagnostiquer l'impact du cache partagé — utilisez `PivotCache.GetPivotTables()`. Cette méthode renvoie la collection de tous les `PivotTable` qui dépendent du cache donné.

C'est aussi le moyen le plus direct pour confirmer que deux tableaux croisés dynamiques partagent bien la même instance de `PivotCache` : vous pouvez comparer les références du cache, ou simplement itérer la collection renvoyée par `GetPivotTables()` et observer quels tableaux croisés dynamiques y apparaissent.

L'exemple suivant crée deux tableaux croisés dynamiques sur la même plage source, vérifie qu'ils partagent la même instance de cache, puis énumère les tableaux croisés dynamiques du cache.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Sheet1");

worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

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
worksheet.getCells().get("C6").putValue(500);

worksheet.getCells().get("A7").putValue("Blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(600);

worksheet.getCells().get("A8").putValue("Kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(700);

worksheet.getCells().get("A9").putValue("Cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(800);

worksheet.getCells().get("A10").putValue("Grape");
worksheet.getCells().get("B10").putValue(2021);
worksheet.getCells().get("C10").putValue(900);

let pivot1Index = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
let pivotTable1 = worksheet.getPivotTables().get(pivot1Index);
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

let pivot2Index = worksheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
let pivotTable2 = worksheet.getPivotTables().get(pivot2Index);
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

let sameCache = pivotTable1.getPivotCache() === pivotTable2.getPivotCache();
console.log("Pivot1 and Pivot2 share the same PivotCache: " + sameCache);

let sharedPivotTables = pivotTable1.getPivotCache().getPivotTables();
console.log("Number of pivot tables sharing the cache: " + sharedPivotTables.length);

for (let pt of sharedPivotTables) {
    console.log("Pivot table name: " + pt.getName());
}

workbook.save("output.xlsx");
```

## Migration depuis l'obsolète `PivotTable.RefreshData()`

Avant Aspose.Cells for Aspose.Cells for Node.js via Java v26.7, la façon standard d'actualiser un tableau croisé dynamique était d'appeler `PivotTable.RefreshData()` sur chaque tableau croisé dynamique individuellement. Depuis la v26.7, cette méthode est marquée comme **obsolète** et doit être remplacée par les API tenant compte du cache décrites ci-dessus.

Il y a deux raisons pour lesquelles l'approche `RefreshData()` par tableau est problématique dans les classeurs du monde réel :

- Elle récupère les données depuis la source *à chaque* appel, même lorsque la source n'a pas changé.
- Chaque appel actualise le cache partagé entier. Lorsque plusieurs tableaux croisés dynamiques partagent un cache, appeler à plusieurs reprises `RefreshData()` par tableau croisé dynamique provoque la récupération répétée du même cache, ce qui est très lent.

Les remplacements recommandés sont :

- **Actualiser TOUS les tableaux croisés dynamiques du classeur** → utilisez `workbook.refreshAll();`
- **Actualiser CERTAINS d'entre eux** → utilisez `pivotTable.getPivotCache().refresh();` pour un cache. Parce que le cache est partagé, cet unique appel met à jour chaque tableau croisé dynamique construit sur ce cache. Les autres tableaux croisés dynamiques qui reposent sur un cache déjà actualisé peuvent être ignorés en toute sécurité.
- **Seule la vue/disposition du tableau croisé a changé** → utilisez `pivotTable.calculateData();` pour restituer depuis le cache existant sans aller-retour vers la source.

L'exemple suivant démontre le nouveau modèle efficace pour les classeurs avec plusieurs tableaux croisés dynamiques partageant un seul cache.

```javascript
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);

// --- Construire les données source : Fruit / Année / Montant (en-tête + 9 lignes) ---
sheet.getCells().get("A1").putValue("Fruit");
sheet.getCells().get("B1").putValue("Year");
sheet.getCells().get("C1").putValue("Amount");

sheet.getCells().get("A2").putValue("Grape");      sheet.getCells().get("B2").putValue(2020); sheet.getCells().get("C2").putValue(1000);
sheet.getCells().get("A3").putValue("Blueberry");  sheet.getCells().get("B3").putValue(2020); sheet.getCells().get("C3").putValue(2000);
sheet.getCells().get("A4").putValue("Kiwi");       sheet.getCells().get("B4").putValue(2020); sheet.getCells().get("C4").putValue(1500);
sheet.getCells().get("A5").putValue("Cherry");     sheet.getCells().get("B5").putValue(2020); sheet.getCells().get("C5").putValue(2500);
sheet.getCells().get("A6").putValue("Grape");      sheet.getCells().get("B6").putValue(2021); sheet.getCells().get("C6").putValue(3000);
sheet.getCells().get("A7").putValue("Blueberry");  sheet.getCells().get("B7").putValue(2021); sheet.getCells().get("C7").putValue(1800);
sheet.getCells().get("A8").putValue("Kiwi");       sheet.getCells().get("B8").putValue(2021); sheet.getCells().get("C8").putValue(2200);
sheet.getCells().get("A9").putValue("Cherry");     sheet.getCells().get("B9").putValue(2021); sheet.getCells().get("C9").putValue(2700);

// --- Ajouter le premier tableau croisé dynamique (Pivot1) à la cellule de destination E3 ---
let idx1 = sheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
let pivotTable1 = sheet.getPivotTables().get(idx1);
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// --- Ajouter le DEUXIÈME tableau croisé dynamique (Pivot2) sur la MÊME plage source ---
// Pivot1 et Pivot2 partagent UN PivotCache sous-jacent.
// C'est exactement le scénario où l'approche héritée RefreshData() par table
// devient inefficace : rafraîchir une table re-récupère l'ensemble du
// cache partagé, donc rafraîchir N tables effectue la même récupération coûteuse N fois.
let idx2 = sheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
let pivotTable2 = sheet.getPivotTables().get(idx2);
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// --- Modifier plusieurs valeurs de Montant dans les données source ---
sheet.getCells().get("C2").putValue(5000);   // Raisin  2020
sheet.getCells().get("C5").putValue(7500);   // Cerise 2020
sheet.getCells().get("C9").putValue(9500);   // Cerise 2021

// --- Modèle OBSOLÈTE (avant 26.7) — PivotTable.RefreshData() ---
// pivotTable1.refreshData();  // re-récupère depuis la source, rafraîchit tout le cache
// pivotTable2.refreshData();  // re-récupère ENCORE — le cache est déjà frais !
// Chaque appel reconstruit le cache partagé, donc N tables = N récupérations redondantes.

// --- NOUVEAU modèle v26.7+ : rafraîchir le cache UNE FOIS, puis re-afficher au besoin ---
// Un appel à PivotCache.Refresh() récupère les valeurs modifiées dans le
// cache partagé ET recalcule l'affichage de CHAQUE tableau croisé dynamique qui le référence.
// Parce que Pivot1 et Pivot2 partagent un seul PivotCache, ce simple appel met à jour
// les deux tables — aucune seconde récupération depuis la source n'est nécessaire.
pivotTable1.getPivotCache().refresh();

// CalculateData() ne fait que re-afficher la vue d'un tableau croisé dynamique (données + style)
// à partir des données déjà présentes dans le cache — il ne touche PAS à la source.
// Nous l'appelons sur Pivot2 ici uniquement pour démontrer l'API : après que le cache
// a été rafraîchi une fois, toute table dépendante peut être re-affichée sans
// revenir à la source. Utilisez CalculateData() seul quand seuls les
// paramètres de vue/mise en page du tableau croisé dynamique ont changé et que le cache est à jour.
pivotTable2.calculateData();

workbook.save("output.xlsx");
```

## Quelle API d'actualisation dois-je utiliser ?

Le tableau ci-dessous résume les API d'actualisation disponibles et quand choisir chacune d'elles.

| Objectif | API recommandée | Notes |
|------|-----------------|-------|
| Actualiser tout dans le classeur | `Workbook.RefreshAll()` | Un seul appel ; couvre tous les caches et tableaux. |
| Actualiser uniquement les tableaux croisés dynamiques d'une seule feuille | `Worksheet.RefreshPivotTables()` | Limité à une seule feuille de calcul. |
| Les données source ont changé pour un cache | `pivotTable.PivotCache.Refresh()` | Actualise TOUS les tableaux croisés dynamiques sur ce cache partagé. |
| Seuls les paramètres de vue/disposition ont changé | `pivotTable.CalculateData()` | Évite l'aller-retour inutile vers la source. |
| Lister tous les tableaux croisés dynamiques sur un cache partagé | `pivotCache.GetPivotTables()` | À utiliser pour énumérer avant une actualisation en bloc. |

En pratique, privilégiez les API basées sur le cache par rapport à l'obsolète `RefreshData()` par tableau. Elles sont conscientes des caches partagés, elles évitent les récupérations redondantes depuis la source, et elles vous permettent de choisir la plus petite portée qui satisfait votre besoin d'actualisation.

{{< app/cells/assistant language="javascript" >}}