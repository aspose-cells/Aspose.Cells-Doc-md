---
title: Ajouter des champs de filtre à un tableau croisé dynamique dans Aspose.Cells pour .NET
linktitle: Ajouter des champs de filtre
description: Apprenez à ajouter et configurer des champs de filtre dans des tableaux croisés dynamiques avec Aspose.Cells for .NET, y compris l'ajout de champs de filtre, le filtrage en sélection unique et le filtrage en sélection multiple.
keywords: Aspose.Cells, .NET, tableau croisé dynamique, champ de filtre, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, filtre
type: docs
weight: 250
url: /fr/net/add-filter-field-in-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells prend en charge le cycle de vie complet des champs de filtre dans les tableaux croisés dynamiques. Vous pouvez ajouter un champ de filtre via une API pratique de haut niveau ou via la collection `PageFields` de bas niveau, et vous pouvez piloter le filtre en mode sélection unique, le réinitialiser pour afficher tous les éléments de page, ou basculer le champ vers la sélection multiple afin que les utilisateurs puissent choisir plusieurs éléments de page à la fois grâce à l'interface à cases à cocher d'Excel.
{{% /alert %}}

## **Introduction**

Un champ de filtre est un champ de tableau croisé dynamique qui contrôle *quel sous-ensemble* des données source le corps du tableau croisé dynamique affiche. L'utilisateur final le voit comme une liste déroulante en haut d'un tableau croisé dynamique rendu dans Excel, et sélectionner l'un des éléments de page disponibles reconstruit le corps du tableau croisé dynamique de sorte que seuls les enregistrements appartenant à cet élément de page soient synthétisés. Un champ de tableau croisé dynamique devient un champ de filtre lorsqu'il est enregistré en tant que `PivotFieldType.Page` plutôt que `PivotFieldType.Row`, `PivotFieldType.Column` ou `PivotFieldType.Data`.

Un champ de filtre peut fonctionner selon deux comportements. Dans le comportement par défaut en **sélection unique**, seul un élément de page est visible à la fois, de sorte que le corps du tableau croisé dynamique synthétise exactement un sous-ensemble. Dans le comportement en **sélection multiple**, le champ expose une liste de cases à cocher, et le corps du tableau croisé dynamique synthétise l'union de tous les éléments de page cochés. Le même champ source peut basculer entre ces comportements en activant ou désactivant une seule propriété.

Aspose.Cells for .NET expose deux façons équivalentes d'enregistrer un champ de filtre. L'API de haut niveau est `PivotTable.AddFieldToArea(PivotFieldType.Page, "fieldName")`, qui prend le nom de la colonne source et ajoute le champ en un seul appel. L'API de bas niveau est `PivotTable.PageFields.Add(PivotField)`, qui est utilisée lorsque vous détenez déjà une référence `PivotField` et souhaitez ajouter la même instance de champ à la zone de filtre. Les deux API finissent par remplir la même collection `PageFields`, et la suite de cet article montre comment choisir entre elles et comment piloter chaque mode de filtrage.

## **Ajout d'un champ de filtre**

Il existe deux façons d'enregistrer un champ de tableau croisé dynamique dans la zone de filtre. L'appel de haut niveau prend le nom de la colonne source sous forme de chaîne et constitue le chemin le plus courant. L'appel de bas niveau accepte une instance `PivotField` existante et est pratique lorsque le même objet champ doit être réutilisé dans plusieurs zones du tableau croisé dynamique. Les deux appels placent le champ dans `PivotTable.PageFields`, après quoi il apparaît comme la liste déroulante de page en haut du tableau croisé dynamique rendu.

### Ajout d'un champ de filtre avec AddFieldToArea

L'exemple suivant construit un petit jeu de données Fruit / Année / Montant, place un tableau croisé dynamique dans la cellule E3 avec `Fruit` dans la zone de ligne, `Amount` dans la zone de données, et `Year` dans la zone de filtre, actualise le tableau croisé dynamique, et enregistre le classeur.

```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// Créer un nouveau classeur
var workbook = new Workbook();
var worksheet = workbook.Worksheets[0];
worksheet.Name = "Data";

// Configurer la ligne d'en-tête
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");

// Remplir 9 lignes de données d'exemple : Fruit, Année, Montant
object[,] data = new object[,]
{
    { "apple", 2020, 100 },
    { "banana", 2021, 200 },
    { "apple", 2021, 150 },
    { "grape", 2020, 120 },
    { "orange", 2022, 180 },
    { "banana", 2020, 90 },
    { "grape", 2021, 130 },
    { "apple", 2022, 170 },
    { "orange", 2021, 110 }
};

for (int i = 0; i < data.GetLength(0); i++)
{
    worksheet.Cells[i + 1, 0].PutValue(data[i, 0]);
    worksheet.Cells[i + 1, 1].PutValue(data[i, 1]);
    worksheet.Cells[i + 1, 2].PutValue(data[i, 2]);
}

// Ajouter un tableau croisé dynamique ancré à la cellule E3
int pivotIndex = worksheet.PivotTables.Add("A1:C10", "E3", "PivotTable1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];

// Ajouter des champs à leurs zones : Fruit comme Ligne, Montant comme Données, Année comme champ de Page
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.AddFieldToArea(PivotFieldType.Page, "Year");

// Actualiser et calculer les données du tableau croisé dynamique
pivotTable.RefreshData();
pivotTable.CalculateData();

// Enregistrer le classeur
workbook.Save("pageFieldSample.xlsx");
```

### Ajout d'un champ de filtre avec PageFields.Add

Lorsque vous travaillez déjà avec une instance `PivotField`, vous pouvez la passer directement à `PivotTable.PageFields.Add`. Le tableau croisé dynamique et le champ de filtre sont construits exactement comme dans le scénario précédent ; seule l'enregistrement final dans la zone de filtre est remplacé par l'appel d'API de bas niveau.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// — Le tableau croisé dynamique et le champ de page sont construits exactement comme dans
//   Scénario 1a (données Fruit/Année/Montant, pivot à E3, Fruit→Ligne,
//   Montant→Données). Ci-dessous, nous obtenons le PivotField Année à partir de la
//   collection BaseFields et le passons à PageFields.Add — l'
//   alternative de bas niveau à AddFieldToArea. Le résultat est
//   fonctionnellement identique au Scénario 1a.

Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];

// En-têtes
sheet.Cells["A1"].PutValue("Fruit");
sheet.Cells["B1"].PutValue("Year");
sheet.Cells["C1"].PutValue("Amount");

// Données d'exemple (9 lignes)
sheet.Cells["A2"].PutValue("apple");    sheet.Cells["B2"].PutValue("2020"); sheet.Cells["C2"].PutValue(100);
sheet.Cells["A3"].PutValue("apple");    sheet.Cells["B3"].PutValue("2021"); sheet.Cells["C3"].PutValue(150);
sheet.Cells["A4"].PutValue("apple");    sheet.Cells["B4"].PutValue("2022"); sheet.Cells["C4"].PutValue(200);
sheet.Cells["A5"].PutValue("grape");    sheet.Cells["B5"].PutValue("2020"); sheet.Cells["C5"].PutValue(300);
sheet.Cells["A6"].PutValue("grape");    sheet.Cells["B6"].PutValue("2021"); sheet.Cells["C6"].PutValue(400);
sheet.Cells["A7"].PutValue("grape");    sheet.Cells["B7"].PutValue("2022"); sheet.Cells["C7"].PutValue(500);
sheet.Cells["A8"].PutValue("blueberry"); sheet.Cells["B8"].PutValue("2020"); sheet.Cells["C8"].PutValue(250);
sheet.Cells["A9"].PutValue("blueberry"); sheet.Cells["B9"].PutValue("2021"); sheet.Cells["C9"].PutValue(350);
sheet.Cells["A10"].PutValue("blueberry");sheet.Cells["B10"].PutValue("2022"); sheet.Cells["C10"].PutValue(450);

// Ajouter un tableau croisé dynamique à E3 couvrant A1:C10
int pivotIndex = sheet.PivotTables.Add("E3", "A1:C10", "PivotTable1");
PivotTable pivotTable = sheet.PivotTables[pivotIndex];

// Fruit -> Ligne, Montant -> Données (Année ira à la Page ci-dessous)
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

// Approche de bas niveau : récupérer le PivotField Année existant à partir de BaseFields
// et l'enregistrer dans la zone Page via PageFields.Add(PivotField).
PivotField yearField = pivotTable.BaseFields["Year"];
pivotTable.PageFields.Add(yearField);

// Actualiser pour que le nouveau champ de page soit reflété dans le classeur enregistré
pivotTable.RefreshData();
pivotTable.CalculateData();

workbook.Save("output.xlsx");
```

## **Filtrage en sélection unique (affichage d'un seul élément de page)**

Dans le comportement par défaut en sélection unique, le champ de filtre s'affiche sous forme de liste déroulante unique et l'entier `PivotField.CurrentPageItem` sélectionne l'élément de page qui pilote le corps du tableau croisé dynamique. Attribuer un index spécifique sélectionne cet élément ; attribuer la valeur sentinelle spéciale `0x7FFD` (décimale 32765) réinitialise le filtre de sorte que tous les éléments de page soient synthétisés en même temps. La sélection unique est le mode par défaut ; vous n'avez pas besoin de l'activer explicitement.

### Afficher tous les éléments

Définir `CurrentPageItem` sur la valeur magique `0x7FFD` revient à effacer le filtre : le corps du tableau croisé dynamique synthétise tous les éléments de page comme si aucun filtre n'était appliqué.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

class Program
{
    static void Main()
    {
        // Créer un nouveau classeur
        Workbook workbook = new Workbook();
        Worksheet sheet = workbook.Worksheets[0];

        // Remplir les données Fruit/Année/Montant
        sheet.Cells["A1"].PutValue("Fruit");
        sheet.Cells["B1"].PutValue("Year");
        sheet.Cells["C1"].PutValue("Amount");

        object[,] data = new object[,]
        {
            {"Apple", 2022, 100},
            {"Apple", 2023, 150},
            {"Banana", 2022, 80},
            {"Banana", 2023, 120},
            {"Cherry", 2022, 200},
            {"Cherry", 2023, 250}
        };

        for (int r = 0; r < data.GetLength(0); r++)
        {
            for (int c = 0; c < data.GetLength(1); c++)
            {
                sheet.Cells[r + 1, c].PutValue(data[r, c]);
            }
        }

        // Créer un tableau croisé dynamique à E3
        var pivotTables = sheet.PivotTables;
        int index = pivotTables.Add("=A1:C7", "E3", "PivotTable1");
        PivotTable pivotTable = pivotTables[index];

        // Configurer les champs du tableau croisé : Fruit→Ligne, Montant→Données, Année→Page
        pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
        pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
        pivotTable.AddFieldToArea(PivotFieldType.Page, "Year");

        pivotTable.RefreshData();
        pivotTable.CalculateData();

        // Effacer le filtre de page afin que chaque élément du champ de page soit visible.
        // 0x7FFD (32765 en décimal) est la valeur sentinelle spéciale qui signifie « tous les éléments » —
        // équivalent à sélectionner « (Tous) » dans la liste déroulante du champ de page d'Excel.
        pivotTable.PageFields[0].CurrentPageItem = 0x7FFD;

        workbook.Save("output.xlsx");
    }
}
```

### Afficher un élément spécifique

Définir `CurrentPageItem` sur un index réel ne sélectionne que cet élément de page. L'index correspond à la position de l'élément dans la liste triée des éléments du champ de filtre ; par exemple, `1` sélectionne le deuxième élément après le tri.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// Créer le classeur
var workbook = new Workbook();
var sheet = workbook.Worksheets[0];
var cells = sheet.Cells;

// Ajouter des données d'exemple (Fruit/Année/Montant)
cells["A1"].PutValue("Fruit");
cells["B1"].PutValue("Year");
cells["C1"].PutValue("Amount");

cells["A2"].PutValue("Apple");
cells["B2"].PutValue("2020");
cells["C2"].PutValue("100");

cells["A3"].PutValue("Apple");
cells["B3"].PutValue("2021");
cells["C3"].PutValue("150");

cells["A4"].PutValue("Banana");
cells["B4"].PutValue("2020");
cells["C4"].PutValue("200");

cells["A5"].PutValue("Banana");
cells["B5"].PutValue("2021");
cells["C5"].PutValue("250");

// Ajouter un tableau croisé dynamique à E3
var pivotTables = sheet.PivotTables;
int pivotIndex = pivotTables.Add("A1:C5", "E3", "PivotTable1");
var pivotTable = pivotTables[pivotIndex];

// Ajouter des champs : Fruit→Ligne, Montant→Données, Année→Page
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.AddFieldToArea(PivotFieldType.Page, "Year");

// Opérations spécifiques au champ de page
pivotTable.PageFields[0].CurrentPageItem = 1; // 1 = deuxième élément dans l'ordre trié (par ex. "2021")

// Actualiser et calculer le tableau croisé dynamique
pivotTable.RefreshData();
pivotTable.CalculateData();

workbook.Save("output.xlsx");
```

## **Filtrage en sélection multiple**

Le filtrage en sélection multiple transforme la liste déroulante de page en une liste de cases à cocher et permet à l'utilisateur final de sélectionner simultanément plusieurs éléments de page. Aspose.Cells expose deux propriétés qui fonctionnent ensemble. `PivotField.IsMultipleItemSelectionAllowed` doit être définie sur `true` pour que l'interface de sélection multiple prenne effet. Une fois activée, `PivotItem.IsHidden` contrôle quels éléments apparaissent dans la liste de cases à cocher, ce qui vous permet soit d'afficher tous les éléments, soit d'autoriser uniquement des éléments spécifiques.

Le code ci-dessous active la sélection multiple sur le même champ de filtre Year construit dans le scénario 1a, puis montre deux schémas : la partie A révèle tous les éléments de page en laissant `IsHidden` défini sur `false` pour chaque entrée, tandis que la partie B autorise uniquement les valeurs source que vous choisissez et masque tout le reste via un bloc `switch (pivotItems[i].GetStringValue())`.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// — Le tableau croisé dynamique et le champ de page sont construits exactement comme dans
//   le scénario 1a (données Fruit/Année/Montant, tableau croisé à E3, Fruit→Ligne,
//   Montant→Données, Année→Page via AddFieldToArea).
//   Ci-dessous, nous appliquons un filtrage multi-sélection sur le champ de page.

Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];
Cells cells = sheet.Cells;

// Données d'exemple : Fruit | Année | Montant
cells[0, 0].PutValue("Fruit");
cells[0, 1].PutValue("Year");
cells[0, 2].PutValue("Amount");

string[,] data = new string[,]
{
    { "apple",  "2019", "100" },
    { "apple",  "2020", "150" },
    { "apple",  "2021", "200" },
    { "banana", "2019", "110" },
    { "banana", "2020", "160" },
    { "banana", "2021", "210" },
    { "grape",  "2019", "120" },
    { "grape",  "2020", "170" },
    { "grape",  "2021", "220" }
};

for (int i = 0; i < data.GetLength(0); i++)
{
    cells[i + 1, 0].PutValue(data[i, 0]);
    cells[i + 1, 1].PutValue(Convert.ToInt32(data[i, 1]));
    cells[i + 1, 2].PutValue(Convert.ToInt32(data[i, 2]));
}

Worksheet pivotSheet = workbook.Worksheets.Add("Pivot");
PivotTableCollection pivots = pivotSheet.PivotTables;
int pivotIndex = pivots.Add("E3", "A1:C10", "PivotTable1");
PivotTable pivotTable = pivots[pivotIndex];

pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.AddFieldToArea(PivotFieldType.Page, "Year");

// — Activer la multi-sélection sur le champ de page
pivotTable.PageFields[0].IsMultipleItemSelectionAllowed = true;

// Partie A — sélectionner TOUS les éléments (rendre chaque élément visible)
PivotItemCollection pivotItems = pivotTable.PageFields[0].PivotItems;
for (int i = 0; i < pivotItems.Count; i++)
{
    pivotItems[i].IsHidden = false;
}

// Partie B — sélectionner uniquement des éléments spécifiques par valeur source
for (int i = 0; i < pivotItems.Count; i++)
{
    switch (pivotItems[i].GetStringValue())
    {
        case "2020":
        case "grape":
        case "blueberry":
            pivotItems[i].IsHidden = false;
            break;
        default:
            pivotItems[i].IsHidden = true;
            break;
    }
}

pivotTable.RefreshData();
pivotTable.CalculateData();

workbook.Save("output.xlsx");
```

> **Remarque :** Lors de l'utilisation du filtrage en sélection multiple via `PivotItem.IsHidden`, **au moins un `PivotItem` doit rester visible** (`IsHidden == false`). Si tous les éléments sont masqués, Excel plante à l'ouverture du fichier ou affiche un tableau croisé dynamique vide. Vérifiez toujours que votre liste autorisée de sélection multiple inclut au moins un élément de vos données source.

## **Quelle API et quel mode dois-je utiliser ?**

Le tableau ci-dessous résume quand utiliser chaque API et chaque mode afin que vous puissiez choisir la bonne combinaison sans lire chaque scénario en détail.

| Scénario / Cas d'utilisation | API recommandée | Propriété utilisée | Remarques |
|---|---|---|---|
| Ajouter un champ de filtre par nom de colonne source (le plus courant) | `PivotTable.AddFieldToArea(PivotFieldType.Page, "fieldName")` | n/a | Haut niveau, une seule ligne. Utilisez ceci sauf si vous avez besoin d'une référence `PivotField`. |
| Ajouter un champ de filtre lorsque vous avez déjà un objet `PivotField` | `PivotTable.PageFields.Add(PivotField)` | n/a | À utiliser lorsque l'objet champ a été obtenu ailleurs ou doit être réutilisé. |
| Filtrer sur un seul élément de page (mode par défaut) | `PivotField.CurrentPageItem` | définir sur un index spécifique | Par exemple, `1` affiche le deuxième élément de la liste triée. |
| Afficher tous les éléments / effacer le filtre | `PivotField.CurrentPageItem` | définir sur `0x7FFD` | La valeur magique `0x7FFD` (décimale 32765) est la sentinelle pour « tous les éléments ». |
| Activer l'interface de sélection multiple dans Excel | `PivotField.IsMultipleItemSelectionAllowed` | définir sur `true` | Requis avant que tout appel à `IsHidden` ne prenne effet. |
| Masquer / afficher des éléments individuels dans une liste à sélection multiple | `PivotItem.IsHidden` | définir par élément | Au moins un élément doit rester visible (`IsHidden == false`). |

{{% alert color="primary" %}}
N'oubliez jamais la contrainte de visibilité lors de la configuration du filtrage en sélection multiple. Si chaque `PivotItem` d'un champ de filtre à sélection multiple est masqué, Excel plante à l'ouverture ou affiche un tableau croisé dynamique vide. Construisez votre liste autorisée à partir de vos données source afin qu'au moins un élément reste visible, et vos classeurs enregistrés s'ouvriront de manière fiable sur toutes les machines.
{{% /alert %}}



## **Articles connexes**

- [Refreshing Pivot Tables in Aspose.Cells for .NET](/cells/fr/net/refresh-pivot-table/)
- [Splitting Excel Files into Multiple Files](/cells/fr/net/splitting-excel-files-into-multiple-files/)
- [Applying Styles to Pivot Tables](/cells/fr/net/apply-style-to-pivot-table/)
- [Converting Excel to OFD Format](/cells/fr/net/ofd/)
- [SmartMarker Single Cell Array Rendering | Aspose.Cells .NET](/cells/fr/net/SmartMarker-Single-Cell-Array-Rendering/)

{{< app/cells/assistant language="csharp" >}}
