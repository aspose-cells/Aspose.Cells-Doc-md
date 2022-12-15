---
title: Aspose.Cells for .NET 8.1.0 Release Notes
type: docs
weight: 60
url: /sv/net/aspose-cells-for-net-8-1-0-release-notes/
---
{{% alert color="primary" %}} 

 Den här sidan innehåller release notes för[Aspose.Cells for .NET 8.1.0](https://downloads.aspose.com/cells/net/new-releases/aspose.cells-for-.net-8.1.0/)

{{% /alert %}} 

 Aspose.Cells for .NET har uppdaterats till version 8.1.1 och vi är glada att kunna meddela att denna utgåva kommer med över 20 nya användbara förbättringar.
Med Aspose.Cells for .NET kan du arbeta med XLS, SpreadsheetML, OOXML, XLSB, CSV, HTML, ODS, PDF, XPS och andra format i dina applikationer. Du kan också visa, generera, ändra, konvertera, rendera och skriva ut arbetsböcker utan att använda Microsoft Excel.
Besök dokumentationen för att lära dig hur du kommer igång med Aspose.Cells for .NET.
Observera att den här nedladdningen innehåller en fullt fungerande version av produkten, men utan en licensuppsättning kommer den att köras i utvärderingsläge med vissa begränsningar. För att testa Aspose.Cells utan dessa utvärderingsbegränsningar kan du begära en gratis 30-dagars tillfällig licens.
Följande är en lista över ändringar i denna version av Aspose.Cells.

\1) Aspose.Cells 
## **Andra förbättringar och förändringar**

## **Nya egenskaper**


(CELLSNET-42761) - Ta bort scenarier från kalkylbladen


## **Buggar**


 (CELLSNET-42523) - SheetRender misslyckas när UpdateSelectedValue används

 (CELLSNET-42387) - Text har flyttats från bannern.

 (CELLSNET-42385) - Krökt anslutningsform visas inte när XLSX renderas till PDF

 (CELLSNET-42379) - Text i matrisen visas annorlunda

 (CELLSNET-42752) - Pivottabells delsummor har felaktig cellsammanslagning

 (CELLSNET-42703) - Att konvertera kalkylarket med pivottabell till PDF har stilrelaterade problem

 (CELLSNET-42386) - GetPivotData-funktionen beräknar felaktigt värde

 (CELLSNET-42742) - Aspose.Cells Bäddar in felaktiga teckensnitt i PDF-filen

 (CELLSNET-42697) - Header dupliceras i utdata-pdf

 (CELLSNET-42759) - X-axeletiketter på sjökortet är avskurna

 (CELLSNET-42756) - Punktpunkter återges inte korrekt om de finns i en textruta

 (CELLSNET-42750) - Pilar visar spegelvända på en vertikal axel

(CELLSNET-42748) - Förklaringslinjer är tunnare än i Excel

 (CELLSNET-42730) - XLSM till PDF tenderar att hänga sig när ändringar görs i Cell Value & Format

 (CELLSNET-42381) - Punktlistan skrivs inte ut korrekt under rubriken List

 (CELLSNET-42375) - Punktlistan under rubriken Cykel är inte korrekt konverterad till pdf

 (CELLSNET-42779) - Xlam-filen öppnas inte i Excel efter att ha öppnats och sparats på nytt

 (CELLSNET-42766) - Att öppna och spara filen orsakar fel med anpassade vyer

 (CELLSNET-42725) - Infogad bild förlorar originalstorlek

 (CELLSNET-42716) - XLSM-band förlorade efter att ha sparat XLSM-filen igen

 (CELLSNET-42711) - Row.ApplyStyle fungerar inte korrekt

 (CELLSNET-42708) - Grön bakgrundsfärg för celler försvinner i HTML

 (CELLSNET-42695) - Skyddat vyfel i MS Excel-fil - Utredning krävs


## **Undantag**


 (CELLSNET-42782) - System.FormatException vid läsning av xlsx-fil

(CELLSNET-42758) - Angiven cast är inte ett giltigt undantag på Cell.GetDisplayStyle()

 (CELLSNET-42724) - StackOverflowException inträffade när metoden Worksheet/Workbook.CalculateFormula() anropades

 (CELLSNET-42710) - Ogiltig formel vid laddning av ett eventuellt skadat kalkylark

 (CELLSNET-42706) - System.OutOfMemoryException på DetectFileFormat


## **Offentlig API och bakåtinkompatibla ändringar**


 Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for .NET. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.



 Lägger till egenskapen HtmlSaveOptions.PresentationPreference

 Anger om html- eller mht-fil är presentationspreferens. Standardvärdet är falskt. Om du vill få en vackrare presentation, ställ in värdet på sant.



Public ScenarioCollection, Scenario, ScenarioInputCellCollection, ScenarioInputCell-klasser och Worksheet.Scenarios-egenskapen.

 Stöder att lägga till, ändra och ta bort scenarieinställningar.


