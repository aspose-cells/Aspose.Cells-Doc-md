---
title: Uppdatera en slicer
linktitle: Uppdatera en slicer
type: docs
weight: 50
url: /sv/python-net/updating-slicer/
description: Lär dig hur du uppdaterar en slicer för att filtrera data i den länkade pivottabellen eller tabellen med Aspose.Cells for Python via .NET.
keywords: Aspose.Cells for Python Excel, Excel Python-bibliotek, Python uppdatera slicer utan Excel, filtrera pivottabell med slicer i Python, Slicer select_items, Slicer clear_filter.
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Möjliga användningsscenarier**
Att uppdatera en slicer innebär att filtrera data i pivottabellen eller tabellen som slicern är kopplad till. När du markerar eller avmarkerar slicerobjekt i Microsoft Excel beräknas den länkade pivottabellen eller tabellen om därefter. Med Aspose.Cells for Python via .NET behöver du inte iterera över slicer-cacheobjekten och uppdatera slicern manuellt — metoden [**Slicer.select_items(labels, append)**](https://reference.aspose.com/cells/python-net/aspose.cells.slicers/slicer/selectitems/) uppdaterar slicern och beräknar om den länkade pivottabellen eller tabellen direkt från filterobjekten:
- `Slicer.select_items(labels, append)` — markerar de angivna etiketterna och beräknar om den länkade pivottabellen eller tabellen. När `append` är `True` behålls de ursprungligen markerade etiketterna och de angivna etiketterna läggs till i urvalet; när `append` är `False` rensas alla ursprungliga markeringar och endast de angivna etiketterna förblir markerade.
- `Slicer.unselect_items(labels)` — avmarkerar en del av de för närvarande markerade objekten.
- `Slicer.clear_filter()` — tar bort filtret och markerar alla objekt.

{{% alert color="primary" %}}
Från och med Aspose.Cells for Python via .NET 26.10 blir egenskapen `SlicerCacheItem.selected` skrivskyddad och dess setter stöds inte längre. Använd metoderna `Slicer.select_items`, `Slicer.unselect_items` och `Slicer.clear_filter` istället för att sätta `SlicerCacheItem.selected` objekt för objekt.
{{% /alert %}}

## **Hur man uppdaterar en slicer med Excel-biblioteket Aspose.Cells for Python**
Följande exempelkod laddar [exempel-Excel-filen](67338475.xlsx) som innehåller en befintlig slicer som är kopplad till en pivottabell. Den markerar endast objekten "Blue" och "Pink" i slicern med `Slicer.select_items(labels, False)` — pivottabellen beräknas om direkt från filterobjekten, utan ett manuellt anrop av `Slicer.refresh()`. Därefter sparas arbetsboken som [utdata-Excel-filen](67338476.xlsx). Skärmbilden nedan visar effekten av exempelkoden på exempel-Excel-filen. Som du kan se på skärmbilden visar pivottabellen endast de filtrerade objekten.
![todo:image_alt_text](updating-slicer_1.png)

## **Exempelkod**
Ersätt den aktuella markeringen (endast de angivna etiketterna förblir markerade) och beräkna om den länkade pivottabellen eller tabellen:

```python
import aspose.cells as ac
# Load sample Excel file containing slicer.
workbook = ac.Workbook("sampleUpdatingSlicer.xlsx")
# Access first worksheet.
worksheet = workbook.worksheets[0]
# Access the first slicer inside the slicer collection.
slicer = worksheet.slicers[0]
# Select only "Blue" and "Pink"; the linked pivot table or table
# is recalculated directly from the filter items.
slicer.select_items(["Blue", "Pink"], False)
# Save the modified workbook.
workbook.save("out.xlsx")
```

Behåll de för närvarande markerade etiketterna och markera ytterligare objekt:

```python
# Keep the current selection and add "Red" to it.
slicer.select_items(["Red"], True)
```

Avmarkera en del av de markerade objekten:

```python
# Remove "Pink" from the current selection.
slicer.unselect_items(["Pink"])
```

Ta bort filtret (markera alla objekt):

```python
# Clear the filter; all slicer items become selected again.
slicer.clear_filter()
```

{{< app/cells/assistant language="python-net" >}}