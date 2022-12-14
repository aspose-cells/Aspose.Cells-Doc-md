---
title: Aspose.Cells för Java 8.1.2 Release Notes
type: docs
weight: 30
url: /sv/java/aspose-cells-for-java-8-1-2-release-notes/
---
{{% alert color="primary" %}} 

 Den här sidan innehåller release notes för[Aspose.Cells för Java 8.1.2](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-8.1.2/)

{{% /alert %}} 

 Aspose.Cells för Java har uppdaterats till version 8.1.2 och vi är glada att kunna meddela att denna utgåva innehåller över 20 nya användbara förbättringar.
Med Aspose.Cells för Java kan du arbeta med XLS, SpreadsheetML, OOXML, XLSB, CSV, HTML, ODS, PDF, XPS och andra format i dina applikationer. Du kan också generera, ändra, konvertera, rendera och skriva ut arbetsböcker utan att använda Microsoft Excel.
Besök dokumentationen för att lära dig hur du kommer igång med Aspose.Cells för Java.
Observera att den här nedladdningen innehåller en fullt fungerande version av produkten, men utan en licensuppsättning kommer den att köras i utvärderingsläge med vissa begränsningar. För att testa Aspose.Cells utan dessa utvärderingsbegränsningar kan du begära en gratis 30-dagars tillfällig licens.
 Följande är en lista över ändringar i denna version av Aspose.Cells för Java.

\1) Aspose.Cells

Andra förbättringar och förändringar

Nya egenskaper

(CELLSJAVA-40875) - Få varningar för teckensnittsersättning när du renderar kalkylblad

Förbättringar

(CELLSJAVA-40900) - Obfuskering av offentliga API-metoder
(CELLSJAVA-40891) - Processen hänger sig när ett fullständigt skadat kalkylblad laddas
(CELLSJAVA-40883) - Problem med datumformat vid import av CSV
(CELLSJAVA-40872) - arbetsblad.getCells().importResultSet, tid från datumkolumnen är alltid 00:00

Buggar

(CELLSJAVA-40866) - Konvertering till HTML respekterar inte ImageFormat i SaveOptions
(CELLSJAVA-40854) - HtmlHiddenRowDisplayType.HIDDEN får cellerna att skifta i resulterande HTML (spanning problem)
(CELLSJAVA-40835) - Exportproblem med dolda kolumner i den renderade HTML-filen
(CELLSJAVA-40879) - Problem med att skapa bild av dataområdet (ark till bild)
(CELLSJAVA-40878) - Att ställa in vertikal och horisontell upplösning när du sparar kalkylark till Jpeg-bild träder inte i kraft
(CELLSJAVA-40877) - Excel till PDF - Dålig bildkvalitet renderad av Aspose Cells 8.xx
(CELLSJAVA-40910) - Bilder går förlorade när PDF renderas med PdfSaveOptions.setImageType(ImageFormat.getPng())
(CELLSJAVA-40907) - Datapunktsmarkörer saknas i diagrammet när en Excel-mall-fil sparas som HTML
(CELLSJAVA-40904) - Vissa diagram renderas inte bra till ut HTML-filformat
(CELLSJAVA-40899) - Data Trunked Issue i Sheet18
(CELLSJAVA-40898) - Data Trunked Issue i Sheet17
(CELLSJAVA-40886) - Seriemärken trasiga när en Excel-fil sparas på nytt
(CELLSJAVA-40885) - Diagramexport av saknad datapunktsform i utdatabildformatet
(CELLSJAVA-40869) - Ekvationer saknar glyfer och viss formaterad text är trunkerad i den renderade PDF-filen
(CELLSJAVA-40865) - Bilden är inte tydlig i utdata-pdf
(CELLSJAVA-40860) - Bubbelegenskaper ändrade i diagrammet när mallen XLSX-fil sparades på nytt
(CELLSJAVA-40859) - Bubbelegenskaper ändrade i diagrammet när mallen XLSX-fil sparades på nytt
(CELLSJAVA-40858) - Column100PercentStacked eller Bar label-egenskapen har förlorats
(CELLSJAVA-40817) - Bilden i utdata-pdf:n blir suddig
(CELLSJAVA-40880) - DateTime-typen upptäcks inte när ett DateTime-värde läggs till vid körning via Aspose.Cells
(CELLSJAVA-40851) - Bredden på formerna ändrade och andra formatering förlorade i den kopierade arbetsboken

Undantag

(CELLSJAVA-40901) - Undantag: "Fel i form till bild! " vid rendering till PDF-filformat


Public API och bakåtinkompatibla ändringar

Följande är en lista över eventuella ändringar som gjorts i det offentliga API:t som tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts i Aspose.Cells för Java. Om du har funderingar på någon av de listade ändringarna, vänligen ta upp det på Aspose.Cells supportforum.

Public WarningInfo, WarningType-klasser, IWarningCallback-gränssnitt och SaveOptions.WarningCallback, ImageOrPrintOptions.WarningCallback-egenskapen.
Stöder varningar när teckensnitt har ersatts.

Ta bort föråldrad PdfSaveOptions.ChartImageType-egenskap.


Notera
Eftersom kodbasen för Aspose.Cells för Java matchar koden för relevant .NET-version, ingår de flesta ändringar, förbättringar och korrigeringar som ingår i Aspose.Cells för .NET v8.1.2 också i denna Aspose.Cells för Java v8.1.2.
