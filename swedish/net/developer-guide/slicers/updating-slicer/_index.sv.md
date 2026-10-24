---
title: Uppdatera en slicer
linktitle: Uppdatera en slicer
type: docs
weight: 50
url: /sv/net/updating-slicer/
description: Den här artikeln visar hur man uppdaterar en slicer för att filtrera data i den länkade pivottabellen eller tabellen med hjälp av Aspose.Cells for .NET API.
keywords: Aspose.Cells C# Uppdatera slicer, C# hur man ändrar slicern, hur man filtrerar en pivottabell med slicer i C#, C# Slicer SelectItems, C# Slicer ClearFilter, C# Slicer UnselectItems.
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Möjliga användningsscenarier**
Att uppdatera en slicer innebär att filtrera data i pivottabellen eller tabellen som slicern är kopplad till. När du markerar eller avmarkerar slicerobjekt i Microsoft Excel beräknas den länkade pivottabellen eller tabellen om därefter. Med Aspose.Cells for .NET behöver du inte iterera över slicer-cacheobjekten och uppdatera slicern manuellt — metoden [**Slicer.SelectItems(string[], bool)**](https://reference.aspose.com/cells/net/aspose.cells.slicers/slicer/selectitems/) uppdaterar slicern och beräknar om den länkade pivottabellen eller tabellen direkt från filterobjekten:
- `Slicer.SelectItems(labels, append)` — markerar de angivna etiketterna och beräknar om den länkade pivottabellen eller tabellen. När `append` är `true` behålls de ursprungligen markerade etiketterna och de angivna etiketterna läggs till i urvalet; när `append` är `false` rensas alla ursprungliga markeringar och endast de angivna etiketterna förblir markerade.
- `Slicer.UnselectItems(labels)` — avmarkerar en del av de för närvarande markerade objekten.
- `Slicer.ClearFilter()` — tar bort filtret och markerar alla objekt.

{{% alert color="primary" %}}
Från och med Aspose.Cells for .NET 26.10 blir egenskapen `SlicerCacheItem.Selected` skrivskyddad och dess setter stöds inte längre. Använd metoderna `Slicer.SelectItems`, `Slicer.UnselectItems` och `Slicer.ClearFilter` istället för att sätta `SlicerCacheItem.Selected` objekt för objekt.
{{% /alert %}}

## **Hur man uppdaterar en slicer**
Följande exempelkod laddar [exempel-Excel-filen](67338475.xlsx) som innehåller en befintlig slicer som är kopplad till en pivottabell. Den markerar endast objekten "Blue" och "Pink" i slicern med `Slicer.SelectItems(labels, false)` — pivottabellen beräknas om direkt från filterobjekten, utan ett manuellt anrop av `Slicer.Refresh()`. Därefter sparas arbetsboken som [utdata-Excel-filen](67338476.xlsx). Skärmbilden nedan visar effekten av exempelkoden på exempel-Excel-filen. Som du kan se på skärmbilden visar pivottabellen endast de filtrerade objekten.
![todo:image_alt_text](updating-slicer_1.png)

## **Exempelkod**
Ersätt den aktuella markeringen (endast de angivna etiketterna förblir markerade) och beräkna om den länkade pivottabellen eller tabellen:

```csharp
using Aspose.Cells;
using Aspose.Cells.Slicers;
// Load sample Excel file containing slicer.
Workbook workbook = new Workbook("sampleUpdatingSlicer.xlsx");
// Access first worksheet.
Worksheet worksheet = workbook.Worksheets[0];
// Access the first slicer inside the slicer collection.
Slicer slicer = worksheet.Slicers[0];
// Select only "Blue" and "Pink"; the linked pivot table or table
// is recalculated directly from the filter items.
slicer.SelectItems(new string[] { "Blue", "Pink" }, false);
// Save the modified workbook.
workbook.Save("out.xlsx");
```

Behåll de för närvarande markerade etiketterna och markera ytterligare objekt:

```csharp
// Keep the current selection and add "Red" to it.
slicer.SelectItems(new string[] { "Red" }, true);
```

Avmarkera en del av de markerade objekten:

```csharp
// Remove "Pink" from the current selection.
slicer.UnselectItems(new string[] { "Pink" });
```

Ta bort filtret (markera alla objekt):

```csharp
// Clear the filter; all slicer items become selected again.
slicer.ClearFilter();
```

{{< app/cells/assistant language="csharp" >}}