---
title: Aspose.Cells för Java 8.2.1 Release Notes
type: docs
weight: 20
url: /sv/java/aspose-cells-for-java-8-2-1-release-notes/
---
{{% alert color="primary" %}} 

 Den här sidan innehåller release notes för[Aspose.Cells för Java 8.2.1](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-8.2.1/)

{{% /alert %}} 

 Aspose.Cells för Java har uppdaterats till version 8.2.1 och vi är glada att kunna meddela att denna utgåva innehåller över 30 nya användbara förbättringar.
Med Aspose.Cells för Java kan du arbeta med XLS, SpreadsheetML, OOXML, XLSB, CSV, HTML, ODS, PDF, XPS och andra format i dina applikationer. Du kan också generera, ändra, konvertera, rendera och skriva ut arbetsböcker utan att använda Microsoft Excel.
Besök dokumentationen för att lära dig hur du kommer igång med Aspose.Cells för Java.
Observera att den här nedladdningen innehåller en fullt fungerande version av produkten, men utan en licensuppsättning kommer den att köras i utvärderingsläge med vissa begränsningar. För att testa Aspose.Cells utan dessa utvärderingsbegränsningar kan du begära en gratis 30-dagars tillfällig licens.
 Följande är en lista över ändringar i denna version av Aspose.Cells för Java.

\1) Aspose.Cells

Andra förbättringar och förändringar

Nya egenskaper

(CELLSJAVA-40955) - Forma absolut positionering
(CELLSJAVA-40943) - Lägg till ett alternativ till PasteOptions för att bara klistra in synliga celler från intervallet

Buggar

(CELLSJAVA-40977) - Villkorlig formatering fungerar inte när Excel-fil konverteras till HTML
(CELLSJAVA-40959) - Extra align-attribut i HTML-utdata.
(CELLSJAVA-40954) - Kolumner matchar inte i HTML-utdata
(CELLSJAVA-40953) - Vissa cellkanter förlängdes lite när Excel konverterades till html
(CELLSJAVA-40980) - Länkat cellvärde uppdateras inte från den externa arbetsboken
(CELLSJAVA-40957) - Skydda arbetsblad i licensierat läge gör att MS Excel kraschar vid förhandsgranskning
(CELLSJAVA-40956) - Chart.getName() returnerar fel diagramnamn
(CELLSJAVA-40952) - Series.hasLeaderLines() returnerar inte korrekt värde
(CELLSJAVA-40944) - Inbäddad PDF blir skadad efter sammanslagning av arbetsböcker
(CELLSJAVA-40979) - Vissa rutor är fästa på dataetiketter i cirkeldiagrammet i den renderade PDF-filen
(CELLSJAVA-40975) - XLSX till Jpeg-konvertering - Prestanda
(CELLSJAVA-40973) - Inaktivera setExtractContentPermission - alternativet "Tillstånd att kopiera eller extrahera innehåll" fungerar inte
(CELLSJAVA-40965) - Cells stöter på varandra i PDF:en
(CELLSJAVA-40962) - Aspose.Cells återger #N/A-värdet annorlunda än MS Excel
(CELLSJAVA-40926) - Bordskanten är normal istället för fet vid 100 % zoom
(CELLSJAVA-40833) - Bildkvaliteten på diagrammet är låg - Konvertering från diagram till bild
(CELLSJAVA-40949) - Horisontell axel visas inte i diagrambilden
(CELLSJAVA-40948) - Anpassad bild i datapunkter visas inte i diagrambild
(CELLSJAVA-40947) - Kinesiska tecken visas inte i diagrambilden
(CELLSJAVA-40946) - Dataetiketter är i fel position inuti sjökortsbilden
(CELLSJAVA-40821) - Textruta saknas när diagrammet sparas som EMF med ToImage
(CELLSJAVA-40819) - Fel axelvärden när diagram sparas som EMF med ToImage
(CELLSJAVA-40818) - Saknad axeltitel när diagram sparas som EMF med hjälp av ToImage
(CELLSJAVA-40830) - Inverterat z-index i staplat område och stapeldiagram vid export till PDF

Undantag

(CELLSJAVA-40985) - CellsException: Slutet på filen nås på Workbook.save
(CELLSJAVA-40983) - java.lang.NullPointerException på Workbook.save
(CELLSJAVA-40981) - Aspose.Cells kan inte läsa lösenordsskyddade Excel 2013-filer
(CELLSJAVA-40976) - Sparkline kommer att kasta NullPointerException när du använder insertRows
(CELLSJAVA-40969) - Undantag: "java.lang.StringIndexOutOfBoundsException: Stringindex utanför intervallet" vid uppdatering av en Shapes värde
(CELLSJAVA-40967) - Kan inte casta till LineShape

Public API och bakåtinkompatibla ändringar

Följande är en lista över eventuella ändringar som gjorts i det offentliga API:t som tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts i Aspose.Cells för Java. Om du har funderingar på någon av de listade ändringarna, vänligen ta upp det på Aspose.Cells supportforum.

 Lägger till metoden Cell.GetValidation().
Får valideringen som gäller för cellen.

 Lägger till metoden Cell.GetValidationValue().
Indikerar om cellens värde är giltigt.

 Lägger till metoden WorkbookRender.ToPrinter(PrinterSettings PrinterSettings).
Återge arbetsbok till skrivare via PrinterSettings.


Notera
Eftersom kodbasen för Aspose.Cells för Java matchar koden för relevant .NET-version, ingår de flesta ändringar, förbättringar och korrigeringar som ingår i Aspose.Cells för .NET v8.2.1 också i denna Aspose.Cells för Java v8.2.1.
