---
title: Ajouter des champs de filtre à un tableau croisé dynamique dans Aspose.Cells for .NET
linktitle: Ajouter des champs de filtre à un tableau croisé dynamique dans Aspose.Cells for .NET
description: Apprenez à ajouter et configurer des champs de filtre dans les tableaux croisés dynamiques avec Aspose.Cells for .NET, y compris l'ajout de champs de filtre, le filtrage à sélection unique et le filtrage multi-sélection.
keywords: Aspose.Cells, .NET, tableau croisé dynamique, champ de filtre, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, filtre
type: docs
weight: 250
url: /fr/net/add-page-field-in-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells prend en charge le cycle de vie complet des champs de filtre dans les tableaux croisés dynamiques. Vous pouvez ajouter un champ de filtre via une API de commodité de haut niveau ou via la collection de bas niveau `PageFields`, et vous pouvez piloter le filtre en mode sélection unique, le réinitialiser pour afficher chaque élément de filtre, ou basculer le champ vers la multi-sélection afin que les utilisateurs puissent choisir plusieurs éléments de filtre à la fois via l'interface utilisateur à cases à cocher dans Excel.
{{% /alert %}}

## **Introduction**
Un champ de filtre est un champ de tableau croisé dynamique qui contrôle *quel sous-ensemble* des données sources le corps du tableau croisé dynamique affiche. Les utilisateurs finaux le voient sous forme de liste déroulante en haut d'un tableau croisé dynamique rendu dans Excel, et la sélection d'un des éléments de filtre disponibles reconstruit le corps du tableau croisé dynamique de sorte que seuls les enregistrements appartenant à cet élément de filtre soient résumés. Un champ de tableau croisé dynamique devient un champ de filtre lorsqu'il est enregistré en tant que `PivotFieldType.Page` plutôt que `PivotFieldType.Row`, `PivotFieldType.Column` ou `PivotFieldType.Data`.

## **Ajouter un champ de filtre**

### Ajouter un champ de filtre avec AddFieldToArea
L'exemple suivant construit un petit jeu de données Fruit / Année / Montant, place un tableau croisé dynamique à la cellule E3 avec `Fruit` dans la zone des lignes, `Montant` dans la zone des données et `Année` dans la zone de filtre, actualise le tableau croisé dynamique et enregistre le classeur.

```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;
// Create a new workbook
var workbook = new Workbook();
var worksheet = workbook.Worksheets[0];
worksheet.Name = "Data";
// Set up the header row
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");
// Populate 9 rows of sample data: Fruit, Year, Amount
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
// Add a pivot table anchored at cell E3
PivotTable pivotTable = worksheet.PivotTables.Add("A1:C10", 2, 4);
// Add fields to their areas: Fruit as Row, Amount as Data, Year as Page field
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.AddFieldToArea(PivotFieldType.Page, "Year");
// Refresh and calculate the pivot table data
pivotTable.CalculateData();
// Save the workbook
workbook.Save("pageFieldSample.xlsx");
```

### Ajouter un champ de filtre avec PageFields.Add
Lorsque vous travaillez déjà avec une instance de `PivotField`, vous pouvez la transmettre directement à `PivotTable.PageFields.Add`. Le tableau croisé dynamique et le champ de filtre sont construits exactement comme dans le scénario précédent ; seul l'enregistrement final de la zone de filtre est remplacé par l'appel d'API de bas niveau.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
// — The pivot table and page field are constructed exactly as in
//   Scenario 1a (Fruit/Year/Amount data, pivot at E3, Fruit→Row,
//   Amount→Data). Below we obtain the Year PivotField from the
//   BaseFields collection and pass it to PageFields.Add — the
//   low-level alternative to AddFieldToArea. The result is
//   functionally identical to Scenario 1a.
Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];
// Headers
sheet.Cells["A1"].PutValue("Fruit");
sheet.Cells["B1"].PutValue("Year");
sheet.Cells["C1"].PutValue("Amount");
// Sample data (9 rows)
sheet.Cells["A2"].PutValue("apple");    sheet.Cells["B2"].PutValue("2020"); sheet.Cells["C2"].PutValue(100);
sheet.Cells["A3"].PutValue("apple");    sheet.Cells["B3"].PutValue("2021"); sheet.Cells["C3"].PutValue(150);
sheet.Cells["A4"].PutValue("apple");    sheet.Cells["B4"].PutValue("2022"); sheet.Cells["C4"].PutValue(200);
sheet.Cells["A5"].PutValue("grape");    sheet.Cells["B5"].PutValue("2020"); sheet.Cells["C5"].PutValue(300);
sheet.Cells["A6"].PutValue("grape");    sheet.Cells["B6"].PutValue("2021"); sheet.Cells["C6"].PutValue(400);
sheet.Cells["A7"].PutValue("grape");    sheet.Cells["B7"].PutValue("2022"); sheet.Cells["C7"].PutValue(500);
sheet.Cells["A8"].PutValue("blueberry"); sheet.Cells["B8"].PutValue("2020"); sheet.Cells["C8"].PutValue(250);
sheet.Cells["A9"].PutValue("blueberry"); sheet.Cells["B9"].PutValue("2021"); sheet.Cells["C9"].PutValue(350);
sheet.Cells["A10"].PutValue("blueberry");sheet.Cells["B10"].PutValue("2022"); sheet.Cells["C10"].PutValue(450);
// Add pivot table at E3 covering A1:C10
PivotTable pivotTable = sheet.PivotTables.Add("A1:C10", 2, 4);
// Fruit -> Row, Amount -> Data (Year will go to Page below)
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
// Low-level approach: grab the existing Year PivotField from BaseFields
// and register it in the Page area via PageFields.Add(PivotField).
PivotField yearField = pivotTable.BaseFields["Year"];
pivotTable.PageFields.Add(yearField);
// Refresh so the new page field is reflected in the saved workbook
pivotTable.CalculateData();
workbook.Save("output.xlsx");
```

## **Filtrage à sélection unique (affichage d'un seul élément de filtre)**
Dans le comportement par défaut en sélection unique, le champ de filtre est rendu sous forme d'une seule liste déroulante et l'entier `PivotField.CurrentPageItem` sélectionne quel élément de filtre pilote le corps du tableau croisé dynamique. L'affectation d'un index spécifique choisit cet élément ; l'affectation de la valeur sentinelle spéciale `0x7FFD` (32765 en décimal) réinitialise le filtre afin que chaque élément de filtre soit résumé en une seule fois. La sélection unique est le mode par défaut ; vous n'avez pas besoin de l'activer explicitement.

### Afficher tous les éléments
Définir `CurrentPageItem` sur la valeur magique `0x7FFD` équivaut à réinitialiser le filtre : le corps du tableau croisé dynamique résume chaque élément de filtre comme si aucun filtre n'était appliqué.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
class Program
{
    static void Main()
    {
        // Create a new workbook
        Workbook workbook = new Workbook();
        Worksheet sheet = workbook.Worksheets[0];
        // Populate Fruit/Year/Amount data
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
        // Create pivot table at E3
        var pivotTables = sheet.PivotTables;
        PivotTable pivotTable = pivotTables.Add("=A1:C7", 2, 4);
        // Configure pivot fields: Fruit→Row, Amount→Data, Year→Page
        pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
        pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
        pivotTable.AddFieldToArea(PivotFieldType.Page, "Year");
        pivotTable.CalculateData();
        // Clear the page filter so every item in the page field is visible.
        // 0x7FFD (decimal 32765) is the special sentinel value that means "all items" —
        // equivalent to selecting "(All)" in Excel's page-field dropdown.
        pivotTable.PageFields[0].CurrentPageItem = 0x7FFD;
        workbook.Save("output.xlsx");
    }
}
```

### Afficher un élément spécifique
Définir `CurrentPageItem` sur un index réel choisit uniquement cet élément de filtre. L'index est la position de l'élément dans la liste triée des éléments du champ de filtre. Ainsi, par exemple, `1` sélectionne le deuxième élément après le tri.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
// Create workbook
var workbook = new Workbook();
var sheet = workbook.Worksheets[0];
var cells = sheet.Cells;
// Add sample data (Fruit/Year/Amount)
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
// Add pivot table at E3
var pivotTables = sheet.PivotTables;
var pivotTable = pivotTables.Add("A1:C5", 2, 4);
// Add fields: Fruit→Row, Amount→Data, Year→Page
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.AddFieldToArea(PivotFieldType.Page, "Year");
// Page-field-specific operations
pivotTable.PageFields[0].CurrentPageItem = 1; // 1 = second item in sorted order (e.g. "2021")
// Refresh and calculate pivot table
pivotTable.CalculateData();
workbook.Save("output.xlsx");
```

## **Filtrage multi-sélection**
Le filtrage multi-sélection transforme la liste déroulante du filtre en une liste de cases à cocher et permet à l'utilisateur final de choisir simultanément plusieurs éléments de filtre. Aspose.Cells expose deux propriétés qui fonctionnent ensemble. `PivotField.IsMultipleItemSelectionAllowed` doit être défini sur `true` avant que l'interface utilisateur multi-sélection ne prenne effet. Une fois activée, `PivotItem.IsHidden` contrôle quels éléments apparaissent dans la liste de cases à cocher, ce qui vous permet soit d'afficher tous les éléments, soit d'autoriser uniquement des éléments spécifiques.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
// — The pivot table and page field are constructed exactly as in
//   Scenario 1a (Fruit/Year/Amount data, pivot at E3, Fruit→Row,
//   Amount→Data, Year→Page via AddFieldToArea).
//   Below we apply multi-select filtering on the page field.
Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];
Cells cells = sheet.Cells;
// Sample data: Fruit | Year | Amount
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
PivotTable pivotTable = pivots.Add("A1:C10", 2, 4);
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.AddFieldToArea(PivotFieldType.Page, "Year");
// — Enable multi-select on the page field
pivotTable.PageFields[0].IsMultipleItemSelectionAllowed = true;
// Part A — select ALL items (make every item visible)
PivotItemCollection pivotItems = pivotTable.PageFields[0].PivotItems;
for (int i = 0; i < pivotItems.Count; i++)
{
    pivotItems[i].IsHidden = false;
}
// Part B — select only specific items by source value
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
pivotTable.CalculateData();
workbook.Save("output.xlsx");
```

> **Remarque :** Lorsque vous utilisez le filtrage multi-sélection via `PivotItem.IsHidden`, **au moins un `PivotItem` doit rester visible** (`IsHidden == false`). Si chaque élément est masqué, Excel plante à l'ouverture du fichier ou affiche un tableau croisé dynamique vide. Vérifiez toujours que votre liste autorisée multi-sélection inclut au moins un élément de vos données sources.

## **Quelle API et quel mode dois-je utiliser ?**
Le tableau ci-dessous résume quand utiliser chaque API et chaque mode afin que vous puissiez choisir la bonne combinaison sans avoir à lire chaque scénario en détail.
| Scénario / Cas d'utilisation | API recommandée | Propriété utilisée | Remarques |
|---|---|---|---|
| Ajouter un champ de filtre par nom de colonne source (le plus courant) | `PivotTable.AddFieldToArea(PivotFieldType.Page, "fieldName")` | n/a | Haut niveau, une ligne. Utilisez cette option sauf si vous avez besoin d'une référence `PivotField`. |
| Ajouter un champ de filtre lorsque vous avez déjà un objet `PivotField` | `PivotTable.PageFields.Add(PivotField)` | n/a | Utilisez cette option lorsque l'objet champ a été obtenu ailleurs ou doit être réutilisé. |
| Filtrer sur un seul élément de filtre (mode par défaut) | `PivotField.CurrentPageItem` | défini sur un index spécifique | Par exemple, `1` affiche le deuxième élément dans la liste triée. |
| Afficher tous les éléments / réinitialiser le filtre | `PivotField.CurrentPageItem` | défini sur `0x7FFD` | La valeur magique `0x7FFD` (32765 en décimal) est la sentinelle pour « tous les éléments ». |
| Activer l'interface multi-sélection dans Excel | `PivotField.IsMultipleItemSelectionAllowed` | défini sur `true` | Requis avant que tout appel à `IsHidden` ne prenne effet. |
| Masquer / afficher des éléments individuels dans une liste multi-sélection | `PivotItem.IsHidden` | défini par élément | Au moins un élément doit rester visible (`IsHidden == false`). |

{{% alert color="primary" %}}
N'oubliez jamais la contrainte de visibilité lors de la configuration du filtrage multi-sélection. Si chaque `PivotItem` d'un champ de filtre multi-sélection est masqué, Excel plante à l'ouverture ou affiche un tableau croisé dynamique vide. Construisez votre liste autorisée à partir de vos données sources afin qu'au moins un élément reste visible, et vos classeurs enregistrés s'ouvriront de manière fiable sur toutes les machines.
{{% /alert %}}

## **Articles connexes**
- [Actualisation des tableaux croisés dynamiques dans Aspose.Cells for .NET](/cells/fr/net/refresh-pivot-table/)
- [Application de styles aux tableaux croisés dynamiques](/cells/fr/net/apply-style-to-pivot-table/)

{{< app/cells/assistant language="csharp" >}}