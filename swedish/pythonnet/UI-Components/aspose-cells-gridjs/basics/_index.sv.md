---
title: Aspose.Cells.GridJs grunderna
type: docs
weight: 250
url: /sv/python-net/aspose-cells-gridjs/basics/
keywords: gridjs,python,edit,spreadsheet,view,viewer,editor,excel
---

## GridJs-grunder

Aspose.Cells.GridJs är en bibliotek som låter användare utveckla plattformsoberoende webbapplikationer för att snabbt och enkelt visa eller redigera kalkylbladsfiler. 

## Varför använda Aspose.Cells.GridJs


- Det möjliggör för användare att skapa, redigera, formatera, samarbeta och säkert dela kalkylblad med realtidsuppdateringar, formelstöd och verktyg för rik datavisualisering, liknande traditionella skrivbordsapplikationer.
- Det stöder datainmatning och redigering, formatering, kalkylbladsnavigering, formelberäkning, datamanipulering, diagram och visualisering, import och export, säkerhet, tillägg och anpassning för utvecklare att anpassa editorn till specifika affärsbehov.

## Funktioner


- Importera, visa och redigera de populära kalkylbladsformaten.
- Exportera kalkylbladen till olika stödda filformat.
- Visa och hantera bild eller form eller diagramfiler.
- Utför rutnätsdesign och layoutanpassning.
- Hantering av flera kalkylblad.
- Skapa och beräkna Excel®-formler.

## Stödda filformat

https://docs.aspose.com/cells/python-net/supported-file-formats/

## Allmän användning

Nedan följer de grundläggande processstegen för att utveckla en webbapplikation för GridJs.

- Ange cachestorage-katalog genom att Config.set_file_cache_directory(`din lagringsväg`)
- Ange licens genom Config.set_license(`din licensväg`)
- Ange bildrutt-URL GridJsWorkbook.set_image_url_base(`rutnamn för att visa bild`);
- Ställ in en routeaction för att hämta `json` från kalkylbladsfilen. Du kan använda GridJsWorkbook.ImportExcelFile och GridJsWorkbook.ExportToJson API och GridJs kommer automatiskt lagra spridningsfilen i cachen.
- Ställ in en routeaction för att hämta `json` för uppdateringsoperationen. Du kan använda `GridJsWorkbook.UpdateCell` `API, GridJs kommer göra uppdateringsoperationen i cachen och returnera den uppdaterade `json`.
- Ställ in en routeaction för att hämta filen i cachen, så kan vi få bilderna/formerna zip-fil eller kalkylbladsfilen i cachen.
- Ställ in en routeaction för att ladda ner kalkylbladet. Du kan använda `GridJsWorkbook.SaveToCacheWithFileName` API.

Nedan följer en grundläggande demo för att visa användningen av Aspose.Cells.GridJs :

https://github.com/aspose-cells/Aspose.Cells.Grid-for-Python-via-.NET/tree/main/Examples.GridJs

I demot använder vi [gridjs-spreadsheet](https://www.npmjs.com/package/gridjs-spreadsheet) för att rendera sidan på klientens sida.

Om du har några frågor, krav eller behöver hjälp, var god kontakta följande webbplats https://forum.aspose.com/c/cells/9
