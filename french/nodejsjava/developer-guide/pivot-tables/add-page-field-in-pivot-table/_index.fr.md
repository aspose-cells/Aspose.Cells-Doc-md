---
title: Champs de page dans les tableaux croisés dynamiques
linktitle: Champs de page dans les tableaux croisés dynamiques
description: Apprenez à ajouter et configurer des champs de page dans des tableaux croisés dynamiques à l'aide d'Aspose.Cells for Node.js via Java, y compris l'ajout de champs de page, le filtrage à sélection unique et le filtrage à sélection multiple.
keywords: Aspose.Cells, Node.js via Java, tableau croisé dynamique, champ de page, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, filtre
type: docs
weight: 250
url: /fr/nodejs-java/add-page-field-in-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells prend en charge le cycle de vie complet des champs de page dans les tableaux croisés dynamiques. Vous pouvez ajouter un champ de page via une API pratique de haut niveau ou via la collection de bas niveau `PageFields`, et vous pouvez piloter le filtre de page en mode sélection unique, le réinitialiser pour afficher chaque élément de page, ou basculer le champ vers la sélection multiple afin que les utilisateurs puissent choisir plusieurs éléments de page à la fois via l'interface à cases à cocher dans Excel.
{{% /alert %}}

## **Introduction**

Un champ de page est un champ de tableau croisé dynamique qui contrôle *quel sous-ensemble* des données source est affiché dans le corps du tableau croisé dynamique. Les utilisateurs finaux le voient sous la forme d'une liste déroulante en haut d'un tableau croisé dynamique rendu dans Excel, et la sélection d'un des éléments de page disponibles reconstruit le corps du tableau croisé dynamique de sorte que seuls les enregistrements appartenant à cet élément de page soient synthétisés. Un champ de tableau croisé dynamique devient un champ de page lorsqu'il est enregistré en tant que `PivotFieldType.Page` plutôt que `PivotFieldType.Row`, `PivotFieldType.Column` ou `PivotFieldType.Data`.

Un champ de page peut fonctionner selon deux comportements. Dans le comportement par défaut en **sélection unique**, un seul élément de page est visible à la fois, de sorte que le corps du tableau croisé dynamique synthétise exactement un sous-ensemble. Dans le comportement en **sélection multiple**, le champ expose une liste de cases à cocher, et le corps du tableau croisé dynamique synthétise l'union de chaque élément de page coché. Le même champ source peut être déplacé d'avant en arrière entre ces comportements en activant ou désactivant une seule propriété.

Aspose.Cells for Node.js via Java expose deux méthodes équivalentes pour enregistrer un champ de page. L'API de haut niveau est `pivotTable.addFieldToArea(PivotFieldType.Page, "fieldName")`, qui prend le nom de la colonne source et ajoute le champ en un seul appel. L'API de bas niveau est `pivotTable.getPageFields().add(PivotField)`, qui est utilisée lorsque vous détenez déjà une référence `PivotField` et souhaitez ajouter la même instance de champ à la zone de page. Les deux API finissent par alimenter la même collection `PageFields`, et la suite de cet article montre comment choisir entre elles et comment piloter chaque mode de filtrage.

## **Ajout d'un champ de page**

Il existe deux manières d'enregistrer un champ de tableau croisé dynamique dans la zone de page. L'appel de haut niveau prend le nom de la colonne source sous forme de chaîne de caractères et constitue le chemin le plus courant. L'appel de bas niveau accepte une instance `PivotField` existante et s'avère pratique lorsque le même objet de champ doit être réutilisé dans plusieurs zones du tableau croisé dynamique. Les deux appels placent le champ dans `pivotTable.getPageFields()`, après quoi il apparaît comme la liste déroulante de page en haut du tableau croisé dynamique rendu.

### Ajout d'un champ de page avec addFieldToArea

L'exemple suivant construit un petit jeu de données Fruit / Year / Amount, place un tableau croisé dynamique à la cellule E3 avec `Fruit` dans la zone des lignes, `Amount` dans la zone des données et `Year` dans la zone de page, actualise le tableau croisé dynamique et enregistre le classeur.

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

### Ajout d'un champ de page avec getPageFields().add

Lorsque vous travaillez déjà avec une instance `PivotField`, vous pouvez la transmettre directement à `pivotTable.getPageFields().add`. Le tableau croisé dynamique et le champ de page sont construits exactement comme dans le scénario précédent ; seul l'enregistrement final dans la zone de page est remplacé par l'appel d'API de bas niveau.

```javascript
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);

// En-têtes
sheet.getCells().get("A1").putValue("Fruit");
sheet.getCells().get("B1").putValue("Year");
sheet.getCells().get("C1").putValue("Amount");

// Données d'exemple (9 lignes)
sheet.getCells().get("A2").putValue("apple");    sheet.getCells().get("B2").putValue("2020"); sheet.getCells().get("C2").putValue(100);
sheet.getCells().get("A3").putValue("apple");    sheet.getCells().get("B3").putValue("2021"); sheet.getCells().get("C3").putValue(150);
sheet.getCells().get("A4").putValue("apple");    sheet.getCells().get("B4").putValue("2022"); sheet.getCells().get("C4").putValue(200);
sheet.getCells().get("A5").putValue("grape");    sheet.getCells().get("B5").putValue("2020"); sheet.getCells().get("C5").putValue(300);
sheet.getCells().get("A6").putValue("grape");    sheet.getCells().get("B6").putValue("2021"); sheet.getCells().get("C6").putValue(400);
sheet.getCells().get("A7").putValue("grape");    sheet.getCells().get("B7").putValue("2022"); sheet.getCells().get("C7").putValue(500);
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

## **Filtrage à sélection unique (affichage d'un seul élément de page)**

Dans le comportement par défaut en sélection unique, le champ de page s'affiche sous la forme d'une liste déroulante unique et l'entier `PivotField.CurrentPageItem` sélectionne l'élément de page qui pilote le corps du tableau croisé dynamique. L'affectation d'un index spécifique sélectionne cet unique élément ; l'affectation de la valeur sentinelle spéciale `0x7FFD` (32765 en décimal) réinitialise le filtre de sorte que chaque élément de page soit synthétisé en une seule fois. La sélection unique est le mode par défaut ; vous n'avez pas besoin de l'activer explicitement.

### Affichage de tous les éléments

Le réglage de `CurrentPageItem` à la valeur magique `0x7FFD` équivaut à réinitialiser le filtre de page ; le corps du tableau croisé dynamique synthétise chaque élément de page comme si aucun filtre n'était appliqué.

```javascript
var workbook = new AsposeCells.Workbook();
var sheet = workbook.getWorksheets().get(0);

// Remplir les données Fruit/Année/Montant
sheet.getCells().get("A1").putValue("Fruit");
sheet.getCells().get("B1").putValue("Year");
sheet.getCells().get("C1").putValue("Amount");

var data = [
    ["Apple", 2022, 100],
    ["Apple", 2023, 150],
    ["Banana", 2022, 80],
    ["Banana", 2023, 120],
    ["Cherry", 2022, 200],
    ["Cherry", 2023, 250]
];

for (var r = 0; r < data.length; r++) {
    for (var c = 0; c < data[r].length; c++) {
        sheet.getCells().get(r + 1, c).putValue(data[r][c]);
    }
}

// Créer un tableau croisé dynamique à E3
var pivotTables = sheet.getPivotTables();
var index = pivotTables.add("=A1:C7", "E3", "PivotTable1");
var pivotTable = pivotTables.get(index);

// Configurer les champs du tableau croisé : Fruit→Ligne, Montant→Données, Année→Page
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");

pivotTable.refreshData();
pivotTable.calculateData();

// Effacer le filtre de page pour que chaque élément du champ de page soit visible.
// 0x7FFD (32765 en décimal) est la valeur sentinelle spéciale qui signifie "tous les éléments" —
// équivalent à sélectionner "(Tous)" dans le menu déroulant du champ de page d'Excel.
pivotTable.getPageFields().get(0).setCurrentPageItem(0x7FFD);

workbook.save("output.xlsx");
```

### Affichage d'un élément spécifique

Le réglage de `CurrentPageItem` à un index réel sélectionne uniquement cet élément de page. L'index correspond à la position de l'élément dans la liste triée des éléments du champ de page ; ainsi, par exemple, `1` sélectionne le deuxième élément après le tri.

```javascript
var workbook = new AsposeCells.Workbook();
var sheet = workbook.getWorksheets().get(0);
var cells = sheet.getCells();

// Ajouter des données d'exemple (Fruit/Année/Montant)
cells.get("A1").setValue("Fruit");
cells.get("B1").setValue("Year");
cells.get("C1").setValue("Amount");

cells.get("A2").setValue("Apple");
cells.get("B2").setValue("2020");
cells.get("C2").setValue("100");

cells.get("A3").setValue("Apple");
cells.get("B3").setValue("2021");
cells.get("C3").setValue("150");

cells.get("A4").setValue("Banana");
cells.get("B4").setValue("2020");
cells.get("C4").setValue("200");

cells.get("A5").setValue("Banana");
cells.get("B5").setValue("2021");
cells.get("C5").setValue("250");

// Ajouter un tableau croisé dynamique à E3
var pivotTables = sheet.getPivotTables();
var pivotIndex = pivotTables.add("A1:C5", "E3", "PivotTable1");
var pivotTable = pivotTables.get(pivotIndex);

// Ajouter des champs : Fruit→Ligne, Montant→Données, Année→Page
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

Le filtrage à sélection multiple transforme la liste déroulante de page en une liste de cases à cocher et permet à l'utilisateur final de sélectionner simultanément plusieurs éléments de page. Aspose.Cells expose deux propriétés qui fonctionnent ensemble. `PivotField.IsMultipleItemSelectionAllowed` doit être défini sur `true` avant que l'interface utilisateur de sélection multiple ne prenne effet. Une fois activée, `PivotItem.IsHidden` contrôle quels éléments apparaissent dans la liste de cases à cocher, ce qui vous permet d'afficher chaque élément ou de n'autoriser que des éléments spécifiques.

Le code ci-dessous active la sélection multiple sur le même champ de page Year construit dans le scénario 1a, puis présente deux schémas : la partie A révèle chaque élément de page en laissant `IsHidden` défini sur `false` pour chaque entrée, tandis que la partie B n'autorise que les valeurs source que vous choisissez et masque tout le reste via un bloc `switch (pivotItems[i].getStringValue())`.

```javascript
const AsposeCells = require("aspose.cells");

// — Le tableau croisé dynamique et le champ de page sont construits exactement comme dans
//   le scénario 1a (données Fruit/Année/Montant, pivot à E3, Fruit→Ligne,
//   Montant→Données, Année→Page via AddFieldToArea).
//   Ci-dessous, nous appliquons un filtrage à sélection multiple sur le champ de page.

const workbook = new AsposeCells.Workbook();
const sheet = workbook.getWorksheets().get(0);
const cells = sheet.getCells();

// Données d'exemple : Fruit | Année | Montant
cells.get(0, 0).putValue("Fruit");
cells.get(0, 1).putValue("Year");
cells.get(0, 2).putValue("Amount");

const data = [
    ["apple",  "2019", "100"],
    ["apple",  "2020", "150"],
    ["apple",  "2021", "200"],
    ["banana", "2019", "110"],
    ["banana", "2020", "160"],
    ["banana", "2021", "210"],
    ["grape",  "2019", "120"],
    ["grape",  "2020", "170"],
    ["grape",  "2021", "220"]
];

for (let i = 0; i < data.length; i++) {
    cells.get(i + 1, 0).putValue(data[i][0]);
    cells.get(i + 1, 1).putValue(parseInt(data[i][1]));
    cells.get(i + 1, 2).putValue(parseInt(data[i][2]));
}

const pivotSheet = workbook.getWorksheets().add("Pivot");
const pivots = pivotSheet.getPivotTables();
const pivotIndex = pivots.add("E3", "A1:C10", "PivotTable1");
const pivotTable = pivots.get(pivotIndex);

pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.DATA, "Amount");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.PAGE, "Year");

// — Activer la sélection multiple sur le champ de page
pivotTable.getPageFields().get(0).setMultipleItemSelectionAllowed(true);

// Partie A — sélectionner TOUS les éléments (rendre chaque élément visible)
const pivotItems = pivotTable.getPageFields().get(0).getPivotItems();
for (let i = 0; i < pivotItems.getCount(); i++) {
    pivotItems.get(i).setHidden(false);
}

// Partie B — sélectionner uniquement des éléments spécifiques par valeur source
for (let i = 0; i < pivotItems.getCount(); i++) {
    switch (pivotItems.get(i).getStringValue()) {
        case "2020":
        case "grape":
        case "blueberry":
            pivotItems.get(i).setHidden(false);
            break;
        default:
            pivotItems.get(i).setHidden(true);
            break;
    }
}

pivotTable.refreshData();
pivotTable.calculateData();

workbook.save("output.xlsx");
```

> **Remarque :** Lorsque vous utilisez le filtrage à sélection multiple via `PivotItem.IsHidden`, **au moins un `PivotItem` doit rester visible** (`IsHidden == false`). Si tous les éléments sont masqués, Excel plante à l'ouverture du fichier ou affiche un tableau croisé dynamique vide. Vérifiez toujours que votre liste d'éléments autorisés en sélection multiple inclut au moins un élément de vos données source.

## **Quelle API et quel mode dois-je utiliser ?**

Le tableau ci-dessous résume quand utiliser chaque API et chaque mode afin que vous puissiez choisir la bonne combinaison sans avoir à lire chaque scénario en détail.

| Scénario / Cas d'utilisation | API recommandée | Propriété utilisée | Notes |
|---|---|---|---|
| Ajouter un champ de page par nom de colonne source (le plus courant) | `pivotTable.addFieldToArea(PivotFieldType.Page, "fieldName")` | n/a | Haut niveau, une seule ligne. Utilisez cette option sauf si vous avez besoin d'une référence `PivotField`. |
| Ajouter un champ de page lorsque vous disposez déjà d'un objet `PivotField` | `pivotTable.getPageFields().add(PivotField)` | n/a | À utiliser lorsque l'objet de champ a été obtenu ailleurs ou doit être réutilisé. |
| Filtrer sur un seul élément de page (mode par défaut) | `PivotField.CurrentPageItem` | défini sur un index spécifique | Par exemple, `1` affiche le deuxième élément dans la liste triée. |
| Afficher tous les éléments / réinitialiser le filtre de page | `PivotField.CurrentPageItem` | défini sur `0x7FFD` | La valeur magique `0x7FFD` (32765 en décimal) est la sentinelle pour « tous les éléments ». |
| Activer l'interface de sélection multiple dans Excel | `PivotField.IsMultipleItemSelectionAllowed` | défini sur `true` | Requis avant que tout appel à `IsHidden` ne prenne effet. |
| Masquer / afficher des éléments individuels dans une liste à sélection multiple | `PivotItem.IsHidden` | défini par élément | Au moins un élément doit rester visible (`IsHidden == false`). |

{{% alert color="primary" %}}
Gardez toujours à l'esprit la contrainte de visibilité lors de la configuration du filtrage à sélection multiple. Si chaque `PivotItem` d'un champ de page à sélection multiple est masqué, Excel plante à l'ouverture ou affiche un tableau croisé dynamique vide. Construisez votre liste d'éléments autorisés à partir de vos données source afin qu'au moins un élément reste visible, et vos classeurs enregistrés s'ouvriront de manière fiable sur chaque machine.
{{% /alert %}}



{{< app/cells/assistant language="javascript" >}}