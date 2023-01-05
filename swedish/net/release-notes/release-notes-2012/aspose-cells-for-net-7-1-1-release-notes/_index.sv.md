---
title: Aspose.Cells for .NET 7.1.1 Release Notes
type: docs
weight: 100
url: /sv/net/aspose-cells-for-net-7-1-1-release-notes/
---
{{% alert color="primary" %}} 

 Den här sidan innehåller release notes för[Aspose.Cells for .NET 7.1.1](https://downloads.aspose.com/cells/net/new-releases/aspose.cells-for-.net-7.1.1/)

{{% /alert %}} 

 Vi är glada att meddelaAspose.Cells for .NET v7.1.1!

\1) Aspose.Cells 

 Nya egenskaper

- Spåra prejudikat och beroende

 Förbättringar

- Att spara arbetsbok i XLSX ger ett fel
- Alternativ för AutoFitColumn
- Finns det GetDependents()-metoden i .NET-versionen

 -Stöd TH-element i HTML-tabellen

- Excel till PDF (arabiska) - Felaktig ord-/datumformatering vid konvertering
- Antivirusprogram tar bort Excel-filer från e-postmeddelanden

 Undantag

- Fel vid öppning av en fil som har ett kalkylblad med namn som innehåller: "!" karaktär
- Undantag för att ladda giltig Excel-fil - varje gång
- Intervallet för AutoFilter är inte giltigt
- Undantag efter användning av metoderna Combine() och Save() för arbetsböcker med externa referenser

 Buggar

- Problem med villkorlig formatering från och med version 4.8.1

 -Knappegenskaper

- Cells med fötter och tum är felaktiga när de konverteras till PDF
- Problem med att rendera em dash-tecken i PDF-utdata
- Sidlayout ändrad i den sammanslagna arbetsboken
- Spara som XLSX ger ibland en ogiltig fil

 -XLS fil öppnas i skyddat läge efter användning av Aspose.Cells

- Cell.GetDependents() fungerar inte med NamedRange
- Problem med AutoFitRow och IndentLevel
- Problem med namngivet intervall när du använder Kombinera
- TickLabels är inte synliga när nr. av Ticklabels antal är större
- Problem med att översätta MS Excel-diagram till PDF, Y-axel saknas
- Problem med linjebredd i grafik och tomma textområden
- Problem med ADDRESS-, COUNTBLANK- och IF-funktionerna
- VLOOKUP OCH OFFSET FUNKTIONER Problem
- Ingen MS Excel-formelvalidering
- Problem med NETWORKDAYS-funktionen i XLS-utgången
- HTML-till-Excel-konverteringsproblem

 ` `- HTML problem med radspann och klassattribut

-Stöder Cells datauri

- Anpassade formaterade ramar förlorade vid konvertering till PDF
- Rutnät i PDF Export

 -Excel hittade oläsbart innehåll fel

- Extrahera den anpassade pivotstilen från mallfilen
- Problem hittat i MS Excel: "Excel hittade oläsbart innehåll ..."
- Kolumnjustering i bilden när du använder SheetRender API
- Excel-renderingsproblem

\2)
 Aspose.Cells.GridWeb

 Buggar

- Problem med textbrytning för GridWeb

 GridWeb.SaveToExcelFile som inte inkluderar nyinfogade data

- Inställningen för vertikal justering av text fungerar inte

\3)
 Aspose.Cells.GridDesktop

 Buggar

- Strängen kändes inte igen som en giltig Boolean
