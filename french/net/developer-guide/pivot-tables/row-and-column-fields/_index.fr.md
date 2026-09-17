---
title: Ajouter des champs de ligne et de colonne de tableau croisé dynamique dans Aspose.Cells for .NET
linktitle: Ajouter des champs de ligne et de colonne de tableau croisé dynamique dans Aspose.Cells for .NET
description: Apprenez à ajouter des champs de tableau croisé dynamique de ligne et de colonne à un tableau croisé dynamique et à contrôler les sous-totaux des champs de tableau croisé dynamique à l'aide de PivotField.SetSubtotals avec PivotFieldSubtotalType dans Aspose.Cells for .NET.
keywords: Aspose.Cells, .NET, tableau croisé dynamique, champ de ligne, champ de colonne, PivotField, SetSubtotals, PivotFieldSubtotalType, sous-totaux, C#, tableau croisé dynamique Excel
type: docs
weight: 220
url: /fr/net/pivot-table-add-row-and-column-fields/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Ajout d'un champ à la zone de ligne ou de colonne**
La méthode `PivotTable.AddFieldToArea(PivotFieldType fieldType, string fieldName)` déplace un champ de base des données sources vers l'une des quatre zones de tableau croisé dynamique. L'argument `fieldType` accepte l'une des valeurs `PivotFieldType` suivantes.
- `Row` — champs placés verticalement à gauche
- `Column` — champs placés horizontalement en haut
- `Data` — champs dont les valeurs sont agrégées
- `Page` — champs utilisés comme filtres de rapport
L'ordre d'imbrication des champs est important. Ajouter `Category` à la zone de ligne en premier, puis `Item` produit un tableau croisé dynamique dont le regroupement externe est `Category` et dont le regroupement interne est `Item`. Inverser l'ordre inverse la hiérarchie.

## **Sous-totaux des champs de tableau croisé dynamique**
La méthode `PivotField.SetSubtotals(PivotFieldSubtotalType subtotalType, bool shown)` contrôle quelles lignes de sous-total apparaissent pour un champ de tableau croisé dynamique. Chaque appel bascule un seul type de sous-total indépendamment. Passer `shown = true` affiche le sous-total, tandis que `shown = false` le masque. Comme chaque appel n'affecte qu'un seul type, appeler la méthode plusieurs fois avec différentes valeurs `subtotalType` permet de construire un sous-ensemble personnalisé de sous-totaux.
L'énumération `PivotFieldSubtotalType` définit les types de sous-totaux disponibles.
- `Automatic` — Aspose.Cells choisit la sélection par défaut (généralement `Sum` pour les champs numériques)
- `None` — supprime toutes les lignes de sous-total
- `Sum`
- `Count`
- `Average`
- `Max`
- `Min`
- `Product`
- `StdDev`
- `StdDevp`
- `Var`
- `Varp`

{{% alert color="primary" %}}
Les sous-totaux ne s'affichent que lorsqu'il y a au moins deux champs de tableau croisé dynamique dans la zone de ligne (ou dans la zone de colonne). Un seul champ n'a rien de significatif à sous-totaliser entre les valeurs, donc les appels à `SetSubtotals` n'ont aucun effet visible dans ce cas. Par conséquent, cet article place deux champs de ligne (`Category` externe, `Item` interne) dans chaque exemple afin que la limite de sous-total entre chaque groupe `Category` soit visible.
{{% /alert %}}

## **Scénario 1 — Sous-totaux automatiques (par défaut)**
Lorsque vous n'appelez pas du tout `SetSubtotals`, Aspose.Cells applique la sélection `Automatic` aux champs numériques. L'exemple suivant confirme explicitement ce comportement en appelant `SetSubtotals(PivotFieldSubtotalType.Automatic, true)` sur le champ de ligne `Category` externe.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Name = "Data";
worksheet.Cells[0, 0].PutValue("Category");
worksheet.Cells[0, 1].PutValue("Item");
worksheet.Cells[0, 2].PutValue("Year");
worksheet.Cells[0, 3].PutValue("Amount");
worksheet.Cells[1, 0].PutValue("Fruit");
worksheet.Cells[1, 1].PutValue("Apple");
worksheet.Cells[1, 2].PutValue(2020);
worksheet.Cells[1, 3].PutValue(100);
worksheet.Cells[2, 0].PutValue("Fruit");
worksheet.Cells[2, 1].PutValue("Apple");
worksheet.Cells[2, 2].PutValue(2021);
worksheet.Cells[2, 3].PutValue(150);
worksheet.Cells[3, 0].PutValue("Fruit");
worksheet.Cells[3, 1].PutValue("Banana");
worksheet.Cells[3, 2].PutValue(2020);
worksheet.Cells[3, 3].PutValue(80);
worksheet.Cells[4, 0].PutValue("Fruit");
worksheet.Cells[4, 1].PutValue("Banana");
worksheet.Cells[4, 2].PutValue(2021);
worksheet.Cells[4, 3].PutValue(90);
worksheet.Cells[5, 0].PutValue("Vegetable");
worksheet.Cells[5, 1].PutValue("Carrot");
worksheet.Cells[5, 2].PutValue(2020);
worksheet.Cells[5, 3].PutValue(50);
worksheet.Cells[6, 0].PutValue("Vegetable");
worksheet.Cells[6, 1].PutValue("Carrot");
worksheet.Cells[6, 2].PutValue(2021);
worksheet.Cells[6, 3].PutValue(60);
worksheet.Cells[7, 0].PutValue("Vegetable");
worksheet.Cells[7, 1].PutValue("Daikon");
worksheet.Cells[7, 2].PutValue(2020);
worksheet.Cells[7, 3].PutValue(40);
worksheet.Cells[8, 0].PutValue("Vegetable");
worksheet.Cells[8, 1].PutValue("Daikon");
worksheet.Cells[8, 2].PutValue(2021);
worksheet.Cells[8, 3].PutValue(45);
int pivotIndex = worksheet.PivotTables.Add("A1:D9", "F3", "PivotTable1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];
pivotTable.AddFieldToArea(PivotFieldType.Row, "Category");
pivotTable.AddFieldToArea(PivotFieldType.Row, "Item");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
PivotField categoryField = pivotTable.RowFields[0];
categoryField.SetSubtotals(PivotFieldSubtotalType.Automatic, true);
pivotTable.CalculateData();
workbook.Save("output_automatic.xlsx");
```

## **Scénario 2 — Suppression de tous les sous-totaux (None)**
Appeler `SetSubtotals(PivotFieldSubtotalType.None, true)` supprime toutes les lignes de sous-total du tableau croisé dynamique, ne laissant que les lignes de champ et le total général en bas. Cela est utile lorsque vous souhaitez obtenir les données groupées brutes sans aucune ligne de résumé.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Name = "Data";
string[] headers = { "Category", "Item", "Year", "Amount" };
for (int j = 0; j < headers.Length; j++)
{
    worksheet.Cells[0, j].PutValue(headers[j]);
}
object[,] data = {
    { "Fruit",     "Apple",  2020, 100 },
    { "Fruit",     "Apple",  2021, 150 },
    { "Fruit",     "Banana", 2020, 80  },
    { "Fruit",     "Banana", 2021, 90  },
    { "Vegetable", "Carrot", 2020, 50  },
    { "Vegetable", "Carrot", 2021, 60  },
    { "Vegetable", "Daikon", 2020, 40  },
    { "Vegetable", "Daikon", 2021, 45  }
};
for (int i = 0; i < data.GetLength(0); i++)
{
    for (int j = 0; j < data.GetLength(1); j++)
    {
        worksheet.Cells[i + 1, j].PutValue(data[i, j]);
    }
}
int pivotIndex = worksheet.PivotTables.Add("A1:D9", "F3", "PivotTable1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];
pivotTable.AddFieldToArea(PivotFieldType.Row, "Category");
pivotTable.AddFieldToArea(PivotFieldType.Row, "Item");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
PivotField categoryField = pivotTable.RowFields[0];
categoryField.SetSubtotals(PivotFieldSubtotalType.None, true);
pivotTable.CalculateData();
workbook.Save("output_none.xlsx");
```

## **Scénario 3 — Sous-ensemble personnalisé de sous-totaux (Sum + Average)**
Vous n'êtes pas limité à un seul type de sous-total. Chaque appel à `SetSubtotals` opère indépendamment sur un seul type, donc appeler la méthode deux fois — une fois avec `Sum` et une fois avec `Average` — produit un sous-ensemble personnalisé de deux lignes de sous-total pour chaque groupe `Category`.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Name = "Data";
worksheet.Cells["A1"].PutValue("Category");
worksheet.Cells["B1"].PutValue("Item");
worksheet.Cells["C1"].PutValue("Year");
worksheet.Cells["D1"].PutValue("Amount");
worksheet.Cells[1, 0].PutValue("Fruit");
worksheet.Cells[1, 1].PutValue("Apple");
worksheet.Cells[1, 2].PutValue(2020);
worksheet.Cells[1, 3].PutValue(100);
worksheet.Cells[2, 0].PutValue("Fruit");
worksheet.Cells[2, 1].PutValue("Apple");
worksheet.Cells[2, 2].PutValue(2021);
worksheet.Cells[2, 3].PutValue(150);
worksheet.Cells[3, 0].PutValue("Fruit");
worksheet.Cells[3, 1].PutValue("Banana");
worksheet.Cells[3, 2].PutValue(2020);
worksheet.Cells[3, 3].PutValue(80);
worksheet.Cells[4, 0].PutValue("Fruit");
worksheet.Cells[4, 1].PutValue("Banana");
worksheet.Cells[4, 2].PutValue(2021);
worksheet.Cells[4, 3].PutValue(90);
worksheet.Cells[5, 0].PutValue("Vegetable");
worksheet.Cells[5, 1].PutValue("Carrot");
worksheet.Cells[5, 2].PutValue(2020);
worksheet.Cells[5, 3].PutValue(50);
worksheet.Cells[6, 0].PutValue("Vegetable");
worksheet.Cells[6, 1].PutValue("Carrot");
worksheet.Cells[6, 2].PutValue(2021);
worksheet.Cells[6, 3].PutValue(60);
worksheet.Cells[7, 0].PutValue("Vegetable");
worksheet.Cells[7, 1].PutValue("Daikon");
worksheet.Cells[7, 2].PutValue(2020);
worksheet.Cells[7, 3].PutValue(40);
worksheet.Cells[8, 0].PutValue("Vegetable");
worksheet.Cells[8, 1].PutValue("Daikon");
worksheet.Cells[8, 2].PutValue(2021);
worksheet.Cells[8, 3].PutValue(45);
PivotTableCollection pivotTables = worksheet.PivotTables;
int pivotIndex = pivotTables.Add("A1:D9", "F3", "PivotTable1");
PivotTable pivotTable = pivotTables[pivotIndex];
pivotTable.AddFieldToArea(PivotFieldType.Row, "Category");
pivotTable.AddFieldToArea(PivotFieldType.Row, "Item");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
PivotField categoryField = pivotTable.RowFields[0];
categoryField.SetSubtotals(PivotFieldSubtotalType.Sum, true);
categoryField.SetSubtotals(PivotFieldSubtotalType.Average, true);
pivotTable.CalculateData();
workbook.Save("output_custom.xlsx");
```

## **Récapitulatif**

## **Articles connexes**
- [Champs de page dans les tableaux croisés dynamiques](/cells/fr/net/add-page-field-in-pivot-table/)
- [Actualisation des tableaux croisés dynamiques dans Aspose.Cells for .NET](/cells/fr/net/refresh-pivot-table/)
- [Application de styles aux tableaux croisés dynamiques](/cells/fr/net/apply-style-to-pivot-table/)

{{< app/cells/assistant language="csharp" >}}