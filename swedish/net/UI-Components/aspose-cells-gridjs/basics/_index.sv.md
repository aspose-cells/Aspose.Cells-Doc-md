---
title: Aspose.Cells.GridJs grunder
type: docs
weight: 250
url: /sv/net/aspose-cells-gridjs/basics/
---
## Grunderna i GridJs

 Aspose.Cells.GridJs är ett .NET standardbibliotek som tillåter användare att utveckla webbapplikationer för att visa/redigera kalkylblad snabbt och enkelt.

Aspose.Cells.GridJs stöder import av de populära filformaten för kalkylark (XLS, XLSX, XLSM, XLSB, CSV, SpreadsheetML, ODS).

Det tillåter också export av Excel-filer till PDF, HTML .etc. Nedan är de grundläggande processtegen för att utveckla en webbapplikation av GridJs.

- Implementera GridCacheForStream för att skriva din egen affärslogik för cachelagring.
- Ställ in en kontrollåtgärd för att hämta json från kalkylarksfilen. Du kan använda GridJsWorkbook.ImportExcelFile och GridJsWorkbook.ExportToJson API:er, GridJs lagrar automatiskt spridningsfilen i cache.
- Ställ in en kontrollåtgärd för att hämta json för uppdateringsåtgärden. Du kan använda GridJsWorkbook.UpdateCell API，GridJs kommer att utföra uppdateringsåtgärder i cachen och returnera den uppdaterade json.
- Ställ in en kontrollåtgärd för att få bilderna/formfilernas url i kalkylarket, GridJs kommer automatiskt att zippa alla bilder/former i cachen. Den kommer att använda GridCacheForStream.GetFileUrl API.
- Ställ in en kontrollåtgärd för att få filen i cache, så att vi kan få bilderna/formerna zip-filen eller kalkylarksfilen i cache. Den kommer att använda GridCacheForStream.LoadStream API.
- Ställ in en kontrollåtgärd för att ladda ner kalkylarket. Du kan använda GridJsWorkbook.SaveToCacheWithFileName API.

 Nedan finns en grundläggande demo för att visa användningen av Aspose.Cells.GridJs: https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Examples_GridJs

Om du har några frågor, krav eller behöver hjälp, vänligen återkoppla till följande webbplats https://forum.aspose.com/c/cells/9