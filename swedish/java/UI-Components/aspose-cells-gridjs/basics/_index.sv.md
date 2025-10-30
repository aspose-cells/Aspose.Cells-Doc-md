---
title: Aspose.Cells.GridJs grunderna
type: docs
weight: 250
url: /sv/net/aspose-cells-gridjs/basics/
keywords: GridJs
description: Den här artikeln introducerar de grundläggande stegen för att ställa in en webbapplikation för GridJs.
---

## GridJs-grunder

Aspose.Cells.GridJs är ett .NET-standardsbibliotek som låter användare utveckla webbapplikationer för att snabbt och enkelt visa/redigera kalkylblad. 

Aspose.Cells.GridJs stöder import av populära kalkylbladsfilformat (XLS, XLSX, XLSM, XLSB,  CSV, SpreadsheetML, ODS).

Det tillåter också export av Excel-filer till PDF, HTML etc. Nedan följer de grundläggande processstegen för att utveckla en webbapplikation för GridJs.

- Implementera GridCacheForStream för att skriva din egen affärslogik för cachestorage.
- Ställ in en kontrolleråtgärd för att hämta json från kalkylbladsfilen. Du kan använda GridJsWorkbook.ImportExcelFile och GridJsWorkbook.ExportToJson API:er, GridJs kommer automatiskt lagra spridfilen i cache.
- Ställ in en kontrolleråtgärd för att hämta json för uppdateringsoperationen. Du kan använda GridJsWorkbook.UpdateCell API, GridJs kommer att utföra uppdateringsoperationen i cachen och returnera den uppdaterade json.
- Ställ in en kontrolleråtgärd för att hämta bildernas/formernas filadress i kalkylarket. GridJs kommer automatiskt att komprimera alla bilderna/formerna i cachen. Den kommer att använda API:n GridCacheForStream.GetFileUrl.
- Ställ in en kontrolleråtgärd för att hämta filen i cachen, så att vi kan hämta zip-filen med bilderna/formerna eller kalkylarksfilen i cachen. Den kommer att använda API:n GridCacheForStream.LoadStream.
- Ställ in en kontrolleråtgärd för att ladda ner kalkylarket. Du kan använda API:n GridJsWorkbook.SaveToCacheWithFileName.

Nedan är en grundläggande demo för att visa användningen av Aspose.Cells.GridJs: https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/tree/master/Examples.GridJs


Om du har några frågor, krav eller behöver hjälp, var god kontakta följande webbplats https://forum.aspose.com/c/cells/9
