---
title: Aspose.Cells för .NET 8.6.0 Release Notes
type: docs
weight: 40
url: /sv/net/aspose-cells-for-net-8-6-0-release-notes/
---
{{% alert color="primary" %}} 

 Den här sidan innehåller release notes för[Aspose.Cells för .NET 8.6.0](https://downloads.aspose.com/cells/net/new-releases/aspose.cells-for-.net-8.6.0/)

{{% /alert %}} 

 Följande är en lista över förbättringar och ändringar i denna version av Aspose.Cells



\1) Aspose.Cells 


## **Andra förbättringar och förändringar**

## **Nya egenskaper**


 (CELLSNET-43880) - Tilldela makro för att bilda kontroller


## **Förbättringar**


 (CELLSNET-43832) - Worksheet.Shapes.UpdateSelectedValue kastar CellsException ibland

 (CELLSNET-43823) - Att inkludera en teckensnittskatalog med CellsHelper verkar inte fungera

 (CELLSNET-43900) - Hyperlink.TextToDisplay uppdateras inte

 (CELLSNET-43892) - XLSX-dokumentstorleken ökar för varje lagring

 (CELLSNET-43869) - Aspose.Cells kan inte köras i Medium Trust


## **Buggar**


(CELLSNET-43884) - Wingdings-symboler återges inte korrekt när vissa kalkylblad konverteras till HTML

 (CELLSNET-43877) - Excel reparerar alltid det resulterande kalkylarket efter att ha lagt till pivottabellen

 (CELLSNET-43831) - HTML till Excel - CSS-styling ignoreras

 (CELLSNET-43750) - Diagramändringar i det resulterande kalkylbladet efter att ha uppdaterat diagrammet

 (CELLSNET-43843) - Arbetsbok.CalculateFormula återkommer aldrig

 (CELLSNET-43842) - Aspose.Cells Radinsättningsfel

 (CELLSNET-43879) - tecken överlappade och konverterades till ######## i Excel till PDF-rendering

 (CELLSNET-43854) - Upphöjd och nedsänkt skiftade upp för mycket när bilden genererades

 (CELLSNET-42762) - Sjökortsaxeletiketter återges i ojämn text

 (CELLSNET-42384) - WordArt-lådor försvinner när XLSX konverteras till PDF

 (CELLSNET-42380) - SmartArt-lådor kommer som svarta.

 (CELLSNET-42377) - SmartArt-layoutrubrik överlappar med understrykning under bildrubrik.

(CELLSNET-41493) - Texten trunkeras/lindas in i den genererade PDF-filen

 (CELLSNET-41398) - Kalkylarksdokument producerar flera dokument när de konverteras

 (CELLSNET-43894) - OLE-länk ObjectSourceFullName kunde inte uppdateras

 (CELLSNET-43882) - PageSetup.Zoom har ändrats efter att ha öppnat och sparat arbetsboken

 (CELLSNET-43881) - Vissa cellformler går förlorade när raden kopieras

 (CELLSNET-43876) - Dubbelläsning av linjematningar för vagnretur

 (CELLSNET-43864) - Att kombinera två XLSM-arbetsböcker ger en skadad arbetsbok

 (CELLSNET-43839) - Bilder i kalkylarket återges inte vid konvertering till PDF

 (CELLSNET-43837) - Länkad bild finns inte i diagrammet efter att ha instansierat Workbook-objektet och sparat det

 (CELLSNET-43836) - Range.CopyData fungerar men Range.Copy fungerar inte

 (CELLSNET-43830) - Lägga till mer än 2084 tecken i hyperlänken förstör utdatafilen xlsx

 (CELLSNET-43829) - Excel-funktion renderas med #NAME? fel på blad 1


## **Undantag**


(CELLSNET-43866) - CellsException vid rendering av ett kalkylblad till PDF

 (CELLSNET-43847) - Undantag uppstår när man försöker anropa RefreshPivotTables

 (CELLSNET-43852) - CellsException at Workbook.CalculateFormula

 (CELLSNET-43893) - CellsException när ett kalkylblad renderas till PDF-format

 (CELLSNET-42108) - CellsException: Parametern är inte giltig: vid konvertering av XLS till PDF

 (CELLSNET-43835) - System.OutOfMemoryException vid konvertering av en XLS-fil till PDF-filformat

 (CELLSNET-43865) - ArgumentException vid rendering av kalkylblad till PDF och HTML

 (CELLSNET-43862) - NullReferenceException vid Workbook.Save



\2) Aspose.Cells Grid Suite


## **Andra förbättringar och förändringar**

## **Buggar**


 (CELLSNET-43875) - Gridweb Print på Chrome fungerar inte korrekt


## **Public API och bakåtinkompatibla ändringar**


Följande är en lista över eventuella ändringar som gjorts i det offentliga API:t, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts i Aspose.Cells för .NET. Om du har funderingar på någon av de listade ändringarna, vänligen ta upp det på Aspose.Cells supportforum.



 Lägger till WorkbookMetadata namnutrymme och klasser.

 Den är van vid att läsa och spara metadata för filen.



 Lägger till HtmlSaveOptions. Egenskapen ExportFrameScriptsAndProperties

Anger om ramskript och dokumentegenskaper exporteras. Standardvärdet är sant.



 Lägger till egenskapen Shape.MarcoName

 Det används för att hämta och ställa in namnet på makrot.



 Lägger till egenskapen OoxmlSaveOptions.UpdateZoom

 Den används för att uppdatera PageSetup.Zoom om egenskaperna PageSetup.FitToPagesWide och PageSetup.FitToPagesTall styr hur kalkylbladet skalas.


