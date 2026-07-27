---
title: Ajouter des champs de filtre à un tableau croisé dynamique dans Aspose.Cells pour .NET
linktitle: Ajouter des champs de filtre
description: Apprenez à ajouter et configurer des champs de filtre dans les tableaux croisés dynamiques à l'aide d'Aspose.Cells for Node.js via C++, y compris l'ajout de champs de filtre, le filtrage à sélection unique et le filtrage à sélection multiple.
keywords: Aspose.Cells, Node.js via C++, tableau croisé dynamique, champ de filtre, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, filtre
type: docs
weight: 250
url: /fr/nodejs-cpp/add-filter-field-in-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells prend en charge le cycle de vie complet des champs de filtre dans les tableaux croisés dynamiques. Vous pouvez ajouter un champ de filtre via une API de commodité de haut niveau ou via la collection `PageFields` de bas niveau, et vous pouvez piloter le filtre en mode sélection unique, l'effacer pour afficher chaque élément de page, ou basculer le champ en sélection multiple afin que les utilisateurs puissent choisir plusieurs éléments de page à la fois via l'interface utilisateur à cases à cocher dans Excel.
{{% /alert %}}

## **Introduction**

Un champ de filtre est un champ pivot qui contrôle *quel sous-ensemble* des données source le corps du tableau croisé dynamique affiche. Les utilisateurs finaux le voient comme une liste déroulante en haut d'un tableau croisé dynamique rendu dans Excel, et la sélection de l'un des éléments de page disponibles reconstruit le corps du tableau croisé dynamique de sorte que seuls les enregistrements appartenant à cet élément de page soient résumés. Un champ pivot devient un champ de filtre lorsqu'il est enregistré en tant que `PivotFieldType.Page` plutôt que `PivotFieldType.Row`, `PivotFieldType.Column` ou `PivotFieldType.Data`.

Un champ de filtre peut fonctionner selon deux comportements. Dans le comportement par défaut de **sélection unique**, seul un élément de page est visible à la fois, de sorte que le corps du tableau croisé dynamique résume exactement un sous-ensemble. Dans le comportement de **sélection multiple**, le champ expose une liste de cases à cocher, et le corps du tableau croisé dynamique résume l'union de chaque élément de page coché. Le même champ source peut basculer entre ces comportements en activant/désactivant une seule propriété.

Aspose.Cells for Node.js via C++ expose deux façons équivalentes d'enregistrer un champ de filtre. L'API de haut niveau est `PivotTable.addFieldToArea(PivotFieldType.Page, "fieldName")`, qui prend le nom de la colonne source et ajoute le champ en un seul appel. L'API de bas niveau est `PivotTable.pageFields.add(PivotField)`, qui est utilisée lorsque vous détenez déjà une référence `PivotField` et souhaitez ajouter la même instance de champ à la zone de filtre. Les deux API finissent par remplir la même collection `PageFields`, et le reste de cet article démontre comment choisir entre elles et comment piloter chaque mode de filtrage.

## **Ajout d'un champ de filtre**

Il existe deux façons d'enregistrer un champ pivot dans la zone de filtre. L'appel de haut niveau prend le nom de la colonne source sous forme de chaîne et constitue le chemin le plus courant. L'appel de bas niveau accepte une instance `PivotField` existante et est pratique lorsque le même objet champ doit être réutilisé dans plusieurs zones pivot. Les deux appels placent le champ dans `PivotTable.pageFields`, après quoi il apparaît comme la liste déroulante de page en haut du tableau croisé dynamique rendu.

### Ajout d'un champ de filtre avec addFieldToArea

L'exemple suivant construit un petit jeu de données Fruit / Année / Montant, place un tableau croisé dynamique à la cellule E3 avec `Fruit` dans la zone de ligne, `Amount` dans la zone de données et `Year` dans la zone de filtre, actualise le tableau croisé dynamique et enregistre le classeur.

```javascript
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

// Configurer la ligne d'en-tête
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// Remplir 9 lignes de données d'exemple : Fruit, Année, Montant
var data = [
    [ "apple", 2020, 100 ],
    [ "banana", 2021, 200 ],
    [ "apple", 2021, 150 ],
    [ "grape", 2020, 120 ],
    [ "orange", 2022, 180 ],
    [ "banana", 2020, 90 ],
    [ "grape", 2021, 130 ],
    [ "apple", 2022, 170 ],
    [ "orange", 2021, 110 ]
];

for (var i = 0; i < data.length; i++)
{
    worksheet.getCells().get(i + 1, 0).putValue(data[i][0]);
    worksheet.getCells().get(i + 1, 1).putValue(data[i][1]);
    worksheet.getCells().get(i + 1, 2).putValue(data[i][2]);
}

// Ajouter un tableau croisé dynamique ancré à la cellule E3
var pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "PivotTable1");
var pivotTable = worksheet.getPivotTables().get(pivotIndex);

// Ajouter des champs à leurs zones : Fruit comme Ligne, Montant comme Données, Année comme champ Page
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");

// Actualiser et calculer les données du tableau croisé dynamique
pivotTable.refreshData();
pivotTable.calculateData();

// Enregistrer le classeur
workbook.save("pageFieldSample.xlsx");
```

### Ajout d'un champ de filtre avec pageFields.add

Lorsque vous travaillez déjà avec une instance `PivotField`, vous pouvez la transmettre directement à `PivotTable.pageFields.add`. Le tableau croisé dynamique et le champ de filtre sont construits exactement comme dans le scénario précédent ; seul l'enregistrement final de la zone de filtre est remplacé par l'appel d'API de bas niveau.

```javascript
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);

// En-têtes
sheet.getCells().get("A1").putValue("Fruit");
sheet.getCells().get("B1").putValue("Year");
sheet.getCells().get("C1").putValue("Amount");

// Données d'exemple (9 lignes)
sheet.getCells().get("A2").putValue("apple");     sheet.getCells().get("B2").putValue("2020"); sheet.getCells().get("C2").putValue(100);
sheet.getCells().get("A3").putValue("apple");     sheet.getCells().get("B3").putValue("2021"); sheet.getCells().get("C3").putValue(150);
sheet.getCells().get("A4").putValue("apple");     sheet.getCells().get("B4").putValue("2022"); sheet.getCells().get("C4").putValue(200);
sheet.getCells().get("A5").putValue("grape");     sheet.getCells().get("B5").putValue("2020"); sheet.getCells().get("C5").putValue(300);
sheet.getCells().get("A6").putValue("grape");     sheet.getCells().get("B6").putValue("2021"); sheet.getCells().get("C6").putValue(400);
sheet.getCells().get("A7").putValue("grape");     sheet.getCells().get("B7").putValue("2022"); sheet.getCells().get("C7").putValue(500);
sheet.getCells().get("A8").putValue("blueberry"); sheet.getCells().get("B8").putValue("2020"); sheet.getCells().get("C8").putValue(250);
sheet.getCells().get("A9").putValue("blueberry"); sheet.getCells().get("B9").putValue("2021"); sheet.getCells().get("C9").putValue(350);
sheet.getCells().get("A10").putValue("blueberry");sheet.getCells().get("B10").putValue("2022"); sheet.getCells().get("C10").putValue(450);

// Ajouter un tableau croisé dynamique à E3 couvrant A1:C10
let pivotIndex = sheet.getPivotTables().add("E3", "A1:C10", "PivotTable1");
let pivotTable = sheet.getPivotTables().get(pivotIndex);

// Fruit -> Ligne, Montant -> Données (Année ira à Page ci-dessous)
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// Approche bas niveau : récupérer le PivotField Année existant depuis BaseFields
// et l'enregistrer dans la zone Page via PageFields.Add(PivotField).
let yearField = pivotTable.getBaseFields().get("Year");
pivotTable.getPageFields().add(yearField);

// Actualiser pour que le nouveau champ de page soit reflété dans le classeur enregistré
pivotTable.refreshData();
pivotTable.calculateData();

workbook.save("output.xlsx");
```

## **Filtrage à sélection unique (affichage d'un élément de page)**

Dans le comportement par défaut de sélection unique, le champ de filtre est rendu sous forme de liste déroulante unique et l'entier `PivotField.currentPageItem` sélectionne quel élément de page pilote le corps du tableau croisé dynamique. L'attribution d'un index spécifique sélectionne cet élément ; l'attribution de la sentinelle spéciale `0x7FFD` (décimale 32765) efface le filtre afin que chaque élément de page soit résumé simultanément. La sélection unique est la valeur par défaut ; vous n'avez pas besoin de l'activer explicitement.

### Affichage de tous les éléments

Définir `currentPageItem` sur la valeur magique `0x7FFD` équivaut à effacer le filtre : le corps du tableau croisé dynamique résume chaque élément de page comme si aucun filtre n'était appliqué.

```javascript
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);

// Remplir les données Fruit/Année/Montant
sheet.getCells().get("A1").putValue("Fruit");
sheet.getCells().get("B1").putValue("Year");
sheet.getCells().get("C1").putValue("Amount");

let data = [
    ["Apple", 2022, 100],
    ["Apple", 2023, 150],
    ["Banana", 2022, 80],
    ["Banana", 2023, 120],
    ["Cherry", 2022, 200],
    ["Cherry", 2023, 250]
];

for (let r = 0; r < data.length; r++) {
    for (let c = 0; c < data[r].length; c++) {
        sheet.getCells().get(r + 1, c).putValue(data[r][c]);
    }
}

// Créer un tableau croisé dynamique à E3
let pivotTables = sheet.getPivotTables();
let index = pivotTables.add("=A1:C7", "E3", "PivotTable1");
let pivotTable = pivotTables.get(index);

// Configurer les champs du tableau croisé : Fruit→Ligne, Amount→Données, Year→Page
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");

pivotTable.refreshData();
pivotTable.calculateData();

// Effacer le filtre de page afin que chaque élément du champ de page soit visible.
// 0x7FFD (32765 en décimal) est la valeur sentinelle spéciale qui signifie « tous les éléments » —
// équivalent à sélectionner « (Tous) » dans la liste déroulante du champ de page d'Excel.
pivotTable.getPageFields().get(0).setCurrentPageItem(0x7FFD);

workbook.save("output.xlsx");
```

### Affichage d'un élément spécifique

Définir `currentPageItem` sur un index réel ne sélectionne qu'un seul élément de page. L'index est la position de l'élément dans la liste triée des éléments du champ de filtre, donc par exemple `1` sélectionne le deuxième élément après le tri.

```javascript
var workbook = new AsposeCells.Workbook();
var sheet = workbook.getWorksheets().get(0);
var cells = sheet.getCells();

// Ajouter des données d'exemple (Fruit/Année/Montant)
cells.get("A1").putValue("Fruit");
cells.get("B1").putValue("Year");
cells.get("C1").putValue("Amount");

cells.get("A2").putValue("Apple");
cells.get("B2").putValue("2020");
cells.get("C2").putValue("100");

cells.get("A3").putValue("Apple");
cells.get("B3").putValue("2021");
cells.get("C3").putValue("150");

cells.get("A4").putValue("Banana");
cells.get("B4").putValue("2020");
cells.get("C4").putValue("200");

cells.get("A5").putValue("Banana");
cells.get("B5").putValue("2021");
cells.get("C5").putValue("250");

// Ajouter un tableau croisé dynamique à E3
var pivotTables = sheet.getPivotTables();
var pivotIndex = pivotTables.add("A1:C5", "E3", "PivotTable1");
var pivotTable = pivotTables.get(pivotIndex);

// Ajouter des champs : Fruit→Ligne, Amount→Données, Year→Page
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");

// Opérations spécifiques au champ de page
pivotTable.getPageFields().get(0).setCurrentPageItem(1); // 1 = deuxième élément dans l'ordre trié (par ex. "2021")

// Actualiser et calculer le tableau croisé dynamique
pivotTable.refreshData();
pivotTable.calculateData();

workbook.save("output.xlsx");
```

## **Filtrage à sélection multiple**

Le filtrage à sélection multiple transforme la liste déroulante de page en une liste de cases à cocher et permet à l'utilisateur final de sélectionner simultanément plusieurs éléments de page. Aspose.Cells expose deux propriétés qui fonctionnent ensemble. `PivotField.isMultipleItemSelectionAllowed` doit être défini sur `true` avant que l'interface utilisateur de sélection multiple ne prenne effet. Une fois activé, `PivotItem.isHidden` contrôle quels éléments apparaissent dans la liste de cases à cocher, de sorte que vous pouvez afficher chaque élément ou n'autoriser que des éléments spécifiques.

Le code ci-dessous active la sélection multiple sur le même champ de filtre Year construit dans le scénario 1a, puis montre deux modèles : la partie A révèle chaque élément de page en laissant `isHidden` défini sur `false` pour chaque entrée, tandis que la partie B n'autorise que les valeurs source que vous choisissez et masque tout le reste via un bloc `switch (pivotItems[i].getStringValue())`.

```javascript
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);
let cells = sheet.getCells();

// Données d'exemple : Fruit | Année | Montant
cells.get(0, 0).putValue("Fruit");
cells.get(0, 1).putValue("Year");
cells.get(0, 2).putValue("Amount");

let data = [
    ["apple", "2019", "100"],
    ["apple", "2020", "150"],
    ["apple", "2021", "200"],
    ["banana", "2019", "110"],
    ["banana", "2020", "160"],
    ["banana", "2021", "210"],
    ["grape", "2019", "120"],
    ["grape", "2020", "170"],
    ["grape", "2021", "220"]
];

for (let i = 0; i < data.length; i++) {
    cells.get(i + 1, 0).putValue(data[i][0]);
    cells.get(i + 1, 1).putValue(parseInt(data[i][1]));
    cells.get(i + 1, 2).putValue(parseInt(data[i][2]));
}

let pivotSheet = workbook.getWorksheets().add("Pivot");
let pivots = pivotSheet.getPivotTables();
let pivotIndex = pivots.add("E3", "A1:C10", "PivotTable1");
let pivotTable = pivots.get(pivotIndex);

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");

// — Activer la sélection multiple sur le champ de page
pivotTable.getPageFields().get(0).setIsMultipleItemSelectionAllowed(true);

// Partie A — sélectionner TOUS les éléments (rendre chaque élément visible)
let pivotItems = pivotTable.getPageFields().get(0).getPivotItems();
for (let i = 0; i < pivotItems.getCount(); i++) {
    pivotItems.get(i).setIsHidden(false);
}

// Partie B — sélectionner uniquement des éléments spécifiques par valeur source
for (let i = 0; i < pivotItems.getCount(); i++) {
    switch (pivotItems.get(i).getStringValue()) {
        case "2020":
        case "grape":
        case "blueberry":
            pivotItems.get(i).setIsHidden(false);
            break;
        default:
            pivotItems.get(i).setIsHidden(true);
            break;
    }
}

pivotTable.refreshData();
pivotTable.calculateData();

workbook.save("output.xlsx");
```

> **Remarque :** Lors de l'utilisation du filtrage à sélection multiple via `PivotItem.isHidden`, **au moins un `PivotItem` doit rester visible** (`isHidden == false`). Si chaque élément est masqué, Excel se plante à l'ouverture du fichier ou affiche un tableau croisé dynamique vide. Vérifiez toujours que votre liste d'autorisation de sélection multiple inclut au moins un élément de vos données source.

## **Quelle API et quel mode dois-je utiliser ?**

Le tableau ci-dessous résume quand utiliser chaque API et chaque mode afin que vous puissiez choisir la bonne combinaison sans lire chaque scénario en détail.

| Scénario / Cas d'utilisation | API recommandée | Propriété utilisée | Notes |
|---|---|---|---|
| Ajouter un champ de filtre par nom de colonne source (le plus courant) | `PivotTable.addFieldToArea(PivotFieldType.Page, "fieldName")` | n/a | Haut niveau, une seule ligne. Utilisez ceci sauf si vous avez besoin d'une référence `PivotField`. |
| Ajouter un champ de filtre lorsque vous avez déjà un objet `PivotField` | `PivotTable.pageFields.add(PivotField)` | n/a | À utiliser lorsque l'objet champ a été obtenu ailleurs ou doit être réutilisé. |
| Filtrer à un seul élément de page (mode par défaut) | `PivotField.currentPageItem` | défini sur un index spécifique | Par exemple, `1` affiche le deuxième élément de la liste triée. |
| Afficher tous les éléments / effacer le filtre | `PivotField.currentPageItem` | défini sur `0x7FFD` | La valeur magique `0x7FFD` (décimale 32765) est la sentinelle pour « tous les éléments ». |
| Activer l'interface utilisateur de sélection multiple dans Excel | `PivotField.isMultipleItemSelectionAllowed` | défini sur `true` | Requis avant que les appels `isHidden` ne prennent effet. |
| Masquer / afficher des éléments individuels dans une liste à sélection multiple | `PivotItem.isHidden` | défini par élément | Au moins un élément doit rester visible (`isHidden == false`). |

{{% alert color="primary" %}}
N'oubliez jamais la contrainte de visibilité lors de la configuration du filtrage à sélection multiple. Si chaque `PivotItem` dans un champ de filtre à sélection multiple est masqué, Excel se plante à l'ouverture ou affiche un tableau croisé dynamique vide. Construisez votre liste d'autorisation par rapport à vos données source afin qu'au moins un élément reste visible, et vos classeurs enregistrés s'ouvriront de manière fiable sur chaque machine.
{{% /alert %}}



{{< app/cells/assistant language="javascript" >}}