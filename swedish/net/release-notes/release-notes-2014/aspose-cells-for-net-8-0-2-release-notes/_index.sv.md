---
title: Aspose.Cells for .NET 8.0.2 Release Notes
type: docs
weight: 70
url: /sv/net/aspose-cells-for-net-8-0-2-release-notes/
---
{{% alert color="primary" %}} 

 Den här sidan innehåller release notes för[Aspose.Cells for .NET 8.0.2](https://downloads.aspose.com/cells/net/new-releases/aspose.cells-for-.net-8.0.2/)

{{% /alert %}} 

 Aspose.Cells for .NET har uppdaterats till version 8.0.2 och vi är glada att kunna meddela att denna utgåva kommer med över 30 nya användbara förbättringar.
Med Aspose.Cells for .NET kan du arbeta med XLS, SpreadsheetML,OOXML,XLSB, CSV, HTML, ODS, PDF, XPS och andra format i dina applikationer. Du kan också visa, generera, ändra, konvertera, rendera och skriva ut arbetsböcker utan att använda Microsoft Excel.
Besök dokumentationen för att lära dig hur du kommer igång med Aspose.Cells for .NET.
Observera att den här nedladdningen innehåller en fullt fungerande version av produkten, men utan en licensuppsättning kommer den att köras i utvärderingsläge med vissa begränsningar. För att testa Aspose.Cells utan dessa utvärderingsbegränsningar kan du begära en gratis 30-dagars tillfällig licens.
Följande är en lista över ändringar i denna version av Aspose.Cells.

\1) Aspose.Cells 


## **Andra förbättringar och förändringar**

## **Nya egenskaper**


 (CELLSNET-42585) - Ändra kommentartextriktning


## **Prestanda**


 (CELLSNET-42278) - System.OutOfMemoryException samtidigt som XLSX sparas till PDF där XLSX har massor av tomma celler med formatering


## **Buggar**


 (CELLSNET-42524) - CalculateTextSize-funktionen för Shape-objektproblemen

 (CELLSNET-42401) - CalculateTextSize() returnerar inte korrekt höjd

(CELLSNET-42235) - Problem med TextBox AutoSizing

 (CELLSNET-42104) - CalculateTextSize returnerar inte korrekt höjd

 (CELLSNET-42612) - Funktionen för automatisk anpassning av kolumner fungerar inte för pivotens filtrerade rullgardinskolonner

 (CELLSNET-42562) - Formler fungerar inte med utländsk valuta

 (CELLSNET-42269) - Pivottabellformatering i utdata-XPS är inte korrekt

 (CELLSNET-42597) - AutoFitRows gör att den raderade texten döljs i resulterande PDF

 (CELLSNET-42615) - SheetRender renderar inte upphöjd korrekt

 (CELLSNET-42594) - Vertikal textjustering fungerar inte korrekt i SheetRender

 (CELLSNET-42580) - Spara Excel-fil till PDF ignorerar färginställningar i sidhuvudet

 (CELLSNET-42579) - Problem med sidbrytning vid rendering till PDF

 (CELLSNET-42498) - Border kopieras till nästa sida medan XLSX konverteras till PDF

 (CELLSNET-42495) - Pdf-rendering innehåller oönskade rader på sidan 2 och 3

(CELLSNET-42567) - Grafen försvinner när den konverteras till PDF

 (CELLSNET-42527) - Linjediagram och stapeldiagram i samma graf är inte i rätt position

 (CELLSNET-42595) - Rutnätslinjer visas i MS-Excel Print Preview när arbetsboken sparas i Xlsb-format

 (CELLSNET-42591) - AutoFitColumns fungerar inte med ListObjects när nya rader läggs till.

 (CELLSNET-42590) - xml:space="bevara"-attribut förlorat för Excel Cell:s v (värde) OpenXML-nod

 (CELLSNET-42588) - Det går inte att infoga en tabell i XLSB-filen

 (CELLSNET-42586) - Kommentarstextjustering när den är inställd till höger fungerar inte

 (CELLSNET-42582) - Excel hittade oläsbart innehållsfel vid öppning av Aspose.Cells konverterad XLSM från XLSB

 (CELLSNET-42581) - ArgumentOutOfRangeException - när du öppnar Excel XLSX-filen

 (CELLSNET-42570) - Cell formler i de smarta markörerna expanderar inte

 (CELLSNET-42568) - Kolumnen, nämligen Sieve Size, visar #N/A


## **Undantag**


(CELLSNET-42576) - Nullreferensundantag för att spara xls som pdf

 (CELLSNET-42628) - System.NullReferenceException när ett MHTML-kalkylblad laddas

 (CELLSNET-42609) - Cell.GetDispalyStyle() misslyckas för vissa villkorliga formateringsregler

 (CELLSNET-42587) - System.NullReferenceException vid öppning av filen

 (CELLSNET-42577) - NullReferenceException - medan den villkorliga stilen för en cell hämtas





\2) Aspose.Cells Grid Suite


## **Andra förbättringar och förändringar**

## **Buggar**


 (CELLSNET-42572) - Färg på arkfliken bevaras inte i GridWeb

 (CELLSNET-42302) - WebGrid kontextmeny - FIND misslyckas på IE11 med JS-fel: Det går inte att hämta egenskapen 'acwFindReplaceDialog_Element' för odefinierad eller nollreferens

 (CELLSNET-40531) - Formelproblem vid laddning av mallfil till GridWeb

 (CELLSNET-42571) - Talformat i kolumn H inne i GridWeb bevaras inte

 (CELLSNET-42553) - Lista objekt/tabellformatering/ stil förlorad vid import av Excel-fil till GridWeb

 (CELLSNET-42623) - Fel vid skapande av kontroll för GridWeb




## **Offentlig API och bakåtinkompatibla ändringar**


 Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for .NET. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.



Lägger till egenskapen Shape.TextDirection

 Hämtar/ställer in textflödets riktning för formen.



 Lägger till egenskapen HTMLLoadOptions.ConvertFormulasData

 Anger om konvertera sträng till formel eller inte när strängvärdet som börjar med tecknet '=' är formelsträng, är standardvärdet falskt.



 Lägger till egenskapen HtmlSaveOptions.ImageOptions

 Hämtar/ställer in alternativ för rendering när html-filer sparas.



 Föråldrad egenskap HtmlSaveOptions.ExportChartImageFormat

 Använder istället HtmlSaveOptions.ImageOptions för bildformatinställningar när du sparar html-filer.


