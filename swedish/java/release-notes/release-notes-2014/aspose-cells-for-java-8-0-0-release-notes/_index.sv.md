---
title: Aspose.Cells for Java 8.0.0 Release Notes
type: docs
weight: 70
url: /sv/java/aspose-cells-for-java-8-0-0-release-notes/
---
{{% alert color="primary" %}}

 Den här sidan innehåller release notes för[Aspose.Cells for Java 8.0.0](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-8.0.0/)

{{% /alert %}}

Aspose.Cells for Java har uppdaterats till version 8.0.0 och vi är glada att kunna meddela att denna utgåva kommer med över 30 nya användbara förbättringar.
Med Aspose.Cells for Java kan du arbeta med XLS, SpreadsheetML, OOXML, XLSB, CSV, HTML, ODS, PDF, XPS och andra format i dina applikationer. Du kan också generera, ändra, konvertera, rendera och skriva ut arbetsböcker utan att använda Microsoft Excel.
Besök dokumentationen för att lära dig hur du kommer igång med Aspose.Cells for Java.
Observera att den här nedladdningen innehåller en fullt fungerande version av produkten, men utan en licensuppsättning kommer den att köras i utvärderingsläge med vissa begränsningar. För att testa Aspose.Cells utan dessa utvärderingsbegränsningar kan du begära en gratis 30-dagars tillfällig licens.
Följande är en lista över ändringar i denna version av Aspose.Cells for Java.

Huvudfunktioner

Alternativ för minnesanvändning kan användas för prestandaövervägande.
När du bygger en arbetsbok med datauppsättningar med stora celler kan alternativet MemorySetting.MEMORY_PREFERENCE optimera minnesanvändningen för celldata för att minska minneskostnaden.

Andra förbättringar och förändringar

Nya egenskaper

(CELLSJAVA-40749) - Få startrad/kolumn och slutrad/kolumnindex för en sida med kalkylblad
(CELLSJAVA-40744) - Stöd för Visa Formler MS Excel-funktionen
(CELLSJAVA-40423) - Aspose.Cells och Maven beroenden
(CELLSJAVA-40770) - Ställ in skapelsetiden i den genererade PDF-filen

Förbättringar

(CELLSJAVA-40751) - Skrivfel i metodnamn - SeriesCollection.setSecondCategoryData
(CELLSJAVA-40753) - Custom Series DataLabel Separator
(CELLSJAVA-40764) - Cell.DisplayStringValue beräknade inte exakt för utrymmen som bestämts av kolumnbredd och '*' i anpassad stil

Buggar

(CELLSJAVA-40738) - setExportActiveWorksheetByt ändra justering av tabell i HTML
(CELLSJAVA-40747) - Bakgrundsbilden kopieras inte till målarbetsboken när Workbook.copy anropas
(CELLSJAVA-40276) - Text inuti en bild verkar vara spegelvänd när du sparar en excel-arbetsbok som PDF
(CELLSJAVA-40573) - Vissa ord separeras när du sparar till PDF
(CELLSJAVA-40743) - Tabell autofilter fungerar inte i xls-format men fungerar bra i xlsx-format
(CELLSJAVA-40750) - Vid export till HTML förlorar celler som täcks av bilden bakgrundsfärgen
(CELLSJAVA-40748) - Bakgrundsbildens sökväg är inte korrekt
(CELLSJAVA-40731) - Vertikal textfråga
(CELLSJAVA-40737) - Formateringsproblem av former/kontroller i Excel till PDF-konvertering
(CELLSJAVA-40742) - Felaktig lindning av axeletiketter vid konvertering av XLSX till PDF
(CELLSJAVA-40757) - DateTime-kolumner felaktigt lästa från CSV med europeisk språkkod
(CELLSJAVA-40282) - Bildutdata speglas samtidigt som ett excel-kalkylblad omvandlas till PDF
(CELLSJAVA-40585) - Aspose.Cells: inbäddat sigma-diagram renderas inte korrekt till PDF/bilder
(CELLSJAVA-40742) - Felaktig lindning av axeletiketter vid konvertering av XLSX till PDF
(CELLSJAVA-40758) - Data är inte korrekta i utdata-pdf
(CELLSJAVA-40762) - Cell.getDependents(true) issue - Cells från andra ark som inte borde finnas i listan
(CELLSJAVA-40756) - CellsException: null vid Workbook.calculateFormula(false)
(CELLSJAVA-40748) - Bakgrundsbildens sökväg är inte korrekt
(CELLSJAVA-40754) - Exportera former till html med felbakgrundsfärg
(CELLSJAVA-40766) - XLSX till HTML: Problem med hideColumn som producerar nollvärden i HTML
(CELLSJAVA-40769) - Omräkningscellens formel

(CELLSJAVA-40771) - Problem med raddold och radhöjd


Undantag

(CELLSJAVA-40736) - com.aspose.cells.CellsException: Ogiltigt cellnamn
(CELLSJAVA-40767) - NullpointerException när du sparar en bok
(CELLSJAVA-40755) - CellsException: Överflöde i sträng till int-konvertering. Strängvärde: #N/A.
(CELLSJAVA-40761) - CellsException: Form till bild Fel!

Offentlig API och bakåtinkompatibla ändringar

Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for Java. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.

Föråldrade egenskapen AutoFilter.FilterColumnCollection
Använder AutoFilter.FilterColumns istället.

Lägger till egenskapen Worksheet.ShowFormulas
Anger om formlerna visas eller värdet på formlerna.

Lägger till egenskapen PdfSaveOptions.CreatedTime
Hämtar och ställer in tiden för generering av pdf-dokumentet.

Lägger till FileFormatType.Ooxml enum
Representerar krypterad office open xml-fil (som XLSX, DOCX, PPTX, etc).

Lägger till egenskapen LoadOptions.MemorySetting och WorkbookSettings.MemorySetting-egenskapen
Från den här versionen tillhandahåller vi minnesanvändningsalternativ för användaren för prestandaövervägande. Standardalternativet MemorySetting.NORMAL tillämpas för alla versioner. För vissa situationer som att bygga en arbetsbok med stor datamängd för celler kan alternativet MemorySetting.MEMORY_PREFERENCE optimera minnesanvändningen och minska minneskostnaden för användarens applikation. Det här alternativet kan dock försämra prestandan i vissa speciella fall, som att få åtkomst till celler slumpmässigt och upprepade gånger.

Föråldrar egenskapen SeriesCollection.SecondCatergoryData och lägger till egenskapen SeriesCollection.SecondCategoryData
Använder SeriesCollection.SecondCategoryData för att ersätta SeriesCollection.SecondCatergoryData.

Implementeringarna av Row/Cell/RowCollection ändras
gamla versioner hålls Row- och Cell-objekt i minnet för att representera motsvarande rad och cell i ett kalkylblad. Samma instans kommer att returneras när användaranropsmetoder som RowCollection[int index], Cells[int, int] och så vidare. Av hänsyn till minnesprestanda kommer från och med den här versionen endast egenskaper och data för Row och Cell att lagras i minnet. Row/Cell-objektet blir omslaget av dessa egenskaper och data för användarens bekvämlighet för att manipulera cellmodellen och kommer att instansieras på nytt när användaren anropar dessa metoder. Så nu kommer användaren att få olika objekt när de anropar samma metod för att få Row/Cell många gånger även om de olika objekten alla refererar till samma rad/cell i kalkylbladet. Denna ändring kan påverka användarens applikation i följande situationer:1. Om användaren använde koden likeif(rad1==rad2)...if(cell1==cell2)...för att kontrollera samma rad/Cell, med nya versioner kan dessa kontroller misslyckas. Använd row1.equals(row2) och cell1.equals(cell2) istället.2. Eftersom Row/Cell-objekt nyligen instansierats enligt användarens anrop kommer de inte att behållas och hanteras i minnet av cellkomponenten. Efter vissa insättnings-/borttagningsoperationer kanske deras position (rad/kolumnindex) inte uppdateras eller ännu värre, dessa objekt blir ogiltiga. Till exempel, för följande kod:Cell cell = cells.get("A2");System.out.println(cell.getName() + ":" + cell.getValue());cells.insertRange(CellArea.createCellArea( "A1", "A1"), ShiftType.DOWN);System.out.println(cell.getName() + ":" + cell.getValue()); med gamla versioner kommer cellen att referera till A3 efter infogningen operation och dess värde är detsamma som före insert. Men med ny version blir cellobjektet ogiltigt eller fortfarande refererar till A2 med annat värde. För en sådan situation måste användaren hämta objektet Row/Cell igen från cellsamlingen för att få rätt resultat:Cell cell = cells.get("A2");System.out.println(cell.getName() + ": " + cell.getValue());cells.insertRange(CellArea.createCellArea("A1", "A1"), ShiftType.DOWN);cell = cells.get("A3");System.out.println(cell. getName() + ":" + cell.getValue());3. RowCollection ärver nu inte CollectionBase eftersom det inte finns något radobjekt i dess inre lista längre.

Cell.StringValue ändras för speciellt formateringsmönster med '*' och '_'
I gamla versioner, specialmönster '* kommer att ignoreras vid formatering av cellvärde för Cell.StringValue och '** producerar alltid ett tecken i det formaterade resultatet. Från den här versionen ändrar vi logiken för att göra med '* och '**' för att göra det formaterade resultatet samma som det du kan få från ms excel när du kopierar en cell som text (som att kopiera en cell till en textredigerare eller exportera cellen till csv). Använd till exempel det anpassade "*($* #,##0.00*)" för att formatera cellvärdet 123, med gamla versioner Cell. StringValue kommer att ge resultatet som "$ 123.00". Nu med nya versioner kommer Cell.StringValue att ge resultatet som " $123.00 " vilket är samma sak som du kan få från ms excel genom att kopiera denna cell till text.

Notera
Eftersom kodbasen för Aspose.Cells for Java matchar koden för relevant version .NET, är de flesta ändringar, förbättringar och korrigeringar som ingår i Aspose.Cells for .NET v8.0.0 också inkluderade i denna 076153480.0.4816.
