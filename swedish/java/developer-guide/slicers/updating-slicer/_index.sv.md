---
title: Uppdatera en slicer
linktitle: Uppdatera en slicer
type: docs
weight: 50
url: /sv/java/updating-slicer/
description: Den här artikeln visar hur man uppdaterar en slicer för att filtrera data i den länkade pivottabellen eller tabellen med hjälp av Aspose.Cells for Java API.
keywords: Aspose.Cells Java Uppdatera slicer, Java hur man ändrar slicern, hur man filtrerar en pivottabell med slicer i Java, Java Slicer selectItems, Java Slicer clearFilter, Java Slicer unselectItems.
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Möjliga användningsscenarier**
Att uppdatera en slicer innebär att filtrera data i pivottabellen eller tabellen som slicern är kopplad till. När du markerar eller avmarkerar slicerobjekt i Microsoft Excel beräknas den länkade pivottabellen eller tabellen om därefter. Med Aspose.Cells for Java behöver du inte iterera över slicer-cacheobjekten och uppdatera slicern manuellt — metoden [Slicer.selectItems(String[], boolean)](https://reference.aspose.com/cells/java/com.aspose.cells/slicer/#selectItems-java.lang.String---boolean-) uppdaterar slicern och beräknar om den länkade pivottabellen eller tabellen direkt från filterobjekten:
- `Slicer.selectItems(labels, append)` — markerar de angivna etiketterna och beräknar om den länkade pivottabellen eller tabellen. När `append` är `true` behålls de ursprungligen markerade etiketterna och de angivna etiketterna läggs till i urvalet; när `append` är `false` rensas alla ursprungliga markeringar och endast de angivna etiketterna förblir markerade.
- `Slicer.unselectItems(labels)` — avmarkerar en del av de för närvarande markerade objekten.
- `Slicer.clearFilter()` — tar bort filtret och markerar alla objekt.

{{% alert color="primary" %}}
Från och med Aspose.Cells for Java 26.10 blir egenskapen `SlicerCacheItem.Selected` skrivskyddad och dess setter stöds inte längre. Använd metoderna `Slicer.selectItems`, `Slicer.unselectItems` och `Slicer.clearFilter` istället för att sätta `SlicerCacheItem.Selected` objekt för objekt.
{{% /alert %}}

## **Uppdatera en slicer**
Följande exempelkod laddar [exempel-Excel-filen](67338506.xlsx) som innehåller en befintlig slicer som är kopplad till en pivottabell. Den markerar endast objekten "Blue" och "Pink" i slicern med `Slicer.selectItems(labels, false)` — pivottabellen beräknas om direkt från filterobjekten, utan ett manuellt anrop av `Slicer.refresh()`. Därefter sparas arbetsboken som [utdata-Excel-filen](67338505.xlsx). Skärmbilden nedan visar effekten av exempelkoden på exempel-Excel-filen. Som du kan se på skärmbilden visar pivottabellen endast de filtrerade objekten.
![todo:image_alt_text](updating-slicer_1.png)

## **Exempelkod**
Ersätt den aktuella markeringen (endast de angivna etiketterna förblir markerade) och beräkna om den länkade pivottabellen eller tabellen:

```java
import com.aspose.cells.Workbook;
import com.aspose.cells.Worksheet;
import com.aspose.cells.Slicer;
// Load sample Excel file containing slicer.
Workbook workbook = new Workbook("sampleUpdatingSlicer.xlsx");
// Access first worksheet.
Worksheet worksheet = workbook.getWorksheets().get(0);
// Access the first slicer inside the slicer collection.
Slicer slicer = worksheet.getSlicers().get(0);
// Select only "Blue" and "Pink"; the linked pivot table or table
// is recalculated directly from the filter items.
slicer.selectItems(new String[] { "Blue", "Pink" }, false);
// Save the modified workbook.
workbook.save("out.xlsx");
```

Behåll de för närvarande markerade etiketterna och markera ytterligare objekt:

```java
// Keep the current selection and add "Red" to it.
slicer.selectItems(new String[] { "Red" }, true);
```

Avmarkera en del av de markerade objekten:

```java
// Remove "Pink" from the current selection.
slicer.unselectItems(new String[] { "Pink" });
```

Ta bort filtret (markera alla objekt):

```java
// Clear the filter; all slicer items become selected again.
slicer.clearFilter();
```

{{< app/cells/assistant language="java" >}}