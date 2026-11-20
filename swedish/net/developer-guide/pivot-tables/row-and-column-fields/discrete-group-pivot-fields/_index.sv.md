---
title: Diskret gruppering av poster i pivotfält
linktitle: Diskret gruppering
description: Lär dig hur du grupperar poster i pivotfält till anpassade grupper med namn, till exempel frukt och grönsaker, med hjälp av DiscreteGroupItem och PivotFieldGroupOptions.DiscreteGroupItems i Aspose.Cells for .NET.
keywords: Aspose.Cells, pivottabell, diskret gruppering, DiscreteGroupItem, PivotFieldGroupOptions, gruppera poster i pivotfält, anpassade grupper, PivotField.Group, C#, Excel-pivottabell
type: docs
weight: 90
url: /sv/net/discrete-group-pivot-fields/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Möjliga användningsscenarier**
- Automatisk gruppering samlar in poster efter datatyp, till exempel datum till månader och kvartal eller tal till intervall. Diskret gruppering löser det motsatta problemet genom att samla in specifika, orelaterade poster i anpassade grupper med namn, exempelvis produkter till frukt och grönsaker, butiker till regioner eller konton till zoner. Aspose.Cells erbjuder diskret gruppering med hjälp av klassen `DiscreteGroupItem` och egenskapen `PivotFieldGroupOptions.DiscreteGroupItems`.
- En `DiscreteGroupItem` består av ett gruppnamn och de poster som tillhör det. Posterna kan identifieras på två sätt: antingen efter sina namn (`new DiscreteGroupItem("fruit", new string[] { "grape", "cherry" })`) eller efter sina nollbaserade positioner i källdatan (`new DiscreteGroupItem("fruit", new int[] { 0, 3 })`). Båda formerna ger samma resultat.
- Diskret gruppering tillämpas på ett fält i rad- eller kolumnområdet i pivottabellen genom att skicka grupperingsalternativet till `PivotField.Group(PivotFieldGroupOptions)`.

## **Gruppera poster i pivotfält efter namn**
Följande exempel bygger en liten försäljningslista (produkt, datum och belopp), skapar en pivottabell från den med `product` i radområdet, `date` i kolumnområdet och `amount` i dataområdet och definierar sedan två anpassade grupper efter namn: frukt (`grape`, `cherry`) och grönsaker (`carrot`, `potato`). Resultatet visar en layout med två nivåer i radområdet, där gruppnamnet utgör den yttre nivån och de ursprungliga posterna är nästlade under, så att trender kan utläsas för varje anpassad grupp och post.

```csharp
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook wb = new Workbook();
Worksheet sheet = wb.Worksheets[0];
Cells cells = sheet.Cells;
cells[0, 0].Value = "product";
cells[1, 0].Value = "grape";
cells[2, 0].Value = "carrot";
cells[3, 0].Value = "potato";
cells[4, 0].Value = "cherry";
Style dateStyle = wb.CreateStyle();
dateStyle.Custom = "m/d/yyyy";
cells[0, 1].Value = "date";
cells[1, 1].Value = new DateTime(2021, 2, 5);
cells[2, 1].Value = new DateTime(2022, 3, 8);
cells[3, 1].Value = new DateTime(2023, 4, 10);
cells[4, 1].Value = new DateTime(2024, 5, 16);
for (int r = 1; r <= 4; r++) cells[r, 1].SetStyle(dateStyle);
cells[0, 2].Value = "amount";
cells[1, 2].Value = 50;
cells[2, 2].Value = 60;
cells[3, 2].Value = 70;
cells[4, 2].Value = 80;
// Add a pivot table with the destination cell A12 (row 11, column 0)
PivotTable pivotTable = sheet.PivotTables.Add("=Sheet1!A1:C5", 11, 0);
pivotTable.AddFieldToArea(PivotFieldType.Row, "product");
pivotTable.AddFieldToArea(PivotFieldType.Column, "date");
pivotTable.AddFieldToArea(PivotFieldType.Data, "amount");
pivotTable.PivotTableStyleType = PivotTableStyleType.PivotTableStyleMedium10;
// Group specific items into custom groups by item names
DiscreteGroupItem fruit = new DiscreteGroupItem("fruit", new string[] { "grape", "cherry" });
DiscreteGroupItem vegetable = new DiscreteGroupItem("vegetable", new string[] { "carrot", "potato" });
PivotFieldGroupOptions groupOptions = new PivotFieldGroupOptions();
groupOptions.DiscreteGroupItems = new DiscreteGroupItem[] { fruit, vegetable };
pivotTable.RowFields[0].Group(groupOptions);
pivotTable.CalculateData();
wb.Save("outputDiscreteGroupPivotField.xlsx");
```

Efter `CalculateData()` visar pivottabellens radområde frukt (`grape` 50, `cherry` 80) och grönsak (`carrot` 60, `potato` 70) med totalsumman 260, och kolumnetiketterna behåller de fyra datumen (2/5/2021, 3/8/2022, 4/10/2023, 5/16/2024).

## **Gruppera poster i pivotfält efter index**
När postnamnen är långa eller lokaliserade identifierar den andra konstruktorvarianten av `DiscreteGroupItem` posterna efter index. Varje index är en nollbaserad position för en post i den ordning posterna förekommer i källdatan, inte i alfabetisk ordning. I dataexemplet ovan har `grape` index 0, `carrot` index 1, `potato` index 2 och `cherry` index 3, så fruktgruppen är `{ 0, 3 }` och grönsaksgruppen är `{ 1, 2 }`. Resultatet är identiskt med exemplet baserat på namn.

```csharp
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook wb = new Workbook();
Worksheet sheet = wb.Worksheets[0];
Cells cells = sheet.Cells;
cells[0, 0].Value = "product";
cells[1, 0].Value = "grape";
cells[2, 0].Value = "carrot";
cells[3, 0].Value = "potato";
cells[4, 0].Value = "cherry";
Style dateStyle = wb.CreateStyle();
dateStyle.Custom = "m/d/yyyy";
cells[0, 1].Value = "date";
cells[1, 1].Value = new DateTime(2021, 2, 5);
cells[2, 1].Value = new DateTime(2022, 3, 8);
cells[3, 1].Value = new DateTime(2023, 4, 10);
cells[4, 1].Value = new DateTime(2024, 5, 16);
for (int r = 1; r <= 4; r++) cells[r, 1].SetStyle(dateStyle);
cells[0, 2].Value = "amount";
cells[1, 2].Value = 50;
cells[2, 2].Value = 60;
cells[3, 2].Value = 70;
cells[4, 2].Value = 80;
// Add a pivot table with the destination cell A12 (row 11, column 0)
PivotTable pivotTable = sheet.PivotTables.Add("=Sheet1!A1:C5", 11, 0);
pivotTable.AddFieldToArea(PivotFieldType.Row, "product");
pivotTable.AddFieldToArea(PivotFieldType.Column, "date");
pivotTable.AddFieldToArea(PivotFieldType.Data, "amount");
pivotTable.PivotTableStyleType = PivotTableStyleType.PivotTableStyleMedium10;
// grape is item 0, carrot is item 1, potato is item 2, cherry is item 3
// (zero-based positions in the order the items appear in the source data)
DiscreteGroupItem fruit = new DiscreteGroupItem("fruit", new int[] { 0, 3 });
DiscreteGroupItem vegetable = new DiscreteGroupItem("vegetable", new int[] { 1, 2 });
PivotFieldGroupOptions groupOptions = new PivotFieldGroupOptions();
groupOptions.DiscreteGroupItems = new DiscreteGroupItem[] { fruit, vegetable };
pivotTable.RowFields[0].Group(groupOptions);
pivotTable.CalculateData();
wb.Save("outputDiscreteGroupPivotFieldByIndex.xlsx");
```

## **Obs!**

{{% alert color="primary" %}}
- Poster som inte tilldelas någon anpassad grupp försvinner inte. De stannar i pivottabellen på samma nivå som de anpassade grupperna och visas var för sig som enskilda poster. I exemplet ovan, där endast fruktgruppen definieras, visas `carrot` och `potato` som fristående poster i radområdet bredvid fruktgruppen.
- Egenskapen `PivotFieldGroupOptions.NewPivotField` styr layouten för diskret gruppering. Standardvärdet är `true`, vilket lägger till det grupperade fältet som ett nytt yttre fält bredvid det ursprungliga fältet och skapar den layout med två nivåer som visas ovan (`RowFields` växer till 2). Ställ in egenskapen på `false` för att i stället ersätta det ursprungliga fältet. Då visar radområdet en enda nivå med endast gruppnamnen och deras aggregerade värden: frukt 130 (50 + 80) och grönsak 130 (60 + 70).
- De namn- och indexbaserade konstruktorvarianterna av `DiscreteGroupItem` kan kombineras inom samma `DiscreteGroupItems`-array.
{{% /alert %}}

## **Relaterade artiklar**
- [Gruppera pivotfält i pivottabellen](/cells/sv/net/group-pivot-fields-in-the-pivot-table/)
- [Lägg till rad- och kolumnfält i pivottabellen](/cells/sv/net/pivot-table-add-row-and-column-fields/)
- [Filtrera pivottabeller efter etikett eller värde](/cells/sv/net/filter-by-label-or-value-of-pivot-table/)
- [Tillämpa format på pivottabellen](/cells/sv/net/apply-style-to-pivot-table/)
- [Uppdatera pivottabellen](/cells/sv/net/refresh-pivot-table/)

{{< app/cells/assistant language="csharp" >}}