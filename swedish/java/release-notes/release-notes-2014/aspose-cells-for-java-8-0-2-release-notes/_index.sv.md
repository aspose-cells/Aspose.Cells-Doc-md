---
title: Aspose.Cells för Java 8.0.2 Release Notes
type: docs
weight: 60
url: /sv/java/aspose-cells-for-java-8-0-2-release-notes/
---
{{% alert color="primary" %}} 

 Den här sidan innehåller release notes för[Aspose.Cells för Java 8.0.2](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-8.0.2/)

{{% /alert %}} 

 Aspose.Cells för Java har uppdaterats till version 8.0.2 och vi är glada att kunna meddela att denna utgåva innehåller över 10 nya användbara förbättringar.
Med Aspose.Cells för Java kan du arbeta med XLS, SpreadsheetML, OOXML, XLSB, CSV, HTML, ODS, PDF, XPS och andra format i dina applikationer. Du kan också generera, ändra, konvertera, rendera och skriva ut arbetsböcker utan att använda Microsoft Excel.
Besök dokumentationen för att lära dig hur du kommer igång med Aspose.Cells för Java.
Observera att den här nedladdningen innehåller en fullt fungerande version av produkten, men utan en licensuppsättning kommer den att köras i utvärderingsläge med vissa begränsningar. För att testa Aspose.Cells utan dessa utvärderingsbegränsningar kan du begära en gratis 30-dagars tillfällig licens.
Följande är en lista över ändringar i denna version av Aspose.Cells för Java.


Andra förbättringar och förändringar

Förbättringar

(CELLSJAVA-40788) - Stöd anpassat tema för formegenskaper
(CELLSJAVA-40803) - Ställ in renderingstips för bilder när du exporterar kalkylark till HTML

Buggar

(CELLSJAVA-40793) - Räckvidden hänvisar inte till korrekt område
(CELLSJAVA-40768) - Metoden WorkbookRender.toPrinter() skriver inte ut bild
(CELLSJAVA-40669) - Pivot Column Stort problem vid rendering av XLTX till PDF
(CELLSJAVA-40801) - Cell anpassningsproblem i den renderade PDF-filen
(CELLSJAVA-40406) - Konvertera Excel-fil med stort antal kolumner till PDF-fil
(CELLSJAVA-40794) - AutoFitColumns fungerar inte när de används med olika teckensnittsinställningar
(CELLSJAVA-40816) - Markören flyttas fortfarande till sista kolumnen efter att ha använt Cells.DeleteColumn() för att ta bort den
(CELLSJAVA-40786) - Genererad emf-form är inte samma som originalet
(CELLSJAVA-40806) - Excel-bokmärken genereras inte när de konverteras till PDF


Undantag

(CELLSJAVA-40797) - Cell.getDependents() kastar NullPointerException
(CELLSJAVA-40800) - CellsException vid konvertering av kalkylblad till PDF på MAC OS

Public API och bakåtinkompatibla ändringar

Följande är en lista över eventuella ändringar som gjorts i det offentliga API:t, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts i Aspose.Cells för .NET. Om du har funderingar på någon av de listade ändringarna, vänligen ta upp det på Aspose.Cells supportforum.

Lägger till egenskapen Shape.TextDirection
Hämtar/ställer in textflödets riktning för formen.

Lägger till egenskapen HTMLLoadOptions.ConvertFormulasData
Anger om konvertera sträng till formel eller inte när strängvärdet som börjar med tecknet '=' är formelsträng, är standardvärdet falskt.

Lägger till egenskapen HtmlSaveOptions.ImageOptions
Hämtar/ställer in alternativ för rendering när html-filer sparas.

Föråldrad egenskap HtmlSaveOptions.ExportChartImageFormat
Använder istället HtmlSaveOptions.ImageOptions för bildformatinställningar när du sparar html-filer.


Notera
Eftersom kodbasen för Aspose.Cells för Java matchar koden för relevant .NET-version, är de flesta ändringar, förbättringar och korrigeringar som ingår i Aspose.Cells för .NET v8.0.2 också inkluderade i denna Aspose.Cells för Java v8.0.2.
